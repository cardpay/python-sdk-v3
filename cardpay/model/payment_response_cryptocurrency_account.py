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


class PaymentResponseCryptocurrencyAccount(object):
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
        'crypto_address': 'str',
        'crypto_transaction_id': 'str',
        'prc_amount': 'float',
        'prc_currency': 'str'
    }

    attribute_map = {
        'crypto_address': 'crypto_address',
        'crypto_transaction_id': 'crypto_transaction_id',
        'prc_amount': 'prc_amount',
        'prc_currency': 'prc_currency'
    }

    def __init__(self, crypto_address=None, crypto_transaction_id=None, prc_amount=None, prc_currency=None):  # noqa: E501
        """PaymentResponseCryptocurrencyAccount - a model defined in Swagger"""  # noqa: E501

        self._crypto_address = None
        self._crypto_transaction_id = None
        self._prc_amount = None
        self._prc_currency = None
        self.discriminator = None

        if crypto_address is not None:
            self.crypto_address = crypto_address
        if crypto_transaction_id is not None:
            self.crypto_transaction_id = crypto_transaction_id
        if prc_amount is not None:
            self.prc_amount = prc_amount
        if prc_currency is not None:
            self.prc_currency = prc_currency

    @property
    def crypto_address(self):
        """Gets the crypto_address of this PaymentResponseCryptocurrencyAccount.  # noqa: E501

        Bitcoin address for created transaction  # noqa: E501

        :return: The crypto_address of this PaymentResponseCryptocurrencyAccount.  # noqa: E501
        :rtype: str
        """
        return self._crypto_address

    @crypto_address.setter
    def crypto_address(self, crypto_address):
        """Sets the crypto_address of this PaymentResponseCryptocurrencyAccount.

        Bitcoin address for created transaction  # noqa: E501

        :param crypto_address: The crypto_address of this PaymentResponseCryptocurrencyAccount.  # noqa: E501
        :type: str
        """

        self._crypto_address = crypto_address

    @property
    def crypto_transaction_id(self):
        """Gets the crypto_transaction_id of this PaymentResponseCryptocurrencyAccount.  # noqa: E501

        Id of created transaction in the bitcoin system  # noqa: E501

        :return: The crypto_transaction_id of this PaymentResponseCryptocurrencyAccount.  # noqa: E501
        :rtype: str
        """
        return self._crypto_transaction_id

    @crypto_transaction_id.setter
    def crypto_transaction_id(self, crypto_transaction_id):
        """Sets the crypto_transaction_id of this PaymentResponseCryptocurrencyAccount.

        Id of created transaction in the bitcoin system  # noqa: E501

        :param crypto_transaction_id: The crypto_transaction_id of this PaymentResponseCryptocurrencyAccount.  # noqa: E501
        :type: str
        """

        self._crypto_transaction_id = crypto_transaction_id

    @property
    def prc_amount(self):
        """Gets the prc_amount of this PaymentResponseCryptocurrencyAccount.  # noqa: E501

        Transaction amount (only for FIAT-BTC scenario)  # noqa: E501

        :return: The prc_amount of this PaymentResponseCryptocurrencyAccount.  # noqa: E501
        :rtype: float
        """
        return self._prc_amount

    @prc_amount.setter
    def prc_amount(self, prc_amount):
        """Sets the prc_amount of this PaymentResponseCryptocurrencyAccount.

        Transaction amount (only for FIAT-BTC scenario)  # noqa: E501

        :param prc_amount: The prc_amount of this PaymentResponseCryptocurrencyAccount.  # noqa: E501
        :type: float
        """

        self._prc_amount = prc_amount

    @property
    def prc_currency(self):
        """Gets the prc_currency of this PaymentResponseCryptocurrencyAccount.  # noqa: E501

        Currency of transaction (only for FIAT-BTC scenario)  # noqa: E501

        :return: The prc_currency of this PaymentResponseCryptocurrencyAccount.  # noqa: E501
        :rtype: str
        """
        return self._prc_currency

    @prc_currency.setter
    def prc_currency(self, prc_currency):
        """Sets the prc_currency of this PaymentResponseCryptocurrencyAccount.

        Currency of transaction (only for FIAT-BTC scenario)  # noqa: E501

        :param prc_currency: The prc_currency of this PaymentResponseCryptocurrencyAccount.  # noqa: E501
        :type: str
        """

        self._prc_currency = prc_currency

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
        if issubclass(PaymentResponseCryptocurrencyAccount, dict):
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
        if not isinstance(other, PaymentResponseCryptocurrencyAccount):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
