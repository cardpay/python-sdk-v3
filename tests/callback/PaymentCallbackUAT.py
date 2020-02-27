# coding: utf-8

from __future__ import absolute_import

import pytest
from callback import read_file
from cardpay import *
from config import *

logger = create_logger(__name__)

client = ApiClient(baseUrl=CARDPAY_API_URL, terminal_code="", password="", callback_secret="pzQf529Wa0AV")


def test_check_callback_signature():
    # given
    json = read_file("fixtures/paymentCallback.json")
    expected_signature = read_file("fixtures/paymentCallback.signature")

    # when
    signature = client.calc_signature(json)

    # then
    assert expected_signature == signature


def test_check_callback_invalid_signature():
    # given
    json = read_file("fixtures/paymentCallback.json")
    expected_signature = read_file("fixtures/paymentCallback_invalid.signature")

    # when
    signature = client.calc_signature(json)

    # then
    assert expected_signature != signature


def test_process_callback():
    # payment callback structure example, JSON body
    json = read_file("fixtures/paymentCallback.json")

    # 'Signature' header example
    signature = read_file("fixtures/paymentCallback.signature")

    if not client.is_valid_signature(json, signature):

        pytest.fail("Incorrect signature")

    else:
        callback = client.from_json(json, PaymentCallback)

        print(callback)

        data = callback.payment_data
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
