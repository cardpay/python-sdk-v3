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


class PixAccountDetailsRequest(object):
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
    swagger_types = {"customer_identity": "str"}

    attribute_map = {"customer_identity": "customer_identity"}

    def __init__(self, customer_identity=None):  # noqa: E501
        """PixAccountDetailsRequest - a model defined in Swagger"""  # noqa: E501

        self._customer_identity = None
        self.discriminator = None

        self.customer_identity = customer_identity

    @property
    def customer_identity(self):
        """Gets the customer_identity of this PixAccountDetailsRequest.  # noqa: E501

        Customer identity  # noqa: E501

        :return: The customer_identity of this PixAccountDetailsRequest.  # noqa: E501
        :rtype: str
        """
        return self._customer_identity

    @customer_identity.setter
    def customer_identity(self, customer_identity):
        """Sets the customer_identity of this PixAccountDetailsRequest.

        Customer identity  # noqa: E501

        :param customer_identity: The customer_identity of this PixAccountDetailsRequest.  # noqa: E501
        :type: str
        """
        if customer_identity is None:
            raise ValueError(
                "Invalid value for `customer_identity`, must not be `None`"
            )  # noqa: E501

        self._customer_identity = customer_identity

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
        if issubclass(PixAccountDetailsRequest, dict):
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
        if not isinstance(other, PixAccountDetailsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other