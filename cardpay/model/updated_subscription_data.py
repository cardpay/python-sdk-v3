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

from cardpay.model.recurring_response_filing import RecurringResponseFiling  # noqa: F401,E501
from cardpay.model.updated_subscription_recurring_data import UpdatedSubscriptionRecurringData  # noqa: F401,E501


class UpdatedSubscriptionData(object):
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
        'change_status_claim_id': 'str',
        'details': 'str',
        'filing': 'RecurringResponseFiling',
        'id': 'str',
        'is_executed': 'bool',
        'recurring_data': 'UpdatedSubscriptionRecurringData',
        'remaining_amount': 'float',
        'status': 'str',
        'status_to': 'str',
        'updated': 'datetime'
    }

    attribute_map = {
        'change_status_claim_id': 'change_status_claim_id',
        'details': 'details',
        'filing': 'filing',
        'id': 'id',
        'is_executed': 'is_executed',
        'recurring_data': 'recurring_data',
        'remaining_amount': 'remaining_amount',
        'status': 'status',
        'status_to': 'status_to',
        'updated': 'updated'
    }

    def __init__(self, change_status_claim_id=None, details=None, filing=None, id=None, is_executed=None, recurring_data=None, remaining_amount=None, status=None, status_to=None, updated=None):  # noqa: E501
        """UpdatedSubscriptionData - a model defined in Swagger"""  # noqa: E501

        self._change_status_claim_id = None
        self._details = None
        self._filing = None
        self._id = None
        self._is_executed = None
        self._recurring_data = None
        self._remaining_amount = None
        self._status = None
        self._status_to = None
        self._updated = None
        self.discriminator = None

        if change_status_claim_id is not None:
            self.change_status_claim_id = change_status_claim_id
        if details is not None:
            self.details = details
        if filing is not None:
            self.filing = filing
        if id is not None:
            self.id = id
        if is_executed is not None:
            self.is_executed = is_executed
        if recurring_data is not None:
            self.recurring_data = recurring_data
        if remaining_amount is not None:
            self.remaining_amount = remaining_amount
        if status is not None:
            self.status = status
        if status_to is not None:
            self.status_to = status_to
        if updated is not None:
            self.updated = updated

    @property
    def change_status_claim_id(self):
        """Gets the change_status_claim_id of this UpdatedSubscriptionData.  # noqa: E501

        ID of claim; appears in case of request change was processed asynchronously and put in queue. Mandatory if request was put in queue.  # noqa: E501

        :return: The change_status_claim_id of this UpdatedSubscriptionData.  # noqa: E501
        :rtype: str
        """
        return self._change_status_claim_id

    @change_status_claim_id.setter
    def change_status_claim_id(self, change_status_claim_id):
        """Sets the change_status_claim_id of this UpdatedSubscriptionData.

        ID of claim; appears in case of request change was processed asynchronously and put in queue. Mandatory if request was put in queue.  # noqa: E501

        :param change_status_claim_id: The change_status_claim_id of this UpdatedSubscriptionData.  # noqa: E501
        :type: str
        """

        self._change_status_claim_id = change_status_claim_id

    @property
    def details(self):
        """Gets the details of this UpdatedSubscriptionData.  # noqa: E501

        Operation details, errors, etc.  # noqa: E501

        :return: The details of this UpdatedSubscriptionData.  # noqa: E501
        :rtype: str
        """
        return self._details

    @details.setter
    def details(self, details):
        """Sets the details of this UpdatedSubscriptionData.

        Operation details, errors, etc.  # noqa: E501

        :param details: The details of this UpdatedSubscriptionData.  # noqa: E501
        :type: str
        """

        self._details = details

    @property
    def filing(self):
        """Gets the filing of this UpdatedSubscriptionData.  # noqa: E501

        Filing data  # noqa: E501

        :return: The filing of this UpdatedSubscriptionData.  # noqa: E501
        :rtype: RecurringResponseFiling
        """
        return self._filing

    @filing.setter
    def filing(self, filing):
        """Sets the filing of this UpdatedSubscriptionData.

        Filing data  # noqa: E501

        :param filing: The filing of this UpdatedSubscriptionData.  # noqa: E501
        :type: RecurringResponseFiling
        """

        self._filing = filing

    @property
    def id(self):
        """Gets the id of this UpdatedSubscriptionData.  # noqa: E501

        ID of subscription  # noqa: E501

        :return: The id of this UpdatedSubscriptionData.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UpdatedSubscriptionData.

        ID of subscription  # noqa: E501

        :param id: The id of this UpdatedSubscriptionData.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def is_executed(self):
        """Gets the is_executed of this UpdatedSubscriptionData.  # noqa: E501

        Status of operation  # noqa: E501

        :return: The is_executed of this UpdatedSubscriptionData.  # noqa: E501
        :rtype: bool
        """
        return self._is_executed

    @is_executed.setter
    def is_executed(self, is_executed):
        """Sets the is_executed of this UpdatedSubscriptionData.

        Status of operation  # noqa: E501

        :param is_executed: The is_executed of this UpdatedSubscriptionData.  # noqa: E501
        :type: bool
        """

        self._is_executed = is_executed

    @property
    def recurring_data(self):
        """Gets the recurring_data of this UpdatedSubscriptionData.  # noqa: E501

        Payment data  # noqa: E501

        :return: The recurring_data of this UpdatedSubscriptionData.  # noqa: E501
        :rtype: UpdatedSubscriptionRecurringData
        """
        return self._recurring_data

    @recurring_data.setter
    def recurring_data(self, recurring_data):
        """Sets the recurring_data of this UpdatedSubscriptionData.

        Payment data  # noqa: E501

        :param recurring_data: The recurring_data of this UpdatedSubscriptionData.  # noqa: E501
        :type: UpdatedSubscriptionRecurringData
        """

        self._recurring_data = recurring_data

    @property
    def remaining_amount(self):
        """Gets the remaining_amount of this UpdatedSubscriptionData.  # noqa: E501

        The amount remained to be paid after repayment operation. Mandatory for `REPAYMENT` operation only  # noqa: E501

        :return: The remaining_amount of this UpdatedSubscriptionData.  # noqa: E501
        :rtype: float
        """
        return self._remaining_amount

    @remaining_amount.setter
    def remaining_amount(self, remaining_amount):
        """Sets the remaining_amount of this UpdatedSubscriptionData.

        The amount remained to be paid after repayment operation. Mandatory for `REPAYMENT` operation only  # noqa: E501

        :param remaining_amount: The remaining_amount of this UpdatedSubscriptionData.  # noqa: E501
        :type: float
        """

        self._remaining_amount = remaining_amount

    class Status(object):
        ACTIVE = "ACTIVE"
        INACTIVE = "INACTIVE"
        CANCELLED = "CANCELLED"
        PAST_DUE = "PAST_DUE"
        PENDING = "PENDING"
        COMPLETED = "COMPLETED"
        CARD_EXPIRED = "CARD_EXPIRED"
        

    @property
    def status(self):
        """Gets the status of this UpdatedSubscriptionData.  # noqa: E501

        Resulted status of subscription  # noqa: E501

        :return: The status of this UpdatedSubscriptionData.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this UpdatedSubscriptionData.

        Resulted status of subscription  # noqa: E501

        :param status: The status of this UpdatedSubscriptionData.  # noqa: E501
        :type: str
        """
        allowed_values = ["ACTIVE", "INACTIVE", "CANCELLED", "PAST_DUE", "PENDING", "COMPLETED", "CARD_EXPIRED"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    class StatusTo(object):
        ACTIVE = "ACTIVE"
        INACTIVE = "INACTIVE"
        CANCELLED = "CANCELLED"
        PAST_DUE = "PAST_DUE"
        PENDING = "PENDING"
        COMPLETED = "COMPLETED"
        CARD_EXPIRED = "CARD_EXPIRED"
        

    @property
    def status_to(self):
        """Gets the status_to of this UpdatedSubscriptionData.  # noqa: E501

        Requested status of subscription. Mandatory for `CHANGE_STATUS` operation only.  # noqa: E501

        :return: The status_to of this UpdatedSubscriptionData.  # noqa: E501
        :rtype: str
        """
        return self._status_to

    @status_to.setter
    def status_to(self, status_to):
        """Sets the status_to of this UpdatedSubscriptionData.

        Requested status of subscription. Mandatory for `CHANGE_STATUS` operation only.  # noqa: E501

        :param status_to: The status_to of this UpdatedSubscriptionData.  # noqa: E501
        :type: str
        """
        allowed_values = ["ACTIVE", "INACTIVE", "CANCELLED", "PAST_DUE", "PENDING", "COMPLETED", "CARD_EXPIRED"]  # noqa: E501
        if status_to not in allowed_values:
            raise ValueError(
                "Invalid value for `status_to` ({0}), must be one of {1}"  # noqa: E501
                .format(status_to, allowed_values)
            )

        self._status_to = status_to

    @property
    def updated(self):
        """Gets the updated of this UpdatedSubscriptionData.  # noqa: E501

        If request is successful then date and time returned in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format (format - yyyy-MM-dd'T'HH:mm:ss'Z').  # noqa: E501

        :return: The updated of this UpdatedSubscriptionData.  # noqa: E501
        :rtype: datetime
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """Sets the updated of this UpdatedSubscriptionData.

        If request is successful then date and time returned in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format (format - yyyy-MM-dd'T'HH:mm:ss'Z').  # noqa: E501

        :param updated: The updated of this UpdatedSubscriptionData.  # noqa: E501
        :type: datetime
        """

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
        if issubclass(UpdatedSubscriptionData, dict):
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
        if not isinstance(other, UpdatedSubscriptionData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
