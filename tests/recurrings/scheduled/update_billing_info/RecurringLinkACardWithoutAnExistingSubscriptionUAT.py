# coding: utf-8

from __future__ import absolute_import

from cardpay import *
from config import *
from constants import CARD_NON3DS_CONFIRMED, PAYMENT_METHOD_BANKCARD
from recurrings import do_cancel_subscription
from utils.data_utils import randomString, fake, generateCardExpiration, generateEmail, generatePhoneNumber
from utils.http_utils import do_get

logger = create_logger(__name__)

config = Configuration(base_url=CARDPAY_API_URL, terminal_code=GATEWAY_TERMINAL_CODE, password=GATEWAY_PASSWORD, debug=DEBUG_MODE)
recurrings = RecurringsApi(ApiClient(config))
subscription_id = None


def teardown_function():
    global subscription_id
    do_cancel_subscription(recurrings, subscription_id) if subscription_id is not None else None


def test_link_a_card_without_an_existing_subscription():
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Filling Data
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    # merchant order data
    merchantOrderId = randomString(20)
    merchantDescription = fake.sentence()
    initiator = "cit"

    # card data
    cardPan = CARD_NON3DS_CONFIRMED
    cardHolder = fake.name().upper()
    cardExpiration = formatExpirationDate(generateCardExpiration())
    securityCode = "100"

    # customer data
    customerId = randomString(15)
    customerFullname = fake.name()
    customerBirthdate = formatBirthDate(fake.profile()['birthdate'])
    customerEmail = generateEmail(customerId)
    customerPhoneNumber = generatePhoneNumber()

    #  prepare filing request data
    request = FilingRequest(
        request=ApiClient.uuid_request(),
        merchant_order=PaymentRequestMerchantOrder(
            id=merchantOrderId,
            description=merchantDescription
        ),
        customer=PaymentRequestCustomer(
            id=customerId,
            full_name=customerFullname,
            email=customerEmail,
            birth_date=customerBirthdate,
            phone=customerPhoneNumber
        ),
        payment_method=PAYMENT_METHOD_BANKCARD,
        card_account=PaymentRequestCardAccount(card=PaymentRequestCard(
            pan=cardPan,
            holder=cardHolder,
            expiration=cardExpiration,
            security_code=securityCode
        )),
        recurring_data=FilingRecurringData(
            currency=TERMINAL_CURRENCY,
            initiator=initiator
        ),
        return_urls=ReturnUrls(
            success_url=SUCCESS_URL,
            decline_url=DECLINE_URL,
            cancel_url=CANCEL_URL,
            inprocess_url=INPROCESS_URL
        )
    )
    logger.info(request)

    response = recurrings.create_filing(filing_request=request)
    assert response is not None

    # get redirect url
    redirect_url = response.redirect_url
    assert redirect_url is not None

    # Emulate customer behaviour performing GET request to redirect url
    do_get(response.redirect_url)

    # resolve subscriptionId for clean up
    # TODO
