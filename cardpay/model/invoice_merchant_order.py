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

from cardpay.model.invoice_item import InvoiceItem  # noqa: F401,E501


class InvoiceMerchantOrder(object):
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
    swagger_types = {"id": "str", "items": "list[InvoiceItem]"}

    attribute_map = {"id": "id", "items": "items"}

    def __init__(self, id=None, items=None):  # noqa: E501
        """InvoiceMerchantOrder - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._items = None
        self.discriminator = None

        self.id = id
        self.items = items

    @property
    def id(self):
        """Gets the id of this InvoiceMerchantOrder.  # noqa: E501

        Order ID used by the merchant’s shopping cart  # noqa: E501

        :return: The id of this InvoiceMerchantOrder.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this InvoiceMerchantOrder.

        Order ID used by the merchant’s shopping cart  # noqa: E501

        :param id: The id of this InvoiceMerchantOrder.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501
        if id is not None and len(id) > 50:
            raise ValueError(
                "Invalid value for `id`, length must be less than or equal to `50`"
            )  # noqa: E501
        if id is not None and len(id) < 1:
            raise ValueError(
                "Invalid value for `id`, length must be greater than or equal to `1`"
            )  # noqa: E501

        self._id = id

    @property
    def items(self):
        """Gets the items of this InvoiceMerchantOrder.  # noqa: E501

        Array of items (in the shopping cart)  # noqa: E501

        :return: The items of this InvoiceMerchantOrder.  # noqa: E501
        :rtype: list[InvoiceItem]
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this InvoiceMerchantOrder.

        Array of items (in the shopping cart)  # noqa: E501

        :param items: The items of this InvoiceMerchantOrder.  # noqa: E501
        :type: list[InvoiceItem]
        """
        if items is None:
            raise ValueError(
                "Invalid value for `items`, must not be `None`"
            )  # noqa: E501

        self._items = items

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
        if issubclass(InvoiceMerchantOrder, dict):
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
        if not isinstance(other, InvoiceMerchantOrder):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other