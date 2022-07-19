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


class PaymentRequestPaymentData(object):
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
        "authentication_request": "bool",
        "currency": "str",
        "dynamic_descriptor": "str",
        "encrypted_data": "str",
        "generate_token": "bool",
        "installment_amount": "float",
        "installment_type": "str",
        "installments": "str",
        "note": "str",
        "preauth": "bool",
        "three_ds_challenge_indicator": "str",
        "trans_type": "str",
    }

    attribute_map = {
        "amount": "amount",
        "authentication_request": "authentication_request",
        "currency": "currency",
        "dynamic_descriptor": "dynamic_descriptor",
        "encrypted_data": "encrypted_data",
        "generate_token": "generate_token",
        "installment_amount": "installment_amount",
        "installment_type": "installment_type",
        "installments": "installments",
        "note": "note",
        "preauth": "preauth",
        "three_ds_challenge_indicator": "three_ds_challenge_indicator",
        "trans_type": "trans_type",
    }

    def __init__(
        self,
        amount=None,
        authentication_request=None,
        currency=None,
        dynamic_descriptor=None,
        encrypted_data=None,
        generate_token=None,
        installment_amount=None,
        installment_type=None,
        installments=None,
        note=None,
        preauth=None,
        three_ds_challenge_indicator=None,
        trans_type=None,
    ):  # noqa: E501
        """PaymentRequestPaymentData - a model defined in Swagger"""  # noqa: E501

        self._amount = None
        self._authentication_request = None
        self._currency = None
        self._dynamic_descriptor = None
        self._encrypted_data = None
        self._generate_token = None
        self._installment_amount = None
        self._installment_type = None
        self._installments = None
        self._note = None
        self._preauth = None
        self._three_ds_challenge_indicator = None
        self._trans_type = None
        self.discriminator = None

        if amount is not None:
            self.amount = amount
        if authentication_request is not None:
            self.authentication_request = authentication_request
        self.currency = currency
        if dynamic_descriptor is not None:
            self.dynamic_descriptor = dynamic_descriptor
        if encrypted_data is not None:
            self.encrypted_data = encrypted_data
        if generate_token is not None:
            self.generate_token = generate_token
        if installment_amount is not None:
            self.installment_amount = installment_amount
        if installment_type is not None:
            self.installment_type = installment_type
        if installments is not None:
            self.installments = installments
        if note is not None:
            self.note = note
        if preauth is not None:
            self.preauth = preauth
        if three_ds_challenge_indicator is not None:
            self.three_ds_challenge_indicator = three_ds_challenge_indicator
        if trans_type is not None:
            self.trans_type = trans_type

    @property
    def amount(self):
        """Gets the amount of this PaymentRequestPaymentData.  # noqa: E501

        The total transaction amount in selected currency with dot as a decimal separator, must be less than 10 billion If 'payment_method' = `BITCOIN` then minimum order amount is approximately 0.003 bitcoins or its equivalent. The exact value should be provided by the account manager.  # noqa: E501

        :return: The amount of this PaymentRequestPaymentData.  # noqa: E501
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this PaymentRequestPaymentData.

        The total transaction amount in selected currency with dot as a decimal separator, must be less than 10 billion If 'payment_method' = `BITCOIN` then minimum order amount is approximately 0.003 bitcoins or its equivalent. The exact value should be provided by the account manager.  # noqa: E501

        :param amount: The amount of this PaymentRequestPaymentData.  # noqa: E501
        :type: float
        """

        self._amount = amount

    @property
    def authentication_request(self):
        """Gets the authentication_request of this PaymentRequestPaymentData.  # noqa: E501

        If set to `true`, amount must not be presented in request, no payment will be made, only cardholder authentication will be performed. Also can be used to generate token. *(for BANKCARD payment method only)*  # noqa: E501

        :return: The authentication_request of this PaymentRequestPaymentData.  # noqa: E501
        :rtype: bool
        """
        return self._authentication_request

    @authentication_request.setter
    def authentication_request(self, authentication_request):
        """Sets the authentication_request of this PaymentRequestPaymentData.

        If set to `true`, amount must not be presented in request, no payment will be made, only cardholder authentication will be performed. Also can be used to generate token. *(for BANKCARD payment method only)*  # noqa: E501

        :param authentication_request: The authentication_request of this PaymentRequestPaymentData.  # noqa: E501
        :type: bool
        """

        self._authentication_request = authentication_request

    @property
    def currency(self):
        """Gets the currency of this PaymentRequestPaymentData.  # noqa: E501

        [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) currency code  # noqa: E501

        :return: The currency of this PaymentRequestPaymentData.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this PaymentRequestPaymentData.

        [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) currency code  # noqa: E501

        :param currency: The currency of this PaymentRequestPaymentData.  # noqa: E501
        :type: str
        """
        if currency is None:
            raise ValueError(
                "Invalid value for `currency`, must not be `None`"
            )  # noqa: E501

        self._currency = currency

    @property
    def dynamic_descriptor(self):
        """Gets the dynamic_descriptor of this PaymentRequestPaymentData.  # noqa: E501

        Short description of the service or product, must be enabled by CardPay manager to be used *(for BANKCARD payment method only)*  # noqa: E501

        :return: The dynamic_descriptor of this PaymentRequestPaymentData.  # noqa: E501
        :rtype: str
        """
        return self._dynamic_descriptor

    @dynamic_descriptor.setter
    def dynamic_descriptor(self, dynamic_descriptor):
        """Sets the dynamic_descriptor of this PaymentRequestPaymentData.

        Short description of the service or product, must be enabled by CardPay manager to be used *(for BANKCARD payment method only)*  # noqa: E501

        :param dynamic_descriptor: The dynamic_descriptor of this PaymentRequestPaymentData.  # noqa: E501
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
    def encrypted_data(self):
        """Gets the encrypted_data of this PaymentRequestPaymentData.  # noqa: E501

        The encrypted payment credentials encoded in base64. *(for APPLEPAY payment method only)*  # noqa: E501

        :return: The encrypted_data of this PaymentRequestPaymentData.  # noqa: E501
        :rtype: str
        """
        return self._encrypted_data

    @encrypted_data.setter
    def encrypted_data(self, encrypted_data):
        """Sets the encrypted_data of this PaymentRequestPaymentData.

        The encrypted payment credentials encoded in base64. *(for APPLEPAY payment method only)*  # noqa: E501

        :param encrypted_data: The encrypted_data of this PaymentRequestPaymentData.  # noqa: E501
        :type: str
        """
        if encrypted_data is not None and len(encrypted_data) > 10000:
            raise ValueError(
                "Invalid value for `encrypted_data`, length must be less than or equal to `10000`"
            )  # noqa: E501
        if encrypted_data is not None and len(encrypted_data) < 0:
            raise ValueError(
                "Invalid value for `encrypted_data`, length must be greater than or equal to `0`"
            )  # noqa: E501

        self._encrypted_data = encrypted_data

    @property
    def generate_token(self):
        """Gets the generate_token of this PaymentRequestPaymentData.  # noqa: E501

        If set to `true`, token will be generated and returned in the response. Token can be generated only for successful transactions (not for declined transactions) *(for BANKCARD payment method only)*  # noqa: E501

        :return: The generate_token of this PaymentRequestPaymentData.  # noqa: E501
        :rtype: bool
        """
        return self._generate_token

    @generate_token.setter
    def generate_token(self, generate_token):
        """Sets the generate_token of this PaymentRequestPaymentData.

        If set to `true`, token will be generated and returned in the response. Token can be generated only for successful transactions (not for declined transactions) *(for BANKCARD payment method only)*  # noqa: E501

        :param generate_token: The generate_token of this PaymentRequestPaymentData.  # noqa: E501
        :type: bool
        """

        self._generate_token = generate_token

    @property
    def installment_amount(self):
        """Gets the installment_amount of this PaymentRequestPaymentData.  # noqa: E501

        Amount of 1 installment payment, should be less or equal to total amount of subscription, can have dot as a decimal separator. Mandatory for Payment Page Mode only.  # noqa: E501

        :return: The installment_amount of this PaymentRequestPaymentData.  # noqa: E501
        :rtype: float
        """
        return self._installment_amount

    @installment_amount.setter
    def installment_amount(self, installment_amount):
        """Sets the installment_amount of this PaymentRequestPaymentData.

        Amount of 1 installment payment, should be less or equal to total amount of subscription, can have dot as a decimal separator. Mandatory for Payment Page Mode only.  # noqa: E501

        :param installment_amount: The installment_amount of this PaymentRequestPaymentData.  # noqa: E501
        :type: float
        """

        self._installment_amount = installment_amount

    @property
    def installment_type(self):
        """Gets the installment_type of this PaymentRequestPaymentData.  # noqa: E501

        Installment type, 2 possible values: `IF` - issuer financed `MF_HOLD' - merchant financed. For installment subscription with hold rest amount.  # noqa: E501

        :return: The installment_type of this PaymentRequestPaymentData.  # noqa: E501
        :rtype: str
        """
        return self._installment_type

    @installment_type.setter
    def installment_type(self, installment_type):
        """Sets the installment_type of this PaymentRequestPaymentData.

        Installment type, 2 possible values: `IF` - issuer financed `MF_HOLD' - merchant financed. For installment subscription with hold rest amount.  # noqa: E501

        :param installment_type: The installment_type of this PaymentRequestPaymentData.  # noqa: E501
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
    def installments(self):
        """Gets the installments of this PaymentRequestPaymentData.  # noqa: E501

        Number of total installment payments, to be charged per defined interval. For installment subscription with installment_type = `MF_HOLD` can be 1-12. For installment subscription with installment_type = `IF` can be 1-99.  # noqa: E501

        :return: The installments of this PaymentRequestPaymentData.  # noqa: E501
        :rtype: str
        """
        return self._installments

    @installments.setter
    def installments(self, installments):
        """Sets the installments of this PaymentRequestPaymentData.

        Number of total installment payments, to be charged per defined interval. For installment subscription with installment_type = `MF_HOLD` can be 1-12. For installment subscription with installment_type = `IF` can be 1-99.  # noqa: E501

        :param installments: The installments of this PaymentRequestPaymentData.  # noqa: E501
        :type: str
        """

        self._installments = installments

    @property
    def note(self):
        """Gets the note of this PaymentRequestPaymentData.  # noqa: E501

        Note about the transaction that will not be displayed to Customer  # noqa: E501

        :return: The note of this PaymentRequestPaymentData.  # noqa: E501
        :rtype: str
        """
        return self._note

    @note.setter
    def note(self, note):
        """Sets the note of this PaymentRequestPaymentData.

        Note about the transaction that will not be displayed to Customer  # noqa: E501

        :param note: The note of this PaymentRequestPaymentData.  # noqa: E501
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
        """Gets the preauth of this PaymentRequestPaymentData.  # noqa: E501

        If set to `true`, the amount will not be captured but only blocked. Payments with 'preauth' attribute will be captured automatically in 7 days from the time of creating the preauth transaction. *(for BANKCARD payment method only)*.  # noqa: E501

        :return: The preauth of this PaymentRequestPaymentData.  # noqa: E501
        :rtype: bool
        """
        return self._preauth

    @preauth.setter
    def preauth(self, preauth):
        """Sets the preauth of this PaymentRequestPaymentData.

        If set to `true`, the amount will not be captured but only blocked. Payments with 'preauth' attribute will be captured automatically in 7 days from the time of creating the preauth transaction. *(for BANKCARD payment method only)*.  # noqa: E501

        :param preauth: The preauth of this PaymentRequestPaymentData.  # noqa: E501
        :type: bool
        """

        self._preauth = preauth

    @property
    def three_ds_challenge_indicator(self):
        """Gets the three_ds_challenge_indicator of this PaymentRequestPaymentData.  # noqa: E501


        :return: The three_ds_challenge_indicator of this PaymentRequestPaymentData.  # noqa: E501
        :rtype: str
        """
        return self._three_ds_challenge_indicator

    @three_ds_challenge_indicator.setter
    def three_ds_challenge_indicator(self, three_ds_challenge_indicator):
        """Sets the three_ds_challenge_indicator of this PaymentRequestPaymentData.


        :param three_ds_challenge_indicator: The three_ds_challenge_indicator of this PaymentRequestPaymentData.  # noqa: E501
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
        """Gets the trans_type of this PaymentRequestPaymentData.  # noqa: E501


        :return: The trans_type of this PaymentRequestPaymentData.  # noqa: E501
        :rtype: str
        """
        return self._trans_type

    @trans_type.setter
    def trans_type(self, trans_type):
        """Sets the trans_type of this PaymentRequestPaymentData.


        :param trans_type: The trans_type of this PaymentRequestPaymentData.  # noqa: E501
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
        if issubclass(PaymentRequestPaymentData, dict):
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
        if not isinstance(other, PaymentRequestPaymentData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
