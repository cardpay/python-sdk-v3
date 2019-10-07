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


class PaymentRequestEWalletAccount(object):
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
        "bank_code": "str",
        "expiration": "str",
        "id": "str",
        "verification_code": "str",
    }

    attribute_map = {
        "bank_code": "bank_code",
        "expiration": "expiration",
        "id": "id",
        "verification_code": "verification_code",
    }

    def __init__(
        self, bank_code=None, expiration=None, id=None, verification_code=None
    ):  # noqa: E501
        """PaymentRequestEWalletAccount - a model defined in Swagger"""  # noqa: E501

        self._bank_code = None
        self._expiration = None
        self._id = None
        self._verification_code = None
        self.discriminator = None

        if bank_code is not None:
            self.bank_code = bank_code
        if expiration is not None:
            self.expiration = expiration
        if id is not None:
            self.id = id
        if verification_code is not None:
            self.verification_code = verification_code

    @property
    def bank_code(self):
        """Gets the bank_code of this PaymentRequestEWalletAccount.  # noqa: E501

        Card issuer's code. For DIRECTBANKINGNGA: Customer bank code (3 digits). Mandatory for DIRECTBANKINGNGA payment method only.  # noqa: E501

        :return: The bank_code of this PaymentRequestEWalletAccount.  # noqa: E501
        :rtype: str
        """
        return self._bank_code

    @bank_code.setter
    def bank_code(self, bank_code):
        """Sets the bank_code of this PaymentRequestEWalletAccount.

        Card issuer's code. For DIRECTBANKINGNGA: Customer bank code (3 digits). Mandatory for DIRECTBANKINGNGA payment method only.  # noqa: E501

        :param bank_code: The bank_code of this PaymentRequestEWalletAccount.  # noqa: E501
        :type: str
        """

        self._bank_code = bank_code

    @property
    def expiration(self):
        """Gets the expiration of this PaymentRequestEWalletAccount.  # noqa: E501

        Card expiration date  # noqa: E501

        :return: The expiration of this PaymentRequestEWalletAccount.  # noqa: E501
        :rtype: str
        """
        return self._expiration

    @expiration.setter
    def expiration(self, expiration):
        """Sets the expiration of this PaymentRequestEWalletAccount.

        Card expiration date  # noqa: E501

        :param expiration: The expiration of this PaymentRequestEWalletAccount.  # noqa: E501
        :type: str
        """
        if expiration is not None and not re.search(
            r"^\\d{1,2}\/\\d{4}", expiration
        ):  # noqa: E501
            raise ValueError(
                r"Invalid value for `expiration`, must be a follow pattern or equal to `/^\\d{1,2}\/\\d{4}/`"
            )  # noqa: E501

        self._expiration = expiration

    @property
    def id(self):
        """Gets the id of this PaymentRequestEWalletAccount.  # noqa: E501

        For QIWI: Customer phone number (from 1 to 15 digits). For NETELLER: email address of Customer. For 'Latin America': Customer personal identification number: CPF or CNPJ for Brazil, DNI for Argentina and ID for other countries. For AIRTEL, MPESA, MTN, UGANDAMOBILE, VODAFONE and TIGO: phone number linked to Customer's mobile money account. For DIRECTBANKINGNGA: bank account number Mandatory for QIWI, NETELLER, 'Latin America', AIRTEL, MPESA, MTN, UGANDAMOBILE, VODAFONE, TIGO and DIRECTBANKINGNGA payment methods only.  # noqa: E501

        :return: The id of this PaymentRequestEWalletAccount.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PaymentRequestEWalletAccount.

        For QIWI: Customer phone number (from 1 to 15 digits). For NETELLER: email address of Customer. For 'Latin America': Customer personal identification number: CPF or CNPJ for Brazil, DNI for Argentina and ID for other countries. For AIRTEL, MPESA, MTN, UGANDAMOBILE, VODAFONE and TIGO: phone number linked to Customer's mobile money account. For DIRECTBANKINGNGA: bank account number Mandatory for QIWI, NETELLER, 'Latin America', AIRTEL, MPESA, MTN, UGANDAMOBILE, VODAFONE, TIGO and DIRECTBANKINGNGA payment methods only.  # noqa: E501

        :param id: The id of this PaymentRequestEWalletAccount.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def verification_code(self):
        """Gets the verification_code of this PaymentRequestEWalletAccount.  # noqa: E501

        Provider security code. For NETELLER: member's 6 digits Secure Id or Google Authenticator OTP For VODAFONE: Customer voucher code (6 digits) For UBA bank in DIRECTBANKINGNGA: Customer BVN (bank verification number) number, 11 digits Mandatory for NETELLER, VODAFONE and DIRECTBANKINGNGA payment methods only.  # noqa: E501

        :return: The verification_code of this PaymentRequestEWalletAccount.  # noqa: E501
        :rtype: str
        """
        return self._verification_code

    @verification_code.setter
    def verification_code(self, verification_code):
        """Sets the verification_code of this PaymentRequestEWalletAccount.

        Provider security code. For NETELLER: member's 6 digits Secure Id or Google Authenticator OTP For VODAFONE: Customer voucher code (6 digits) For UBA bank in DIRECTBANKINGNGA: Customer BVN (bank verification number) number, 11 digits Mandatory for NETELLER, VODAFONE and DIRECTBANKINGNGA payment methods only.  # noqa: E501

        :param verification_code: The verification_code of this PaymentRequestEWalletAccount.  # noqa: E501
        :type: str
        """

        self._verification_code = verification_code

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
        if issubclass(PaymentRequestEWalletAccount, dict):
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
        if not isinstance(other, PaymentRequestEWalletAccount):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
