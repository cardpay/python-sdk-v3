# coding: utf-8

"""
    CardPay REST API

    Welcome to the CardPay REST API. The CardPay API uses HTTP verbs and a [REST](https://en.wikipedia.org/wiki/Representational_state_transfer) resources endpoint structure (see more info about REST). Request and response payloads are formatted as JSON. Merchant uses API to create payments, refunds, payouts or recurrings, check or update transaction status and get information about created transactions. In API authentication process based on [OAuth 2.0](https://oauth.net/2/) standard. For recent changes see changelog section.  # noqa: E501

    OpenAPI spec version: 3.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from cardpay.model.payout_payment_data import PayoutPaymentData  # noqa: F401,E501
from cardpay.model.payout_request_card_account import (
    PayoutRequestCardAccount,
)  # noqa: F401,E501
from cardpay.model.payout_request_customer import (
    PayoutRequestCustomer,
)  # noqa: F401,E501
from cardpay.model.payout_request_e_wallet_account import (
    PayoutRequestEWalletAccount,
)  # noqa: F401,E501
from cardpay.model.payout_request_merchant_order import (
    PayoutRequestMerchantOrder,
)  # noqa: F401,E501
from cardpay.model.payout_request_payout_data import (
    PayoutRequestPayoutData,
)  # noqa: F401,E501
from cardpay.model.request import Request  # noqa: F401,E501


class PayoutRequest(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        "request": "Request",
        "card_account": "PayoutRequestCardAccount",
        "customer": "PayoutRequestCustomer",
        "ewallet_account": "PayoutRequestEWalletAccount",
        "merchant_order": "PayoutRequestMerchantOrder",
        "payment_data": "PayoutPaymentData",
        "payment_method": "str",
        "payout_data": "PayoutRequestPayoutData",
    }

    attribute_map = {
        "request": "request",
        "card_account": "card_account",
        "customer": "customer",
        "ewallet_account": "ewallet_account",
        "merchant_order": "merchant_order",
        "payment_data": "payment_data",
        "payment_method": "payment_method",
        "payout_data": "payout_data",
    }

    def __init__(
        self,
        request=None,
        card_account=None,
        customer=None,
        ewallet_account=None,
        merchant_order=None,
        payment_data=None,
        payment_method=None,
        payout_data=None,
    ):  # noqa: E501
        """PayoutRequest - a model defined in Swagger"""  # noqa: E501

        self._request = None
        self._card_account = None
        self._customer = None
        self._ewallet_account = None
        self._merchant_order = None
        self._payment_data = None
        self._payment_method = None
        self._payout_data = None
        self.discriminator = None

        self.request = request
        if card_account is not None:
            self.card_account = card_account
        if customer is not None:
            self.customer = customer
        if ewallet_account is not None:
            self.ewallet_account = ewallet_account
        self.merchant_order = merchant_order
        if payment_data is not None:
            self.payment_data = payment_data
        self.payment_method = payment_method
        self.payout_data = payout_data

    @property
    def request(self):
        """Gets the request of this PayoutRequest.  # noqa: E501

        Request  # noqa: E501

        :return: The request of this PayoutRequest.  # noqa: E501
        :rtype: Request
        """
        return self._request

    @request.setter
    def request(self, request):
        """Sets the request of this PayoutRequest.

        Request  # noqa: E501

        :param request: The request of this PayoutRequest.  # noqa: E501
        :type: Request
        """
        if request is None:
            raise ValueError(
                "Invalid value for `request`, must not be `None`"
            )  # noqa: E501

        self._request = request

    @property
    def card_account(self):
        """Gets the card_account of this PayoutRequest.  # noqa: E501

        Bank card account data *(for BANKCARD method only)*  # noqa: E501

        :return: The card_account of this PayoutRequest.  # noqa: E501
        :rtype: PayoutRequestCardAccount
        """
        return self._card_account

    @card_account.setter
    def card_account(self, card_account):
        """Sets the card_account of this PayoutRequest.

        Bank card account data *(for BANKCARD method only)*  # noqa: E501

        :param card_account: The card_account of this PayoutRequest.  # noqa: E501
        :type: PayoutRequestCardAccount
        """

        self._card_account = card_account

    @property
    def customer(self):
        """Gets the customer of this PayoutRequest.  # noqa: E501

        Customer data  # noqa: E501

        :return: The customer of this PayoutRequest.  # noqa: E501
        :rtype: PayoutRequestCustomer
        """
        return self._customer

    @customer.setter
    def customer(self, customer):
        """Sets the customer of this PayoutRequest.

        Customer data  # noqa: E501

        :param customer: The customer of this PayoutRequest.  # noqa: E501
        :type: PayoutRequestCustomer
        """

        self._customer = customer

    @property
    def ewallet_account(self):
        """Gets the ewallet_account of this PayoutRequest.  # noqa: E501

        eWallet account data *(for payout methods only)*  # noqa: E501

        :return: The ewallet_account of this PayoutRequest.  # noqa: E501
        :rtype: PayoutRequestEWalletAccount
        """
        return self._ewallet_account

    @ewallet_account.setter
    def ewallet_account(self, ewallet_account):
        """Sets the ewallet_account of this PayoutRequest.

        eWallet account data *(for payout methods only)*  # noqa: E501

        :param ewallet_account: The ewallet_account of this PayoutRequest.  # noqa: E501
        :type: PayoutRequestEWalletAccount
        """

        self._ewallet_account = ewallet_account

    @property
    def merchant_order(self):
        """Gets the merchant_order of this PayoutRequest.  # noqa: E501

        Merchant order  # noqa: E501

        :return: The merchant_order of this PayoutRequest.  # noqa: E501
        :rtype: PayoutRequestMerchantOrder
        """
        return self._merchant_order

    @merchant_order.setter
    def merchant_order(self, merchant_order):
        """Sets the merchant_order of this PayoutRequest.

        Merchant order  # noqa: E501

        :param merchant_order: The merchant_order of this PayoutRequest.  # noqa: E501
        :type: PayoutRequestMerchantOrder
        """
        if merchant_order is None:
            raise ValueError(
                "Invalid value for `merchant_order`, must not be `None`"
            )  # noqa: E501

        self._merchant_order = merchant_order

    @property
    def payment_data(self):
        """Gets the payment_data of this PayoutRequest.  # noqa: E501

        Payment data *(for BANKCARD method only)*  # noqa: E501

        :return: The payment_data of this PayoutRequest.  # noqa: E501
        :rtype: PayoutPaymentData
        """
        return self._payment_data

    @payment_data.setter
    def payment_data(self, payment_data):
        """Sets the payment_data of this PayoutRequest.

        Payment data *(for BANKCARD method only)*  # noqa: E501

        :param payment_data: The payment_data of this PayoutRequest.  # noqa: E501
        :type: PayoutPaymentData
        """

        self._payment_data = payment_data

    @property
    def payment_method(self):
        """Gets the payment_method of this PayoutRequest.  # noqa: E501

        Used payment method type name from methods list  # noqa: E501

        :return: The payment_method of this PayoutRequest.  # noqa: E501
        :rtype: str
        """
        return self._payment_method

    @payment_method.setter
    def payment_method(self, payment_method):
        """Sets the payment_method of this PayoutRequest.

        Used payment method type name from methods list  # noqa: E501

        :param payment_method: The payment_method of this PayoutRequest.  # noqa: E501
        :type: str
        """
        if payment_method is None:
            raise ValueError(
                "Invalid value for `payment_method`, must not be `None`"
            )  # noqa: E501
        if payment_method is not None and len(payment_method) > 50:
            raise ValueError(
                "Invalid value for `payment_method`, length must be less than or equal to `50`"
            )  # noqa: E501
        if payment_method is not None and len(payment_method) < 1:
            raise ValueError(
                "Invalid value for `payment_method`, length must be greater than or equal to `1`"
            )  # noqa: E501

        self._payment_method = payment_method

    @property
    def payout_data(self):
        """Gets the payout_data of this PayoutRequest.  # noqa: E501

        Payout data  # noqa: E501

        :return: The payout_data of this PayoutRequest.  # noqa: E501
        :rtype: PayoutRequestPayoutData
        """
        return self._payout_data

    @payout_data.setter
    def payout_data(self, payout_data):
        """Sets the payout_data of this PayoutRequest.

        Payout data  # noqa: E501

        :param payout_data: The payout_data of this PayoutRequest.  # noqa: E501
        :type: PayoutRequestPayoutData
        """
        if payout_data is None:
            raise ValueError(
                "Invalid value for `payout_data`, must not be `None`"
            )  # noqa: E501

        self._payout_data = payout_data

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(
                    map(lambda x: x.to_dict() if hasattr(x, "to_dict") else x, value)
                )
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(
                    map(
                        lambda item: (item[0], item[1].to_dict())
                        if hasattr(item[1], "to_dict")
                        else item,
                        value.items(),
                    )
                )
            else:
                if value is not None:
                    result[attr] = value
        if issubclass(PayoutRequest, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, PayoutRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
