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


class PaymentResponsePaymentData(object):
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
        "action_code": "str",
        "amount": "float",
        "arn": "str",
        "auth_code": "str",
        "created": "str",
        "currency": "str",
        "decline_code": "str",
        "decline_reason": "str",
        "extended_data": "dict(str, str)",
        "id": "str",
        "installment_type": "str",
        "installments": "str",
        "invalid_data": "list[str]",
        "is_3d": "bool",
        "note": "str",
        "rrn": "str",
        "status": "str",
        "trans_type": "str",
    }

    attribute_map = {
        "action_code": "action_code",
        "amount": "amount",
        "arn": "arn",
        "auth_code": "auth_code",
        "created": "created",
        "currency": "currency",
        "decline_code": "decline_code",
        "decline_reason": "decline_reason",
        "extended_data": "extended_data",
        "id": "id",
        "installment_type": "installment_type",
        "installments": "installments",
        "invalid_data": "invalid_data",
        "is_3d": "is_3d",
        "note": "note",
        "rrn": "rrn",
        "status": "status",
        "trans_type": "trans_type",
    }

    def __init__(
        self,
        action_code=None,
        amount=None,
        arn=None,
        auth_code=None,
        created=None,
        currency=None,
        decline_code=None,
        decline_reason=None,
        extended_data=None,
        id=None,
        installment_type=None,
        installments=None,
        invalid_data=None,
        is_3d=None,
        note=None,
        rrn=None,
        status=None,
        trans_type=None,
    ):  # noqa: E501
        """PaymentResponsePaymentData - a model defined in Swagger"""  # noqa: E501

        self._action_code = None
        self._amount = None
        self._arn = None
        self._auth_code = None
        self._created = None
        self._currency = None
        self._decline_code = None
        self._decline_reason = None
        self._extended_data = None
        self._id = None
        self._installment_type = None
        self._installments = None
        self._invalid_data = None
        self._is_3d = None
        self._note = None
        self._rrn = None
        self._status = None
        self._trans_type = None
        self.discriminator = None

        if action_code is not None:
            self.action_code = action_code
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
        if extended_data is not None:
            self.extended_data = extended_data
        if id is not None:
            self.id = id
        if installment_type is not None:
            self.installment_type = installment_type
        if installments is not None:
            self.installments = installments
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
        if trans_type is not None:
            self.trans_type = trans_type

    @property
    def action_code(self):
        """Gets the action_code of this PaymentResponsePaymentData.  # noqa: E501

        Action code (only in decline case)  # noqa: E501

        :return: The action_code of this PaymentResponsePaymentData.  # noqa: E501
        :rtype: str
        """
        return self._action_code

    @action_code.setter
    def action_code(self, action_code):
        """Sets the action_code of this PaymentResponsePaymentData.

        Action code (only in decline case)  # noqa: E501

        :param action_code: The action_code of this PaymentResponsePaymentData.  # noqa: E501
        :type: str
        """

        self._action_code = action_code

    @property
    def amount(self):
        """Gets the amount of this PaymentResponsePaymentData.  # noqa: E501

        Payment amount  # noqa: E501

        :return: The amount of this PaymentResponsePaymentData.  # noqa: E501
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this PaymentResponsePaymentData.

        Payment amount  # noqa: E501

        :param amount: The amount of this PaymentResponsePaymentData.  # noqa: E501
        :type: float
        """

        self._amount = amount

    @property
    def arn(self):
        """Gets the arn of this PaymentResponsePaymentData.  # noqa: E501

        ARN (Acquirer Reference Number), supplied by the acquiring financial institution, return only after receiving ARN from bank acquirer *(for BANKCARD payment method only)*  # noqa: E501

        :return: The arn of this PaymentResponsePaymentData.  # noqa: E501
        :rtype: str
        """
        return self._arn

    @arn.setter
    def arn(self, arn):
        """Sets the arn of this PaymentResponsePaymentData.

        ARN (Acquirer Reference Number), supplied by the acquiring financial institution, return only after receiving ARN from bank acquirer *(for BANKCARD payment method only)*  # noqa: E501

        :param arn: The arn of this PaymentResponsePaymentData.  # noqa: E501
        :type: str
        """

        self._arn = arn

    @property
    def auth_code(self):
        """Gets the auth_code of this PaymentResponsePaymentData.  # noqa: E501

        Authorization code, provided by bank *(for BANKCARD payment method only)*  # noqa: E501

        :return: The auth_code of this PaymentResponsePaymentData.  # noqa: E501
        :rtype: str
        """
        return self._auth_code

    @auth_code.setter
    def auth_code(self, auth_code):
        """Sets the auth_code of this PaymentResponsePaymentData.

        Authorization code, provided by bank *(for BANKCARD payment method only)*  # noqa: E501

        :param auth_code: The auth_code of this PaymentResponsePaymentData.  # noqa: E501
        :type: str
        """

        self._auth_code = auth_code

    @property
    def created(self):
        """Gets the created of this PaymentResponsePaymentData.  # noqa: E501

        Time when this payment started in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format (yyyy-MM-dd'T'HH:mm:ss'Z')  # noqa: E501

        :return: The created of this PaymentResponsePaymentData.  # noqa: E501
        :rtype: str
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this PaymentResponsePaymentData.

        Time when this payment started in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format (yyyy-MM-dd'T'HH:mm:ss'Z')  # noqa: E501

        :param created: The created of this PaymentResponsePaymentData.  # noqa: E501
        :type: str
        """

        self._created = created

    @property
    def currency(self):
        """Gets the currency of this PaymentResponsePaymentData.  # noqa: E501

        Payment currency code ([ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code)  # noqa: E501

        :return: The currency of this PaymentResponsePaymentData.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this PaymentResponsePaymentData.

        Payment currency code ([ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code)  # noqa: E501

        :param currency: The currency of this PaymentResponsePaymentData.  # noqa: E501
        :type: str
        """

        self._currency = currency

    @property
    def decline_code(self):
        """Gets the decline_code of this PaymentResponsePaymentData.  # noqa: E501

        Decline code (only in decline case)  # noqa: E501

        :return: The decline_code of this PaymentResponsePaymentData.  # noqa: E501
        :rtype: str
        """
        return self._decline_code

    @decline_code.setter
    def decline_code(self, decline_code):
        """Sets the decline_code of this PaymentResponsePaymentData.

        Decline code (only in decline case)  # noqa: E501

        :param decline_code: The decline_code of this PaymentResponsePaymentData.  # noqa: E501
        :type: str
        """

        self._decline_code = decline_code

    @property
    def decline_reason(self):
        """Gets the decline_reason of this PaymentResponsePaymentData.  # noqa: E501

        Bank's message about transaction decline reason (only in decline case)  # noqa: E501

        :return: The decline_reason of this PaymentResponsePaymentData.  # noqa: E501
        :rtype: str
        """
        return self._decline_reason

    @decline_reason.setter
    def decline_reason(self, decline_reason):
        """Sets the decline_reason of this PaymentResponsePaymentData.

        Bank's message about transaction decline reason (only in decline case)  # noqa: E501

        :param decline_reason: The decline_reason of this PaymentResponsePaymentData.  # noqa: E501
        :type: str
        """

        self._decline_reason = decline_reason

    @property
    def extended_data(self):
        """Gets the extended_data of this PaymentResponsePaymentData.  # noqa: E501

        Extended structure with information for processing a payment in gateway mode. Contact your account manager to enable it  # noqa: E501

        :return: The extended_data of this PaymentResponsePaymentData.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._extended_data

    @extended_data.setter
    def extended_data(self, extended_data):
        """Sets the extended_data of this PaymentResponsePaymentData.

        Extended structure with information for processing a payment in gateway mode. Contact your account manager to enable it  # noqa: E501

        :param extended_data: The extended_data of this PaymentResponsePaymentData.  # noqa: E501
        :type: dict(str, str)
        """

        self._extended_data = extended_data

    @property
    def id(self):
        """Gets the id of this PaymentResponsePaymentData.  # noqa: E501

        CardPay's payment id  # noqa: E501

        :return: The id of this PaymentResponsePaymentData.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PaymentResponsePaymentData.

        CardPay's payment id  # noqa: E501

        :param id: The id of this PaymentResponsePaymentData.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def installment_type(self):
        """Gets the installment_type of this PaymentResponsePaymentData.  # noqa: E501

        Selected installment type  # noqa: E501

        :return: The installment_type of this PaymentResponsePaymentData.  # noqa: E501
        :rtype: str
        """
        return self._installment_type

    @installment_type.setter
    def installment_type(self, installment_type):
        """Sets the installment_type of this PaymentResponsePaymentData.

        Selected installment type  # noqa: E501

        :param installment_type: The installment_type of this PaymentResponsePaymentData.  # noqa: E501
        :type: str
        """

        self._installment_type = installment_type

    @property
    def installments(self):
        """Gets the installments of this PaymentResponsePaymentData.  # noqa: E501

        Number of total installment payments, to be charged  # noqa: E501

        :return: The installments of this PaymentResponsePaymentData.  # noqa: E501
        :rtype: str
        """
        return self._installments

    @installments.setter
    def installments(self, installments):
        """Sets the installments of this PaymentResponsePaymentData.

        Number of total installment payments, to be charged  # noqa: E501

        :param installments: The installments of this PaymentResponsePaymentData.  # noqa: E501
        :type: str
        """

        self._installments = installments

    @property
    def invalid_data(self):
        """Gets the invalid_data of this PaymentResponsePaymentData.  # noqa: E501

        Invalid card or billing data  # noqa: E501

        :return: The invalid_data of this PaymentResponsePaymentData.  # noqa: E501
        :rtype: list[str]
        """
        return self._invalid_data

    @invalid_data.setter
    def invalid_data(self, invalid_data):
        """Sets the invalid_data of this PaymentResponsePaymentData.

        Invalid card or billing data  # noqa: E501

        :param invalid_data: The invalid_data of this PaymentResponsePaymentData.  # noqa: E501
        :type: list[str]
        """

        self._invalid_data = invalid_data

    @property
    def is_3d(self):
        """Gets the is_3d of this PaymentResponsePaymentData.  # noqa: E501

        Was 3-D Secure authentication made or not *(for BANKCARD payment method only)*  # noqa: E501

        :return: The is_3d of this PaymentResponsePaymentData.  # noqa: E501
        :rtype: bool
        """
        return self._is_3d

    @is_3d.setter
    def is_3d(self, is_3d):
        """Sets the is_3d of this PaymentResponsePaymentData.

        Was 3-D Secure authentication made or not *(for BANKCARD payment method only)*  # noqa: E501

        :param is_3d: The is_3d of this PaymentResponsePaymentData.  # noqa: E501
        :type: bool
        """

        self._is_3d = is_3d

    @property
    def note(self):
        """Gets the note of this PaymentResponsePaymentData.  # noqa: E501

        Payment note  # noqa: E501

        :return: The note of this PaymentResponsePaymentData.  # noqa: E501
        :rtype: str
        """
        return self._note

    @note.setter
    def note(self, note):
        """Sets the note of this PaymentResponsePaymentData.

        Payment note  # noqa: E501

        :param note: The note of this PaymentResponsePaymentData.  # noqa: E501
        :type: str
        """

        self._note = note

    @property
    def rrn(self):
        """Gets the rrn of this PaymentResponsePaymentData.  # noqa: E501

        RRN (Retrieval Reference Number), supplied by the acquiring financial institution *(for BANKCARD payment method only)*  # noqa: E501

        :return: The rrn of this PaymentResponsePaymentData.  # noqa: E501
        :rtype: str
        """
        return self._rrn

    @rrn.setter
    def rrn(self, rrn):
        """Sets the rrn of this PaymentResponsePaymentData.

        RRN (Retrieval Reference Number), supplied by the acquiring financial institution *(for BANKCARD payment method only)*  # noqa: E501

        :param rrn: The rrn of this PaymentResponsePaymentData.  # noqa: E501
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
        VOIDED = "VOIDED"
        TERMINATED = "TERMINATED"
        CHARGED_BACK = "CHARGED_BACK"
        CHARGEBACK_RESOLVED = "CHARGEBACK_RESOLVED"

    @property
    def status(self):
        """Gets the status of this PaymentResponsePaymentData.  # noqa: E501

        Current payment status, *(mandatory for WEBMONEY and BITCOIN payment method only)*  # noqa: E501

        :return: The status of this PaymentResponsePaymentData.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this PaymentResponsePaymentData.

        Current payment status, *(mandatory for WEBMONEY and BITCOIN payment method only)*  # noqa: E501

        :param status: The status of this PaymentResponsePaymentData.  # noqa: E501
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
        ]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}".format(  # noqa: E501
                    status, allowed_values
                )
            )

        self._status = status

    class TransType(object):
        _01 = "01"
        _03 = "03"
        _10 = "10"
        _11 = "11"
        _28 = "28"

    @property
    def trans_type(self):
        """Gets the trans_type of this PaymentResponsePaymentData.  # noqa: E501


        :return: The trans_type of this PaymentResponsePaymentData.  # noqa: E501
        :rtype: str
        """
        return self._trans_type

    @trans_type.setter
    def trans_type(self, trans_type):
        """Sets the trans_type of this PaymentResponsePaymentData.


        :param trans_type: The trans_type of this PaymentResponsePaymentData.  # noqa: E501
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
        if issubclass(PaymentResponsePaymentData, dict):
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
        if not isinstance(other, PaymentResponsePaymentData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
