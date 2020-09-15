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

from cardpay.model.recurring_gateway_response_recurring_data import (
    RecurringGatewayResponseRecurringData,
)  # noqa: F401,E501
from cardpay.model.subscription import Subscription  # noqa: F401,E501


class RecurringGatewayCreationResponse(object):
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
        "recurring_data": "RecurringGatewayResponseRecurringData",
        "subscription": "Subscription",
        "redirect_url": "str",
    }

    attribute_map = {
        "recurring_data": "recurring_data",
        "subscription": "subscription",
        "redirect_url": "redirect_url",
    }

    def __init__(
        self, recurring_data=None, subscription=None, redirect_url=None
    ):  # noqa: E501
        """RecurringGatewayCreationResponse - a model defined in Swagger"""  # noqa: E501

        self._recurring_data = None
        self._subscription = None
        self._redirect_url = None
        self.discriminator = None

        if recurring_data is not None:
            self.recurring_data = recurring_data
        if subscription is not None:
            self.subscription = subscription
        if redirect_url is not None:
            self.redirect_url = redirect_url

    @property
    def recurring_data(self):
        """Gets the recurring_data of this RecurringGatewayCreationResponse.  # noqa: E501

        Recurring data  # noqa: E501

        :return: The recurring_data of this RecurringGatewayCreationResponse.  # noqa: E501
        :rtype: RecurringGatewayResponseRecurringData
        """
        return self._recurring_data

    @recurring_data.setter
    def recurring_data(self, recurring_data):
        """Sets the recurring_data of this RecurringGatewayCreationResponse.

        Recurring data  # noqa: E501

        :param recurring_data: The recurring_data of this RecurringGatewayCreationResponse.  # noqa: E501
        :type: RecurringGatewayResponseRecurringData
        """

        self._recurring_data = recurring_data

    @property
    def subscription(self):
        """Gets the subscription of this RecurringGatewayCreationResponse.  # noqa: E501

        Subscription (applicable to scheduled payments and installment payments)  # noqa: E501

        :return: The subscription of this RecurringGatewayCreationResponse.  # noqa: E501
        :rtype: Subscription
        """
        return self._subscription

    @subscription.setter
    def subscription(self, subscription):
        """Sets the subscription of this RecurringGatewayCreationResponse.

        Subscription (applicable to scheduled payments and installment payments)  # noqa: E501

        :param subscription: The subscription of this RecurringGatewayCreationResponse.  # noqa: E501
        :type: Subscription
        """

        self._subscription = subscription

    @property
    def redirect_url(self):
        """Gets the redirect_url of this RecurringGatewayCreationResponse.  # noqa: E501

        URL Customer should be redirected to  # noqa: E501

        :return: The redirect_url of this RecurringGatewayCreationResponse.  # noqa: E501
        :rtype: str
        """
        return self._redirect_url

    @redirect_url.setter
    def redirect_url(self, redirect_url):
        """Sets the redirect_url of this RecurringGatewayCreationResponse.

        URL Customer should be redirected to  # noqa: E501

        :param redirect_url: The redirect_url of this RecurringGatewayCreationResponse.  # noqa: E501
        :type: str
        """

        self._redirect_url = redirect_url

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
        if issubclass(RecurringGatewayCreationResponse, dict):
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
        if not isinstance(other, RecurringGatewayCreationResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other