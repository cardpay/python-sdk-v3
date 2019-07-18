# coding: utf-8

from __future__ import absolute_import

from cardpay import *
from config import *
from constants import CARD_NON3DS_CONFIRMED, PAYMENT_METHOD_BANKCARD
from utils.data_utils import fake, randomString, generateCardExpiration, generateAmount

logger = create_logger(__name__)

config = Configuration(base_url=CARDPAY_API_URL, terminal_code=GATEWAY_TERMINAL_CODE, password=GATEWAY_PASSWORD, debug=DEBUG_MODE)
payouts = PayoutsApi(ApiClient(config))


def test_create_payout():
    # merchant order data
    merchantOrderId = randomString(20)
    merchantDescription = fake.sentence()
    amount = generateAmount()
    currency = TERMINAL_CURRENCY
    note = fake.sentence()

    # card data
    cardPan = CARD_NON3DS_CONFIRMED
    cardHolder = fake.name()
    cardExpiration = formatExpirationDate(generateCardExpiration())

    # prepare request data
    request = PayoutRequest(
        request=ApiClient.uuid_request(),
        merchant_order=PayoutRequestMerchantOrder(
            id=merchantOrderId,
            description=merchantDescription
        ),
        payment_method=PAYMENT_METHOD_BANKCARD,
        payout_data=PayoutRequestPayoutData(
            currency=currency,
            amount=amount,
            note=note
        ),
        card_account=PayoutRequestCardAccount(
            recipient_info=cardHolder,
            card=PayoutRequestCard(
                pan=cardPan,
                expiration=cardExpiration
            )
        )
    )

    logger.info(request)

    # perform create payment
    response = payouts.create_payout(request)

    # explore response result
    assert response is not None
    assert response.payout_data.Status.COMPLETED == response.payout_data.status
