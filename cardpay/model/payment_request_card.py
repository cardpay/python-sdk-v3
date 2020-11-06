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


class PaymentRequestCard(object):
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
        "acct_type": "str",
        "expiration": "str",
        "holder": "str",
        "pan": "str",
        "security_code": "str",
    }

    attribute_map = {
        "acct_type": "acct_type",
        "expiration": "expiration",
        "holder": "holder",
        "pan": "pan",
        "security_code": "security_code",
    }

    def __init__(
        self, acct_type=None, expiration=None, holder=None, pan=None, security_code=None
    ):  # noqa: E501
        """PaymentRequestCard - a model defined in Swagger"""  # noqa: E501

        self._acct_type = None
        self._expiration = None
        self._holder = None
        self._pan = None
        self._security_code = None
        self.discriminator = None

        if acct_type is not None:
            self.acct_type = acct_type
        self.expiration = expiration
        if holder is not None:
            self.holder = holder
        self.pan = pan
        self.security_code = security_code

    class AcctType(object):
        _01 = "01"
        _02 = "02"
        _03 = "03"

    @property
    def acct_type(self):
        """Gets the acct_type of this PaymentRequestCard.  # noqa: E501


        :return: The acct_type of this PaymentRequestCard.  # noqa: E501
        :rtype: str
        """
        return self._acct_type

    @acct_type.setter
    def acct_type(self, acct_type):
        """Sets the acct_type of this PaymentRequestCard.


        :param acct_type: The acct_type of this PaymentRequestCard.  # noqa: E501
        :type: str
        """
        allowed_values = ["01", "02", "03"]  # noqa: E501
        if acct_type not in allowed_values:
            raise ValueError(
                "Invalid value for `acct_type` ({0}), must be one of {1}".format(  # noqa: E501
                    acct_type, allowed_values
                )
            )

        self._acct_type = acct_type

    @property
    def expiration(self):
        """Gets the expiration of this PaymentRequestCard.  # noqa: E501

        Customer's card expiration date. Format: `mm/yyyy`  # noqa: E501

        :return: The expiration of this PaymentRequestCard.  # noqa: E501
        :rtype: str
        """
        return self._expiration

    @expiration.setter
    def expiration(self, expiration):
        """Sets the expiration of this PaymentRequestCard.

        Customer's card expiration date. Format: `mm/yyyy`  # noqa: E501

        :param expiration: The expiration of this PaymentRequestCard.  # noqa: E501
        :type: str
        """
        if expiration is None:
            raise ValueError(
                "Invalid value for `expiration`, must not be `None`"
            )  # noqa: E501
        if expiration is not None and not re.search(
            r"([0-9]{2}\/[0-9]{4})", expiration
        ):  # noqa: E501
            raise ValueError(
                r"Invalid value for `expiration`, must be a follow pattern or equal to `/([0-9]{2}\/[0-9]{4})/`"
            )  # noqa: E501

        self._expiration = expiration

    @property
    def holder(self):
        """Gets the holder of this PaymentRequestCard.  # noqa: E501

        Customer's cardholder name. Any valid cardholder name  # noqa: E501

        :return: The holder of this PaymentRequestCard.  # noqa: E501
        :rtype: str
        """
        return self._holder

    @holder.setter
    def holder(self, holder):
        """Sets the holder of this PaymentRequestCard.

        Customer's cardholder name. Any valid cardholder name  # noqa: E501

        :param holder: The holder of this PaymentRequestCard.  # noqa: E501
        :type: str
        """
        if holder is not None and len(holder) > 50:
            raise ValueError(
                "Invalid value for `holder`, length must be less than or equal to `50`"
            )  # noqa: E501
        if holder is not None and len(holder) < 1:
            raise ValueError(
                "Invalid value for `holder`, length must be greater than or equal to `1`"
            )  # noqa: E501

        self._holder = holder

    @property
    def pan(self):
        """Gets the pan of this PaymentRequestCard.  # noqa: E501

        Customer's card number (PAN). Any valid card number, may contain spaces  # noqa: E501

        :return: The pan of this PaymentRequestCard.  # noqa: E501
        :rtype: str
        """
        return self._pan

    @pan.setter
    def pan(self, pan):
        """Sets the pan of this PaymentRequestCard.

        Customer's card number (PAN). Any valid card number, may contain spaces  # noqa: E501

        :param pan: The pan of this PaymentRequestCard.  # noqa: E501
        :type: str
        """
        if pan is None:
            raise ValueError(
                "Invalid value for `pan`, must not be `None`"
            )  # noqa: E501
        if pan is not None and len(pan) > 19:
            raise ValueError(
                "Invalid value for `pan`, length must be less than or equal to `19`"
            )  # noqa: E501
        if pan is not None and len(pan) < 13:
            raise ValueError(
                "Invalid value for `pan`, length must be greater than or equal to `13`"
            )  # noqa: E501

        self._pan = pan

    @property
    def security_code(self):
        """Gets the security_code of this PaymentRequestCard.  # noqa: E501

        Customer's CVV2 / CVC2 / CAV2  # noqa: E501

        :return: The security_code of this PaymentRequestCard.  # noqa: E501
        :rtype: str
        """
        return self._security_code

    @security_code.setter
    def security_code(self, security_code):
        """Sets the security_code of this PaymentRequestCard.

        Customer's CVV2 / CVC2 / CAV2  # noqa: E501

        :param security_code: The security_code of this PaymentRequestCard.  # noqa: E501
        :type: str
        """
        if security_code is None:
            raise ValueError(
                "Invalid value for `security_code`, must not be `None`"
            )  # noqa: E501
        if security_code is not None and not re.search(
            r"[0-9]{3,4}", security_code
        ):  # noqa: E501
            raise ValueError(
                r"Invalid value for `security_code`, must be a follow pattern or equal to `/[0-9]{3,4}/`"
            )  # noqa: E501

        self._security_code = security_code

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
        if issubclass(PaymentRequestCard, dict):
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
        if not isinstance(other, PaymentRequestCard):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
