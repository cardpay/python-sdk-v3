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

from cardpay.model.refund_response import RefundResponse  # noqa: F401,E501


class RefundsList(object):
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
        'data': 'list[RefundResponse]',
        'has_more': 'bool'
    }

    attribute_map = {
        'data': 'data',
        'has_more': 'has_more'
    }

    def __init__(self, data=None, has_more=None):  # noqa: E501
        """RefundsList - a model defined in Swagger"""  # noqa: E501

        self._data = None
        self._has_more = None
        self.discriminator = None

        if data is not None:
            self.data = data
        if has_more is not None:
            self.has_more = has_more

    @property
    def data(self):
        """Gets the data of this RefundsList.  # noqa: E501

        List of found objects  # noqa: E501

        :return: The data of this RefundsList.  # noqa: E501
        :rtype: list[RefundResponse]
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this RefundsList.

        List of found objects  # noqa: E501

        :param data: The data of this RefundsList.  # noqa: E501
        :type: list[RefundResponse]
        """

        self._data = data

    @property
    def has_more(self):
        """Gets the has_more of this RefundsList.  # noqa: E501

        Indicates if there are more elements for this period than were returned  # noqa: E501

        :return: The has_more of this RefundsList.  # noqa: E501
        :rtype: bool
        """
        return self._has_more

    @has_more.setter
    def has_more(self, has_more):
        """Sets the has_more of this RefundsList.

        Indicates if there are more elements for this period than were returned  # noqa: E501

        :param has_more: The has_more of this RefundsList.  # noqa: E501
        :type: bool
        """

        self._has_more = has_more

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
        if issubclass(RefundsList, dict):
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
        if not isinstance(other, RefundsList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
