# coding: utf-8

from __future__ import absolute_import

from cardpay import *
from config import *
from utils.data_utils import generateAmount, randomBetween, randomString

logger = create_logger(__name__)

config = Configuration(base_url=CARDPAY_API_URL, terminal_code=GATEWAY_TERMINAL_CODE, password=GATEWAY_PASSWORD, debug=DEBUG_MODE)
recurrings = RecurringsApi(ApiClient(config))


def test_create_new_plan():

    # prepare recurring plan request data
    request = RecurringPlanRequest(
        request=ApiClient.uuid_request(),
        plan_data=RecurringPlanRequestPlanData(
            currency=TERMINAL_CURRENCY,
            amount=generateAmount(10, 300),
            interval=randomBetween(1, 52),
            name=randomString(15),
            period=RecurringPlanRequestPlanData.Period.WEEK,
            retries=2
        )
    )

    # perform operation
    response = recurrings.create_plan(request)

    # explore response result
    assert response is not None
    assert response.plan_data is not None

    assert response.plan_data.Status.ACTIVE == response.plan_data.status
