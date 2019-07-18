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


class PaymentResponseCardAccount(object):
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
        'expiration': 'str',
        'holder': 'str',
        'issuing_country_code': 'str',
        'masked_pan': 'str',
        'token': 'str'
    }

    attribute_map = {
        'expiration': 'expiration',
        'holder': 'holder',
        'issuing_country_code': 'issuing_country_code',
        'masked_pan': 'masked_pan',
        'token': 'token'
    }

    def __init__(self, expiration=None, holder=None, issuing_country_code=None, masked_pan=None, token=None):  # noqa: E501
        """PaymentResponseCardAccount - a model defined in Swagger"""  # noqa: E501

        self._expiration = None
        self._holder = None
        self._issuing_country_code = None
        self._masked_pan = None
        self._token = None
        self.discriminator = None

        if expiration is not None:
            self.expiration = expiration
        if holder is not None:
            self.holder = holder
        if issuing_country_code is not None:
            self.issuing_country_code = issuing_country_code
        if masked_pan is not None:
            self.masked_pan = masked_pan
        if token is not None:
            self.token = token

    @property
    def expiration(self):
        """Gets the expiration of this PaymentResponseCardAccount.  # noqa: E501

        Customer’s card expiration date. Format: mm/yyyy. Returned only if setting 'Callback: card expiry' in a wallet in PM system is ON  # noqa: E501

        :return: The expiration of this PaymentResponseCardAccount.  # noqa: E501
        :rtype: str
        """
        return self._expiration

    @expiration.setter
    def expiration(self, expiration):
        """Sets the expiration of this PaymentResponseCardAccount.

        Customer’s card expiration date. Format: mm/yyyy. Returned only if setting 'Callback: card expiry' in a wallet in PM system is ON  # noqa: E501

        :param expiration: The expiration of this PaymentResponseCardAccount.  # noqa: E501
        :type: str
        """

        self._expiration = expiration

    @property
    def holder(self):
        """Gets the holder of this PaymentResponseCardAccount.  # noqa: E501

        Customer's cardholder name. Any valid cardholder name. Not present by default, ask CardPay manager to enable it if needed.  # noqa: E501

        :return: The holder of this PaymentResponseCardAccount.  # noqa: E501
        :rtype: str
        """
        return self._holder

    @holder.setter
    def holder(self, holder):
        """Sets the holder of this PaymentResponseCardAccount.

        Customer's cardholder name. Any valid cardholder name. Not present by default, ask CardPay manager to enable it if needed.  # noqa: E501

        :param holder: The holder of this PaymentResponseCardAccount.  # noqa: E501
        :type: str
        """

        self._holder = holder

    @property
    def issuing_country_code(self):
        """Gets the issuing_country_code of this PaymentResponseCardAccount.  # noqa: E501

        Country code of issuing card country  # noqa: E501

        :return: The issuing_country_code of this PaymentResponseCardAccount.  # noqa: E501
        :rtype: str
        """
        return self._issuing_country_code

    @issuing_country_code.setter
    def issuing_country_code(self, issuing_country_code):
        """Sets the issuing_country_code of this PaymentResponseCardAccount.

        Country code of issuing card country  # noqa: E501

        :param issuing_country_code: The issuing_country_code of this PaymentResponseCardAccount.  # noqa: E501
        :type: str
        """

        self._issuing_country_code = issuing_country_code

    @property
    def masked_pan(self):
        """Gets the masked_pan of this PaymentResponseCardAccount.  # noqa: E501

        Masked PAN (shows first 6 digits and 4 last digits)  # noqa: E501

        :return: The masked_pan of this PaymentResponseCardAccount.  # noqa: E501
        :rtype: str
        """
        return self._masked_pan

    @masked_pan.setter
    def masked_pan(self, masked_pan):
        """Sets the masked_pan of this PaymentResponseCardAccount.

        Masked PAN (shows first 6 digits and 4 last digits)  # noqa: E501

        :param masked_pan: The masked_pan of this PaymentResponseCardAccount.  # noqa: E501
        :type: str
        """

        self._masked_pan = masked_pan

    @property
    def token(self):
        """Gets the token of this PaymentResponseCardAccount.  # noqa: E501

        Generated card token value. For payment: PaymentResponsePaymentData, for recurring: RecurringResponseRecurringData. Token can be returned only for successful transactions (not for declined transactions)  # noqa: E501

        :return: The token of this PaymentResponseCardAccount.  # noqa: E501
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this PaymentResponseCardAccount.

        Generated card token value. For payment: PaymentResponsePaymentData, for recurring: RecurringResponseRecurringData. Token can be returned only for successful transactions (not for declined transactions)  # noqa: E501

        :param token: The token of this PaymentResponseCardAccount.  # noqa: E501
        :type: str
        """

        self._token = token

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
        if issubclass(PaymentResponseCardAccount, dict):
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
        if not isinstance(other, PaymentResponseCardAccount):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
