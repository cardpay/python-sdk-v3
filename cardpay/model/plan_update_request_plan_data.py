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


class PlanUpdateRequestPlanData(object):
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
        "name_to": "str",
        "quantity": "list[PlanQuantity]",
        "status_to": "str",
    }

    attribute_map = {
        "name_to": "name_to",
        "quantity": "quantity",
        "status_to": "status_to",
    }

    def __init__(self, name_to=None, quantity=None, status_to=None):  # noqa: E501
        """PlanUpdateRequestPlanData - a model defined in Swagger"""  # noqa: E501

        self._name_to = None
        self._quantity = None
        self._status_to = None
        self.discriminator = None

        if name_to is not None:
            self.name_to = name_to
        if quantity is not None:
            self.quantity = quantity
        if status_to is not None:
            self.status_to = status_to

    @property
    def name_to(self):
        """Gets the name_to of this PlanUpdateRequestPlanData.  # noqa: E501

        New plan name - for RENAME operation only  # noqa: E501

        :return: The name_to of this PlanUpdateRequestPlanData.  # noqa: E501
        :rtype: str
        """
        return self._name_to

    @name_to.setter
    def name_to(self, name_to):
        """Sets the name_to of this PlanUpdateRequestPlanData.

        New plan name - for RENAME operation only  # noqa: E501

        :param name_to: The name_to of this PlanUpdateRequestPlanData.  # noqa: E501
        :type: str
        """
        if name_to is not None and len(name_to) > 25:
            raise ValueError(
                "Invalid value for `name_to`, length must be less than or equal to `25`"
            )  # noqa: E501
        if name_to is not None and len(name_to) < 0:
            raise ValueError(
                "Invalid value for `name_to`, length must be greater than or equal to `0`"
            )  # noqa: E501

        self._name_to = name_to

    @property
    def quantity(self):
        """Gets the quantity of this PlanUpdateRequestPlanData.  # noqa: E501

        Array with units params  # noqa: E501

        :return: The quantity of this PlanUpdateRequestPlanData.  # noqa: E501
        :rtype: list[PlanQuantity]
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this PlanUpdateRequestPlanData.

        Array with units params  # noqa: E501

        :param quantity: The quantity of this PlanUpdateRequestPlanData.  # noqa: E501
        :type: list[PlanQuantity]
        """

        self._quantity = quantity

    class StatusTo(object):
        ACTIVE = "ACTIVE"
        INACTIVE = "INACTIVE"

    @property
    def status_to(self):
        """Gets the status_to of this PlanUpdateRequestPlanData.  # noqa: E501

        New state of plan (ACTIVE or INACTIVE) - for CHANGE_STATUS operation only  # noqa: E501

        :return: The status_to of this PlanUpdateRequestPlanData.  # noqa: E501
        :rtype: str
        """
        return self._status_to

    @status_to.setter
    def status_to(self, status_to):
        """Sets the status_to of this PlanUpdateRequestPlanData.

        New state of plan (ACTIVE or INACTIVE) - for CHANGE_STATUS operation only  # noqa: E501

        :param status_to: The status_to of this PlanUpdateRequestPlanData.  # noqa: E501
        :type: str
        """
        allowed_values = ["ACTIVE", "INACTIVE"]  # noqa: E501
        if status_to not in allowed_values:
            raise ValueError(
                "Invalid value for `status_to` ({0}), must be one of {1}".format(  # noqa: E501
                    status_to, allowed_values
                )
            )

        self._status_to = status_to

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
        if issubclass(PlanUpdateRequestPlanData, dict):
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
        if not isinstance(other, PlanUpdateRequestPlanData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
