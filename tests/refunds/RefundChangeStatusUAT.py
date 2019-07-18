# coding: utf-8

from __future__ import absolute_import

from cardpay import *
from config import *
from constants import CARD_NON3DS_CONFIRMED
from payment import do_payment
from refunds import do_refund
from utils.data_utils import generateAmount

logger = create_logger(__name__)

config = Configuration(base_url=CARDPAY_API_URL, terminal_code=GATEWAY_POSTPONED_TERMINAL_CODE, password=GATEWAY_POSTPONED_PASSWORD, debug=DEBUG_MODE)
payments = PaymentsApi(ApiClient(config))
refunds = RefundsApi(ApiClient(config))


def test_change_refund_status():
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Phase 1: create payment
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    payment_id = do_payment(payments, CARD_NON3DS_CONFIRMED, amount=300)

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Phase 2: create postponed refund
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    refund_id = do_refund(refunds, payment_id, generateAmount(max=100))

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Phase 3: change refund status
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    # prepare request data
    request = RefundUpdateRequest(
        request=ApiClient.uuid_request(),
        refund_data=RequestUpdatedTransactionData(status_to=RequestUpdatedTransactionData.StatusTo.REVERSE)
    )

    # perform change refund status
    response = refunds.update_refund(refund_id, request)
    assert response is not None

    # explore response result
    data = response.refund_data
    assert data is not None
    assert data.Status.VOIDED == data.status
