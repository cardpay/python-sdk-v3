# coding: utf-8

from __future__ import absolute_import

import uuid

from cardpay import *
from config import *

logger = create_logger(__name__)

config = Configuration(base_url=CARDPAY_API_URL, terminal_code=GATEWAY_TERMINAL_CODE, password=GATEWAY_PASSWORD, debug=DEBUG_MODE)
limits = LimitsApi(ApiClient(config))


def test_get_limits_info():
    response = limits.get_limits_info(request_id=str(uuid.uuid4()))

    logger.info(response)

    assert response is not None
    assert len(response.remaining_limits.keys()) > 0
