# coding: utf-8

from cardpay import *
from config import *

from utils.data_utils import fake, randomString


def do_refund(api, payment_id, amount):
    # prepare request data
    request = create_refund_request(payment_id, amount)

    # perform api call
    response = api.create_refund(request)

    return response.refund_data.id


def create_refund_request(payment_id, amount):
    return RefundRequest(
        request=ApiClient.uuid_request(),
        merchant_order=RefundRequestMerchantOrder(
            id=randomString(20),
            description=fake.sentence()
        ),
        payment_data=RefundRequestPaymentData(payment_id),
        refund_data=RefundRequestRefundData(
            amount=amount,
            currency=TERMINAL_CURRENCY
        )
    )
