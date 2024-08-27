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


class ResponseUpdatedTransactionData(object):
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
        "details": "str",
        "id": "str",
        "is_executed": "bool",
        "status": "str",
        "status_to": "str",
        "updated": "datetime",
    }

    attribute_map = {
        "details": "details",
        "id": "id",
        "is_executed": "is_executed",
        "status": "status",
        "status_to": "status_to",
        "updated": "updated",
    }

    def __init__(
        self,
        details=None,
        id=None,
        is_executed=None,
        status=None,
        status_to=None,
        updated=None,
    ):  # noqa: E501
        """ResponseUpdatedTransactionData - a model defined in Swagger"""  # noqa: E501

        self._details = None
        self._id = None
        self._is_executed = None
        self._status = None
        self._status_to = None
        self._updated = None
        self.discriminator = None

        if details is not None:
            self.details = details
        if id is not None:
            self.id = id
        if is_executed is not None:
            self.is_executed = is_executed
        if status is not None:
            self.status = status
        if status_to is not None:
            self.status_to = status_to
        if updated is not None:
            self.updated = updated

    @property
    def details(self):
        """Gets the details of this ResponseUpdatedTransactionData.  # noqa: E501

        The reason why request was unsuccessful  # noqa: E501

        :return: The details of this ResponseUpdatedTransactionData.  # noqa: E501
        :rtype: str
        """
        return self._details

    @details.setter
    def details(self, details):
        """Sets the details of this ResponseUpdatedTransactionData.

        The reason why request was unsuccessful  # noqa: E501

        :param details: The details of this ResponseUpdatedTransactionData.  # noqa: E501
        :type: str
        """

        self._details = details

    @property
    def id(self):
        """Gets the id of this ResponseUpdatedTransactionData.  # noqa: E501

        Represents the ID of the modified transaction  # noqa: E501

        :return: The id of this ResponseUpdatedTransactionData.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ResponseUpdatedTransactionData.

        Represents the ID of the modified transaction  # noqa: E501

        :param id: The id of this ResponseUpdatedTransactionData.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def is_executed(self):
        """Gets the is_executed of this ResponseUpdatedTransactionData.  # noqa: E501

        Indicates was the request successful or not  # noqa: E501

        :return: The is_executed of this ResponseUpdatedTransactionData.  # noqa: E501
        :rtype: bool
        """
        return self._is_executed

    @is_executed.setter
    def is_executed(self, is_executed):
        """Sets the is_executed of this ResponseUpdatedTransactionData.

        Indicates was the request successful or not  # noqa: E501

        :param is_executed: The is_executed of this ResponseUpdatedTransactionData.  # noqa: E501
        :type: bool
        """

        self._is_executed = is_executed

    class Status(object):
        NEW = "NEW"
        IN_PROGRESS = "IN_PROGRESS"
        DECLINED = "DECLINED"
        AUTHORIZED = "AUTHORIZED"
        COMPLETED = "COMPLETED"
        CANCELLED = "CANCELLED"
        REFUNDED = "REFUNDED"
        VOIDED = "VOIDED"
        TERMINATED = "TERMINATED"
        CHARGED_BACK = "CHARGED_BACK"
        CHARGEBACK_RESOLVED = "CHARGEBACK_RESOLVED"
        UNPAID = "UNPAID"
        WAITING = "WAITING"

    @property
    def status(self):
        """Gets the status of this ResponseUpdatedTransactionData.  # noqa: E501

        Status of modified or created transaction  # noqa: E501

        :return: The status of this ResponseUpdatedTransactionData.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ResponseUpdatedTransactionData.

        Status of modified or created transaction  # noqa: E501

        :param status: The status of this ResponseUpdatedTransactionData.  # noqa: E501
        :type: str
        """
        allowed_values = [
            "NEW",
            "IN_PROGRESS",
            "DECLINED",
            "AUTHORIZED",
            "COMPLETED",
            "CANCELLED",
            "REFUNDED",
            "VOIDED",
            "TERMINATED",
            "CHARGED_BACK",
            "CHARGEBACK_RESOLVED",
            "UNPAID",
            "WAITING",
        ]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}".format(  # noqa: E501
                    status, allowed_values
                )
            )

        self._status = status

    class StatusTo(object):
        REVERSE = "REVERSE"
        COMPLETE = "COMPLETE"
        TERMINATE = "TERMINATE"

    @property
    def status_to(self):
        """Gets the status_to of this ResponseUpdatedTransactionData.  # noqa: E501

        Requested action (status to be set).  Payment: `COMPLETE` or `REVERSE`.  Refund, payout: `REVERSE`.  # noqa: E501

        :return: The status_to of this ResponseUpdatedTransactionData.  # noqa: E501
        :rtype: str
        """
        return self._status_to

    @status_to.setter
    def status_to(self, status_to):
        """Sets the status_to of this ResponseUpdatedTransactionData.

        Requested action (status to be set).  Payment: `COMPLETE` or `REVERSE`.  Refund, payout: `REVERSE`.  # noqa: E501

        :param status_to: The status_to of this ResponseUpdatedTransactionData.  # noqa: E501
        :type: str
        """
        allowed_values = ["REVERSE", "COMPLETE", "TERMINATE"]  # noqa: E501
        if status_to not in allowed_values:
            raise ValueError(
                "Invalid value for `status_to` ({0}), must be one of {1}".format(  # noqa: E501
                    status_to, allowed_values
                )
            )

        self._status_to = status_to

    @property
    def updated(self):
        """Gets the updated of this ResponseUpdatedTransactionData.  # noqa: E501

        Transaction update date and time in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. Returned only for successful update operations.  # noqa: E501

        :return: The updated of this ResponseUpdatedTransactionData.  # noqa: E501
        :rtype: datetime
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """Sets the updated of this ResponseUpdatedTransactionData.

        Transaction update date and time in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. Returned only for successful update operations.  # noqa: E501

        :param updated: The updated of this ResponseUpdatedTransactionData.  # noqa: E501
        :type: datetime
        """

        self._updated = updated

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
        if issubclass(ResponseUpdatedTransactionData, dict):
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
        if not isinstance(other, ResponseUpdatedTransactionData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
