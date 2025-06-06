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


class InstallmentData(object):
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
        "generate_token": "bool",
        "hold_period": "int",
        "initiator": "str",
        "installment_amount": "float",
        "installment_type": "str",
        "note": "str",
        "payments": "list[int]",
        "postauth_status": "str",
        "preauth": "bool",
        "three_ds_challenge_indicator": "str",
        "trans_type": "str",
    }

    attribute_map = {
        "amount": "amount",
        "currency": "currency",
        "dynamic_descriptor": "dynamic_descriptor",
        "generate_token": "generate_token",
        "hold_period": "hold_period",
        "initiator": "initiator",
        "installment_amount": "installment_amount",
        "installment_type": "installment_type",
        "note": "note",
        "payments": "payments",
        "postauth_status": "postauth_status",
        "preauth": "preauth",
        "three_ds_challenge_indicator": "three_ds_challenge_indicator",
        "trans_type": "trans_type",
    }

    def __init__(
        self,
        amount=None,
        currency=None,
        dynamic_descriptor=None,
        generate_token=None,
        hold_period=None,
        initiator=None,
        installment_amount=None,
        installment_type=None,
        note=None,
        payments=None,
        postauth_status=None,
        preauth=None,
        three_ds_challenge_indicator=None,
        trans_type=None,
    ):  # noqa: E501
        """InstallmentData - a model defined in Swagger"""  # noqa: E501

        self._amount = None
        self._currency = None
        self._dynamic_descriptor = None
        self._generate_token = None
        self._hold_period = None
        self._initiator = None
        self._installment_amount = None
        self._installment_type = None
        self._note = None
        self._payments = None
        self._postauth_status = None
        self._preauth = None
        self._three_ds_challenge_indicator = None
        self._trans_type = None
        self.discriminator = None

        if amount is not None:
            self.amount = amount
        self.currency = currency
        if dynamic_descriptor is not None:
            self.dynamic_descriptor = dynamic_descriptor
        if generate_token is not None:
            self.generate_token = generate_token
        if hold_period is not None:
            self.hold_period = hold_period
        self.initiator = initiator
        if installment_amount is not None:
            self.installment_amount = installment_amount
        if installment_type is not None:
            self.installment_type = installment_type
        if note is not None:
            self.note = note
        if payments is not None:
            self.payments = payments
        if postauth_status is not None:
            self.postauth_status = postauth_status
        if preauth is not None:
            self.preauth = preauth
        if three_ds_challenge_indicator is not None:
            self.three_ds_challenge_indicator = three_ds_challenge_indicator
        if trans_type is not None:
            self.trans_type = trans_type

    @property
    def amount(self):
        """Gets the amount of this InstallmentData.  # noqa: E501

        The total transaction amount in selected currency with dot as a decimal separator, must be less than 10 billion  # noqa: E501

        :return: The amount of this InstallmentData.  # noqa: E501
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this InstallmentData.

        The total transaction amount in selected currency with dot as a decimal separator, must be less than 10 billion  # noqa: E501

        :param amount: The amount of this InstallmentData.  # noqa: E501
        :type: float
        """

        self._amount = amount

    @property
    def currency(self):
        """Gets the currency of this InstallmentData.  # noqa: E501

        [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) currency code  # noqa: E501

        :return: The currency of this InstallmentData.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this InstallmentData.

        [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) currency code  # noqa: E501

        :param currency: The currency of this InstallmentData.  # noqa: E501
        :type: str
        """
        if currency is None:
            raise ValueError(
                "Invalid value for `currency`, must not be `None`"
            )  # noqa: E501

        self._currency = currency

    @property
    def dynamic_descriptor(self):
        """Gets the dynamic_descriptor of this InstallmentData.  # noqa: E501

        Short description of the service or product, must be enabled by CardPay manager to be used.  # noqa: E501

        :return: The dynamic_descriptor of this InstallmentData.  # noqa: E501
        :rtype: str
        """
        return self._dynamic_descriptor

    @dynamic_descriptor.setter
    def dynamic_descriptor(self, dynamic_descriptor):
        """Sets the dynamic_descriptor of this InstallmentData.

        Short description of the service or product, must be enabled by CardPay manager to be used.  # noqa: E501

        :param dynamic_descriptor: The dynamic_descriptor of this InstallmentData.  # noqa: E501
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
    def generate_token(self):
        """Gets the generate_token of this InstallmentData.  # noqa: E501

        This attribute can be received only in first recurring request. In all requests with recurring_id card.token can't be generated. If set to 'true', Card token will be generated and returned in GET response. Will be generated only for successful transactions (not for declined).  # noqa: E501

        :return: The generate_token of this InstallmentData.  # noqa: E501
        :rtype: bool
        """
        return self._generate_token

    @generate_token.setter
    def generate_token(self, generate_token):
        """Sets the generate_token of this InstallmentData.

        This attribute can be received only in first recurring request. In all requests with recurring_id card.token can't be generated. If set to 'true', Card token will be generated and returned in GET response. Will be generated only for successful transactions (not for declined).  # noqa: E501

        :param generate_token: The generate_token of this InstallmentData.  # noqa: E501
        :type: bool
        """

        self._generate_token = generate_token

    @property
    def hold_period(self):
        """Gets the hold_period of this InstallmentData.  # noqa: E501

        The delay between the authorisation and scheduled auto-capture or auto-void, specified in hours. The minimum hold period is 1 hour, maximum hold period is: VISA cards: 96 hours MasterCard cards: 144 hours Other cards: 168 hours In Payment Page mode, the maximum delay is 96 hours.  # noqa: E501

        :return: The hold_period of this InstallmentData.  # noqa: E501
        :rtype: int
        """
        return self._hold_period

    @hold_period.setter
    def hold_period(self, hold_period):
        """Sets the hold_period of this InstallmentData.

        The delay between the authorisation and scheduled auto-capture or auto-void, specified in hours. The minimum hold period is 1 hour, maximum hold period is: VISA cards: 96 hours MasterCard cards: 144 hours Other cards: 168 hours In Payment Page mode, the maximum delay is 96 hours.  # noqa: E501

        :param hold_period: The hold_period of this InstallmentData.  # noqa: E501
        :type: int
        """
        if hold_period is not None and hold_period < 1:  # noqa: E501
            raise ValueError(
                "Invalid value for `hold_period`, must be a value greater than or equal to `1`"
            )  # noqa: E501

        self._hold_period = hold_period

    @property
    def initiator(self):
        """Gets the initiator of this InstallmentData.  # noqa: E501

        Use `cit` for initiator attribute (cardholder initiated transaction).  # noqa: E501

        :return: The initiator of this InstallmentData.  # noqa: E501
        :rtype: str
        """
        return self._initiator

    @initiator.setter
    def initiator(self, initiator):
        """Sets the initiator of this InstallmentData.

        Use `cit` for initiator attribute (cardholder initiated transaction).  # noqa: E501

        :param initiator: The initiator of this InstallmentData.  # noqa: E501
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
    def installment_amount(self):
        """Gets the installment_amount of this InstallmentData.  # noqa: E501

        Amount of 1 installment payment, should be less or equal to total amount of subscription, can have dot as a decimal separator. Mandatory for Payment Page Mode only.  # noqa: E501

        :return: The installment_amount of this InstallmentData.  # noqa: E501
        :rtype: float
        """
        return self._installment_amount

    @installment_amount.setter
    def installment_amount(self, installment_amount):
        """Sets the installment_amount of this InstallmentData.

        Amount of 1 installment payment, should be less or equal to total amount of subscription, can have dot as a decimal separator. Mandatory for Payment Page Mode only.  # noqa: E501

        :param installment_amount: The installment_amount of this InstallmentData.  # noqa: E501
        :type: float
        """

        self._installment_amount = installment_amount

    @property
    def installment_type(self):
        """Gets the installment_type of this InstallmentData.  # noqa: E501

        Installment type, 2 possible values: `IF` - issuer financed `MF_HOLD' - merchant financed hold  # noqa: E501

        :return: The installment_type of this InstallmentData.  # noqa: E501
        :rtype: str
        """
        return self._installment_type

    @installment_type.setter
    def installment_type(self, installment_type):
        """Sets the installment_type of this InstallmentData.

        Installment type, 2 possible values: `IF` - issuer financed `MF_HOLD' - merchant financed hold  # noqa: E501

        :param installment_type: The installment_type of this InstallmentData.  # noqa: E501
        :type: str
        """
        if installment_type is not None and not re.search(
            r"IF|MF_HOLD", installment_type
        ):  # noqa: E501
            raise ValueError(
                r"Invalid value for `installment_type`, must be a follow pattern or equal to `/IF|MF_HOLD/`"
            )  # noqa: E501

        self._installment_type = installment_type

    @property
    def note(self):
        """Gets the note of this InstallmentData.  # noqa: E501

        Note about the recurring that will not be displayed to customer.  # noqa: E501

        :return: The note of this InstallmentData.  # noqa: E501
        :rtype: str
        """
        return self._note

    @note.setter
    def note(self, note):
        """Sets the note of this InstallmentData.

        Note about the recurring that will not be displayed to customer.  # noqa: E501

        :param note: The note of this InstallmentData.  # noqa: E501
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
    def payments(self):
        """Gets the payments of this InstallmentData.  # noqa: E501

        Number of total payments, to be charged per defined interval. For installment subscription with installment_type = `MF_HOLD` can be 2-12. For Mexican installment subscription (installment_type = `IF`) should be 1-99.  # noqa: E501

        :return: The payments of this InstallmentData.  # noqa: E501
        :rtype: list[int]
        """
        return self._payments

    @payments.setter
    def payments(self, payments):
        """Sets the payments of this InstallmentData.

        Number of total payments, to be charged per defined interval. For installment subscription with installment_type = `MF_HOLD` can be 2-12. For Mexican installment subscription (installment_type = `IF`) should be 1-99.  # noqa: E501

        :param payments: The payments of this InstallmentData.  # noqa: E501
        :type: list[int]
        """

        self._payments = payments

    class PostauthStatus(object):
        REVERSE = "REVERSE"
        COMPLETE = "COMPLETE"

    @property
    def postauth_status(self):
        """Gets the postauth_status of this InstallmentData.  # noqa: E501

        The value contains payment status after hold period if payment has not been completed. Possible values: COMPLETE, REVERSE  # noqa: E501

        :return: The postauth_status of this InstallmentData.  # noqa: E501
        :rtype: str
        """
        return self._postauth_status

    @postauth_status.setter
    def postauth_status(self, postauth_status):
        """Sets the postauth_status of this InstallmentData.

        The value contains payment status after hold period if payment has not been completed. Possible values: COMPLETE, REVERSE  # noqa: E501

        :param postauth_status: The postauth_status of this InstallmentData.  # noqa: E501
        :type: str
        """
        allowed_values = ["REVERSE", "COMPLETE"]  # noqa: E501
        if postauth_status not in allowed_values:
            raise ValueError(
                "Invalid value for `postauth_status` ({0}), must be one of {1}".format(  # noqa: E501
                    postauth_status, allowed_values
                )
            )

        self._postauth_status = postauth_status

    @property
    def preauth(self):
        """Gets the preauth of this InstallmentData.  # noqa: E501

        If set to `true`, the amount will not be captured but only blocked. Installment with `preauth` attribute will be voided automatically in 7 days from the time of creating the preauth transaction.  # noqa: E501

        :return: The preauth of this InstallmentData.  # noqa: E501
        :rtype: bool
        """
        return self._preauth

    @preauth.setter
    def preauth(self, preauth):
        """Sets the preauth of this InstallmentData.

        If set to `true`, the amount will not be captured but only blocked. Installment with `preauth` attribute will be voided automatically in 7 days from the time of creating the preauth transaction.  # noqa: E501

        :param preauth: The preauth of this InstallmentData.  # noqa: E501
        :type: bool
        """

        self._preauth = preauth

    @property
    def three_ds_challenge_indicator(self):
        """Gets the three_ds_challenge_indicator of this InstallmentData.  # noqa: E501


        :return: The three_ds_challenge_indicator of this InstallmentData.  # noqa: E501
        :rtype: str
        """
        return self._three_ds_challenge_indicator

    @three_ds_challenge_indicator.setter
    def three_ds_challenge_indicator(self, three_ds_challenge_indicator):
        """Sets the three_ds_challenge_indicator of this InstallmentData.


        :param three_ds_challenge_indicator: The three_ds_challenge_indicator of this InstallmentData.  # noqa: E501
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
        """Gets the trans_type of this InstallmentData.  # noqa: E501


        :return: The trans_type of this InstallmentData.  # noqa: E501
        :rtype: str
        """
        return self._trans_type

    @trans_type.setter
    def trans_type(self, trans_type):
        """Sets the trans_type of this InstallmentData.


        :param trans_type: The trans_type of this InstallmentData.  # noqa: E501
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
        if issubclass(InstallmentData, dict):
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
        if not isinstance(other, InstallmentData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
