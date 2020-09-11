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


class RecurringResponseMerchantOrder(object):
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
    swagger_types = {"description": "str", "id": "str"}

    attribute_map = {"description": "description", "id": "id"}

    def __init__(self, description=None, id=None):  # noqa: E501
        """RecurringResponseMerchantOrder - a model defined in Swagger"""  # noqa: E501

        self._description = None
        self._id = None
        self.discriminator = None

        if description is not None:
            self.description = description
        self.id = id

    @property
    def description(self):
        """Gets the description of this RecurringResponseMerchantOrder.  # noqa: E501

        The description of product / service, provided to Customer  # noqa: E501

        :return: The description of this RecurringResponseMerchantOrder.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this RecurringResponseMerchantOrder.

        The description of product / service, provided to Customer  # noqa: E501

        :param description: The description of this RecurringResponseMerchantOrder.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def id(self):
        """Gets the id of this RecurringResponseMerchantOrder.  # noqa: E501

        Merchant's ID of the order  # noqa: E501

        :return: The id of this RecurringResponseMerchantOrder.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this RecurringResponseMerchantOrder.

        Merchant's ID of the order  # noqa: E501

        :param id: The id of this RecurringResponseMerchantOrder.  # noqa: E501
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
        if issubclass(RecurringResponseMerchantOrder, dict):
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
        if not isinstance(other, RecurringResponseMerchantOrder):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
