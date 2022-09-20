# coding: utf-8

# flake8: noqa

"""
    CardPay REST API

    Welcome to the CardPay REST API. The CardPay API uses HTTP verbs and a [REST](https://en.wikipedia.org/wiki/Representational_state_transfer) resources endpoint structure (see more info about REST). Request and response payloads are formatted as JSON. Merchant uses API to create payments, refunds, payouts or recurrings, check or update transaction status and get information about created transactions. In API authentication process based on [OAuth 2.0](https://oauth.net/2/) standard. For recent changes see changelog section.  # noqa: E501

    OpenAPI spec version: 3.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

# import ApiClient
from cardpay.api_client import ApiClient
from cardpay.configuration import Configuration

# import models into sdk package
from cardpay.model.api_error import ApiError
from cardpay.model.api_tokens import ApiTokens
from cardpay.model.authentication_customer import AuthenticationCustomer
from cardpay.model.authentication_data import AuthenticationData
from cardpay.model.authentication_data_response import AuthenticationDataResponse
from cardpay.model.authentication_error import AuthenticationError
from cardpay.model.bad_request_error import BadRequestError
from cardpay.model.bank_card_payout_data import BankCardPayoutData
from cardpay.model.billing_address import BillingAddress
from cardpay.model.card_info_request import CardInfoRequest
from cardpay.model.card_info_response import CardInfoResponse
from cardpay.model.change_subscription_status_claim_response import (
    ChangeSubscriptionStatusClaimResponse,
)
from cardpay.model.changed_plan_data import ChangedPlanData
from cardpay.model.claim_response_subscription_data import ClaimResponseSubscriptionData
from cardpay.model.confirm3ds_request import Confirm3dsRequest
from cardpay.model.dispute_list import DisputeList
from cardpay.model.dispute_response import DisputeResponse
from cardpay.model.dispute_response_card import DisputeResponseCard
from cardpay.model.dispute_response_card_account import DisputeResponseCardAccount
from cardpay.model.dispute_response_customer import DisputeResponseCustomer
from cardpay.model.dispute_response_dispute_data import DisputeResponseDisputeData
from cardpay.model.dispute_response_merchant_order import DisputeResponseMerchantOrder
from cardpay.model.dispute_response_payment_data import DisputeResponsePaymentData
from cardpay.model.filing_recurring_data import FilingRecurringData
from cardpay.model.filing_request import FilingRequest
from cardpay.model.filing_request_merchant_order import FilingRequestMerchantOrder
from cardpay.model.filing_request_subscription_data import FilingRequestSubscriptionData
from cardpay.model.filter_parameters import FilterParameters
from cardpay.model.flight import Flight
from cardpay.model.flights import Flights
from cardpay.model.installment_data import InstallmentData
from cardpay.model.item import Item
from cardpay.model.limit_info_response import LimitInfoResponse
from cardpay.model.next_subscription_payment import NextSubscriptionPayment
from cardpay.model.not_found_error import NotFoundError
from cardpay.model.o_auth_error import OAuthError
from cardpay.model.oneclick_data import OneclickData
from cardpay.model.payment_callback import PaymentCallback
from cardpay.model.payment_gateway_creation_response import (
    PaymentGatewayCreationResponse,
)
from cardpay.model.payment_gateway_response_payment_data import (
    PaymentGatewayResponsePaymentData,
)
from cardpay.model.payment_methods_response import PaymentMethodsResponse
from cardpay.model.payment_patch_request import PaymentPatchRequest
from cardpay.model.payment_request import PaymentRequest
from cardpay.model.payment_request_card import PaymentRequestCard
from cardpay.model.payment_request_card_account import PaymentRequestCardAccount
from cardpay.model.payment_request_cryptocurrency_account import (
    PaymentRequestCryptocurrencyAccount,
)
from cardpay.model.payment_request_customer import PaymentRequestCustomer
from cardpay.model.payment_request_e_wallet_account import PaymentRequestEWalletAccount
from cardpay.model.payment_request_living_address import PaymentRequestLivingAddress
from cardpay.model.payment_request_merchant_order import PaymentRequestMerchantOrder
from cardpay.model.payment_request_payment_data import PaymentRequestPaymentData
from cardpay.model.payment_response import PaymentResponse
from cardpay.model.payment_response_card_account import PaymentResponseCardAccount
from cardpay.model.payment_response_cryptocurrency_account import (
    PaymentResponseCryptocurrencyAccount,
)
from cardpay.model.payment_response_customer import PaymentResponseCustomer
from cardpay.model.payment_response_payment_data import PaymentResponsePaymentData
from cardpay.model.payment_update_response import PaymentUpdateResponse
from cardpay.model.payment_update_transaction_data import PaymentUpdateTransactionData
from cardpay.model.payments_list import PaymentsList
from cardpay.model.payout_callback import PayoutCallback
from cardpay.model.payout_creation_response import PayoutCreationResponse
from cardpay.model.payout_payment_data import PayoutPaymentData
from cardpay.model.payout_request import PayoutRequest
from cardpay.model.payout_request_card import PayoutRequestCard
from cardpay.model.payout_request_card_account import PayoutRequestCardAccount
from cardpay.model.payout_request_cryptocurrency_account import (
    PayoutRequestCryptocurrencyAccount,
)
from cardpay.model.payout_request_customer import PayoutRequestCustomer
from cardpay.model.payout_request_e_wallet_account import PayoutRequestEWalletAccount
from cardpay.model.payout_request_living_address import PayoutRequestLivingAddress
from cardpay.model.payout_request_merchant_order import PayoutRequestMerchantOrder
from cardpay.model.payout_request_payout_data import PayoutRequestPayoutData
from cardpay.model.payout_response import PayoutResponse
from cardpay.model.payout_response_card import PayoutResponseCard
from cardpay.model.payout_response_card_account import PayoutResponseCardAccount
from cardpay.model.payout_response_cryptocurrency_account import (
    PayoutResponseCryptocurrencyAccount,
)
from cardpay.model.payout_response_customer import PayoutResponseCustomer
from cardpay.model.payout_response_e_wallet_account import PayoutResponseEWalletAccount
from cardpay.model.payout_response_payout_data import PayoutResponsePayoutData
from cardpay.model.payout_update_request import PayoutUpdateRequest
from cardpay.model.payout_update_response import PayoutUpdateResponse
from cardpay.model.payouts_list import PayoutsList
from cardpay.model.plan import Plan
from cardpay.model.plan_data_list import PlanDataList
from cardpay.model.plan_update_request import PlanUpdateRequest
from cardpay.model.plan_update_request_plan_data import PlanUpdateRequestPlanData
from cardpay.model.plan_update_response import PlanUpdateResponse
from cardpay.model.recurring_callback import RecurringCallback
from cardpay.model.recurring_creation_request import RecurringCreationRequest
from cardpay.model.recurring_customer import RecurringCustomer
from cardpay.model.recurring_filter_parameters import RecurringFilterParameters
from cardpay.model.recurring_gateway_creation_response import (
    RecurringGatewayCreationResponse,
)
from cardpay.model.recurring_gateway_response_recurring_data import (
    RecurringGatewayResponseRecurringData,
)
from cardpay.model.recurring_patch_request import RecurringPatchRequest
from cardpay.model.recurring_plan_request import RecurringPlanRequest
from cardpay.model.recurring_plan_request_plan_data import RecurringPlanRequestPlanData
from cardpay.model.recurring_plan_response import RecurringPlanResponse
from cardpay.model.recurring_request_filing import RecurringRequestFiling
from cardpay.model.recurring_request_recurring_data import RecurringRequestRecurringData
from cardpay.model.recurring_response import RecurringResponse
from cardpay.model.recurring_response_filing import RecurringResponseFiling
from cardpay.model.recurring_response_merchant_order import (
    RecurringResponseMerchantOrder,
)
from cardpay.model.recurring_response_recurring_data import (
    RecurringResponseRecurringData,
)
from cardpay.model.recurring_update_response import RecurringUpdateResponse
from cardpay.model.recurrings_list import RecurringsList
from cardpay.model.redirect_url_response import RedirectUrlResponse
from cardpay.model.refund_callback import RefundCallback
from cardpay.model.refund_request import RefundRequest
from cardpay.model.refund_request_customer import RefundRequestCustomer
from cardpay.model.refund_request_e_wallet_account import RefundRequestEWalletAccount
from cardpay.model.refund_request_merchant_order import RefundRequestMerchantOrder
from cardpay.model.refund_request_payment_data import RefundRequestPaymentData
from cardpay.model.refund_request_refund_data import RefundRequestRefundData
from cardpay.model.refund_response import RefundResponse
from cardpay.model.refund_response_card import RefundResponseCard
from cardpay.model.refund_response_card_account import RefundResponseCardAccount
from cardpay.model.refund_response_customer import RefundResponseCustomer
from cardpay.model.refund_response_e_wallet_account import RefundResponseEWalletAccount
from cardpay.model.refund_response_payment_data import RefundResponsePaymentData
from cardpay.model.refund_response_refund_data import RefundResponseRefundData
from cardpay.model.refund_update_request import RefundUpdateRequest
from cardpay.model.refund_update_response import RefundUpdateResponse
from cardpay.model.refunds_list import RefundsList
from cardpay.model.renamed_plan_data import RenamedPlanData
from cardpay.model.report import Report
from cardpay.model.reports_data import ReportsData
from cardpay.model.reports_request import ReportsRequest
from cardpay.model.reports_response import ReportsResponse
from cardpay.model.request import Request
from cardpay.model.request_updated_transaction_data import RequestUpdatedTransactionData
from cardpay.model.response_plan_data import ResponsePlanData
from cardpay.model.response_updated_transaction_data import (
    ResponseUpdatedTransactionData,
)
from cardpay.model.return_urls import ReturnUrls
from cardpay.model.scheduled_by_merchant_data import ScheduledByMerchantData
from cardpay.model.scheduled_data import ScheduledData
from cardpay.model.shipping_address import ShippingAddress
from cardpay.model.subscription import Subscription
from cardpay.model.subscription_customer import SubscriptionCustomer
from cardpay.model.subscription_filter_parameters import SubscriptionFilterParameters
from cardpay.model.subscription_get_response import SubscriptionGetResponse
from cardpay.model.subscription_get_response_plan import SubscriptionGetResponsePlan
from cardpay.model.subscription_list import SubscriptionList
from cardpay.model.subscription_update_request import SubscriptionUpdateRequest
from cardpay.model.subscription_update_request_subscription_data import (
    SubscriptionUpdateRequestSubscriptionData,
)
from cardpay.model.subscription_update_response import SubscriptionUpdateResponse
from cardpay.model.supported_payment_method import SupportedPaymentMethod
from cardpay.model.three_d_secure_data import ThreeDSecureData
from cardpay.model.three_d_secure_response import ThreeDSecureResponse
from cardpay.model.transaction_methods_list import TransactionMethodsList
from cardpay.model.transaction_request import TransactionRequest
from cardpay.model.transaction_response_e_wallet_account import (
    TransactionResponseEWalletAccount,
)
from cardpay.model.transaction_response_merchant_order import (
    TransactionResponseMerchantOrder,
)
from cardpay.model.transaction_update_request import TransactionUpdateRequest
from cardpay.model.updated_plan_data import UpdatedPlanData
from cardpay.model.updated_subscription_data import UpdatedSubscriptionData
from cardpay.model.updated_subscription_recurring_data import (
    UpdatedSubscriptionRecurringData,
)
from cardpay.model.payment_confirm3ds_request import PaymentConfirm3dsRequest
from cardpay.model.payment_execute_request import PaymentExecuteRequest
from cardpay.model.payment_update_request import PaymentUpdateRequest
from cardpay.model.recurring_confirm3ds_request import RecurringConfirm3dsRequest
from cardpay.model.recurring_execute_request import RecurringExecuteRequest
from cardpay.model.recurring_update_request import RecurringUpdateRequest


# import apis into api package
from cardpay.api.auth_api import AuthApi
from cardpay.api.card_info_api import CardInfoApi
from cardpay.api.limits_api import LimitsApi
from cardpay.api.payments_api import PaymentsApi
from cardpay.api.payouts_api import PayoutsApi
from cardpay.api.recurrings_api import RecurringsApi
from cardpay.api.refunds_api import RefundsApi
from cardpay.api.reports_api_controller_api import ReportsApiControllerApi


def formatExpirationDate(date):
    return date.strftime("%m/%Y")


def formatBirthDate(date):
    return date.strftime("%Y-%m-%d")
