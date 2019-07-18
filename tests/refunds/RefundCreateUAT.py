# coding: utf-8

from __future__ import absolute_import

from cardpay import *
from config import *
from constants import CARD_NON3DS_CONFIRMED
from payment import do_payment
from utils.data_utils import fake, randomString, generateAmount

logger = create_logger(__name__)

config = Configuration(base_url=CARDPAY_API_URL, terminal_code=GATEWAY_TERMINAL_CODE, password=GATEWAY_PASSWORD, debug=DEBUG_MODE)
payments = PaymentsApi(ApiClient(config))
refunds = RefundsApi(ApiClient(config))


def test_create_refund():
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Phase 1: create payment
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    payment_id = do_payment(payments, CARD_NON3DS_CONFIRMED, amount=300)

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Phase 2: create refund
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    # merchant order data
    merchantOrderId = randomString(20)
    merchantDescription = fake.sentence()
    amount = generateAmount(max=100)
    currency = TERMINAL_CURRENCY

    # prepare refund request data
    request = RefundRequest(
        request=ApiClient.uuid_request(),
        merchant_order=RefundRequestMerchantOrder(
            id=merchantOrderId,
            description=merchantDescription
        ),
        payment_data=RefundRequestPaymentData(payment_id),
        refund_data=RefundRequestRefundData(
            amount=amount,
            currency=currency
        )
    )
    logger.info(request)

    # perform create refund
    response = refunds.create_refund(request)
    assert response is not None

    data = response.refund_data
    assert data is not None
    assert data.Status.COMPLETED == data.status
