# coding: utf-8
from constants import CARD_NON3DS_CONFIRMED
from recurrings import create_recurring_plan_request, create_recurring_request, fetch_recurring
from utils.http_utils import do_get


def do_create_plan(recurrings):
    request = create_recurring_plan_request()
    response = recurrings.create_plan(request)
    assert response is not None

    assert response.plan_data is not None
    return response.plan_data.id


def do_create_subscription(recurrings, pan=CARD_NON3DS_CONFIRMED, plan_id=None):
    request = create_recurring_request(pan=pan, plan_id=plan_id)
    response = recurrings.create_recurring(request)

    redirect_url = response.redirect_url
    assert redirect_url is not None

    do_get(response.redirect_url)

    recurring = fetch_recurring(recurrings, request.merchant_order.id)
    assert recurring is not None
    assert recurring.recurring_data is not None
    assert recurring.recurring_data.subscription is not None

    return recurring.recurring_data.subscription.id
