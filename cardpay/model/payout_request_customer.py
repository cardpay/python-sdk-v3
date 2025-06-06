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

from cardpay.model.device import Device  # noqa: F401,E501
from cardpay.model.payout_request_living_address import (
    PayoutRequestLivingAddress,
)  # noqa: F401,E501


class PayoutRequestCustomer(object):
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
        "birth_date": "datetime",
        "device": "Device",
        "document_type": "str",
        "email": "str",
        "first_name": "str",
        "full_name": "str",
        "id": "str",
        "identity": "str",
        "last_name": "str",
        "living_address": "PayoutRequestLivingAddress",
        "phone": "str",
        "tax_reason_code": "str",
    }

    attribute_map = {
        "birth_date": "birth_date",
        "device": "device",
        "document_type": "document_type",
        "email": "email",
        "first_name": "first_name",
        "full_name": "full_name",
        "id": "id",
        "identity": "identity",
        "last_name": "last_name",
        "living_address": "living_address",
        "phone": "phone",
        "tax_reason_code": "tax_reason_code",
    }

    def __init__(
        self,
        birth_date=None,
        device=None,
        document_type=None,
        email=None,
        first_name=None,
        full_name=None,
        id=None,
        identity=None,
        last_name=None,
        living_address=None,
        phone=None,
        tax_reason_code=None,
    ):  # noqa: E501
        """PayoutRequestCustomer - a model defined in Swagger"""  # noqa: E501

        self._birth_date = None
        self._device = None
        self._document_type = None
        self._email = None
        self._first_name = None
        self._full_name = None
        self._id = None
        self._identity = None
        self._last_name = None
        self._living_address = None
        self._phone = None
        self._tax_reason_code = None
        self.discriminator = None

        if birth_date is not None:
            self.birth_date = birth_date
        if device is not None:
            self.device = device
        if document_type is not None:
            self.document_type = document_type
        if email is not None:
            self.email = email
        if first_name is not None:
            self.first_name = first_name
        if full_name is not None:
            self.full_name = full_name
        if id is not None:
            self.id = id
        if identity is not None:
            self.identity = identity
        if last_name is not None:
            self.last_name = last_name
        if living_address is not None:
            self.living_address = living_address
        if phone is not None:
            self.phone = phone
        if tax_reason_code is not None:
            self.tax_reason_code = tax_reason_code

    @property
    def birth_date(self):
        """Gets the birth_date of this PayoutRequestCustomer.  # noqa: E501

        Customer birth date  # noqa: E501

        :return: The birth_date of this PayoutRequestCustomer.  # noqa: E501
        :rtype: datetime
        """
        return self._birth_date

    @birth_date.setter
    def birth_date(self, birth_date):
        """Sets the birth_date of this PayoutRequestCustomer.

        Customer birth date  # noqa: E501

        :param birth_date: The birth_date of this PayoutRequestCustomer.  # noqa: E501
        :type: datetime
        """

        self._birth_date = birth_date

    @property
    def device(self):
        """Gets the device of this PayoutRequestCustomer.  # noqa: E501

        Customer's device information  # noqa: E501

        :return: The device of this PayoutRequestCustomer.  # noqa: E501
        :rtype: Device
        """
        return self._device

    @device.setter
    def device(self, device):
        """Sets the device of this PayoutRequestCustomer.

        Customer's device information  # noqa: E501

        :param device: The device of this PayoutRequestCustomer.  # noqa: E501
        :type: Device
        """

        self._device = device

    @property
    def document_type(self):
        """Gets the document_type of this PayoutRequestCustomer.  # noqa: E501

        Customer document type *(mandatory for 'Latin America' methods only)* For 'Latin America' is required for methods where country = CO, PE  # noqa: E501

        :return: The document_type of this PayoutRequestCustomer.  # noqa: E501
        :rtype: str
        """
        return self._document_type

    @document_type.setter
    def document_type(self, document_type):
        """Sets the document_type of this PayoutRequestCustomer.

        Customer document type *(mandatory for 'Latin America' methods only)* For 'Latin America' is required for methods where country = CO, PE  # noqa: E501

        :param document_type: The document_type of this PayoutRequestCustomer.  # noqa: E501
        :type: str
        """
        if document_type is not None and len(document_type) > 10:
            raise ValueError(
                "Invalid value for `document_type`, length must be less than or equal to `10`"
            )  # noqa: E501
        if document_type is not None and len(document_type) < 0:
            raise ValueError(
                "Invalid value for `document_type`, length must be greater than or equal to `0`"
            )  # noqa: E501

        self._document_type = document_type

    @property
    def email(self):
        """Gets the email of this PayoutRequestCustomer.  # noqa: E501

        Customer e-mail address *(mandatory for 'Latin America' methods only)* For 'Latin America' is required for methods where country = CO  # noqa: E501

        :return: The email of this PayoutRequestCustomer.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this PayoutRequestCustomer.

        Customer e-mail address *(mandatory for 'Latin America' methods only)* For 'Latin America' is required for methods where country = CO  # noqa: E501

        :param email: The email of this PayoutRequestCustomer.  # noqa: E501
        :type: str
        """
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
    def first_name(self):
        """Gets the first_name of this PayoutRequestCustomer.  # noqa: E501

        Customer first name *(mandatory for 'Latin America' methods only)*  # noqa: E501

        :return: The first_name of this PayoutRequestCustomer.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this PayoutRequestCustomer.

        Customer first name *(mandatory for 'Latin America' methods only)*  # noqa: E501

        :param first_name: The first_name of this PayoutRequestCustomer.  # noqa: E501
        :type: str
        """
        if first_name is not None and len(first_name) > 100:
            raise ValueError(
                "Invalid value for `first_name`, length must be less than or equal to `100`"
            )  # noqa: E501
        if first_name is not None and len(first_name) < 0:
            raise ValueError(
                "Invalid value for `first_name`, length must be greater than or equal to `0`"
            )  # noqa: E501

        self._first_name = first_name

    @property
    def full_name(self):
        """Gets the full_name of this PayoutRequestCustomer.  # noqa: E501

        Customer full name. Mandatory for DIRECTBANKINGNGA methods only: For DIRECTBANKINGNGA: only for non NGN currency  # noqa: E501

        :return: The full_name of this PayoutRequestCustomer.  # noqa: E501
        :rtype: str
        """
        return self._full_name

    @full_name.setter
    def full_name(self, full_name):
        """Sets the full_name of this PayoutRequestCustomer.

        Customer full name. Mandatory for DIRECTBANKINGNGA methods only: For DIRECTBANKINGNGA: only for non NGN currency  # noqa: E501

        :param full_name: The full_name of this PayoutRequestCustomer.  # noqa: E501
        :type: str
        """
        if full_name is not None and len(full_name) > 100:
            raise ValueError(
                "Invalid value for `full_name`, length must be less than or equal to `100`"
            )  # noqa: E501
        if full_name is not None and len(full_name) < 0:
            raise ValueError(
                "Invalid value for `full_name`, length must be greater than or equal to `0`"
            )  # noqa: E501

        self._full_name = full_name

    @property
    def id(self):
        """Gets the id of this PayoutRequestCustomer.  # noqa: E501

        Customer id *(mandatory for WEBMONEY method only)*  # noqa: E501

        :return: The id of this PayoutRequestCustomer.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PayoutRequestCustomer.

        Customer id *(mandatory for WEBMONEY method only)*  # noqa: E501

        :param id: The id of this PayoutRequestCustomer.  # noqa: E501
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
    def identity(self):
        """Gets the identity of this PayoutRequestCustomer.  # noqa: E501

        Customer identity  - Customer’s personal identification number: 'CPF' or 'CNPJ' for Brazil, 'DNI' for Argentina and ID for other countries.  For SPEI - Customer CPF or CURP  # noqa: E501

        :return: The identity of this PayoutRequestCustomer.  # noqa: E501
        :rtype: str
        """
        return self._identity

    @identity.setter
    def identity(self, identity):
        """Sets the identity of this PayoutRequestCustomer.

        Customer identity  - Customer’s personal identification number: 'CPF' or 'CNPJ' for Brazil, 'DNI' for Argentina and ID for other countries.  For SPEI - Customer CPF or CURP  # noqa: E501

        :param identity: The identity of this PayoutRequestCustomer.  # noqa: E501
        :type: str
        """

        self._identity = identity

    @property
    def last_name(self):
        """Gets the last_name of this PayoutRequestCustomer.  # noqa: E501

        Customer last name *(mandatory for 'Latin America' methods only)* For 'Latin America' is required for methods where country = AR, BR, CO, MX, PE, UY  # noqa: E501

        :return: The last_name of this PayoutRequestCustomer.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this PayoutRequestCustomer.

        Customer last name *(mandatory for 'Latin America' methods only)* For 'Latin America' is required for methods where country = AR, BR, CO, MX, PE, UY  # noqa: E501

        :param last_name: The last_name of this PayoutRequestCustomer.  # noqa: E501
        :type: str
        """
        if last_name is not None and len(last_name) > 100:
            raise ValueError(
                "Invalid value for `last_name`, length must be less than or equal to `100`"
            )  # noqa: E501
        if last_name is not None and len(last_name) < 0:
            raise ValueError(
                "Invalid value for `last_name`, length must be greater than or equal to `0`"
            )  # noqa: E501

        self._last_name = last_name

    @property
    def living_address(self):
        """Gets the living_address of this PayoutRequestCustomer.  # noqa: E501

        Customer address *(mandatory for 'Latin America' methods only)* For 'Latin America' is required for methods where country = CO  # noqa: E501

        :return: The living_address of this PayoutRequestCustomer.  # noqa: E501
        :rtype: PayoutRequestLivingAddress
        """
        return self._living_address

    @living_address.setter
    def living_address(self, living_address):
        """Sets the living_address of this PayoutRequestCustomer.

        Customer address *(mandatory for 'Latin America' methods only)* For 'Latin America' is required for methods where country = CO  # noqa: E501

        :param living_address: The living_address of this PayoutRequestCustomer.  # noqa: E501
        :type: PayoutRequestLivingAddress
        """

        self._living_address = living_address

    @property
    def phone(self):
        """Gets the phone of this PayoutRequestCustomer.  # noqa: E501

        Customer's phone number  # noqa: E501

        :return: The phone of this PayoutRequestCustomer.  # noqa: E501
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this PayoutRequestCustomer.

        Customer's phone number  # noqa: E501

        :param phone: The phone of this PayoutRequestCustomer.  # noqa: E501
        :type: str
        """
        if phone is not None and len(phone) > 18:
            raise ValueError(
                "Invalid value for `phone`, length must be less than or equal to `18`"
            )  # noqa: E501
        if phone is not None and len(phone) < 5:
            raise ValueError(
                "Invalid value for `phone`, length must be greater than or equal to `5`"
            )  # noqa: E501

        self._phone = phone

    @property
    def tax_reason_code(self):
        """Gets the tax_reason_code of this PayoutRequestCustomer.  # noqa: E501

        Customer's tax reason codeFor 'BANK131 back account mode' is required for methods where country = RU  # noqa: E501

        :return: The tax_reason_code of this PayoutRequestCustomer.  # noqa: E501
        :rtype: str
        """
        return self._tax_reason_code

    @tax_reason_code.setter
    def tax_reason_code(self, tax_reason_code):
        """Sets the tax_reason_code of this PayoutRequestCustomer.

        Customer's tax reason codeFor 'BANK131 back account mode' is required for methods where country = RU  # noqa: E501

        :param tax_reason_code: The tax_reason_code of this PayoutRequestCustomer.  # noqa: E501
        :type: str
        """
        if tax_reason_code is not None and not re.search(
            r"^[0-9]{9}$", tax_reason_code
        ):  # noqa: E501
            raise ValueError(
                r"Invalid value for `tax_reason_code`, must be a follow pattern or equal to `/^[0-9]{9}$/`"
            )  # noqa: E501

        self._tax_reason_code = tax_reason_code

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
        if issubclass(PayoutRequestCustomer, dict):
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
        if not isinstance(other, PayoutRequestCustomer):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
