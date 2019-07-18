# coding: utf-8

from __future__ import absolute_import

import time

from cardpay import *
from config import *
from recurrings import do_cancel_subscription, create_recurring_request, fetch_recurring, create_recurring_plan_request
from recurrings.scheduled import do_create_plan
from utils.http_utils import do_get

logger = create_logger(__name__)

config = Configuration(base_url=CARDPAY_API_URL, terminal_code=GATEWAY_POSTPONED_TERMINAL_CODE, password=GATEWAY_POSTPONED_PASSWORD, debug=DEBUG_MODE)
recurrings = RecurringsApi(ApiClient(config))
subscription_id = None


def teardown_function():
    global subscription_id
    do_cancel_subscription(recurrings, subscription_id) if subscription_id is not None else None


def test_hold_subscription():
    global subscription_id

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Phase 1:  prepare a new plan
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    plan_id = do_create_plan(recurrings)

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Phase 2:  create scheduled subscription
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    recurring_request = create_recurring_request(plan_id=plan_id)

    # perform create scheduled subscription
    creation_response = recurrings.create_recurring(recurring_request)
    logger.info(creation_response)

    # get redirect url
    redirect_url = creation_response.redirect_url
    assert redirect_url is not None

    # Emulate customer behaviour performing GET request to redirect url
    do_get(redirect_url)

    recurring_response = fetch_recurring(recurrings, recurring_request.merchant_order.id)
    assert recurring_response is not None

    subscription_id = recurring_response.recurring_data.subscription.id

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Phase 3: Change status of Scheduled subscription to INACTIVE
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    time.sleep(2)

    # prepare subscription update request data
    request = SubscriptionUpdateRequest(
        request=ApiClient.uuid_request(),
        operation=SubscriptionUpdateRequest.Operation.CHANGE_STATUS,
        subscription_data=SubscriptionUpdateRequestSubscriptionData(status_to=SubscriptionUpdateRequestSubscriptionData.StatusTo.INACTIVE)
    )

    response = recurrings.update_subscription(subscription_id, request)
    assert response is not None

    # explore response result
    data = response.subscription_data
    assert data.is_executed
    assert data.StatusTo.INACTIVE == data.status_to
