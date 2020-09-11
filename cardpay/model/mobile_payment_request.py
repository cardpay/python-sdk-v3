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

from cardpay.model.mobile_payment_merchant_order import (
    MobilePaymentMerchantOrder,
)  # noqa: F401,E501
from cardpay.model.payment_request_card_account import (
    PaymentRequestCardAccount,
)  # noqa: F401,E501
from cardpay.model.payment_request_customer import (
    PaymentRequestCustomer,
)  # noqa: F401,E501
from cardpay.model.payment_request_payment_data import (
    PaymentRequestPaymentData,
)  # noqa: F401,E501
from cardpay.model.request import Request  # noqa: F401,E501
from cardpay.model.return_urls import ReturnUrls  # noqa: F401,E501


class MobilePaymentRequest(object):
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
        "card_account": "PaymentRequestCardAccount",
        "customer": "PaymentRequestCustomer",
        "merchant_order": "MobilePaymentMerchantOrder",
        "mobile_token": "str",
        "payment_data": "PaymentRequestPaymentData",
        "payment_method": "str",
        "return_urls": "ReturnUrls",
    }

    attribute_map = {
        "request": "request",
        "card_account": "card_account",
        "customer": "customer",
        "merchant_order": "merchant_order",
        "mobile_token": "mobile_token",
        "payment_data": "payment_data",
        "payment_method": "payment_method",
        "return_urls": "return_urls",
    }

    def __init__(
        self,
        request=None,
        card_account=None,
        customer=None,
        merchant_order=None,
        mobile_token=None,
        payment_data=None,
        payment_method=None,
        return_urls=None,
    ):  # noqa: E501
        """MobilePaymentRequest - a model defined in Swagger"""  # noqa: E501

        self._request = None
        self._card_account = None
        self._customer = None
        self._merchant_order = None
        self._mobile_token = None
        self._payment_data = None
        self._payment_method = None
        self._return_urls = None
        self.discriminator = None

        self.request = request
        self.card_account = card_account
        self.customer = customer
        self.merchant_order = merchant_order
        if mobile_token is not None:
            self.mobile_token = mobile_token
        self.payment_data = payment_data
        if payment_method is not None:
            self.payment_method = payment_method
        if return_urls is not None:
            self.return_urls = return_urls

    @property
    def request(self):
        """Gets the request of this MobilePaymentRequest.  # noqa: E501

        Request  # noqa: E501

        :return: The request of this MobilePaymentRequest.  # noqa: E501
        :rtype: Request
        """
        return self._request

    @request.setter
    def request(self, request):
        """Sets the request of this MobilePaymentRequest.

        Request  # noqa: E501

        :param request: The request of this MobilePaymentRequest.  # noqa: E501
        :type: Request
        """
        if request is None:
            raise ValueError(
                "Invalid value for `request`, must not be `None`"
            )  # noqa: E501

        self._request = request

    @property
    def card_account(self):
        """Gets the card_account of this MobilePaymentRequest.  # noqa: E501

        Information about card *(for BANKCARD payment method only)*  # noqa: E501

        :return: The card_account of this MobilePaymentRequest.  # noqa: E501
        :rtype: PaymentRequestCardAccount
        """
        return self._card_account

    @card_account.setter
    def card_account(self, card_account):
        """Sets the card_account of this MobilePaymentRequest.

        Information about card *(for BANKCARD payment method only)*  # noqa: E501

        :param card_account: The card_account of this MobilePaymentRequest.  # noqa: E501
        :type: PaymentRequestCardAccount
        """
        if card_account is None:
            raise ValueError(
                "Invalid value for `card_account`, must not be `None`"
            )  # noqa: E501

        self._card_account = card_account

    @property
    def customer(self):
        """Gets the customer of this MobilePaymentRequest.  # noqa: E501

        Customer data  # noqa: E501

        :return: The customer of this MobilePaymentRequest.  # noqa: E501
        :rtype: PaymentRequestCustomer
        """
        return self._customer

    @customer.setter
    def customer(self, customer):
        """Sets the customer of this MobilePaymentRequest.

        Customer data  # noqa: E501

        :param customer: The customer of this MobilePaymentRequest.  # noqa: E501
        :type: PaymentRequestCustomer
        """
        if customer is None:
            raise ValueError(
                "Invalid value for `customer`, must not be `None`"
            )  # noqa: E501

        self._customer = customer

    @property
    def merchant_order(self):
        """Gets the merchant_order of this MobilePaymentRequest.  # noqa: E501

        Merchant order data  # noqa: E501

        :return: The merchant_order of this MobilePaymentRequest.  # noqa: E501
        :rtype: MobilePaymentMerchantOrder
        """
        return self._merchant_order

    @merchant_order.setter
    def merchant_order(self, merchant_order):
        """Sets the merchant_order of this MobilePaymentRequest.

        Merchant order data  # noqa: E501

        :param merchant_order: The merchant_order of this MobilePaymentRequest.  # noqa: E501
        :type: MobilePaymentMerchantOrder
        """
        if merchant_order is None:
            raise ValueError(
                "Invalid value for `merchant_order`, must not be `None`"
            )  # noqa: E501

        self._merchant_order = merchant_order

    @property
    def mobile_token(self):
        """Gets the mobile_token of this MobilePaymentRequest.  # noqa: E501

        Unique identifier, max 128 symbols  # noqa: E501

        :return: The mobile_token of this MobilePaymentRequest.  # noqa: E501
        :rtype: str
        """
        return self._mobile_token

    @mobile_token.setter
    def mobile_token(self, mobile_token):
        """Sets the mobile_token of this MobilePaymentRequest.

        Unique identifier, max 128 symbols  # noqa: E501

        :param mobile_token: The mobile_token of this MobilePaymentRequest.  # noqa: E501
        :type: str
        """

        self._mobile_token = mobile_token

    @property
    def payment_data(self):
        """Gets the payment_data of this MobilePaymentRequest.  # noqa: E501

        Payment data  # noqa: E501

        :return: The payment_data of this MobilePaymentRequest.  # noqa: E501
        :rtype: PaymentRequestPaymentData
        """
        return self._payment_data

    @payment_data.setter
    def payment_data(self, payment_data):
        """Sets the payment_data of this MobilePaymentRequest.

        Payment data  # noqa: E501

        :param payment_data: The payment_data of this MobilePaymentRequest.  # noqa: E501
        :type: PaymentRequestPaymentData
        """
        if payment_data is None:
            raise ValueError(
                "Invalid value for `payment_data`, must not be `None`"
            )  # noqa: E501

        self._payment_data = payment_data

    @property
    def payment_method(self):
        """Gets the payment_method of this MobilePaymentRequest.  # noqa: E501

        Used payment method type name from payment methods list  # noqa: E501

        :return: The payment_method of this MobilePaymentRequest.  # noqa: E501
        :rtype: str
        """
        return self._payment_method

    @payment_method.setter
    def payment_method(self, payment_method):
        """Sets the payment_method of this MobilePaymentRequest.

        Used payment method type name from payment methods list  # noqa: E501

        :param payment_method: The payment_method of this MobilePaymentRequest.  # noqa: E501
        :type: str
        """

        self._payment_method = payment_method

    @property
    def return_urls(self):
        """Gets the return_urls of this MobilePaymentRequest.  # noqa: E501

        Return URLs are the URLs where Customer returns by pressing 'Back to the shop' or 'Cancel' button in Payment page mode and redirected automatically in Gateway mode  # noqa: E501

        :return: The return_urls of this MobilePaymentRequest.  # noqa: E501
        :rtype: ReturnUrls
        """
        return self._return_urls

    @return_urls.setter
    def return_urls(self, return_urls):
        """Sets the return_urls of this MobilePaymentRequest.

        Return URLs are the URLs where Customer returns by pressing 'Back to the shop' or 'Cancel' button in Payment page mode and redirected automatically in Gateway mode  # noqa: E501

        :param return_urls: The return_urls of this MobilePaymentRequest.  # noqa: E501
        :type: ReturnUrls
        """

        self._return_urls = return_urls

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
        if issubclass(MobilePaymentRequest, dict):
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
        if not isinstance(other, MobilePaymentRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
