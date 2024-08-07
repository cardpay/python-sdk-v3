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

from cardpay.model.plan import Plan  # noqa: F401,E501


class RecurringData(object):
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
        "contract_number": "str",
        "initial_amount": "float",
        "plan": "Plan",
        "subscription_start": "str",
        "type": "str",
    }

    attribute_map = {
        "contract_number": "contract_number",
        "initial_amount": "initial_amount",
        "plan": "plan",
        "subscription_start": "subscription_start",
        "type": "type",
    }

    def __init__(
        self,
        contract_number=None,
        initial_amount=None,
        plan=None,
        subscription_start=None,
        type=None,
    ):  # noqa: E501
        """RecurringData - a model defined in Swagger"""  # noqa: E501

        self._contract_number = None
        self._initial_amount = None
        self._plan = None
        self._subscription_start = None
        self._type = None
        self.discriminator = None

        if contract_number is not None:
            self.contract_number = contract_number
        if initial_amount is not None:
            self.initial_amount = initial_amount
        if plan is not None:
            self.plan = plan
        if subscription_start is not None:
            self.subscription_start = subscription_start
        if type is not None:
            self.type = type

    @property
    def contract_number(self):
        """Gets the contract_number of this RecurringData.  # noqa: E501

        Contract number between customer and merchant. Required for Mexican merchants  # noqa: E501

        :return: The contract_number of this RecurringData.  # noqa: E501
        :rtype: str
        """
        return self._contract_number

    @contract_number.setter
    def contract_number(self, contract_number):
        """Sets the contract_number of this RecurringData.

        Contract number between customer and merchant. Required for Mexican merchants  # noqa: E501

        :param contract_number: The contract_number of this RecurringData.  # noqa: E501
        :type: str
        """
        if contract_number is not None and len(contract_number) > 20:
            raise ValueError(
                "Invalid value for `contract_number`, length must be less than or equal to `20`"
            )  # noqa: E501
        if contract_number is not None and len(contract_number) < 0:
            raise ValueError(
                "Invalid value for `contract_number`, length must be greater than or equal to `0`"
            )  # noqa: E501

        self._contract_number = contract_number

    @property
    def initial_amount(self):
        """Gets the initial_amount of this RecurringData.  # noqa: E501

        The amount of subscription initiated transaction in selected currency with dot as a decimal separator, must be less than 100 millions  # noqa: E501

        :return: The initial_amount of this RecurringData.  # noqa: E501
        :rtype: float
        """
        return self._initial_amount

    @initial_amount.setter
    def initial_amount(self, initial_amount):
        """Sets the initial_amount of this RecurringData.

        The amount of subscription initiated transaction in selected currency with dot as a decimal separator, must be less than 100 millions  # noqa: E501

        :param initial_amount: The initial_amount of this RecurringData.  # noqa: E501
        :type: float
        """

        self._initial_amount = initial_amount

    @property
    def plan(self):
        """Gets the plan of this RecurringData.  # noqa: E501

        Plan data  # noqa: E501

        :return: The plan of this RecurringData.  # noqa: E501
        :rtype: Plan
        """
        return self._plan

    @plan.setter
    def plan(self, plan):
        """Sets the plan of this RecurringData.

        Plan data  # noqa: E501

        :param plan: The plan of this RecurringData.  # noqa: E501
        :type: Plan
        """

        self._plan = plan

    @property
    def subscription_start(self):
        """Gets the subscription_start of this RecurringData.  # noqa: E501

        The time in 'yyyy-MM-dd' format when subscription will actually become activated (grace period).Leave it empty to activate subscription at once without any grace period applied.  # noqa: E501

        :return: The subscription_start of this RecurringData.  # noqa: E501
        :rtype: str
        """
        return self._subscription_start

    @subscription_start.setter
    def subscription_start(self, subscription_start):
        """Sets the subscription_start of this RecurringData.

        The time in 'yyyy-MM-dd' format when subscription will actually become activated (grace period).Leave it empty to activate subscription at once without any grace period applied.  # noqa: E501

        :param subscription_start: The subscription_start of this RecurringData.  # noqa: E501
        :type: str
        """

        self._subscription_start = subscription_start

    @property
    def type(self):
        """Gets the type of this RecurringData.  # noqa: E501

        Scheduled payment type attribute. Supported values are: `SM` - value for scheduled by merchant case `SA` - value for scheduled by acquirer case The default value is SA  # noqa: E501

        :return: The type of this RecurringData.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this RecurringData.

        Scheduled payment type attribute. Supported values are: `SM` - value for scheduled by merchant case `SA` - value for scheduled by acquirer case The default value is SA  # noqa: E501

        :param type: The type of this RecurringData.  # noqa: E501
        :type: str
        """

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
        if issubclass(RecurringData, dict):
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
        if not isinstance(other, RecurringData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
