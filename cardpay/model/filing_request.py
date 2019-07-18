# coding: utf-8

"""
    CardPay REST API

    Welcome to the CardPay REST API. The CardPay API uses HTTP verbs and a REST resources endpoint structure (see more info about REST). Request and response payloads are formatted as JSON. Merchant uses API to create payments, refunds, payouts or recurrings, check or update transaction status and get information about created transactions. In API authentication process based on OAuth 2.0 standard. For recent changes see changelog section.  # noqa: E501

    OpenAPI spec version: 3.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from cardpay.model.filing_recurring_data import FilingRecurringData  # noqa: F401,E501
from cardpay.model.filing_request_merchant_order import FilingRequestMerchantOrder  # noqa: F401,E501
from cardpay.model.filing_request_subscription_data import FilingRequestSubscriptionData  # noqa: F401,E501
from cardpay.model.payment_request_card_account import PaymentRequestCardAccount  # noqa: F401,E501
from cardpay.model.recurring_customer import RecurringCustomer  # noqa: F401,E501
from cardpay.model.request import Request  # noqa: F401,E501
from cardpay.model.return_urls import ReturnUrls  # noqa: F401,E501


class FilingRequest(object):
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
        'request': 'Request',
        'card_account': 'PaymentRequestCardAccount',
        'customer': 'RecurringCustomer',
        'merchant_order': 'FilingRequestMerchantOrder',
        'payment_method': 'str',
        'recurring_data': 'FilingRecurringData',
        'return_urls': 'ReturnUrls',
        'subscription_data': 'FilingRequestSubscriptionData'
    }

    attribute_map = {
        'request': 'request',
        'card_account': 'card_account',
        'customer': 'customer',
        'merchant_order': 'merchant_order',
        'payment_method': 'payment_method',
        'recurring_data': 'recurring_data',
        'return_urls': 'return_urls',
        'subscription_data': 'subscription_data'
    }

    def __init__(self, request=None, card_account=None, customer=None, merchant_order=None, payment_method=None, recurring_data=None, return_urls=None, subscription_data=None):  # noqa: E501
        """FilingRequest - a model defined in Swagger"""  # noqa: E501

        self._request = None
        self._card_account = None
        self._customer = None
        self._merchant_order = None
        self._payment_method = None
        self._recurring_data = None
        self._return_urls = None
        self._subscription_data = None
        self.discriminator = None

        self.request = request
        if card_account is not None:
            self.card_account = card_account
        if customer is not None:
            self.customer = customer
        if merchant_order is not None:
            self.merchant_order = merchant_order
        self.payment_method = payment_method
        if recurring_data is not None:
            self.recurring_data = recurring_data
        if return_urls is not None:
            self.return_urls = return_urls
        if subscription_data is not None:
            self.subscription_data = subscription_data

    @property
    def request(self):
        """Gets the request of this FilingRequest.  # noqa: E501

        Request  # noqa: E501

        :return: The request of this FilingRequest.  # noqa: E501
        :rtype: Request
        """
        return self._request

    @request.setter
    def request(self, request):
        """Sets the request of this FilingRequest.

        Request  # noqa: E501

        :param request: The request of this FilingRequest.  # noqa: E501
        :type: Request
        """
        if request is None:
            raise ValueError("Invalid value for `request`, must not be `None`")  # noqa: E501

        self._request = request

    @property
    def card_account(self):
        """Gets the card_account of this FilingRequest.  # noqa: E501

        Card account  # noqa: E501

        :return: The card_account of this FilingRequest.  # noqa: E501
        :rtype: PaymentRequestCardAccount
        """
        return self._card_account

    @card_account.setter
    def card_account(self, card_account):
        """Sets the card_account of this FilingRequest.

        Card account  # noqa: E501

        :param card_account: The card_account of this FilingRequest.  # noqa: E501
        :type: PaymentRequestCardAccount
        """

        self._card_account = card_account

    @property
    def customer(self):
        """Gets the customer of this FilingRequest.  # noqa: E501

        Customer  # noqa: E501

        :return: The customer of this FilingRequest.  # noqa: E501
        :rtype: RecurringCustomer
        """
        return self._customer

    @customer.setter
    def customer(self, customer):
        """Sets the customer of this FilingRequest.

        Customer  # noqa: E501

        :param customer: The customer of this FilingRequest.  # noqa: E501
        :type: RecurringCustomer
        """

        self._customer = customer

    @property
    def merchant_order(self):
        """Gets the merchant_order of this FilingRequest.  # noqa: E501

        Merchant order  # noqa: E501

        :return: The merchant_order of this FilingRequest.  # noqa: E501
        :rtype: FilingRequestMerchantOrder
        """
        return self._merchant_order

    @merchant_order.setter
    def merchant_order(self, merchant_order):
        """Sets the merchant_order of this FilingRequest.

        Merchant order  # noqa: E501

        :param merchant_order: The merchant_order of this FilingRequest.  # noqa: E501
        :type: FilingRequestMerchantOrder
        """

        self._merchant_order = merchant_order

    @property
    def payment_method(self):
        """Gets the payment_method of this FilingRequest.  # noqa: E501

        Used payment method type name from payment methods list\"  # noqa: E501

        :return: The payment_method of this FilingRequest.  # noqa: E501
        :rtype: str
        """
        return self._payment_method

    @payment_method.setter
    def payment_method(self, payment_method):
        """Sets the payment_method of this FilingRequest.

        Used payment method type name from payment methods list\"  # noqa: E501

        :param payment_method: The payment_method of this FilingRequest.  # noqa: E501
        :type: str
        """
        if payment_method is None:
            raise ValueError("Invalid value for `payment_method`, must not be `None`")  # noqa: E501
        if payment_method is not None and len(payment_method) > 100:
            raise ValueError("Invalid value for `payment_method`, length must be less than or equal to `100`")  # noqa: E501
        if payment_method is not None and len(payment_method) < 1:
            raise ValueError("Invalid value for `payment_method`, length must be greater than or equal to `1`")  # noqa: E501

        self._payment_method = payment_method

    @property
    def recurring_data(self):
        """Gets the recurring_data of this FilingRequest.  # noqa: E501

        Recurring data  # noqa: E501

        :return: The recurring_data of this FilingRequest.  # noqa: E501
        :rtype: FilingRecurringData
        """
        return self._recurring_data

    @recurring_data.setter
    def recurring_data(self, recurring_data):
        """Sets the recurring_data of this FilingRequest.

        Recurring data  # noqa: E501

        :param recurring_data: The recurring_data of this FilingRequest.  # noqa: E501
        :type: FilingRecurringData
        """

        self._recurring_data = recurring_data

    @property
    def return_urls(self):
        """Gets the return_urls of this FilingRequest.  # noqa: E501

        Return URLs  # noqa: E501

        :return: The return_urls of this FilingRequest.  # noqa: E501
        :rtype: ReturnUrls
        """
        return self._return_urls

    @return_urls.setter
    def return_urls(self, return_urls):
        """Sets the return_urls of this FilingRequest.

        Return URLs  # noqa: E501

        :param return_urls: The return_urls of this FilingRequest.  # noqa: E501
        :type: ReturnUrls
        """

        self._return_urls = return_urls

    @property
    def subscription_data(self):
        """Gets the subscription_data of this FilingRequest.  # noqa: E501

        Subscription data  # noqa: E501

        :return: The subscription_data of this FilingRequest.  # noqa: E501
        :rtype: FilingRequestSubscriptionData
        """
        return self._subscription_data

    @subscription_data.setter
    def subscription_data(self, subscription_data):
        """Sets the subscription_data of this FilingRequest.

        Subscription data  # noqa: E501

        :param subscription_data: The subscription_data of this FilingRequest.  # noqa: E501
        :type: FilingRequestSubscriptionData
        """

        self._subscription_data = subscription_data

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                if value is not None:
                    result[attr] = value
        if issubclass(FilingRequest, dict):
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
        if not isinstance(other, FilingRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
