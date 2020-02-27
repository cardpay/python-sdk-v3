# coding: utf-8

from __future__ import absolute_import

import cardpay
import pytest

from callback import read_file

from cardpay import *
from config import *
from cardpay.api_client import CallbackHandler

logger = create_logger(__name__)

client = ApiClient(baseUrl=CARDPAY_API_URL, terminal_code="", password="", callback_secret="pzQf529Wa0AV")
callback_processor = client.create_callback_processor()


class PaymentCallbackHandler(CallbackHandler):
    def process(self, callback):

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


# Preferred callback handler usage
callback_processor.register_handler(PaymentCallback, PaymentCallbackHandler())

# Invalid usage of CallbackHandler. Should be used class extended from CallbackHandler with implementation of process method.
callback_processor.register_handler(PayoutCallback, CallbackHandler())

# Use lambda function as callback handler
callback_processor.register_handler(RefundCallback, lambda callback: print(callback))

# Invalid object as handler
callback_processor.register_handler(RecurringCallback, object())


def test_process_callback_with_invalid_signature():
    #  payment callback structure example, JSON body
    json = read_file("fixtures/paymentCallback.json")

    # 'Signature' header example with invalid value
    signature = read_file("fixtures/paymentCallback_invalid.signature")

    with pytest.raises(Exception) as e:
        callback_processor.process(json, signature)

    assert str(e.value) == "Invalid callback signature"


def test_process_payment_callback():
    #  payment callback structure example, JSON body
    json = read_file("fixtures/paymentCallback.json")

    # 'Signature' header example
    signature = read_file("fixtures/paymentCallback.signature")

    callback_processor.process(json, signature)


def test_process_payout_callback():
    # payout callback structure example, JSON body
    json = read_file("fixtures/payoutCallback.json")

    # 'Signature' header example
    signature = read_file("fixtures/payoutCallback.signature")

    with pytest.raises(Exception) as e:
        callback_processor.process(json, signature)

    assert str(e.value) == "Please implement this method"


def test_process_refund_callback():
    # refund callback structure example, JSON body
    json = read_file("fixtures/refundCallback.json")

    # 'Signature' header example
    signature = read_file("fixtures/refundCallback.signature")

    callback_processor.process(json, signature)


def test_process_recurring_callback():
    # recurring callback structure example, JSON body
    json = read_file("fixtures/recurringCallback.json")

    # 'Signature' header example
    signature = read_file("fixtures/recurringCallback.signature")

    with pytest.raises(Exception) as e:
        callback_processor.process(json, signature)

    assert e.type == cardpay.api_client.CallbackException
    assert "Can not execute handler" in str(e.value)
