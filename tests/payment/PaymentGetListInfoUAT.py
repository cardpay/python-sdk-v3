# coding: utf-8

from __future__ import absolute_import

import uuid

from cardpay import *
from config import *
from constants import CARD_NON3DS_CONFIRMED
from payment import do_payment

logger = create_logger(__name__)

config = Configuration(base_url=CARDPAY_API_URL, terminal_code=GATEWAY_TERMINAL_CODE, password=GATEWAY_PASSWORD, debug=DEBUG_MODE)
payments = PaymentsApi(ApiClient(config))


def test_get_payments_list_information():
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Generate payments
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    # prepare payments
    ids = {do_payment(payments, CARD_NON3DS_CONFIRMED) for _ in range(0, 3)}

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Fetch payments
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    currency = TERMINAL_CURRENCY
    maxCount = 50

    # perform api call
    response = payments.get_payments(
        request_id=str(uuid.uuid4()),
        currency=currency,
        max_count=maxCount
    )

    data = {p.payment_data.id for p in response.data}

    for p in response.data:
        logger.info("%s %f %s" % (p.payment_data.id, p.payment_data.amount, p.payment_data.currency))

    assert ids.issubset(data)
