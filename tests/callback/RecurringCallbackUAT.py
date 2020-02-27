# coding: utf-8

from __future__ import absolute_import

import pytest
from callback import read_file
from cardpay import *
from config import *

logger = create_logger(__name__)

client = ApiClient(baseUrl=CARDPAY_API_URL, terminal_code="", password="", callback_secret="pzQf529Wa0AV")


def test_process_callback():
    # recurring callback structure example, JSON body
    json = read_file("fixtures/recurringCallback.json")

    # 'Signature' header example
    signature = read_file("fixtures/recurringCallback.signature")

    if not client.is_valid_signature(json, signature):

        pytest.fail("Incorrect signature")

    else:
        callback = client.from_json(json, RecurringCallback)

        print(callback)

        data = callback.recurring_data
        status = data.status
        if data.Status.COMPLETED == status:
            # ...
            pass
        elif data.Status.DECLINED == status:
            # ...
            pass
        else:
            # unknown action or unsupported status
            pass
