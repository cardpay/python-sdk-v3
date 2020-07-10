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

from cardpay.model.recurring_response_filing import (
    RecurringResponseFiling,
)  # noqa: F401,E501
from cardpay.model.subscription import Subscription  # noqa: F401,E501


class RecurringResponseRecurringData(object):
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
        "amount": "float",
        "arn": "str",
        "auth_code": "str",
        "created": "str",
        "currency": "str",
        "decline_code": "str",
        "decline_reason": "str",
        "filing": "RecurringResponseFiling",
        "id": "str",
        "invalid_data": "list[str]",
        "is_3d": "bool",
        "note": "str",
        "rrn": "str",
        "status": "str",
        "subscription": "Subscription",
        "type": "str",
        "trans_type": "str",
    }

    attribute_map = {
        "amount": "amount",
        "arn": "arn",
        "auth_code": "auth_code",
        "created": "created",
        "currency": "currency",
        "decline_code": "decline_code",
        "decline_reason": "decline_reason",
        "filing": "filing",
        "id": "id",
        "invalid_data": "invalid_data",
        "is_3d": "is_3d",
        "note": "note",
        "rrn": "rrn",
        "status": "status",
        "subscription": "subscription",
        "type": "type",
        "trans_type": "trans_type",
    }

    def __init__(
        self,
        amount=None,
        arn=None,
        auth_code=None,
        created=None,
        currency=None,
        decline_code=None,
        decline_reason=None,
        filing=None,
        id=None,
        invalid_data=None,
        is_3d=None,
        note=None,
        rrn=None,
        status=None,
        subscription=None,
        type=None,
        trans_type=None,
    ):  # noqa: E501
        """RecurringResponseRecurringData - a model defined in Swagger"""  # noqa: E501

        self._amount = None
        self._arn = None
        self._auth_code = None
        self._created = None
        self._currency = None
        self._decline_code = None
        self._decline_reason = None
        self._filing = None
        self._id = None
        self._invalid_data = None
        self._is_3d = None
        self._note = None
        self._rrn = None
        self._status = None
        self._subscription = None
        self._type = None
        self._trans_type = None
        self.discriminator = None

        if amount is not None:
            self.amount = amount
        if arn is not None:
            self.arn = arn
        if auth_code is not None:
            self.auth_code = auth_code
        if created is not None:
            self.created = created
        if currency is not None:
            self.currency = currency
        if decline_code is not None:
            self.decline_code = decline_code
        if decline_reason is not None:
            self.decline_reason = decline_reason
        if filing is not None:
            self.filing = filing
        if id is not None:
            self.id = id
        if invalid_data is not None:
            self.invalid_data = invalid_data
        if is_3d is not None:
            self.is_3d = is_3d
        if note is not None:
            self.note = note
        if rrn is not None:
            self.rrn = rrn
        if status is not None:
            self.status = status
        if subscription is not None:
            self.subscription = subscription
        if type is not None:
            self.type = type
        if trans_type is not None:
            self.trans_type = trans_type

    @property
    def amount(self):
        """Gets the amount of this RecurringResponseRecurringData.  # noqa: E501

        Recurring amount  # noqa: E501

        :return: The amount of this RecurringResponseRecurringData.  # noqa: E501
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this RecurringResponseRecurringData.

        Recurring amount  # noqa: E501

        :param amount: The amount of this RecurringResponseRecurringData.  # noqa: E501
        :type: float
        """

        self._amount = amount

    @property
    def arn(self):
        """Gets the arn of this RecurringResponseRecurringData.  # noqa: E501

        ARN (Acquirer Reference Number), supplied by the acquiring financial institution, return only after receiving ARN from bank acquirer *(for BANKCARD payment method only)*  # noqa: E501

        :return: The arn of this RecurringResponseRecurringData.  # noqa: E501
        :rtype: str
        """
        return self._arn

    @arn.setter
    def arn(self, arn):
        """Sets the arn of this RecurringResponseRecurringData.

        ARN (Acquirer Reference Number), supplied by the acquiring financial institution, return only after receiving ARN from bank acquirer *(for BANKCARD payment method only)*  # noqa: E501

        :param arn: The arn of this RecurringResponseRecurringData.  # noqa: E501
        :type: str
        """

        self._arn = arn

    @property
    def auth_code(self):
        """Gets the auth_code of this RecurringResponseRecurringData.  # noqa: E501

        Authorization code, provided by bank  # noqa: E501

        :return: The auth_code of this RecurringResponseRecurringData.  # noqa: E501
        :rtype: str
        """
        return self._auth_code

    @auth_code.setter
    def auth_code(self, auth_code):
        """Sets the auth_code of this RecurringResponseRecurringData.

        Authorization code, provided by bank  # noqa: E501

        :param auth_code: The auth_code of this RecurringResponseRecurringData.  # noqa: E501
        :type: str
        """

        self._auth_code = auth_code

    @property
    def created(self):
        """Gets the created of this RecurringResponseRecurringData.  # noqa: E501

        Date and time when this recurring payment was created, [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format  # noqa: E501

        :return: The created of this RecurringResponseRecurringData.  # noqa: E501
        :rtype: str
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this RecurringResponseRecurringData.

        Date and time when this recurring payment was created, [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format  # noqa: E501

        :param created: The created of this RecurringResponseRecurringData.  # noqa: E501
        :type: str
        """

        self._created = created

    @property
    def currency(self):
        """Gets the currency of this RecurringResponseRecurringData.  # noqa: E501

        Recurring currency code ([ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code)  # noqa: E501

        :return: The currency of this RecurringResponseRecurringData.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this RecurringResponseRecurringData.

        Recurring currency code ([ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code)  # noqa: E501

        :param currency: The currency of this RecurringResponseRecurringData.  # noqa: E501
        :type: str
        """

        self._currency = currency

    @property
    def decline_code(self):
        """Gets the decline_code of this RecurringResponseRecurringData.  # noqa: E501

        Decline code (only in decline case)  # noqa: E501

        :return: The decline_code of this RecurringResponseRecurringData.  # noqa: E501
        :rtype: str
        """
        return self._decline_code

    @decline_code.setter
    def decline_code(self, decline_code):
        """Sets the decline_code of this RecurringResponseRecurringData.

        Decline code (only in decline case)  # noqa: E501

        :param decline_code: The decline_code of this RecurringResponseRecurringData.  # noqa: E501
        :type: str
        """

        self._decline_code = decline_code

    @property
    def decline_reason(self):
        """Gets the decline_reason of this RecurringResponseRecurringData.  # noqa: E501

        Bank's message about transaction decline reason (only in decline case)  # noqa: E501

        :return: The decline_reason of this RecurringResponseRecurringData.  # noqa: E501
        :rtype: str
        """
        return self._decline_reason

    @decline_reason.setter
    def decline_reason(self, decline_reason):
        """Sets the decline_reason of this RecurringResponseRecurringData.

        Bank's message about transaction decline reason (only in decline case)  # noqa: E501

        :param decline_reason: The decline_reason of this RecurringResponseRecurringData.  # noqa: E501
        :type: str
        """

        self._decline_reason = decline_reason

    @property
    def filing(self):
        """Gets the filing of this RecurringResponseRecurringData.  # noqa: E501

        CardPay's filing data  # noqa: E501

        :return: The filing of this RecurringResponseRecurringData.  # noqa: E501
        :rtype: RecurringResponseFiling
        """
        return self._filing

    @filing.setter
    def filing(self, filing):
        """Sets the filing of this RecurringResponseRecurringData.

        CardPay's filing data  # noqa: E501

        :param filing: The filing of this RecurringResponseRecurringData.  # noqa: E501
        :type: RecurringResponseFiling
        """

        self._filing = filing

    @property
    def id(self):
        """Gets the id of this RecurringResponseRecurringData.  # noqa: E501

        CardPay's recurring id  # noqa: E501

        :return: The id of this RecurringResponseRecurringData.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this RecurringResponseRecurringData.

        CardPay's recurring id  # noqa: E501

        :param id: The id of this RecurringResponseRecurringData.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def invalid_data(self):
        """Gets the invalid_data of this RecurringResponseRecurringData.  # noqa: E501

        Invalid card or billing data  # noqa: E501

        :return: The invalid_data of this RecurringResponseRecurringData.  # noqa: E501
        :rtype: list[str]
        """
        return self._invalid_data

    @invalid_data.setter
    def invalid_data(self, invalid_data):
        """Sets the invalid_data of this RecurringResponseRecurringData.

        Invalid card or billing data  # noqa: E501

        :param invalid_data: The invalid_data of this RecurringResponseRecurringData.  # noqa: E501
        :type: list[str]
        """

        self._invalid_data = invalid_data

    @property
    def is_3d(self):
        """Gets the is_3d of this RecurringResponseRecurringData.  # noqa: E501

        Was 3-D Secure authentication made or not  # noqa: E501

        :return: The is_3d of this RecurringResponseRecurringData.  # noqa: E501
        :rtype: bool
        """
        return self._is_3d

    @is_3d.setter
    def is_3d(self, is_3d):
        """Sets the is_3d of this RecurringResponseRecurringData.

        Was 3-D Secure authentication made or not  # noqa: E501

        :param is_3d: The is_3d of this RecurringResponseRecurringData.  # noqa: E501
        :type: bool
        """

        self._is_3d = is_3d

    @property
    def note(self):
        """Gets the note of this RecurringResponseRecurringData.  # noqa: E501

        Payment note  # noqa: E501

        :return: The note of this RecurringResponseRecurringData.  # noqa: E501
        :rtype: str
        """
        return self._note

    @note.setter
    def note(self, note):
        """Sets the note of this RecurringResponseRecurringData.

        Payment note  # noqa: E501

        :param note: The note of this RecurringResponseRecurringData.  # noqa: E501
        :type: str
        """

        self._note = note

    @property
    def rrn(self):
        """Gets the rrn of this RecurringResponseRecurringData.  # noqa: E501

        RRN (Retrieval Reference Number), supplied by the acquiring financial institution  # noqa: E501

        :return: The rrn of this RecurringResponseRecurringData.  # noqa: E501
        :rtype: str
        """
        return self._rrn

    @rrn.setter
    def rrn(self, rrn):
        """Sets the rrn of this RecurringResponseRecurringData.

        RRN (Retrieval Reference Number), supplied by the acquiring financial institution  # noqa: E501

        :param rrn: The rrn of this RecurringResponseRecurringData.  # noqa: E501
        :type: str
        """

        self._rrn = rrn

    class Status(object):
        NEW = "NEW"
        IN_PROGRESS = "IN_PROGRESS"
        DECLINED = "DECLINED"
        AUTHORIZED = "AUTHORIZED"
        COMPLETED = "COMPLETED"
        CANCELLED = "CANCELLED"
        REFUNDED = "REFUNDED"
        PARTIALLY_REFUNDED = "PARTIALLY_REFUNDED"
        VOIDED = "VOIDED"
        CHARGED_BACK = "CHARGED_BACK"
        CHARGEBACK_RESOLVED = "CHARGEBACK_RESOLVED"

    @property
    def status(self):
        """Gets the status of this RecurringResponseRecurringData.  # noqa: E501

        Current recurring payment status  # noqa: E501

        :return: The status of this RecurringResponseRecurringData.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this RecurringResponseRecurringData.

        Current recurring payment status  # noqa: E501

        :param status: The status of this RecurringResponseRecurringData.  # noqa: E501
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
            "PARTIALLY_REFUNDED",
            "VOIDED",
            "CHARGED_BACK",
            "CHARGEBACK_RESOLVED",
        ]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}".format(  # noqa: E501
                    status, allowed_values
                )
            )

        self._status = status

    @property
    def subscription(self):
        """Gets the subscription of this RecurringResponseRecurringData.  # noqa: E501

        Subscription data. Mandatory if scheduled payment is requested.  # noqa: E501

        :return: The subscription of this RecurringResponseRecurringData.  # noqa: E501
        :rtype: Subscription
        """
        return self._subscription

    @subscription.setter
    def subscription(self, subscription):
        """Sets the subscription of this RecurringResponseRecurringData.

        Subscription data. Mandatory if scheduled payment is requested.  # noqa: E501

        :param subscription: The subscription of this RecurringResponseRecurringData.  # noqa: E501
        :type: Subscription
        """

        self._subscription = subscription

    class Type(object):
        ONECLICK = "ONECLICK"
        SCHEDULED = "SCHEDULED"
        INSTALLMENT = "INSTALLMENT"

    @property
    def type(self):
        """Gets the type of this RecurringResponseRecurringData.  # noqa: E501

        Recurring payment type name; can be ONECLICK, SCHEDULED, INSTALLMENT  # noqa: E501

        :return: The type of this RecurringResponseRecurringData.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this RecurringResponseRecurringData.

        Recurring payment type name; can be ONECLICK, SCHEDULED, INSTALLMENT  # noqa: E501

        :param type: The type of this RecurringResponseRecurringData.  # noqa: E501
        :type: str
        """
        allowed_values = ["ONECLICK", "SCHEDULED", "INSTALLMENT"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}".format(  # noqa: E501
                    type, allowed_values
                )
            )

        self._type = type

    class TransType(object):
        _01 = "01"
        _03 = "03"
        _10 = "10"
        _11 = "11"
        _28 = "28"

    @property
    def trans_type(self):
        """Gets the trans_type of this RecurringResponseRecurringData.  # noqa: E501


        :return: The trans_type of this RecurringResponseRecurringData.  # noqa: E501
        :rtype: str
        """
        return self._trans_type

    @trans_type.setter
    def trans_type(self, trans_type):
        """Sets the trans_type of this RecurringResponseRecurringData.


        :param trans_type: The trans_type of this RecurringResponseRecurringData.  # noqa: E501
        :type: str
        """
        allowed_values = ["01", "03", "10", "11", "28"]  # noqa: E501
        if trans_type not in allowed_values:
            raise ValueError(
                "Invalid value for `trans_type` ({0}), must be one of {1}".format(  # noqa: E501
                    trans_type, allowed_values
                )
            )

        self._trans_type = trans_type

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
        if issubclass(RecurringResponseRecurringData, dict):
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
        if not isinstance(other, RecurringResponseRecurringData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
