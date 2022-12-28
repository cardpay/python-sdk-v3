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


class RecurringCustomer(object):
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
        "home_phone": "str",
        "id": "str",
        "identity": "str",
        "ip": "str",
        "ip_country": "str",
        "locale": "str",
        "phone": "str",
        "user_agent": "str",
        "work_phone": "str",
    }

    attribute_map = {
        "email": "email",
        "home_phone": "home_phone",
        "id": "id",
        "identity": "identity",
        "ip": "ip",
        "ip_country": "ip_country",
        "locale": "locale",
        "phone": "phone",
        "user_agent": "user_agent",
        "work_phone": "work_phone",
    }

    def __init__(
        self,
        email=None,
        home_phone=None,
        id=None,
        identity=None,
        ip=None,
        ip_country=None,
        locale=None,
        phone=None,
        user_agent=None,
        work_phone=None,
    ):  # noqa: E501
        """RecurringCustomer - a model defined in Swagger"""  # noqa: E501

        self._email = None
        self._home_phone = None
        self._id = None
        self._identity = None
        self._ip = None
        self._ip_country = None
        self._locale = None
        self._phone = None
        self._user_agent = None
        self._work_phone = None
        self.discriminator = None

        self.email = email
        if home_phone is not None:
            self.home_phone = home_phone
        self.id = id
        if identity is not None:
            self.identity = identity
        if ip is not None:
            self.ip = ip
        if ip_country is not None:
            self.ip_country = ip_country
        if locale is not None:
            self.locale = locale
        if phone is not None:
            self.phone = phone
        if user_agent is not None:
            self.user_agent = user_agent
        if work_phone is not None:
            self.work_phone = work_phone

    @property
    def email(self):
        """Gets the email of this RecurringCustomer.  # noqa: E501

        Customer's e-mail address. Mandatory by default, can be defined as optional by CardPay manager.  # noqa: E501

        :return: The email of this RecurringCustomer.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this RecurringCustomer.

        Customer's e-mail address. Mandatory by default, can be defined as optional by CardPay manager.  # noqa: E501

        :param email: The email of this RecurringCustomer.  # noqa: E501
        :type: str
        """
        if email is None:
            raise ValueError(
                "Invalid value for `email`, must not be `None`"
            )  # noqa: E501
        if email is not None and len(email) > 256:
            raise ValueError(
                "Invalid value for `email`, length must be less than or equal to `256`"
            )  # noqa: E501
        if email is not None and len(email) < 3:
            raise ValueError(
                "Invalid value for `email`, length must be greater than or equal to `3`"
            )  # noqa: E501

        self._email = email

    @property
    def home_phone(self):
        """Gets the home_phone of this RecurringCustomer.  # noqa: E501

        The work phone number provided by the Cardholder. Required (if available), unless market or regional mandate restricts sending this information. Characters Format: string (10-18 symbols) country code + Subscriber number. Refer to ITU-E.164 for additional information on format and length.  # noqa: E501

        :return: The home_phone of this RecurringCustomer.  # noqa: E501
        :rtype: str
        """
        return self._home_phone

    @home_phone.setter
    def home_phone(self, home_phone):
        """Sets the home_phone of this RecurringCustomer.

        The work phone number provided by the Cardholder. Required (if available), unless market or regional mandate restricts sending this information. Characters Format: string (10-18 symbols) country code + Subscriber number. Refer to ITU-E.164 for additional information on format and length.  # noqa: E501

        :param home_phone: The home_phone of this RecurringCustomer.  # noqa: E501
        :type: str
        """
        if home_phone is not None and len(home_phone) > 18:
            raise ValueError(
                "Invalid value for `home_phone`, length must be less than or equal to `18`"
            )  # noqa: E501
        if home_phone is not None and len(home_phone) < 8:
            raise ValueError(
                "Invalid value for `home_phone`, length must be greater than or equal to `8`"
            )  # noqa: E501

        self._home_phone = home_phone

    @property
    def id(self):
        """Gets the id of this RecurringCustomer.  # noqa: E501

        Customer's ID in Merchant's system  # noqa: E501

        :return: The id of this RecurringCustomer.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this RecurringCustomer.

        Customer's ID in Merchant's system  # noqa: E501

        :param id: The id of this RecurringCustomer.  # noqa: E501
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
    def identity(self):
        """Gets the identity of this RecurringCustomer.  # noqa: E501

        Customer's identity in Merchant's system required for Brazil Installments  # noqa: E501

        :return: The identity of this RecurringCustomer.  # noqa: E501
        :rtype: str
        """
        return self._identity

    @identity.setter
    def identity(self, identity):
        """Sets the identity of this RecurringCustomer.

        Customer's identity in Merchant's system required for Brazil Installments  # noqa: E501

        :param identity: The identity of this RecurringCustomer.  # noqa: E501
        :type: str
        """
        if identity is not None and len(identity) > 256:
            raise ValueError(
                "Invalid value for `identity`, length must be less than or equal to `256`"
            )  # noqa: E501
        if identity is not None and len(identity) < 0:
            raise ValueError(
                "Invalid value for `identity`, length must be greater than or equal to `0`"
            )  # noqa: E501

        self._identity = identity

    @property
    def ip(self):
        """Gets the ip of this RecurringCustomer.  # noqa: E501

        Customer IPv4  # noqa: E501

        :return: The ip of this RecurringCustomer.  # noqa: E501
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """Sets the ip of this RecurringCustomer.

        Customer IPv4  # noqa: E501

        :param ip: The ip of this RecurringCustomer.  # noqa: E501
        :type: str
        """

        self._ip = ip

    @property
    def ip_country(self):
        """Gets the ip_country of this RecurringCustomer.  # noqa: E501

        Customer country by IP  # noqa: E501

        :return: The ip_country of this RecurringCustomer.  # noqa: E501
        :rtype: str
        """
        return self._ip_country

    @ip_country.setter
    def ip_country(self, ip_country):
        """Sets the ip_country of this RecurringCustomer.

        Customer country by IP  # noqa: E501

        :param ip_country: The ip_country of this RecurringCustomer.  # noqa: E501
        :type: str
        """

        self._ip_country = ip_country

    class Locale(object):
        RU = "ru"
        EN = "en"
        ZH = "zh"
        JA = "ja"

    @property
    def locale(self):
        """Gets the locale of this RecurringCustomer.  # noqa: E501

        Preferred locale for the payment page ([ISO 639-1](https://en.wikipedia.org/wiki/ISO_639-1) language code). The default locale will be applied if the selected locale is not supported. Supported locales are: `ru`, `en`, `zh`, `ja`  # noqa: E501

        :return: The locale of this RecurringCustomer.  # noqa: E501
        :rtype: str
        """
        return self._locale

    @locale.setter
    def locale(self, locale):
        """Sets the locale of this RecurringCustomer.

        Preferred locale for the payment page ([ISO 639-1](https://en.wikipedia.org/wiki/ISO_639-1) language code). The default locale will be applied if the selected locale is not supported. Supported locales are: `ru`, `en`, `zh`, `ja`  # noqa: E501

        :param locale: The locale of this RecurringCustomer.  # noqa: E501
        :type: str
        """
        allowed_values = ["ru", "en", "zh", "ja"]  # noqa: E501
        if locale not in allowed_values:
            raise ValueError(
                "Invalid value for `locale` ({0}), must be one of {1}".format(  # noqa: E501
                    locale, allowed_values
                )
            )

        self._locale = locale

    @property
    def phone(self):
        """Gets the phone of this RecurringCustomer.  # noqa: E501

        Customer phone number. Optional by default, can be defined as mandatory by CardPay manager.  # noqa: E501

        :return: The phone of this RecurringCustomer.  # noqa: E501
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this RecurringCustomer.

        Customer phone number. Optional by default, can be defined as mandatory by CardPay manager.  # noqa: E501

        :param phone: The phone of this RecurringCustomer.  # noqa: E501
        :type: str
        """
        if phone is not None and len(phone) > 18:
            raise ValueError(
                "Invalid value for `phone`, length must be less than or equal to `18`"
            )  # noqa: E501
        if phone is not None and len(phone) < 8:
            raise ValueError(
                "Invalid value for `phone`, length must be greater than or equal to `8`"
            )  # noqa: E501

        self._phone = phone

    @property
    def user_agent(self):
        """Gets the user_agent of this RecurringCustomer.  # noqa: E501

        User agent  # noqa: E501

        :return: The user_agent of this RecurringCustomer.  # noqa: E501
        :rtype: str
        """
        return self._user_agent

    @user_agent.setter
    def user_agent(self, user_agent):
        """Sets the user_agent of this RecurringCustomer.

        User agent  # noqa: E501

        :param user_agent: The user_agent of this RecurringCustomer.  # noqa: E501
        :type: str
        """

        self._user_agent = user_agent

    @property
    def work_phone(self):
        """Gets the work_phone of this RecurringCustomer.  # noqa: E501

        The home phone number provided by the Cardholder. Required (if available) unless market or regional mandate restricts sending this information. Characters Format: string (10-18 symbols) country code + Subscriber number. Refer to ITU-E.164 for additional information on format and length.  # noqa: E501

        :return: The work_phone of this RecurringCustomer.  # noqa: E501
        :rtype: str
        """
        return self._work_phone

    @work_phone.setter
    def work_phone(self, work_phone):
        """Sets the work_phone of this RecurringCustomer.

        The home phone number provided by the Cardholder. Required (if available) unless market or regional mandate restricts sending this information. Characters Format: string (10-18 symbols) country code + Subscriber number. Refer to ITU-E.164 for additional information on format and length.  # noqa: E501

        :param work_phone: The work_phone of this RecurringCustomer.  # noqa: E501
        :type: str
        """
        if work_phone is not None and len(work_phone) > 18:
            raise ValueError(
                "Invalid value for `work_phone`, length must be less than or equal to `18`"
            )  # noqa: E501
        if work_phone is not None and len(work_phone) < 8:
            raise ValueError(
                "Invalid value for `work_phone`, length must be greater than or equal to `8`"
            )  # noqa: E501

        self._work_phone = work_phone

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
        if issubclass(RecurringCustomer, dict):
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
        if not isinstance(other, RecurringCustomer):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
