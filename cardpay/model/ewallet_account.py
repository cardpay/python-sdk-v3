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


class EwalletAccount(object):
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
        "bank_branch": "str",
        "bank_code": "str",
        "id": "str",
        "type": "str",
    }

    attribute_map = {
        "bank_branch": "bank_branch",
        "bank_code": "bank_code",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self, bank_branch=None, bank_code=None, id=None, type=None
    ):  # noqa: E501
        """EwalletAccount - a model defined in Swagger"""  # noqa: E501

        self._bank_branch = None
        self._bank_code = None
        self._id = None
        self._type = None
        self.discriminator = None

        if bank_branch is not None:
            self.bank_branch = bank_branch
        if bank_code is not None:
            self.bank_code = bank_code
        if id is not None:
            self.id = id
        if type is not None:
            self.type = type

    @property
    def bank_branch(self):
        """Gets the bank_branch of this EwalletAccount.  # noqa: E501

        Customer bank branch number (name)  # noqa: E501

        :return: The bank_branch of this EwalletAccount.  # noqa: E501
        :rtype: str
        """
        return self._bank_branch

    @bank_branch.setter
    def bank_branch(self, bank_branch):
        """Sets the bank_branch of this EwalletAccount.

        Customer bank branch number (name)  # noqa: E501

        :param bank_branch: The bank_branch of this EwalletAccount.  # noqa: E501
        :type: str
        """
        if bank_branch is not None and len(bank_branch) > 50:
            raise ValueError(
                "Invalid value for `bank_branch`, length must be less than or equal to `50`"
            )  # noqa: E501
        if bank_branch is not None and len(bank_branch) < 1:
            raise ValueError(
                "Invalid value for `bank_branch`, length must be greater than or equal to `1`"
            )  # noqa: E501

        self._bank_branch = bank_branch

    @property
    def bank_code(self):
        """Gets the bank_code of this EwalletAccount.  # noqa: E501

        Customer bank code  # noqa: E501

        :return: The bank_code of this EwalletAccount.  # noqa: E501
        :rtype: str
        """
        return self._bank_code

    @bank_code.setter
    def bank_code(self, bank_code):
        """Sets the bank_code of this EwalletAccount.

        Customer bank code  # noqa: E501

        :param bank_code: The bank_code of this EwalletAccount.  # noqa: E501
        :type: str
        """
        if bank_code is not None and len(bank_code) > 6:
            raise ValueError(
                "Invalid value for `bank_code`, length must be less than or equal to `6`"
            )  # noqa: E501
        if bank_code is not None and len(bank_code) < 1:
            raise ValueError(
                "Invalid value for `bank_code`, length must be greater than or equal to `1`"
            )  # noqa: E501

        self._bank_code = bank_code

    @property
    def id(self):
        """Gets the id of this EwalletAccount.  # noqa: E501

        Customer personal identification number  # noqa: E501

        :return: The id of this EwalletAccount.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this EwalletAccount.

        Customer personal identification number  # noqa: E501

        :param id: The id of this EwalletAccount.  # noqa: E501
        :type: str
        """
        if id is not None and len(id) > 50:
            raise ValueError(
                "Invalid value for `id`, length must be less than or equal to `50`"
            )  # noqa: E501
        if id is not None and len(id) < 1:
            raise ValueError(
                "Invalid value for `id`, length must be greater than or equal to `1`"
            )  # noqa: E501

        self._id = id

    @property
    def type(self):
        """Gets the type of this EwalletAccount.  # noqa: E501

        Customer account type  # noqa: E501

        :return: The type of this EwalletAccount.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this EwalletAccount.

        Customer account type  # noqa: E501

        :param type: The type of this EwalletAccount.  # noqa: E501
        :type: str
        """
        if type is not None and len(type) > 4:
            raise ValueError(
                "Invalid value for `type`, length must be less than or equal to `4`"
            )  # noqa: E501
        if type is not None and len(type) < 1:
            raise ValueError(
                "Invalid value for `type`, length must be greater than or equal to `1`"
            )  # noqa: E501

        self._type = type

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
        if issubclass(EwalletAccount, dict):
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
        if not isinstance(other, EwalletAccount):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
