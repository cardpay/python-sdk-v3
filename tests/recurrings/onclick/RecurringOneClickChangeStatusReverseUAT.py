# coding: utf-8

from __future__ import absolute_import

from cardpay import *
from config import *
from constants import CARD_NON3DS_CONFIRMED
from recurrings.onclick import do_one_click_payment

logger = create_logger(__name__)

config = Configuration(base_url=CARDPAY_API_URL, terminal_code=GATEWAY_TERMINAL_CODE, password=GATEWAY_PASSWORD, debug=DEBUG_MODE)
recurrings = RecurringsApi(ApiClient(config))


def test_change_one_click_status_reverse():
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Phase 1: create initial recurring
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    # create one click recurring
    recurring_id = do_one_click_payment(recurrings, CARD_NON3DS_CONFIRMED)

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Phase 2: change one-click status (preauth complete operation)
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    # prepare request data to change one-click status
    request = RecurringPatchRequest(
        request=ApiClient.uuid_request(),
        operation=RecurringPatchRequest.Operation.CHANGE_STATUS,
        recurring_data=PaymentUpdateTransactionData(status_to=PaymentUpdateTransactionData.StatusTo.REVERSE)
    )

    # perform operations
    response = recurrings.update_recurring(recurring_id, request)
    assert response is not None

    # explore response result
    data = response.recurring_data
    assert data is not None

    assert data.Status.VOIDED == data.status
