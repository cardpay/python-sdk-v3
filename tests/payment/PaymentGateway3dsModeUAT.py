# coding: utf-8

from __future__ import absolute_import

from cardpay import *
from config import *
from constants import PAYMENT_METHOD_BANKCARD, CARD_3DS_CONFIRMED
from payment import fetch_payment_by_merchant_order_id
from utils.data_utils import fake, randomString, generateEmail, generateCardExpiration, generatePhoneNumber, generateAmount
from utils.http_utils import do_get

logger = create_logger(__name__)

client = ApiClient(baseUrl=CARDPAY_API_URL, terminal_code=GATEWAY_TERMINAL_CODE, password=GATEWAY_PASSWORD, debug=DEBUG_MODE)
payments = PaymentsApi(client)


def test_create_payment_gateway_mode_with_3ds():
    # merchant order data
    merchantOrderId = randomString(20)
    merchantDescription = fake.sentence()
    amount = generateAmount()
    currency = TERMINAL_CURRENCY
    note = fake.sentence()

    # card data
    cardPan = CARD_3DS_CONFIRMED
    cardHolder = fake.name().upper()
    cardExpiration = formatExpirationDate(generateCardExpiration())
    securityCode = "100"

    # customer data
    customerId = randomString(15)
    customerFullname = fake.name()
    customerBirthdate = formatBirthDate(fake.profile()['birthdate'])
    customerEmail = generateEmail(customerId)
    customerPhoneNumber = generatePhoneNumber()

    # prepare request data
    request = PaymentRequest(
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
        payment_data=PaymentRequestPaymentData(
            currency=currency,
            amount=amount,
            note=note
        ),
        customer=PaymentRequestCustomer(
            id=customerId,
            full_name=customerFullname,
            email=customerEmail,
            birth_date=customerBirthdate,
            phone=customerPhoneNumber
        ),
        return_urls=ReturnUrls(
            success_url=SUCCESS_URL,
            decline_url=DECLINE_URL,
            cancel_url=CANCEL_URL,
            inprocess_url=INPROCESS_URL
        )
    )

    logger.info(request)

    # perform api call
    response = payments.create_payment(request)

    # Emulate customer behaviour performing GET request to redirect url
    do_get(response.redirect_url)

    # explore response result
    payment = fetch_payment_by_merchant_order_id(payments, merchantOrderId)
    logger.info(payment)

    data = payment.payment_data
    assert data.Status.COMPLETED == data.status
