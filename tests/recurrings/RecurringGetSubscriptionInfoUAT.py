# coding: utf-8

from __future__ import absolute_import

from cardpay import *
from config import *
from recurrings import do_cancel_subscription
from recurrings.scheduled import do_create_plan, do_create_subscription

logger = create_logger(__name__)

config = Configuration(base_url=CARDPAY_API_URL, terminal_code=GATEWAY_TERMINAL_CODE, password=GATEWAY_PASSWORD, debug=DEBUG_MODE)
recurrings = RecurringsApi(ApiClient(config))

subscription_id = None


def teardown_function():
    global subscription_id
    do_cancel_subscription(recurrings, subscription_id) if subscription_id is not None else None


def test_get_subscription_info():
    global subscription_id

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Create subscriptions
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    subscription_id = do_create_subscription(recurrings, plan_id=do_create_plan(recurrings))

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Fetch subscription information
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    response = recurrings.get_subscription(subscription_id)

    # explore response result
    assert response is not None
    assert response.id == subscription_id

    logger.info(response)
