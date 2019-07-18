# coding: utf-8

from __future__ import absolute_import

from cardpay import *
from config import *

logger = create_logger(__name__)

config = Configuration(base_url=CARDPAY_API_URL, terminal_code=GATEWAY_TERMINAL_CODE, password=GATEWAY_PASSWORD, debug=DEBUG_MODE)
recurrings = RecurringsApi(ApiClient(config))


def test_continue_one_click_payment():
    # TODO
    pass
