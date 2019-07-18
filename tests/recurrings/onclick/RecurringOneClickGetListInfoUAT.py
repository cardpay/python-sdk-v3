# coding: utf-8

from __future__ import absolute_import

import uuid

from cardpay import *
from config import *
from constants import CARD_NON3DS_CONFIRMED
from recurrings.onclick import do_one_click_payment

logger = create_logger(__name__)

config = Configuration(base_url=CARDPAY_API_URL, terminal_code=GATEWAY_TERMINAL_CODE, password=GATEWAY_PASSWORD, debug=DEBUG_MODE)
recurrings = RecurringsApi(ApiClient(config))


def test_get_one_click_payments_list_information():
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Generate recurrings
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    # prepare recurrings
    ids = {do_one_click_payment(recurrings, CARD_NON3DS_CONFIRMED) for _ in range(0, 3)}

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Fetch recurrings
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    # perform api call
    response = recurrings.get_recurrings(
        request_id=str(uuid.uuid4()),
        currency=TERMINAL_CURRENCY,
        max_count=50,
        type="ONECLICK"
    )

    data = {p.recurring_data.id for p in response.data}

    for p in response.data:
        logger.info("%s %f %s" % (p.recurring_data.id, p.recurring_data.amount, p.recurring_data.currency))

    assert ids.issubset(data)
