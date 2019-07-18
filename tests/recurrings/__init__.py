# coding: utf-8
import uuid

from cardpay import *
from config import *
from constants import CARD_NON3DS_CONFIRMED, PAYMENT_METHOD_BANKCARD
from utils.data_utils import randomString, generateEmail, generateMerchantOrderId, fake, generateCardExpiration, generateAmount, randomBetween

logger = create_logger(__name__)


def do_cancel_subscription(recurrings, subscription_id):
    request = SubscriptionUpdateRequest(
        request=ApiClient.uuid_request(),
        operation=SubscriptionUpdateRequest.Operation.CHANGE_STATUS,
        subscription_data=SubscriptionUpdateRequestSubscriptionData(status_to=SubscriptionUpdateRequestSubscriptionData.StatusTo.CANCELLED)
    )
    print("\ndo_cancel_subscription: %s" % request)

    response = recurrings.update_subscription(subscription_id, request)
    print("do_cancel_subscription: %s" % response)

    assert response is not None
    return response


def create_recurring_plan_request():
    return RecurringPlanRequest(
        request=ApiClient.uuid_request(),
        plan_data=RecurringPlanRequestPlanData(
            currency=TERMINAL_CURRENCY,
            amount=generateAmount(10, 300),
            interval=randomBetween(1, 52),
            name=randomString(15),
            period=RecurringPlanRequestPlanData.Period.WEEK
        )
    )


def create_recurring_request(plan_id=None, pan=CARD_NON3DS_CONFIRMED, currency=None, amount=None, preauth=None):
    customer_id = randomString(15)
    result = RecurringCreationRequest(
        request=ApiClient.uuid_request(),
        customer=RecurringCustomer(
            id=customer_id,
            email=generateEmail(customer_id)
        ),
        merchant_order=PaymentRequestMerchantOrder(
            id=generateMerchantOrderId(),
            description=fake.sentence()
        ),
        payment_method=PAYMENT_METHOD_BANKCARD,
        card_account=PaymentRequestCardAccount(card=PaymentRequestCard(
            pan=pan,
            holder=fake.name().upper(),
            expiration=formatExpirationDate(generateCardExpiration()),
            security_code="123"
        )),
        recurring_data=RecurringRequestRecurringData(
            initiator="cit"
        ),
        return_urls=ReturnUrls(
            success_url=SUCCESS_URL,
            decline_url=DECLINE_URL,
            cancel_url=CANCEL_URL,
            inprocess_url=INPROCESS_URL
        )
    )

    if plan_id is not None:
        result.recurring_data.plan = Plan(plan_id)

    if currency is not None:
        result.recurring_data.currency = currency

    if amount is not None:
        result.recurring_data.amount = amount

    if preauth is not None:
        result.recurring_data.preauth = preauth

    return result


def fetch_recurring(recurrings, merchant_order_id):
    if recurrings is None or not len(merchant_order_id):
        return None

    response = recurrings.get_recurrings(
        request_id=str(uuid.uuid4()),
        merchant_order_id=merchant_order_id
    )

    assert response.data is not None

    return response.data[0] if len(response.data) > 0 else None
