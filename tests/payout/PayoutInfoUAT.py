# coding: utf-8

from __future__ import absolute_import

from cardpay import *
from config import *
from constants import CARD_NON3DS_CONFIRMED
from payout import do_payout

logger = create_logger(__name__)

config = Configuration(base_url=CARDPAY_API_URL, terminal_code=GATEWAY_TERMINAL_CODE, password=GATEWAY_PASSWORD, debug=DEBUG_MODE)
payouts = PayoutsApi(ApiClient(config))


def test_payout_information():
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Phase 1: create payout
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    # perform payout
    payout_id = do_payout(payouts, CARD_NON3DS_CONFIRMED)

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Phase 2: update status to COMPLETE for exists payout
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    # prepare request data
    response = payouts.get_payout(payout_id)

    # explore response result
    assert response is not None
    assert payout_id == response.payout_data.id
