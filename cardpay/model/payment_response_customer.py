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


class PaymentResponseCustomer(object):
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
        "email": "str",
        "full_name": "str",
        "id": "str",
        "ip": "str",
        "locale": "str",
        "phone": "str",
    }

    attribute_map = {
        "email": "email",
        "full_name": "full_name",
        "id": "id",
        "ip": "ip",
        "locale": "locale",
        "phone": "phone",
    }

    def __init__(
        self, email=None, full_name=None, id=None, ip=None, locale=None, phone=None
    ):  # noqa: E501
        """PaymentResponseCustomer - a model defined in Swagger"""  # noqa: E501

        self._email = None
        self._full_name = None
        self._id = None
        self._ip = None
        self._locale = None
        self._phone = None
        self.discriminator = None

        if email is not None:
            self.email = email
        if full_name is not None:
            self.full_name = full_name
        if id is not None:
            self.id = id
        if ip is not None:
            self.ip = ip
        if locale is not None:
            self.locale = locale
        if phone is not None:
            self.phone = phone

    @property
    def email(self):
        """Gets the email of this PaymentResponseCustomer.  # noqa: E501

        Email address of the customer (mandatory by default for 'Latin America', 'NETELLER', 'DIRECTBANKINGNGA', 'AQRCODE', 'AIRTEL', 'MPESA', 'MTN', 'UGANDAMOBILE', 'VODAFONE', 'TIGO' payment methods only)). Can be defined as optional by CardPay manager.  # noqa: E501

        :return: The email of this PaymentResponseCustomer.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this PaymentResponseCustomer.

        Email address of the customer (mandatory by default for 'Latin America', 'NETELLER', 'DIRECTBANKINGNGA', 'AQRCODE', 'AIRTEL', 'MPESA', 'MTN', 'UGANDAMOBILE', 'VODAFONE', 'TIGO' payment methods only)). Can be defined as optional by CardPay manager.  # noqa: E501

        :param email: The email of this PaymentResponseCustomer.  # noqa: E501
        :type: str
        """
        if email is not None and len(email) > 256:
            raise ValueError(
                "Invalid value for `email`, length must be less than or equal to `256`"
            )  # noqa: E501
        if email is not None and len(email) < 1:
            raise ValueError(
                "Invalid value for `email`, length must be greater than or equal to `1`"
            )  # noqa: E501

        self._email = email

    @property
    def full_name(self):
        """Gets the full_name of this PaymentResponseCustomer.  # noqa: E501

        Customer's full name  # noqa: E501

        :return: The full_name of this PaymentResponseCustomer.  # noqa: E501
        :rtype: str
        """
        return self._full_name

    @full_name.setter
    def full_name(self, full_name):
        """Sets the full_name of this PaymentResponseCustomer.

        Customer's full name  # noqa: E501

        :param full_name: The full_name of this PaymentResponseCustomer.  # noqa: E501
        :type: str
        """
        if full_name is not None and len(full_name) > 256:
            raise ValueError(
                "Invalid value for `full_name`, length must be less than or equal to `256`"
            )  # noqa: E501
        if full_name is not None and len(full_name) < 1:
            raise ValueError(
                "Invalid value for `full_name`, length must be greater than or equal to `1`"
            )  # noqa: E501

        self._full_name = full_name

    @property
    def id(self):
        """Gets the id of this PaymentResponseCustomer.  # noqa: E501

        Customer's ID in the merchant's system  # noqa: E501

        :return: The id of this PaymentResponseCustomer.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PaymentResponseCustomer.

        Customer's ID in the merchant's system  # noqa: E501

        :param id: The id of this PaymentResponseCustomer.  # noqa: E501
        :type: str
        """
        if id is not None and len(id) > 256:
            raise ValueError(
                "Invalid value for `id`, length must be less than or equal to `256`"
            )  # noqa: E501
        if id is not None and len(id) < 0:
            raise ValueError(
                "Invalid value for `id`, length must be greater than or equal to `0`"
            )  # noqa: E501

        self._id = id

    @property
    def ip(self):
        """Gets the ip of this PaymentResponseCustomer.  # noqa: E501

        IP address of Customer  # noqa: E501

        :return: The ip of this PaymentResponseCustomer.  # noqa: E501
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """Sets the ip of this PaymentResponseCustomer.

        IP address of Customer  # noqa: E501

        :param ip: The ip of this PaymentResponseCustomer.  # noqa: E501
        :type: str
        """
        if ip is not None and len(ip) > 15:
            raise ValueError(
                "Invalid value for `ip`, length must be less than or equal to `15`"
            )  # noqa: E501
        if ip is not None and len(ip) < 1:
            raise ValueError(
                "Invalid value for `ip`, length must be greater than or equal to `1`"
            )  # noqa: E501

        self._ip = ip

    @property
    def locale(self):
        """Gets the locale of this PaymentResponseCustomer.  # noqa: E501

        Preferred locale for the payment page ([ISO 639-1](https://en.wikipedia.org/wiki/ISO_639-1) language code). The default locale will be applied if the selected locale is not supported. Supported locales are: `ru`, `en`, `zh`, `ja`  # noqa: E501

        :return: The locale of this PaymentResponseCustomer.  # noqa: E501
        :rtype: str
        """
        return self._locale

    @locale.setter
    def locale(self, locale):
        """Sets the locale of this PaymentResponseCustomer.

        Preferred locale for the payment page ([ISO 639-1](https://en.wikipedia.org/wiki/ISO_639-1) language code). The default locale will be applied if the selected locale is not supported. Supported locales are: `ru`, `en`, `zh`, `ja`  # noqa: E501

        :param locale: The locale of this PaymentResponseCustomer.  # noqa: E501
        :type: str
        """

        self._locale = locale

    @property
    def phone(self):
        """Gets the phone of this PaymentResponseCustomer.  # noqa: E501

        Customer's phone number. Mandatory for DIRECTBANKINGNGA payment method. For other payment methods: optional by default, can be defined as mandatory by CardPay manager.  # noqa: E501

        :return: The phone of this PaymentResponseCustomer.  # noqa: E501
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this PaymentResponseCustomer.

        Customer's phone number. Mandatory for DIRECTBANKINGNGA payment method. For other payment methods: optional by default, can be defined as mandatory by CardPay manager.  # noqa: E501

        :param phone: The phone of this PaymentResponseCustomer.  # noqa: E501
        :type: str
        """
        if phone is not None and len(phone) > 12:
            raise ValueError(
                "Invalid value for `phone`, length must be less than or equal to `12`"
            )  # noqa: E501
        if phone is not None and len(phone) < 11:
            raise ValueError(
                "Invalid value for `phone`, length must be greater than or equal to `11`"
            )  # noqa: E501

        self._phone = phone

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
        if issubclass(PaymentResponseCustomer, dict):
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
        if not isinstance(other, PaymentResponseCustomer):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
