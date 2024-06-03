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


class InvoiceCustomer(object):
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
    swagger_types = {"email": "str", "id": "str", "locale": "str", "phone": "str"}

    attribute_map = {"email": "email", "id": "id", "locale": "locale", "phone": "phone"}

    def __init__(self, email=None, id=None, locale=None, phone=None):  # noqa: E501
        """InvoiceCustomer - a model defined in Swagger"""  # noqa: E501

        self._email = None
        self._id = None
        self._locale = None
        self._phone = None
        self.discriminator = None

        if email is not None:
            self.email = email
        self.id = id
        if locale is not None:
            self.locale = locale
        if phone is not None:
            self.phone = phone

    @property
    def email(self):
        """Gets the email of this InvoiceCustomer.  # noqa: E501

        Email address of the customer  # noqa: E501

        :return: The email of this InvoiceCustomer.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this InvoiceCustomer.

        Email address of the customer  # noqa: E501

        :param email: The email of this InvoiceCustomer.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def id(self):
        """Gets the id of this InvoiceCustomer.  # noqa: E501

        Customer's ID in Merchant's system  # noqa: E501

        :return: The id of this InvoiceCustomer.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this InvoiceCustomer.

        Customer's ID in Merchant's system  # noqa: E501

        :param id: The id of this InvoiceCustomer.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501
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
    def locale(self):
        """Gets the locale of this InvoiceCustomer.  # noqa: E501

        Preferred locale for the payment page ([ISO 639-1](https://en.wikipedia.org/wiki/ISO_639-1) language code). The default locale (en or other locale if it's set as default in Merchant account) will be applied if the selected locale (received in request) is not supported. Supported locales are: `ar`, `az`, `bg`, `cs`, `de`, `el`, `en`, `es`, `fr`, `hu`, `hy`, `id`, `it`, `ja`, `ka`, `ko`, `ms`, `nl`, `pl`, `pt`, `ro`, `ru`, `sr`, `sv`, `th`, `tr`, `uk`, `vi`, `zh`  # noqa: E501

        :return: The locale of this InvoiceCustomer.  # noqa: E501
        :rtype: str
        """
        return self._locale

    @locale.setter
    def locale(self, locale):
        """Sets the locale of this InvoiceCustomer.

        Preferred locale for the payment page ([ISO 639-1](https://en.wikipedia.org/wiki/ISO_639-1) language code). The default locale (en or other locale if it's set as default in Merchant account) will be applied if the selected locale (received in request) is not supported. Supported locales are: `ar`, `az`, `bg`, `cs`, `de`, `el`, `en`, `es`, `fr`, `hu`, `hy`, `id`, `it`, `ja`, `ka`, `ko`, `ms`, `nl`, `pl`, `pt`, `ro`, `ru`, `sr`, `sv`, `th`, `tr`, `uk`, `vi`, `zh`  # noqa: E501

        :param locale: The locale of this InvoiceCustomer.  # noqa: E501
        :type: str
        """

        self._locale = locale

    @property
    def phone(self):
        """Gets the phone of this InvoiceCustomer.  # noqa: E501

        Customer phone number  # noqa: E501

        :return: The phone of this InvoiceCustomer.  # noqa: E501
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this InvoiceCustomer.

        Customer phone number  # noqa: E501

        :param phone: The phone of this InvoiceCustomer.  # noqa: E501
        :type: str
        """

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
        if issubclass(InvoiceCustomer, dict):
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
        if not isinstance(other, InvoiceCustomer):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
