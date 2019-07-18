# coding: utf-8

from __future__ import absolute_import

from cardpay import *
from config import *
from recurrings.scheduled import do_create_plan

logger = create_logger(__name__)

config = Configuration(base_url=CARDPAY_API_URL, terminal_code=GATEWAY_TERMINAL_CODE, password=GATEWAY_PASSWORD, debug=DEBUG_MODE)
recurrings = RecurringsApi(ApiClient(config))


def test_change_plan_status():
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Phase 1: prepare a new plan
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    plan_id = do_create_plan(recurrings)

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Phase 2: change plan status
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    # prepare request
    request = PlanUpdateRequest(
        request=ApiClient.uuid_request(),
        operation=PlanUpdateRequest.Operation.CHANGE_STATUS,
        plan_data=PlanUpdateRequestPlanData(status_to=PlanUpdateRequestPlanData.StatusTo.INACTIVE)
    )

    # perform operation
    response = recurrings.update_plan(plan_id, request)

    # explore response result
    assert response is not None
    data = response.plan_data

    assert data is not None
    assert data.is_executed
    assert data.StatusTo.INACTIVE == data.status_to
