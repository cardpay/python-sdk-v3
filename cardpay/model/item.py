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


class Item(object):
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
        'count': 'int',
        'description': 'str',
        'name': 'str',
        'price': 'float'
    }

    attribute_map = {
        'count': 'count',
        'description': 'description',
        'name': 'name',
        'price': 'price'
    }

    def __init__(self, count=None, description=None, name=None, price=None):  # noqa: E501
        """Item - a model defined in Swagger"""  # noqa: E501

        self._count = None
        self._description = None
        self._name = None
        self._price = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if description is not None:
            self.description = description
        self.name = name
        if price is not None:
            self.price = price

    @property
    def count(self):
        """Gets the count of this Item.  # noqa: E501

        The count of product / service, provided to Customer. Any positive number  # noqa: E501

        :return: The count of this Item.  # noqa: E501
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this Item.

        The count of product / service, provided to Customer. Any positive number  # noqa: E501

        :param count: The count of this Item.  # noqa: E501
        :type: int
        """

        self._count = count

    @property
    def description(self):
        """Gets the description of this Item.  # noqa: E501

        The description of product / service, provided to Customer  # noqa: E501

        :return: The description of this Item.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Item.

        The description of product / service, provided to Customer  # noqa: E501

        :param description: The description of this Item.  # noqa: E501
        :type: str
        """
        if description is not None and len(description) > 200:
            raise ValueError("Invalid value for `description`, length must be less than or equal to `200`")  # noqa: E501
        if description is not None and len(description) < 1:
            raise ValueError("Invalid value for `description`, length must be greater than or equal to `1`")  # noqa: E501

        self._description = description

    @property
    def name(self):
        """Gets the name of this Item.  # noqa: E501

        The name of product / service, provided to Customer  # noqa: E501

        :return: The name of this Item.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Item.

        The name of product / service, provided to Customer  # noqa: E501

        :param name: The name of this Item.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if name is not None and len(name) > 50:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `50`")  # noqa: E501
        if name is not None and len(name) < 1:
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501

        self._name = name

    @property
    def price(self):
        """Gets the price of this Item.  # noqa: E501

        Price of product / service with dot as a decimal separator, must be less than 1 million  # noqa: E501

        :return: The price of this Item.  # noqa: E501
        :rtype: float
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this Item.

        Price of product / service with dot as a decimal separator, must be less than 1 million  # noqa: E501

        :param price: The price of this Item.  # noqa: E501
        :type: float
        """

        self._price = price

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
        if issubclass(Item, dict):
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
        if not isinstance(other, Item):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
