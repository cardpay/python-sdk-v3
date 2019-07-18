# coding: utf-8

from cardpay import *
from config import *
from constants import PAYMENT_METHOD_BANKCARD

from utils.data_utils import fake, randomString, generateCardExpiration, generateAmount


def do_payout(api, pan):
    # prepare request data
    request = create_payout_request(pan)

    # perform api call
    response = api.create_payout(request)

    return response.payout_data.id


def create_payout_request(pan):
    return PayoutRequest(
        request=ApiClient.uuid_request(),
        merchant_order=PayoutRequestMerchantOrder(
            id=randomString(20),
            description=fake.sentence()
        ),
        payment_method=PAYMENT_METHOD_BANKCARD,
        payout_data=PayoutRequestPayoutData(
            currency=TERMINAL_CURRENCY,
            amount=generateAmount(),
            note=fake.sentence()
        ),
        card_account=PayoutRequestCardAccount(
            recipient_info=fake.name(),
            card=PayoutRequestCard(
                pan=pan,
                expiration=formatExpirationDate(generateCardExpiration())
            )
        )
    )
