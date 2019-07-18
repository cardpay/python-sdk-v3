# coding: utf-8

from __future__ import absolute_import

from cardpay import *
from config import *
from constants import CARD_NON3DS_CONFIRMED
from payment import do_payment

logger = create_logger(__name__)

config = Configuration(base_url=CARDPAY_API_URL, terminal_code=GATEWAY_TERMINAL_CODE, password=GATEWAY_PASSWORD, debug=DEBUG_MODE)
payments = PaymentsApi(ApiClient(config))


def test_get_payment_information():
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Phase 1: create payment
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    # prepare payment in PENDING status
    payment_id = do_payment(payments, CARD_NON3DS_CONFIRMED, preauth=True)

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Phase 2: get payment information
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    # perform getting payment information
    response = payments.get_payment(payment_id)

    # explore response result
    assert response is not None
    assert response.payment_data.id == payment_id

    logger.info(response)
