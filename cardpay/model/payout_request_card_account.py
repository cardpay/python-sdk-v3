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

from cardpay.model.billing_address import BillingAddress  # noqa: F401,E501
from cardpay.model.payout_request_card import PayoutRequestCard  # noqa: F401,E501


class PayoutRequestCardAccount(object):
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
        'billing_address': 'BillingAddress',
        'card': 'PayoutRequestCard',
        'recipient_info': 'str',
        'token': 'str'
    }

    attribute_map = {
        'billing_address': 'billing_address',
        'card': 'card',
        'recipient_info': 'recipient_info',
        'token': 'token'
    }

    def __init__(self, billing_address=None, card=None, recipient_info=None, token=None):  # noqa: E501
        """PayoutRequestCardAccount - a model defined in Swagger"""  # noqa: E501

        self._billing_address = None
        self._card = None
        self._recipient_info = None
        self._token = None
        self.discriminator = None

        if billing_address is not None:
            self.billing_address = billing_address
        self.card = card
        self.recipient_info = recipient_info
        if token is not None:
            self.token = token

    @property
    def billing_address(self):
        """Gets the billing_address of this PayoutRequestCardAccount.  # noqa: E501

        Address for billing  # noqa: E501

        :return: The billing_address of this PayoutRequestCardAccount.  # noqa: E501
        :rtype: BillingAddress
        """
        return self._billing_address

    @billing_address.setter
    def billing_address(self, billing_address):
        """Sets the billing_address of this PayoutRequestCardAccount.

        Address for billing  # noqa: E501

        :param billing_address: The billing_address of this PayoutRequestCardAccount.  # noqa: E501
        :type: BillingAddress
        """

        self._billing_address = billing_address

    @property
    def card(self):
        """Gets the card of this PayoutRequestCardAccount.  # noqa: E501

        Represents a payout card data. Card section shouldn't be present if element `token` was presented.  # noqa: E501

        :return: The card of this PayoutRequestCardAccount.  # noqa: E501
        :rtype: PayoutRequestCard
        """
        return self._card

    @card.setter
    def card(self, card):
        """Sets the card of this PayoutRequestCardAccount.

        Represents a payout card data. Card section shouldn't be present if element `token` was presented.  # noqa: E501

        :param card: The card of this PayoutRequestCardAccount.  # noqa: E501
        :type: PayoutRequestCard
        """
        if card is None:
            raise ValueError("Invalid value for `card`, must not be `None`")  # noqa: E501

        self._card = card

    @property
    def recipient_info(self):
        """Gets the recipient_info of this PayoutRequestCardAccount.  # noqa: E501

        Property `recipient_info` may be required by Bank. In most cases it's Cardholder's name, contact CardPay manager for requirements. It must be omitted when property `token` is presented  # noqa: E501

        :return: The recipient_info of this PayoutRequestCardAccount.  # noqa: E501
        :rtype: str
        """
        return self._recipient_info

    @recipient_info.setter
    def recipient_info(self, recipient_info):
        """Sets the recipient_info of this PayoutRequestCardAccount.

        Property `recipient_info` may be required by Bank. In most cases it's Cardholder's name, contact CardPay manager for requirements. It must be omitted when property `token` is presented  # noqa: E501

        :param recipient_info: The recipient_info of this PayoutRequestCardAccount.  # noqa: E501
        :type: str
        """
        if recipient_info is None:
            raise ValueError("Invalid value for `recipient_info`, must not be `None`")  # noqa: E501
        if recipient_info is not None and len(recipient_info) > 500:
            raise ValueError("Invalid value for `recipient_info`, length must be less than or equal to `500`")  # noqa: E501
        if recipient_info is not None and len(recipient_info) < 0:
            raise ValueError("Invalid value for `recipient_info`, length must be greater than or equal to `0`")  # noqa: E501

        self._recipient_info = recipient_info

    @property
    def token(self):
        """Gets the token of this PayoutRequestCardAccount.  # noqa: E501

        Card token value, used instead of a card data  # noqa: E501

        :return: The token of this PayoutRequestCardAccount.  # noqa: E501
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this PayoutRequestCardAccount.

        Card token value, used instead of a card data  # noqa: E501

        :param token: The token of this PayoutRequestCardAccount.  # noqa: E501
        :type: str
        """
        if token is not None and len(token) > 36:
            raise ValueError("Invalid value for `token`, length must be less than or equal to `36`")  # noqa: E501
        if token is not None and len(token) < 0:
            raise ValueError("Invalid value for `token`, length must be greater than or equal to `0`")  # noqa: E501

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
        if issubclass(PayoutRequestCardAccount, dict):
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
        if not isinstance(other, PayoutRequestCardAccount):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
