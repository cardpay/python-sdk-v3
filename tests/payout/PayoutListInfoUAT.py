# coding: utf-8

from __future__ import absolute_import

import uuid

from cardpay import *
from config import *
from constants import CARD_NON3DS_CONFIRMED
from payout import do_payout

logger = create_logger(__name__)

config = Configuration(base_url=CARDPAY_API_URL, terminal_code=GATEWAY_TERMINAL_CODE, password=GATEWAY_PASSWORD, debug=DEBUG_MODE)
payouts = PayoutsApi(ApiClient(config))


def test_payout_information():
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Generate payouts
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    # perform payout
    ids = {do_payout(payouts, CARD_NON3DS_CONFIRMED) for _ in range(0, 3)}

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Fetch payouts
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    currency = TERMINAL_CURRENCY
    maxCount = 50

    # prepare request data
    response = payouts.get_payouts(
        request_id=str(uuid.uuid4()),
        currency=currency,
        max_count=maxCount
    )

    # explore response result
    assert ids.issubset({p.payout_data.id for p in response.data})
