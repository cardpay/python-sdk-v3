# coding: utf-8

from config import TERMINAL_CURRENCY
from recurrings import create_recurring_request, fetch_recurring
from utils.data_utils import generateAmount
from utils.http_utils import do_get


def do_one_click_payment(recurrings, pan):
    request = create_recurring_request(pan=pan, currency=TERMINAL_CURRENCY, amount=generateAmount(), preauth="true")
    response = recurrings.create_recurring(request)

    redirect_url = response.redirect_url
    assert redirect_url is not None

    do_get(response.redirect_url)

    recurring = fetch_recurring(recurrings, request.merchant_order.id)
    assert recurring is not None

    return recurring.recurring_data.id
