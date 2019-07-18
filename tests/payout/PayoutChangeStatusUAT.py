# coding: utf-8

from __future__ import absolute_import

from cardpay import *
from config import *
from constants import CARD_NON3DS_CONFIRMED
from payout import do_payout

logger = create_logger(__name__)

config = Configuration(base_url=CARDPAY_API_URL, terminal_code=GATEWAY_POSTPONED_TERMINAL_CODE, password=GATEWAY_POSTPONED_PASSWORD, debug=DEBUG_MODE)
payouts = PayoutsApi(ApiClient(config))


def test_change_payout_status():
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Phase 1: create payout
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    # perform payout
    payout_id = do_payout(payouts, CARD_NON3DS_CONFIRMED)

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Phase 2: update status to COMPLETE for exists payment
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    # prepare request data
    request = PayoutUpdateRequest(
        request=ApiClient.uuid_request(),
        payout_data=RequestUpdatedTransactionData(status_to=RequestUpdatedTransactionData.StatusTo.REVERSE)
    )
    logger.info(request)

    # perform create payment
    response = payouts.update_payout(payout_id, request)

    # explore response result
    assert response is not None

    data = response.payout_data
    assert data is not None

    assert data.Status.VOIDED == data.status
    assert data.StatusTo.REVERSE == data.status_to
