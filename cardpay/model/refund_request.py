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

from cardpay.model.refund_request_customer import (
    RefundRequestCustomer,
)  # noqa: F401,E501
from cardpay.model.refund_request_e_wallet_account import (
    RefundRequestEWalletAccount,
)  # noqa: F401,E501
from cardpay.model.refund_request_merchant_order import (
    RefundRequestMerchantOrder,
)  # noqa: F401,E501
from cardpay.model.refund_request_payment_data import (
    RefundRequestPaymentData,
)  # noqa: F401,E501
from cardpay.model.refund_request_refund_data import (
    RefundRequestRefundData,
)  # noqa: F401,E501
from cardpay.model.request import Request  # noqa: F401,E501


class RefundRequest(object):
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
        "customer": "RefundRequestCustomer",
        "ewallet_account": "RefundRequestEWalletAccount",
        "merchant_order": "RefundRequestMerchantOrder",
        "payment_data": "RefundRequestPaymentData",
        "refund_data": "RefundRequestRefundData",
    }

    attribute_map = {
        "request": "request",
        "customer": "customer",
        "ewallet_account": "ewallet_account",
        "merchant_order": "merchant_order",
        "payment_data": "payment_data",
        "refund_data": "refund_data",
    }

    def __init__(
        self,
        request=None,
        customer=None,
        ewallet_account=None,
        merchant_order=None,
        payment_data=None,
        refund_data=None,
    ):  # noqa: E501
        """RefundRequest - a model defined in Swagger"""  # noqa: E501

        self._request = None
        self._customer = None
        self._ewallet_account = None
        self._merchant_order = None
        self._payment_data = None
        self._refund_data = None
        self.discriminator = None

        self.request = request
        if customer is not None:
            self.customer = customer
        if ewallet_account is not None:
            self.ewallet_account = ewallet_account
        if merchant_order is not None:
            self.merchant_order = merchant_order
        self.payment_data = payment_data
        if refund_data is not None:
            self.refund_data = refund_data

    @property
    def request(self):
        """Gets the request of this RefundRequest.  # noqa: E501

        Request  # noqa: E501

        :return: The request of this RefundRequest.  # noqa: E501
        :rtype: Request
        """
        return self._request

    @request.setter
    def request(self, request):
        """Sets the request of this RefundRequest.

        Request  # noqa: E501

        :param request: The request of this RefundRequest.  # noqa: E501
        :type: Request
        """
        if request is None:
            raise ValueError(
                "Invalid value for `request`, must not be `None`"
            )  # noqa: E501

        self._request = request

    @property
    def customer(self):
        """Gets the customer of this RefundRequest.  # noqa: E501

        Customer  # noqa: E501

        :return: The customer of this RefundRequest.  # noqa: E501
        :rtype: RefundRequestCustomer
        """
        return self._customer

    @customer.setter
    def customer(self, customer):
        """Sets the customer of this RefundRequest.

        Customer  # noqa: E501

        :param customer: The customer of this RefundRequest.  # noqa: E501
        :type: RefundRequestCustomer
        """

        self._customer = customer

    @property
    def ewallet_account(self):
        """Gets the ewallet_account of this RefundRequest.  # noqa: E501

        EWallet  # noqa: E501

        :return: The ewallet_account of this RefundRequest.  # noqa: E501
        :rtype: RefundRequestEWalletAccount
        """
        return self._ewallet_account

    @ewallet_account.setter
    def ewallet_account(self, ewallet_account):
        """Sets the ewallet_account of this RefundRequest.

        EWallet  # noqa: E501

        :param ewallet_account: The ewallet_account of this RefundRequest.  # noqa: E501
        :type: RefundRequestEWalletAccount
        """

        self._ewallet_account = ewallet_account

    @property
    def merchant_order(self):
        """Gets the merchant_order of this RefundRequest.  # noqa: E501

        Merchant order data  # noqa: E501

        :return: The merchant_order of this RefundRequest.  # noqa: E501
        :rtype: RefundRequestMerchantOrder
        """
        return self._merchant_order

    @merchant_order.setter
    def merchant_order(self, merchant_order):
        """Sets the merchant_order of this RefundRequest.

        Merchant order data  # noqa: E501

        :param merchant_order: The merchant_order of this RefundRequest.  # noqa: E501
        :type: RefundRequestMerchantOrder
        """

        self._merchant_order = merchant_order

    @property
    def payment_data(self):
        """Gets the payment_data of this RefundRequest.  # noqa: E501

        Payment data  # noqa: E501

        :return: The payment_data of this RefundRequest.  # noqa: E501
        :rtype: RefundRequestPaymentData
        """
        return self._payment_data

    @payment_data.setter
    def payment_data(self, payment_data):
        """Sets the payment_data of this RefundRequest.

        Payment data  # noqa: E501

        :param payment_data: The payment_data of this RefundRequest.  # noqa: E501
        :type: RefundRequestPaymentData
        """
        if payment_data is None:
            raise ValueError(
                "Invalid value for `payment_data`, must not be `None`"
            )  # noqa: E501

        self._payment_data = payment_data

    @property
    def refund_data(self):
        """Gets the refund_data of this RefundRequest.  # noqa: E501

        Refund data  # noqa: E501

        :return: The refund_data of this RefundRequest.  # noqa: E501
        :rtype: RefundRequestRefundData
        """
        return self._refund_data

    @refund_data.setter
    def refund_data(self, refund_data):
        """Sets the refund_data of this RefundRequest.

        Refund data  # noqa: E501

        :param refund_data: The refund_data of this RefundRequest.  # noqa: E501
        :type: RefundRequestRefundData
        """

        self._refund_data = refund_data

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
        if issubclass(RefundRequest, dict):
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
        if not isinstance(other, RefundRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
