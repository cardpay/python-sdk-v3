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


class InvoiceData(object):
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
        "currency": "str",
        "expire_at": "datetime",
        "installment_type": "str",
        "installments": "list[int]",
        "reusable": "bool",
        "reuse_count": "int",
    }

    attribute_map = {
        "amount": "amount",
        "currency": "currency",
        "expire_at": "expire_at",
        "installment_type": "installment_type",
        "installments": "installments",
        "reusable": "reusable",
        "reuse_count": "reuse_count",
    }

    def __init__(
        self,
        amount=None,
        currency=None,
        expire_at=None,
        installment_type=None,
        installments=None,
        reusable=None,
        reuse_count=None,
    ):  # noqa: E501
        """InvoiceData - a model defined in Swagger"""  # noqa: E501

        self._amount = None
        self._currency = None
        self._expire_at = None
        self._installment_type = None
        self._installments = None
        self._reusable = None
        self._reuse_count = None
        self.discriminator = None

        self.amount = amount
        self.currency = currency
        if expire_at is not None:
            self.expire_at = expire_at
        if installment_type is not None:
            self.installment_type = installment_type
        if installments is not None:
            self.installments = installments
        if reusable is not None:
            self.reusable = reusable
        if reuse_count is not None:
            self.reuse_count = reuse_count

    @property
    def amount(self):
        """Gets the amount of this InvoiceData.  # noqa: E501

        The total invoice amount in selected currency with dot as a decimal separator, must be less than 10 billion  # noqa: E501

        :return: The amount of this InvoiceData.  # noqa: E501
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this InvoiceData.

        The total invoice amount in selected currency with dot as a decimal separator, must be less than 10 billion  # noqa: E501

        :param amount: The amount of this InvoiceData.  # noqa: E501
        :type: float
        """
        if amount is None:
            raise ValueError(
                "Invalid value for `amount`, must not be `None`"
            )  # noqa: E501

        self._amount = amount

    @property
    def currency(self):
        """Gets the currency of this InvoiceData.  # noqa: E501

        [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) currency code  # noqa: E501

        :return: The currency of this InvoiceData.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this InvoiceData.

        [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) currency code  # noqa: E501

        :param currency: The currency of this InvoiceData.  # noqa: E501
        :type: str
        """
        if currency is None:
            raise ValueError(
                "Invalid value for `currency`, must not be `None`"
            )  # noqa: E501

        self._currency = currency

    @property
    def expire_at(self):
        """Gets the expire_at of this InvoiceData.  # noqa: E501

        Date and time of invoice expiring. Invoice cannot be used after this date and time.  # noqa: E501

        :return: The expire_at of this InvoiceData.  # noqa: E501
        :rtype: datetime
        """
        return self._expire_at

    @expire_at.setter
    def expire_at(self, expire_at):
        """Sets the expire_at of this InvoiceData.

        Date and time of invoice expiring. Invoice cannot be used after this date and time.  # noqa: E501

        :param expire_at: The expire_at of this InvoiceData.  # noqa: E501
        :type: datetime
        """

        self._expire_at = expire_at

    @property
    def installment_type(self):
        """Gets the installment_type of this InvoiceData.  # noqa: E501

        Installment type  # noqa: E501

        :return: The installment_type of this InvoiceData.  # noqa: E501
        :rtype: str
        """
        return self._installment_type

    @installment_type.setter
    def installment_type(self, installment_type):
        """Sets the installment_type of this InvoiceData.

        Installment type  # noqa: E501

        :param installment_type: The installment_type of this InvoiceData.  # noqa: E501
        :type: str
        """

        self._installment_type = installment_type

    @property
    def installments(self):
        """Gets the installments of this InvoiceData.  # noqa: E501

        Number of installments. It depends on country.  # noqa: E501

        :return: The installments of this InvoiceData.  # noqa: E501
        :rtype: list[int]
        """
        return self._installments

    @installments.setter
    def installments(self, installments):
        """Sets the installments of this InvoiceData.

        Number of installments. It depends on country.  # noqa: E501

        :param installments: The installments of this InvoiceData.  # noqa: E501
        :type: list[int]
        """

        self._installments = installments

    @property
    def reusable(self):
        """Gets the reusable of this InvoiceData.  # noqa: E501

        The flag that can be used for enabling payment link multiple times  # noqa: E501

        :return: The reusable of this InvoiceData.  # noqa: E501
        :rtype: bool
        """
        return self._reusable

    @reusable.setter
    def reusable(self, reusable):
        """Sets the reusable of this InvoiceData.

        The flag that can be used for enabling payment link multiple times  # noqa: E501

        :param reusable: The reusable of this InvoiceData.  # noqa: E501
        :type: bool
        """

        self._reusable = reusable

    @property
    def reuse_count(self):
        """Gets the reuse_count of this InvoiceData.  # noqa: E501

        The number that customer can pay by this link. Default value 10  # noqa: E501

        :return: The reuse_count of this InvoiceData.  # noqa: E501
        :rtype: int
        """
        return self._reuse_count

    @reuse_count.setter
    def reuse_count(self, reuse_count):
        """Sets the reuse_count of this InvoiceData.

        The number that customer can pay by this link. Default value 10  # noqa: E501

        :param reuse_count: The reuse_count of this InvoiceData.  # noqa: E501
        :type: int
        """
        if reuse_count is not None and reuse_count < 1:  # noqa: E501
            raise ValueError(
                "Invalid value for `reuse_count`, must be a value greater than or equal to `1`"
            )  # noqa: E501

        self._reuse_count = reuse_count

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
        if issubclass(InvoiceData, dict):
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
        if not isinstance(other, InvoiceData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
