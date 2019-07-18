# coding: utf-8

from __future__ import absolute_import

from cardpay import *
from config import *
from constants import CARD_NON3DS_CONFIRMED
from payment import do_payment

logger = create_logger(__name__)

config = Configuration(base_url=CARDPAY_API_URL, terminal_code=GATEWAY_TERMINAL_CODE, password=GATEWAY_PASSWORD, debug=DEBUG_MODE)
payments = PaymentsApi(ApiClient(config))


def test_payment_change_status():
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Phase 1: create payment
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    # prepare payment in PENDING status
    payment_id = do_payment(payments, CARD_NON3DS_CONFIRMED, preauth=True)

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Phase 2: update status to COMPLETE for exists payment
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    request = PaymentPatchRequest(
        request=ApiClient.uuid_request(),
        operation=PaymentPatchRequest.Operation.CHANGE_STATUS,
        payment_data=PaymentUpdateTransactionData(status_to=PaymentUpdateTransactionData.StatusTo.COMPLETE)
    )
    logger.info(request)

    response = payments.update_payment(payment_id, request)
    logger.info(response)
