# coding: utf-8

from __future__ import absolute_import

from cardpay import *
from config import *
from utils.data_utils import generateAmount, randomBetween, randomString

logger = create_logger(__name__)

config = Configuration(base_url=CARDPAY_API_URL, terminal_code=GATEWAY_TERMINAL_CODE, password=GATEWAY_PASSWORD, debug=DEBUG_MODE)
recurrings = RecurringsApi(ApiClient(config))


def test_scheduled_subscription():
    # prepare request
    request = RecurringPlanRequest(
        request=ApiClient.uuid_request(),
        plan_data=RecurringPlanRequestPlanData(
            name=randomString(15),
            currency=TERMINAL_CURRENCY,
            amount=generateAmount(10, 300),
            interval=randomBetween(1, 52),
            period=RecurringPlanRequestPlanData.Period.WEEK,
            retries=2
        )
    )

    # perform create scheduled subscription
    response = recurrings.create_plan(request)
    assert response is not None

    assert response.plan_data is not None
    return response.plan_data.id
