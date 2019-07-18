# coding: utf-8

from __future__ import absolute_import

import uuid

from cardpay import *
from config import *
from recurrings import do_cancel_subscription
from recurrings.scheduled import do_create_subscription, do_create_plan

logger = create_logger(__name__)

config = Configuration(base_url=CARDPAY_API_URL, terminal_code=GATEWAY_TERMINAL_CODE, password=GATEWAY_PASSWORD, debug=DEBUG_MODE)
recurrings = RecurringsApi(ApiClient(config))

ids = []


def teardown_function():
    global ids
    for id in ids:
        do_cancel_subscription(recurrings, id)


def test_get_subscriptions_list_information():
    global ids
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Generate subscriptions
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    ids = {do_create_subscription(recurrings, plan_id=do_create_plan(recurrings)) for _ in range(0, 3)}

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Fetch subscriptions
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    response = recurrings.get_subscriptions(
        request_id=str(uuid.uuid4()),
        max_count=50,
        sort_order="desc"
    )

    print("\ncount: %s" % len(response.data))

    for s in response.data:
        print("%s %s: %s %s" % (s.created, s.id, s.currency, s.status))
        if s.status != s.Status.CANCELLED:
            do_cancel_subscription(recurrings, s.id)

    assert ids.issubset({s.id for s in response.data})
