# coding: utf-8

from __future__ import absolute_import

from cardpay import *
from config import *
from constants import PAYMENT_METHOD_BANKCARD
from utils.data_utils import fake, randomString, generateEmail, generatePhoneNumber, generateAmount

logger = create_logger(__name__)

client = ApiClient(baseUrl=CARDPAY_API_URL, terminal_code=PAYMENTPAGE_TERMINAL_CODE, password=PAYMENTPAGE_PASSWORD, debug=DEBUG_MODE)
payments = PaymentsApi(client)


def test_create_payment_page_mode():
    # merchant order data
    merchantOrderId = randomString(20)
    merchantDescription = fake.sentence()
    amount = generateAmount()
    currency = TERMINAL_CURRENCY
    note = fake.sentence()

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
        card_account=PaymentRequestCardAccount(),
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

    assert response.redirect_url is not None
