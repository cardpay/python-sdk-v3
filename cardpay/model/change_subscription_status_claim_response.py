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

from cardpay.model.claim_response_subscription_data import ClaimResponseSubscriptionData  # noqa: F401,E501


class ChangeSubscriptionStatusClaimResponse(object):
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
        'created': 'datetime',
        'details': 'str',
        'id': 'str',
        'status': 'str',
        'subscription_data': 'ClaimResponseSubscriptionData',
        'updated': 'datetime'
    }

    attribute_map = {
        'created': 'created',
        'details': 'details',
        'id': 'id',
        'status': 'status',
        'subscription_data': 'subscription_data',
        'updated': 'updated'
    }

    def __init__(self, created=None, details=None, id=None, status=None, subscription_data=None, updated=None):  # noqa: E501
        """ChangeSubscriptionStatusClaimResponse - a model defined in Swagger"""  # noqa: E501

        self._created = None
        self._details = None
        self._id = None
        self._status = None
        self._subscription_data = None
        self._updated = None
        self.discriminator = None

        self.created = created
        self.details = details
        self.id = id
        self.status = status
        if subscription_data is not None:
            self.subscription_data = subscription_data
        self.updated = updated

    @property
    def created(self):
        """Gets the created of this ChangeSubscriptionStatusClaimResponse.  # noqa: E501

        Creation time, [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.  # noqa: E501

        :return: The created of this ChangeSubscriptionStatusClaimResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this ChangeSubscriptionStatusClaimResponse.

        Creation time, [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.  # noqa: E501

        :param created: The created of this ChangeSubscriptionStatusClaimResponse.  # noqa: E501
        :type: datetime
        """
        if created is None:
            raise ValueError("Invalid value for `created`, must not be `None`")  # noqa: E501

        self._created = created

    @property
    def details(self):
        """Gets the details of this ChangeSubscriptionStatusClaimResponse.  # noqa: E501

        Change claim details, errors etc.  # noqa: E501

        :return: The details of this ChangeSubscriptionStatusClaimResponse.  # noqa: E501
        :rtype: str
        """
        return self._details

    @details.setter
    def details(self, details):
        """Sets the details of this ChangeSubscriptionStatusClaimResponse.

        Change claim details, errors etc.  # noqa: E501

        :param details: The details of this ChangeSubscriptionStatusClaimResponse.  # noqa: E501
        :type: str
        """
        if details is None:
            raise ValueError("Invalid value for `details`, must not be `None`")  # noqa: E501

        self._details = details

    @property
    def id(self):
        """Gets the id of this ChangeSubscriptionStatusClaimResponse.  # noqa: E501

        ID of claim  # noqa: E501

        :return: The id of this ChangeSubscriptionStatusClaimResponse.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ChangeSubscriptionStatusClaimResponse.

        ID of claim  # noqa: E501

        :param id: The id of this ChangeSubscriptionStatusClaimResponse.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    class Status(object):
        IN_PROCESS = "IN_PROCESS"
        STOPPED = "STOPPED"
        COMPLETED = "COMPLETED"
        

    @property
    def status(self):
        """Gets the status of this ChangeSubscriptionStatusClaimResponse.  # noqa: E501

        Status of claim: `IN_PROCESS` - claim is in queue to being processed `STOPPED` - claim failed to be processed `COMPLETED` - claim successfully processed  # noqa: E501

        :return: The status of this ChangeSubscriptionStatusClaimResponse.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ChangeSubscriptionStatusClaimResponse.

        Status of claim: `IN_PROCESS` - claim is in queue to being processed `STOPPED` - claim failed to be processed `COMPLETED` - claim successfully processed  # noqa: E501

        :param status: The status of this ChangeSubscriptionStatusClaimResponse.  # noqa: E501
        :type: str
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501
        allowed_values = ["IN_PROCESS", "STOPPED", "COMPLETED"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def subscription_data(self):
        """Gets the subscription_data of this ChangeSubscriptionStatusClaimResponse.  # noqa: E501

        Subscription data  # noqa: E501

        :return: The subscription_data of this ChangeSubscriptionStatusClaimResponse.  # noqa: E501
        :rtype: ClaimResponseSubscriptionData
        """
        return self._subscription_data

    @subscription_data.setter
    def subscription_data(self, subscription_data):
        """Sets the subscription_data of this ChangeSubscriptionStatusClaimResponse.

        Subscription data  # noqa: E501

        :param subscription_data: The subscription_data of this ChangeSubscriptionStatusClaimResponse.  # noqa: E501
        :type: ClaimResponseSubscriptionData
        """

        self._subscription_data = subscription_data

    @property
    def updated(self):
        """Gets the updated of this ChangeSubscriptionStatusClaimResponse.  # noqa: E501

        Time when claim got the new status, [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.  # noqa: E501

        :return: The updated of this ChangeSubscriptionStatusClaimResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """Sets the updated of this ChangeSubscriptionStatusClaimResponse.

        Time when claim got the new status, [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.  # noqa: E501

        :param updated: The updated of this ChangeSubscriptionStatusClaimResponse.  # noqa: E501
        :type: datetime
        """
        if updated is None:
            raise ValueError("Invalid value for `updated`, must not be `None`")  # noqa: E501

        self._updated = updated

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
        if issubclass(ChangeSubscriptionStatusClaimResponse, dict):
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
        if not isinstance(other, ChangeSubscriptionStatusClaimResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
