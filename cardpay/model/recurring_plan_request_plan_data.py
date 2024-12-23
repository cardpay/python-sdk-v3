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

from cardpay.model.plan_quantity import PlanQuantity  # noqa: F401,E501
from cardpay.model.plan_retry import PlanRetry  # noqa: F401,E501
from cardpay.model.plan_subscription_decline_logic import (
    PlanSubscriptionDeclineLogic,
)  # noqa: F401,E501


class RecurringPlanRequestPlanData(object):
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
        "amount": "float",
        "currency": "str",
        "interval": "int",
        "name": "str",
        "period": "str",
        "pricing_model": "str",
        "quantity": "list[PlanQuantity]",
        "retries": "int",
        "retry": "PlanRetry",
        "subscription_decline_logic": "PlanSubscriptionDeclineLogic",
    }

    attribute_map = {
        "amount": "amount",
        "currency": "currency",
        "interval": "interval",
        "name": "name",
        "period": "period",
        "pricing_model": "pricing_model",
        "quantity": "quantity",
        "retries": "retries",
        "retry": "retry",
        "subscription_decline_logic": "subscription_decline_logic",
    }

    def __init__(
        self,
        amount=None,
        currency=None,
        interval=None,
        name=None,
        period=None,
        pricing_model=None,
        quantity=None,
        retries=None,
        retry=None,
        subscription_decline_logic=None,
    ):  # noqa: E501
        """RecurringPlanRequestPlanData - a model defined in Swagger"""  # noqa: E501

        self._amount = None
        self._currency = None
        self._interval = None
        self._name = None
        self._period = None
        self._pricing_model = None
        self._quantity = None
        self._retries = None
        self._retry = None
        self._subscription_decline_logic = None
        self.discriminator = None

        self.amount = amount
        self.currency = currency
        self.interval = interval
        self.name = name
        self.period = period
        if pricing_model is not None:
            self.pricing_model = pricing_model
        if quantity is not None:
            self.quantity = quantity
        if retries is not None:
            self.retries = retries
        if retry is not None:
            self.retry = retry
        if subscription_decline_logic is not None:
            self.subscription_decline_logic = subscription_decline_logic

    @property
    def amount(self):
        """Gets the amount of this RecurringPlanRequestPlanData.  # noqa: E501

        The amount charged per period defined in plan in selected currency with dot as a decimal separator, limit is defined by payment method and transaction details.  # noqa: E501

        :return: The amount of this RecurringPlanRequestPlanData.  # noqa: E501
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this RecurringPlanRequestPlanData.

        The amount charged per period defined in plan in selected currency with dot as a decimal separator, limit is defined by payment method and transaction details.  # noqa: E501

        :param amount: The amount of this RecurringPlanRequestPlanData.  # noqa: E501
        :type: float
        """
        if amount is None:
            raise ValueError(
                "Invalid value for `amount`, must not be `None`"
            )  # noqa: E501

        self._amount = amount

    @property
    def currency(self):
        """Gets the currency of this RecurringPlanRequestPlanData.  # noqa: E501

        [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) currency code of plan  # noqa: E501

        :return: The currency of this RecurringPlanRequestPlanData.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this RecurringPlanRequestPlanData.

        [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) currency code of plan  # noqa: E501

        :param currency: The currency of this RecurringPlanRequestPlanData.  # noqa: E501
        :type: str
        """
        if currency is None:
            raise ValueError(
                "Invalid value for `currency`, must not be `None`"
            )  # noqa: E501

        self._currency = currency

    @property
    def interval(self):
        """Gets the interval of this RecurringPlanRequestPlanData.  # noqa: E501

        The frequency interval of period, can be 1-365 depending on selected period value. Maximum value of period + interval can be 365 days / 52 weeks / 12 months / 1 year. From 1 to 60 minutes - for **sandbox** environment and testing purpose only  # noqa: E501

        :return: The interval of this RecurringPlanRequestPlanData.  # noqa: E501
        :rtype: int
        """
        return self._interval

    @interval.setter
    def interval(self, interval):
        """Sets the interval of this RecurringPlanRequestPlanData.

        The frequency interval of period, can be 1-365 depending on selected period value. Maximum value of period + interval can be 365 days / 52 weeks / 12 months / 1 year. From 1 to 60 minutes - for **sandbox** environment and testing purpose only  # noqa: E501

        :param interval: The interval of this RecurringPlanRequestPlanData.  # noqa: E501
        :type: int
        """
        if interval is None:
            raise ValueError(
                "Invalid value for `interval`, must not be `None`"
            )  # noqa: E501
        if interval is not None and interval > 365:  # noqa: E501
            raise ValueError(
                "Invalid value for `interval`, must be a value less than or equal to `365`"
            )  # noqa: E501
        if interval is not None and interval < 1:  # noqa: E501
            raise ValueError(
                "Invalid value for `interval`, must be a value greater than or equal to `1`"
            )  # noqa: E501

        self._interval = interval

    @property
    def name(self):
        """Gets the name of this RecurringPlanRequestPlanData.  # noqa: E501

        Plan name  # noqa: E501

        :return: The name of this RecurringPlanRequestPlanData.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this RecurringPlanRequestPlanData.

        Plan name  # noqa: E501

        :param name: The name of this RecurringPlanRequestPlanData.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError(
                "Invalid value for `name`, must not be `None`"
            )  # noqa: E501
        if name is not None and len(name) > 25:
            raise ValueError(
                "Invalid value for `name`, length must be less than or equal to `25`"
            )  # noqa: E501
        if name is not None and len(name) < 0:
            raise ValueError(
                "Invalid value for `name`, length must be greater than or equal to `0`"
            )  # noqa: E501

        self._name = name

    class Period(object):
        MINUTE = "minute"
        DAY = "day"
        WEEK = "week"
        MONTH = "month"
        YEAR = "year"

    @property
    def period(self):
        """Gets the period of this RecurringPlanRequestPlanData.  # noqa: E501

        Initial period of recurring, can be `day`, `week`, `month`, `year`. Additional period: `minute` - for **sandbox** and testing purpose only.  # noqa: E501

        :return: The period of this RecurringPlanRequestPlanData.  # noqa: E501
        :rtype: str
        """
        return self._period

    @period.setter
    def period(self, period):
        """Sets the period of this RecurringPlanRequestPlanData.

        Initial period of recurring, can be `day`, `week`, `month`, `year`. Additional period: `minute` - for **sandbox** and testing purpose only.  # noqa: E501

        :param period: The period of this RecurringPlanRequestPlanData.  # noqa: E501
        :type: str
        """
        if period is None:
            raise ValueError(
                "Invalid value for `period`, must not be `None`"
            )  # noqa: E501
        allowed_values = ["minute", "day", "week", "month", "year"]  # noqa: E501
        if period not in allowed_values:
            raise ValueError(
                "Invalid value for `period` ({0}), must be one of {1}".format(  # noqa: E501
                    period, allowed_values
                )
            )

        self._period = period

    @property
    def pricing_model(self):
        """Gets the pricing_model of this RecurringPlanRequestPlanData.  # noqa: E501

        Parameter regulates the price calculation pricing_model depending on the number of units Possible values: `FIXED` `TIERED` `VOLUME` By default - `FIXED`  # noqa: E501

        :return: The pricing_model of this RecurringPlanRequestPlanData.  # noqa: E501
        :rtype: str
        """
        return self._pricing_model

    @pricing_model.setter
    def pricing_model(self, pricing_model):
        """Sets the pricing_model of this RecurringPlanRequestPlanData.

        Parameter regulates the price calculation pricing_model depending on the number of units Possible values: `FIXED` `TIERED` `VOLUME` By default - `FIXED`  # noqa: E501

        :param pricing_model: The pricing_model of this RecurringPlanRequestPlanData.  # noqa: E501
        :type: str
        """
        if pricing_model is not None and not re.search(
            r"FIXED|TIERED|VOLUME", pricing_model
        ):  # noqa: E501
            raise ValueError(
                r"Invalid value for `pricing_model`, must be a follow pattern or equal to `/FIXED|TIERED|VOLUME/`"
            )  # noqa: E501

        self._pricing_model = pricing_model

    @property
    def quantity(self):
        """Gets the quantity of this RecurringPlanRequestPlanData.  # noqa: E501

        Array with units quantity. Mandatory if `pricing_model` is `TIERED` or `VOLUME`  # noqa: E501

        :return: The quantity of this RecurringPlanRequestPlanData.  # noqa: E501
        :rtype: list[PlanQuantity]
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this RecurringPlanRequestPlanData.

        Array with units quantity. Mandatory if `pricing_model` is `TIERED` or `VOLUME`  # noqa: E501

        :param quantity: The quantity of this RecurringPlanRequestPlanData.  # noqa: E501
        :type: list[PlanQuantity]
        """

        self._quantity = quantity

    @property
    def retries(self):
        """Gets the retries of this RecurringPlanRequestPlanData.  # noqa: E501

        Number of daily basis retry attempts in case of payment has not been captured successfully, from 1 to 15 attempts can be specified.  # noqa: E501

        :return: The retries of this RecurringPlanRequestPlanData.  # noqa: E501
        :rtype: int
        """
        return self._retries

    @retries.setter
    def retries(self, retries):
        """Sets the retries of this RecurringPlanRequestPlanData.

        Number of daily basis retry attempts in case of payment has not been captured successfully, from 1 to 15 attempts can be specified.  # noqa: E501

        :param retries: The retries of this RecurringPlanRequestPlanData.  # noqa: E501
        :type: int
        """
        if retries is not None and retries > 15:  # noqa: E501
            raise ValueError(
                "Invalid value for `retries`, must be a value less than or equal to `15`"
            )  # noqa: E501
        if retries is not None and retries < 1:  # noqa: E501
            raise ValueError(
                "Invalid value for `retries`, must be a value greater than or equal to `1`"
            )  # noqa: E501

        self._retries = retries

    @property
    def retry(self):
        """Gets the retry of this RecurringPlanRequestPlanData.  # noqa: E501

        Structure for establishing the logic of retries for subscription based on created plan  # noqa: E501

        :return: The retry of this RecurringPlanRequestPlanData.  # noqa: E501
        :rtype: PlanRetry
        """
        return self._retry

    @retry.setter
    def retry(self, retry):
        """Sets the retry of this RecurringPlanRequestPlanData.

        Structure for establishing the logic of retries for subscription based on created plan  # noqa: E501

        :param retry: The retry of this RecurringPlanRequestPlanData.  # noqa: E501
        :type: PlanRetry
        """

        self._retry = retry

    @property
    def subscription_decline_logic(self):
        """Gets the subscription_decline_logic of this RecurringPlanRequestPlanData.  # noqa: E501

        Subscription decline logic  # noqa: E501

        :return: The subscription_decline_logic of this RecurringPlanRequestPlanData.  # noqa: E501
        :rtype: PlanSubscriptionDeclineLogic
        """
        return self._subscription_decline_logic

    @subscription_decline_logic.setter
    def subscription_decline_logic(self, subscription_decline_logic):
        """Sets the subscription_decline_logic of this RecurringPlanRequestPlanData.

        Subscription decline logic  # noqa: E501

        :param subscription_decline_logic: The subscription_decline_logic of this RecurringPlanRequestPlanData.  # noqa: E501
        :type: PlanSubscriptionDeclineLogic
        """

        self._subscription_decline_logic = subscription_decline_logic

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
        if issubclass(RecurringPlanRequestPlanData, dict):
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
        if not isinstance(other, RecurringPlanRequestPlanData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
