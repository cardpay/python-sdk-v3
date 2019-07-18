# coding: utf-8

from __future__ import absolute_import

import uuid

from cardpay import *
from config import *
from constants import CARD_NON3DS_CONFIRMED
from payment import do_payment
from refunds import do_refund
from utils.data_utils import generateAmount

logger = create_logger(__name__)

config = Configuration(base_url=CARDPAY_API_URL, terminal_code=GATEWAY_TERMINAL_CODE, password=GATEWAY_PASSWORD, debug=DEBUG_MODE)
payments = PaymentsApi(ApiClient(config))
refunds = RefundsApi(ApiClient(config))


def test_refund_list_information():
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Phase 1: create payment
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    payment_id = do_payment(payments, CARD_NON3DS_CONFIRMED, amount=300)

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Phase 2: create postponed refund
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    ids = {do_refund(refunds, payment_id, generateAmount(min=1, max=10)) for _ in range(0, 3)}

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Phase 3: fetch refunds
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    # prepare request data
    currency = TERMINAL_CURRENCY
    maxCount = 50

    # perform getting refunds list information
    response = refunds.get_refunds(
        request_id=str(uuid.uuid4()),
        currency=currency,
        max_count=maxCount
    )

    # explore response result
    assert ids.issubset({p.refund_data.id for p in response.data})
