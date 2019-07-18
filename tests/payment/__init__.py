# coding: utf-8
import uuid

from cardpay import *
from config import *
from constants import PAYMENT_METHOD_BANKCARD
from utils.data_utils import fake, randomString, generateEmail, generateCardExpiration, generatePhoneNumber, generateAmount, generateMerchantOrderId
from utils.http_utils import do_get


def do_payment(api, pan, amount=None, preauth=False):
    # prepare request data
    request = create_payment_request(pan, amount=amount, preauth=preauth)

    # perform api call
    response = api.create_payment(payment_request=request)

    # Emulate customer behaviour performing GET request to redirect url
    do_get(response.redirect_url)

    # explore response result
    payment = fetch_payment_by_merchant_order_id(api, request.merchant_order.id)
    return payment.payment_data.id


def create_payment_request(pan, amount=None, preauth=False):
    customer_id = randomString(15)
    return PaymentRequest(
        request=ApiClient.uuid_request(),
        merchant_order=PaymentRequestMerchantOrder(
            id=generateMerchantOrderId(),
            description=fake.sentence()
        ),
        payment_method=PAYMENT_METHOD_BANKCARD,
        payment_data=PaymentRequestPaymentData(
            currency=TERMINAL_CURRENCY,
            amount=generateAmount() if not amount else amount,
            note=fake.sentence(),
            preauth=preauth
        ),
        card_account=PaymentRequestCardAccount(card=PaymentRequestCard(
            pan=pan,
            holder=fake.name().upper(),
            expiration=formatExpirationDate(generateCardExpiration()),
            security_code="123"
        )),
        customer=PaymentRequestCustomer(
            id=customer_id,
            full_name=fake.name(),
            email=generateEmail(customer_id),
            birth_date=formatBirthDate(fake.profile()['birthdate']),
            phone=generatePhoneNumber()
        ),
        return_urls=ReturnUrls(
            success_url=SUCCESS_URL,
            decline_url=DECLINE_URL,
            cancel_url=CANCEL_URL,
            inprocess_url=INPROCESS_URL
        )
    )


def fetch_payment_by_merchant_order_id(api, merchant_order_id):
    payments_response = api.get_payments(
        request_id=str(uuid.uuid4()),
        merchant_order_id=merchant_order_id
    )

    assert payments_response.data
    assert 1 == len(payments_response.data)

    return payments_response.data[0]


def fetch_payment_by_id(api, id):
    payments_response = api.get_payment(id)

    assert payments_response

    return payments_response
