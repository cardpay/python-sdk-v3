# coding: utf-8

from __future__ import absolute_import

import uuid

from cardpay import *
from config import *
from recurrings.scheduled import do_create_plan

logger = create_logger(__name__)

config = Configuration(base_url=CARDPAY_API_URL, terminal_code=GATEWAY_TERMINAL_CODE, password=GATEWAY_PASSWORD, debug=DEBUG_MODE)
recurrings = RecurringsApi(ApiClient(config))


def test_get_plan_list_info():
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Generate plans
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    # prepare payments
    ids = {do_create_plan(recurrings) for _ in range(0, 3)}

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Fetch plans
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    # perform operation
    response = recurrings.get_plans(
        request_id=str(uuid.uuid4()),
        max_count=20,
        sort_order='desc'
    )

    # explore response result
    assert response is not None

    data = {p.id for p in response.data}

    for p in response.data:
        logger.info("%s %f %s" % (p.id, p.amount, p.currency))

    assert ids.issubset(data)
