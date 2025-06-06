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

from cardpay.model.invoice_customer import InvoiceCustomer  # noqa: F401,E501
from cardpay.model.invoice_get_data_response import (
    InvoiceGetDataResponse,
)  # noqa: F401,E501
from cardpay.model.invoice_merchant_order import InvoiceMerchantOrder  # noqa: F401,E501
from cardpay.model.payment_data import PaymentData  # noqa: F401,E501


class InvoiceGetResponse(object):
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
        "customer": "InvoiceCustomer",
        "invoice_data": "InvoiceGetDataResponse",
        "invoice_url": "str",
        "merchant_order": "InvoiceMerchantOrder",
        "payment_data": "list[PaymentData]",
    }

    attribute_map = {
        "customer": "customer",
        "invoice_data": "invoice_data",
        "invoice_url": "invoice_url",
        "merchant_order": "merchant_order",
        "payment_data": "payment_data",
    }

    def __init__(
        self,
        customer=None,
        invoice_data=None,
        invoice_url=None,
        merchant_order=None,
        payment_data=None,
    ):  # noqa: E501
        """InvoiceGetResponse - a model defined in Swagger"""  # noqa: E501

        self._customer = None
        self._invoice_data = None
        self._invoice_url = None
        self._merchant_order = None
        self._payment_data = None
        self.discriminator = None

        self.customer = customer
        self.invoice_data = invoice_data
        if invoice_url is not None:
            self.invoice_url = invoice_url
        self.merchant_order = merchant_order
        if payment_data is not None:
            self.payment_data = payment_data

    @property
    def customer(self):
        """Gets the customer of this InvoiceGetResponse.  # noqa: E501

        Customer data  # noqa: E501

        :return: The customer of this InvoiceGetResponse.  # noqa: E501
        :rtype: InvoiceCustomer
        """
        return self._customer

    @customer.setter
    def customer(self, customer):
        """Sets the customer of this InvoiceGetResponse.

        Customer data  # noqa: E501

        :param customer: The customer of this InvoiceGetResponse.  # noqa: E501
        :type: InvoiceCustomer
        """
        if customer is None:
            raise ValueError(
                "Invalid value for `customer`, must not be `None`"
            )  # noqa: E501

        self._customer = customer

    @property
    def invoice_data(self):
        """Gets the invoice_data of this InvoiceGetResponse.  # noqa: E501

        Invoice data  # noqa: E501

        :return: The invoice_data of this InvoiceGetResponse.  # noqa: E501
        :rtype: InvoiceGetDataResponse
        """
        return self._invoice_data

    @invoice_data.setter
    def invoice_data(self, invoice_data):
        """Sets the invoice_data of this InvoiceGetResponse.

        Invoice data  # noqa: E501

        :param invoice_data: The invoice_data of this InvoiceGetResponse.  # noqa: E501
        :type: InvoiceGetDataResponse
        """
        if invoice_data is None:
            raise ValueError(
                "Invalid value for `invoice_data`, must not be `None`"
            )  # noqa: E501

        self._invoice_data = invoice_data

    @property
    def invoice_url(self):
        """Gets the invoice_url of this InvoiceGetResponse.  # noqa: E501

        Invoice URL  # noqa: E501

        :return: The invoice_url of this InvoiceGetResponse.  # noqa: E501
        :rtype: str
        """
        return self._invoice_url

    @invoice_url.setter
    def invoice_url(self, invoice_url):
        """Sets the invoice_url of this InvoiceGetResponse.

        Invoice URL  # noqa: E501

        :param invoice_url: The invoice_url of this InvoiceGetResponse.  # noqa: E501
        :type: str
        """

        self._invoice_url = invoice_url

    @property
    def merchant_order(self):
        """Gets the merchant_order of this InvoiceGetResponse.  # noqa: E501

        Merchant order data  # noqa: E501

        :return: The merchant_order of this InvoiceGetResponse.  # noqa: E501
        :rtype: InvoiceMerchantOrder
        """
        return self._merchant_order

    @merchant_order.setter
    def merchant_order(self, merchant_order):
        """Sets the merchant_order of this InvoiceGetResponse.

        Merchant order data  # noqa: E501

        :param merchant_order: The merchant_order of this InvoiceGetResponse.  # noqa: E501
        :type: InvoiceMerchantOrder
        """
        if merchant_order is None:
            raise ValueError(
                "Invalid value for `merchant_order`, must not be `None`"
            )  # noqa: E501

        self._merchant_order = merchant_order

    @property
    def payment_data(self):
        """Gets the payment_data of this InvoiceGetResponse.  # noqa: E501


        :return: The payment_data of this InvoiceGetResponse.  # noqa: E501
        :rtype: list[PaymentData]
        """
        return self._payment_data

    @payment_data.setter
    def payment_data(self, payment_data):
        """Sets the payment_data of this InvoiceGetResponse.


        :param payment_data: The payment_data of this InvoiceGetResponse.  # noqa: E501
        :type: list[PaymentData]
        """

        self._payment_data = payment_data

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
        if issubclass(InvoiceGetResponse, dict):
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
        if not isinstance(other, InvoiceGetResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
