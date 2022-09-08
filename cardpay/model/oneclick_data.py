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

from cardpay.model.recurring_request_filing import (
    RecurringRequestFiling,
)  # noqa: F401,E501


class OneclickData(object):
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
        "dynamic_descriptor": "str",
        "filing": "RecurringRequestFiling",
        "generate_token": "bool",
        "initiator": "str",
        "note": "str",
        "preauth": "bool",
        "sca_exemption": "str",
        "three_ds_challenge_indicator": "str",
        "trans_type": "str",
    }

    attribute_map = {
        "amount": "amount",
        "currency": "currency",
        "dynamic_descriptor": "dynamic_descriptor",
        "filing": "filing",
        "generate_token": "generate_token",
        "initiator": "initiator",
        "note": "note",
        "preauth": "preauth",
        "sca_exemption": "sca_exemption",
        "three_ds_challenge_indicator": "three_ds_challenge_indicator",
        "trans_type": "trans_type",
    }

    def __init__(
        self,
        amount=None,
        currency=None,
        dynamic_descriptor=None,
        filing=None,
        generate_token=None,
        initiator=None,
        note=None,
        preauth=None,
        sca_exemption=None,
        three_ds_challenge_indicator=None,
        trans_type=None,
    ):  # noqa: E501
        """OneclickData - a model defined in Swagger"""  # noqa: E501

        self._amount = None
        self._currency = None
        self._dynamic_descriptor = None
        self._filing = None
        self._generate_token = None
        self._initiator = None
        self._note = None
        self._preauth = None
        self._sca_exemption = None
        self._three_ds_challenge_indicator = None
        self._trans_type = None
        self.discriminator = None

        if amount is not None:
            self.amount = amount
        self.currency = currency
        if dynamic_descriptor is not None:
            self.dynamic_descriptor = dynamic_descriptor
        if filing is not None:
            self.filing = filing
        if generate_token is not None:
            self.generate_token = generate_token
        self.initiator = initiator
        if note is not None:
            self.note = note
        if preauth is not None:
            self.preauth = preauth
        if sca_exemption is not None:
            self.sca_exemption = sca_exemption
        if three_ds_challenge_indicator is not None:
            self.three_ds_challenge_indicator = three_ds_challenge_indicator
        if trans_type is not None:
            self.trans_type = trans_type

    @property
    def amount(self):
        """Gets the amount of this OneclickData.  # noqa: E501

        The total transaction amount in selected currency with dot as a decimal separator, must be less than 10 billion  # noqa: E501

        :return: The amount of this OneclickData.  # noqa: E501
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this OneclickData.

        The total transaction amount in selected currency with dot as a decimal separator, must be less than 10 billion  # noqa: E501

        :param amount: The amount of this OneclickData.  # noqa: E501
        :type: float
        """

        self._amount = amount

    @property
    def currency(self):
        """Gets the currency of this OneclickData.  # noqa: E501

        [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) currency code  # noqa: E501

        :return: The currency of this OneclickData.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this OneclickData.

        [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) currency code  # noqa: E501

        :param currency: The currency of this OneclickData.  # noqa: E501
        :type: str
        """
        if currency is None:
            raise ValueError(
                "Invalid value for `currency`, must not be `None`"
            )  # noqa: E501

        self._currency = currency

    @property
    def dynamic_descriptor(self):
        """Gets the dynamic_descriptor of this OneclickData.  # noqa: E501

        Short description of the service or product, must be enabled by CardPay manager to be used.  # noqa: E501

        :return: The dynamic_descriptor of this OneclickData.  # noqa: E501
        :rtype: str
        """
        return self._dynamic_descriptor

    @dynamic_descriptor.setter
    def dynamic_descriptor(self, dynamic_descriptor):
        """Sets the dynamic_descriptor of this OneclickData.

        Short description of the service or product, must be enabled by CardPay manager to be used.  # noqa: E501

        :param dynamic_descriptor: The dynamic_descriptor of this OneclickData.  # noqa: E501
        :type: str
        """
        if dynamic_descriptor is not None and len(dynamic_descriptor) > 25:
            raise ValueError(
                "Invalid value for `dynamic_descriptor`, length must be less than or equal to `25`"
            )  # noqa: E501
        if dynamic_descriptor is not None and len(dynamic_descriptor) < 0:
            raise ValueError(
                "Invalid value for `dynamic_descriptor`, length must be greater than or equal to `0`"
            )  # noqa: E501

        self._dynamic_descriptor = dynamic_descriptor

    @property
    def filing(self):
        """Gets the filing of this OneclickData.  # noqa: E501

        Filing data, should be send in all recurring requests besides first recurring request First recurring request should be send without filing attribute  # noqa: E501

        :return: The filing of this OneclickData.  # noqa: E501
        :rtype: RecurringRequestFiling
        """
        return self._filing

    @filing.setter
    def filing(self, filing):
        """Sets the filing of this OneclickData.

        Filing data, should be send in all recurring requests besides first recurring request First recurring request should be send without filing attribute  # noqa: E501

        :param filing: The filing of this OneclickData.  # noqa: E501
        :type: RecurringRequestFiling
        """

        self._filing = filing

    @property
    def generate_token(self):
        """Gets the generate_token of this OneclickData.  # noqa: E501

        This attribute can be received only in first recurring request. If set to 'true', Card token will be generated and returned in GET response for all successful transactions (can't be generated for declined transactions). In all requests with filing_id card.token can't be generated.  # noqa: E501

        :return: The generate_token of this OneclickData.  # noqa: E501
        :rtype: bool
        """
        return self._generate_token

    @generate_token.setter
    def generate_token(self, generate_token):
        """Sets the generate_token of this OneclickData.

        This attribute can be received only in first recurring request. If set to 'true', Card token will be generated and returned in GET response for all successful transactions (can't be generated for declined transactions). In all requests with filing_id card.token can't be generated.  # noqa: E501

        :param generate_token: The generate_token of this OneclickData.  # noqa: E501
        :type: bool
        """

        self._generate_token = generate_token

    @property
    def initiator(self):
        """Gets the initiator of this OneclickData.  # noqa: E501

        Can be only 2 values - 'mit' (merchant initiated transaction), 'cit' (cardholder initiated transaction).  # noqa: E501

        :return: The initiator of this OneclickData.  # noqa: E501
        :rtype: str
        """
        return self._initiator

    @initiator.setter
    def initiator(self, initiator):
        """Sets the initiator of this OneclickData.

        Can be only 2 values - 'mit' (merchant initiated transaction), 'cit' (cardholder initiated transaction).  # noqa: E501

        :param initiator: The initiator of this OneclickData.  # noqa: E501
        :type: str
        """
        if initiator is None:
            raise ValueError(
                "Invalid value for `initiator`, must not be `None`"
            )  # noqa: E501
        if initiator is not None and not re.search(r"mit|cit", initiator):  # noqa: E501
            raise ValueError(
                r"Invalid value for `initiator`, must be a follow pattern or equal to `/mit|cit/`"
            )  # noqa: E501

        self._initiator = initiator

    @property
    def note(self):
        """Gets the note of this OneclickData.  # noqa: E501

        Note about the recurring that will not be displayed to customer.  # noqa: E501

        :return: The note of this OneclickData.  # noqa: E501
        :rtype: str
        """
        return self._note

    @note.setter
    def note(self, note):
        """Sets the note of this OneclickData.

        Note about the recurring that will not be displayed to customer.  # noqa: E501

        :param note: The note of this OneclickData.  # noqa: E501
        :type: str
        """
        if note is not None and len(note) > 100:
            raise ValueError(
                "Invalid value for `note`, length must be less than or equal to `100`"
            )  # noqa: E501
        if note is not None and len(note) < 0:
            raise ValueError(
                "Invalid value for `note`, length must be greater than or equal to `0`"
            )  # noqa: E501

        self._note = note

    @property
    def preauth(self):
        """Gets the preauth of this OneclickData.  # noqa: E501

        This parameter allowed to be used only for first recurring payment. If set to 'true', the amount will not be captured but only blocked. One-click payments with 'preauth' attribute will be captured automatically in 7 days from the time of creating the preauth transaction. In continue recurring request (with 'filing_id') this parameter shouldn't be used.  # noqa: E501

        :return: The preauth of this OneclickData.  # noqa: E501
        :rtype: bool
        """
        return self._preauth

    @preauth.setter
    def preauth(self, preauth):
        """Sets the preauth of this OneclickData.

        This parameter allowed to be used only for first recurring payment. If set to 'true', the amount will not be captured but only blocked. One-click payments with 'preauth' attribute will be captured automatically in 7 days from the time of creating the preauth transaction. In continue recurring request (with 'filing_id') this parameter shouldn't be used.  # noqa: E501

        :param preauth: The preauth of this OneclickData.  # noqa: E501
        :type: bool
        """

        self._preauth = preauth

    @property
    def sca_exemption(self):
        """Gets the sca_exemption of this OneclickData.  # noqa: E501

        Indicates the exemption type that you want to request for the transaction. Possible value: LOW_VALUE  # noqa: E501

        :return: The sca_exemption of this OneclickData.  # noqa: E501
        :rtype: str
        """
        return self._sca_exemption

    @sca_exemption.setter
    def sca_exemption(self, sca_exemption):
        """Sets the sca_exemption of this OneclickData.

        Indicates the exemption type that you want to request for the transaction. Possible value: LOW_VALUE  # noqa: E501

        :param sca_exemption: The sca_exemption of this OneclickData.  # noqa: E501
        :type: str
        """
        if sca_exemption is not None and not re.search(
            r"LOW_VALUE", sca_exemption
        ):  # noqa: E501
            raise ValueError(
                r"Invalid value for `sca_exemption`, must be a follow pattern or equal to `/LOW_VALUE/`"
            )  # noqa: E501

        self._sca_exemption = sca_exemption

    @property
    def three_ds_challenge_indicator(self):
        """Gets the three_ds_challenge_indicator of this OneclickData.  # noqa: E501


        :return: The three_ds_challenge_indicator of this OneclickData.  # noqa: E501
        :rtype: str
        """
        return self._three_ds_challenge_indicator

    @three_ds_challenge_indicator.setter
    def three_ds_challenge_indicator(self, three_ds_challenge_indicator):
        """Sets the three_ds_challenge_indicator of this OneclickData.


        :param three_ds_challenge_indicator: The three_ds_challenge_indicator of this OneclickData.  # noqa: E501
        :type: str
        """
        if three_ds_challenge_indicator is not None and not re.search(
            r"01|04", three_ds_challenge_indicator
        ):  # noqa: E501
            raise ValueError(
                r"Invalid value for `three_ds_challenge_indicator`, must be a follow pattern or equal to `/01|04/`"
            )  # noqa: E501

        self._three_ds_challenge_indicator = three_ds_challenge_indicator

    class TransType(object):
        _01 = "01"
        _03 = "03"
        _10 = "10"
        _11 = "11"
        _28 = "28"

    @property
    def trans_type(self):
        """Gets the trans_type of this OneclickData.  # noqa: E501


        :return: The trans_type of this OneclickData.  # noqa: E501
        :rtype: str
        """
        return self._trans_type

    @trans_type.setter
    def trans_type(self, trans_type):
        """Sets the trans_type of this OneclickData.


        :param trans_type: The trans_type of this OneclickData.  # noqa: E501
        :type: str
        """
        allowed_values = ["01", "03", "10", "11", "28"]  # noqa: E501
        if trans_type not in allowed_values:
            raise ValueError(
                "Invalid value for `trans_type` ({0}), must be one of {1}".format(  # noqa: E501
                    trans_type, allowed_values
                )
            )

        self._trans_type = trans_type

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
        if issubclass(OneclickData, dict):
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
        if not isinstance(other, OneclickData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
