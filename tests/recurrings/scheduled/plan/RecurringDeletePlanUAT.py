# coding: utf-8

from __future__ import absolute_import

from cardpay import *
from config import *
from recurrings.scheduled import do_create_plan

logger = create_logger(__name__)

config = Configuration(base_url=CARDPAY_API_URL, terminal_code=GATEWAY_TERMINAL_CODE, password=GATEWAY_PASSWORD, debug=DEBUG_MODE)
recurrings = RecurringsApi(ApiClient(config))


def test_delete_plan():
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Phase 1: prepare a new plan
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    plan_id = do_create_plan(recurrings)

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Phase 2: delete plan
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    response = recurrings.delete_plan(plan_id)
    assert response is None
