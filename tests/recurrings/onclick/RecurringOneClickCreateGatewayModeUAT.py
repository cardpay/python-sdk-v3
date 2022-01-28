# coding: utf-8

from __future__ import absolute_import

from cardpay import *
from config import *
from constants import PAYMENT_METHOD_BANKCARD, CARD_NON3DS_CONFIRMED
from recurrings import fetch_recurring
from utils.data_utils import fake, randomString, generateEmail, generateCardExpiration, generateAmount
from utils.http_utils import do_get

logger = create_logger(__name__)

config = Configuration(base_url=CARDPAY_API_URL, terminal_code=GATEWAY_TERMINAL_CODE, password=GATEWAY_PASSWORD, debug=DEBUG_MODE)
recurrings = RecurringsApi(ApiClient(config))


def test_create_payment_gateway_mode():
    # merchant order data
    merchantOrderId = randomString(20)
    merchantDescription = fake.sentence()
    amount = generateAmount()
    currency = TERMINAL_CURRENCY
    initiator = "cit"

    # card data
    cardPan = CARD_NON3DS_CONFIRMED
    cardHolder = fake.name().upper()
    cardExpiration = formatExpirationDate(generateCardExpiration())
    securityCode = "100"

    # customer data
    customerId = randomString(15)
    customerEmail = generateEmail(customerId)

    # prepare request data
    request = RecurringCreationRequest(
        request=ApiClient.uuid_request(),
        merchant_order=PaymentRequestMerchantOrder(
            id=merchantOrderId,
            description=merchantDescription
        ),
        payment_method=PAYMENT_METHOD_BANKCARD,
        card_account=PaymentRequestCardAccount(
            card=PaymentRequestCard(
                pan=cardPan,
                holder=cardHolder,
                expiration=cardExpiration,
                security_code=securityCode
            )
        ),
        customer=PaymentRequestCustomer(
            id=customerId,
            email=customerEmail
        ),
        recurring_data=RecurringRequestRecurringData(
            initiator=initiator,
            currency=currency,
            amount=amount
        ),
        return_urls=ReturnUrls(
            success_url=SUCCESS_URL,
            decline_url=DECLINE_URL,
            cancel_url=CANCEL_URL,
            inprocess_url=INPROCESS_URL
        )
    )

    logger.info(request)

    response = recurrings.create_recurring(request)
    logger.info(response)

    # get redirect url
    redirect_url = response.redirect_url
    assert redirect_url is not None

    # Emulate customer behaviour performing GET request to redirect url
    do_get(response.redirect_url)

    # explore response result
    recurring = fetch_recurring(recurrings, merchantOrderId)
    assert recurring is not None
    logger.info(recurring)

    data = recurring.recurring_data
    assert data is not None
    assert data.Status.COMPLETED == data.status
