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


class ClaimResponseSubscriptionData(object):
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
        'id': 'str',
        'status_to': 'str'
    }

    attribute_map = {
        'id': 'id',
        'status_to': 'status_to'
    }

    def __init__(self, id=None, status_to=None):  # noqa: E501
        """ClaimResponseSubscriptionData - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._status_to = None
        self.discriminator = None

        self.id = id
        self.status_to = status_to

    @property
    def id(self):
        """Gets the id of this ClaimResponseSubscriptionData.  # noqa: E501

        ID of subscription  # noqa: E501

        :return: The id of this ClaimResponseSubscriptionData.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ClaimResponseSubscriptionData.

        ID of subscription  # noqa: E501

        :param id: The id of this ClaimResponseSubscriptionData.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    class StatusTo(object):
        ACTIVE = "ACTIVE"
        INACTIVE = "INACTIVE"
        CANCELLED = "CANCELLED"
        PAST_DUE = "PAST_DUE"
        PENDING = "PENDING"
        COMPLETED = "COMPLETED"
        CARD_EXPIRED = "CARD_EXPIRED"
        ACTIVATION_FAILED = "ACTIVATION_FAILED"
        

    @property
    def status_to(self):
        """Gets the status_to of this ClaimResponseSubscriptionData.  # noqa: E501

        Requested status of subscription  # noqa: E501

        :return: The status_to of this ClaimResponseSubscriptionData.  # noqa: E501
        :rtype: str
        """
        return self._status_to

    @status_to.setter
    def status_to(self, status_to):
        """Sets the status_to of this ClaimResponseSubscriptionData.

        Requested status of subscription  # noqa: E501

        :param status_to: The status_to of this ClaimResponseSubscriptionData.  # noqa: E501
        :type: str
        """
        if status_to is None:
            raise ValueError("Invalid value for `status_to`, must not be `None`")  # noqa: E501
        allowed_values = ["ACTIVE", "INACTIVE", "CANCELLED", "PAST_DUE", "PENDING", "COMPLETED", "CARD_EXPIRED", "ACTIVATION_FAILED"]  # noqa: E501
        if status_to not in allowed_values:
            raise ValueError(
                "Invalid value for `status_to` ({0}), must be one of {1}"  # noqa: E501
                .format(status_to, allowed_values)
            )

        self._status_to = status_to

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
        if issubclass(ClaimResponseSubscriptionData, dict):
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
        if not isinstance(other, ClaimResponseSubscriptionData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
