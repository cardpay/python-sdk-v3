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

from cardpay.model.payment_response_living_address import (
    PaymentResponseLivingAddress,
)  # noqa: F401,E501


class PayoutResponseCustomer(object):
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
        "id": "str",
        "ip_country": "str",
        "living_address": "PaymentResponseLivingAddress",
        "phone": "str",
        "user_agent": "str",
    }

    attribute_map = {
        "email": "email",
        "id": "id",
        "ip_country": "ip_country",
        "living_address": "living_address",
        "phone": "phone",
        "user_agent": "user_agent",
    }

    def __init__(
        self,
        email=None,
        id=None,
        ip_country=None,
        living_address=None,
        phone=None,
        user_agent=None,
    ):  # noqa: E501
        """PayoutResponseCustomer - a model defined in Swagger"""  # noqa: E501

        self._email = None
        self._id = None
        self._ip_country = None
        self._living_address = None
        self._phone = None
        self._user_agent = None
        self.discriminator = None

        if email is not None:
            self.email = email
        if id is not None:
            self.id = id
        if ip_country is not None:
            self.ip_country = ip_country
        if living_address is not None:
            self.living_address = living_address
        if phone is not None:
            self.phone = phone
        if user_agent is not None:
            self.user_agent = user_agent

    @property
    def email(self):
        """Gets the email of this PayoutResponseCustomer.  # noqa: E501

        Customer's e-mail address, here can be value returned from payment method - in case then in Merchant request `customer.email` wasn't presented  # noqa: E501

        :return: The email of this PayoutResponseCustomer.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this PayoutResponseCustomer.

        Customer's e-mail address, here can be value returned from payment method - in case then in Merchant request `customer.email` wasn't presented  # noqa: E501

        :param email: The email of this PayoutResponseCustomer.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def id(self):
        """Gets the id of this PayoutResponseCustomer.  # noqa: E501

        Customer's ID in Merchant's system  # noqa: E501

        :return: The id of this PayoutResponseCustomer.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PayoutResponseCustomer.

        Customer's ID in Merchant's system  # noqa: E501

        :param id: The id of this PayoutResponseCustomer.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def ip_country(self):
        """Gets the ip_country of this PayoutResponseCustomer.  # noqa: E501

        Customer country by IP  # noqa: E501

        :return: The ip_country of this PayoutResponseCustomer.  # noqa: E501
        :rtype: str
        """
        return self._ip_country

    @ip_country.setter
    def ip_country(self, ip_country):
        """Sets the ip_country of this PayoutResponseCustomer.

        Customer country by IP  # noqa: E501

        :param ip_country: The ip_country of this PayoutResponseCustomer.  # noqa: E501
        :type: str
        """

        self._ip_country = ip_country

    @property
    def living_address(self):
        """Gets the living_address of this PayoutResponseCustomer.  # noqa: E501

        Living address  # noqa: E501

        :return: The living_address of this PayoutResponseCustomer.  # noqa: E501
        :rtype: PaymentResponseLivingAddress
        """
        return self._living_address

    @living_address.setter
    def living_address(self, living_address):
        """Sets the living_address of this PayoutResponseCustomer.

        Living address  # noqa: E501

        :param living_address: The living_address of this PayoutResponseCustomer.  # noqa: E501
        :type: PaymentResponseLivingAddress
        """

        self._living_address = living_address

    @property
    def phone(self):
        """Gets the phone of this PayoutResponseCustomer.  # noqa: E501

        Customer's phone  # noqa: E501

        :return: The phone of this PayoutResponseCustomer.  # noqa: E501
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this PayoutResponseCustomer.

        Customer's phone  # noqa: E501

        :param phone: The phone of this PayoutResponseCustomer.  # noqa: E501
        :type: str
        """

        self._phone = phone

    @property
    def user_agent(self):
        """Gets the user_agent of this PayoutResponseCustomer.  # noqa: E501

        User agent  # noqa: E501

        :return: The user_agent of this PayoutResponseCustomer.  # noqa: E501
        :rtype: str
        """
        return self._user_agent

    @user_agent.setter
    def user_agent(self, user_agent):
        """Sets the user_agent of this PayoutResponseCustomer.

        User agent  # noqa: E501

        :param user_agent: The user_agent of this PayoutResponseCustomer.  # noqa: E501
        :type: str
        """

        self._user_agent = user_agent

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
        if issubclass(PayoutResponseCustomer, dict):
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
        if not isinstance(other, PayoutResponseCustomer):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
