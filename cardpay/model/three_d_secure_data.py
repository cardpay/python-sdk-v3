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


class ThreeDSecureData(object):
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
        "card_enrollment": "str",
        "cavv": "str",
        "cavv_algorithm": "str",
        "pa_res": "str",
        "status": "str",
        "three_d_secure_flow": "str",
        "xid": "str",
    }

    attribute_map = {
        "card_enrollment": "card_enrollment",
        "cavv": "cavv",
        "cavv_algorithm": "cavv_algorithm",
        "pa_res": "pa_res",
        "status": "status",
        "three_d_secure_flow": "three_d_secure_flow",
        "xid": "xid",
    }

    def __init__(
        self,
        card_enrollment=None,
        cavv=None,
        cavv_algorithm=None,
        pa_res=None,
        status=None,
        three_d_secure_flow=None,
        xid=None,
    ):  # noqa: E501
        """ThreeDSecureData - a model defined in Swagger"""  # noqa: E501

        self._card_enrollment = None
        self._cavv = None
        self._cavv_algorithm = None
        self._pa_res = None
        self._status = None
        self._three_d_secure_flow = None
        self._xid = None
        self.discriminator = None

        if card_enrollment is not None:
            self.card_enrollment = card_enrollment
        if cavv is not None:
            self.cavv = cavv
        if cavv_algorithm is not None:
            self.cavv_algorithm = cavv_algorithm
        if pa_res is not None:
            self.pa_res = pa_res
        if status is not None:
            self.status = status
        if three_d_secure_flow is not None:
            self.three_d_secure_flow = three_d_secure_flow
        if xid is not None:
            self.xid = xid

    @property
    def card_enrollment(self):
        """Gets the card_enrollment of this ThreeDSecureData.  # noqa: E501

        Card enrollment in 3DS flow, possible values are: S - 3D Secure Skipped, N - 3D Secure not enrolled, Y - 3D Secure enrolled  # noqa: E501

        :return: The card_enrollment of this ThreeDSecureData.  # noqa: E501
        :rtype: str
        """
        return self._card_enrollment

    @card_enrollment.setter
    def card_enrollment(self, card_enrollment):
        """Sets the card_enrollment of this ThreeDSecureData.

        Card enrollment in 3DS flow, possible values are: S - 3D Secure Skipped, N - 3D Secure not enrolled, Y - 3D Secure enrolled  # noqa: E501

        :param card_enrollment: The card_enrollment of this ThreeDSecureData.  # noqa: E501
        :type: str
        """
        if card_enrollment is not None and not re.search(
            r"[SNY]", card_enrollment
        ):  # noqa: E501
            raise ValueError(
                r"Invalid value for `card_enrollment`, must be a follow pattern or equal to `/[SNY]/`"
            )  # noqa: E501

        self._card_enrollment = card_enrollment

    @property
    def cavv(self):
        """Gets the cavv of this ThreeDSecureData.  # noqa: E501

        Cardholder authentication verification value  # noqa: E501

        :return: The cavv of this ThreeDSecureData.  # noqa: E501
        :rtype: str
        """
        return self._cavv

    @cavv.setter
    def cavv(self, cavv):
        """Sets the cavv of this ThreeDSecureData.

        Cardholder authentication verification value  # noqa: E501

        :param cavv: The cavv of this ThreeDSecureData.  # noqa: E501
        :type: str
        """

        self._cavv = cavv

    @property
    def cavv_algorithm(self):
        """Gets the cavv_algorithm of this ThreeDSecureData.  # noqa: E501

        CAVV algorithm  # noqa: E501

        :return: The cavv_algorithm of this ThreeDSecureData.  # noqa: E501
        :rtype: str
        """
        return self._cavv_algorithm

    @cavv_algorithm.setter
    def cavv_algorithm(self, cavv_algorithm):
        """Sets the cavv_algorithm of this ThreeDSecureData.

        CAVV algorithm  # noqa: E501

        :param cavv_algorithm: The cavv_algorithm of this ThreeDSecureData.  # noqa: E501
        :type: str
        """

        self._cavv_algorithm = cavv_algorithm

    @property
    def pa_res(self):
        """Gets the pa_res of this ThreeDSecureData.  # noqa: E501

        PaRes bank authentication result  # noqa: E501

        :return: The pa_res of this ThreeDSecureData.  # noqa: E501
        :rtype: str
        """
        return self._pa_res

    @pa_res.setter
    def pa_res(self, pa_res):
        """Sets the pa_res of this ThreeDSecureData.

        PaRes bank authentication result  # noqa: E501

        :param pa_res: The pa_res of this ThreeDSecureData.  # noqa: E501
        :type: str
        """

        self._pa_res = pa_res

    @property
    def status(self):
        """Gets the status of this ThreeDSecureData.  # noqa: E501

        3DS status (from PaRes for 3Ds 1.0, ARes message for 3Ds 2.0) (possible values Y,A,U)  # noqa: E501

        :return: The status of this ThreeDSecureData.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ThreeDSecureData.

        3DS status (from PaRes for 3Ds 1.0, ARes message for 3Ds 2.0) (possible values Y,A,U)  # noqa: E501

        :param status: The status of this ThreeDSecureData.  # noqa: E501
        :type: str
        """
        if status is not None and not re.search(r"[YAU]", status):  # noqa: E501
            raise ValueError(
                r"Invalid value for `status`, must be a follow pattern or equal to `/[YAU]/`"
            )  # noqa: E501

        self._status = status

    @property
    def three_d_secure_flow(self):
        """Gets the three_d_secure_flow of this ThreeDSecureData.  # noqa: E501

        Possible values: 3DS1 - 3DS 1.0 flow, 3DS2C - 3DS 2.0 challenge flow, 3DS2F - 3DS 2.0 frictionless flow  # noqa: E501

        :return: The three_d_secure_flow of this ThreeDSecureData.  # noqa: E501
        :rtype: str
        """
        return self._three_d_secure_flow

    @three_d_secure_flow.setter
    def three_d_secure_flow(self, three_d_secure_flow):
        """Sets the three_d_secure_flow of this ThreeDSecureData.

        Possible values: 3DS1 - 3DS 1.0 flow, 3DS2C - 3DS 2.0 challenge flow, 3DS2F - 3DS 2.0 frictionless flow  # noqa: E501

        :param three_d_secure_flow: The three_d_secure_flow of this ThreeDSecureData.  # noqa: E501
        :type: str
        """
        if three_d_secure_flow is not None and not re.search(
            r"3DS1|3DS2C|3DS2F", three_d_secure_flow
        ):  # noqa: E501
            raise ValueError(
                r"Invalid value for `three_d_secure_flow`, must be a follow pattern or equal to `/3DS1|3DS2C|3DS2F/`"
            )  # noqa: E501

        self._three_d_secure_flow = three_d_secure_flow

    @property
    def xid(self):
        """Gets the xid of this ThreeDSecureData.  # noqa: E501

        Transaction Id in PaRes  # noqa: E501

        :return: The xid of this ThreeDSecureData.  # noqa: E501
        :rtype: str
        """
        return self._xid

    @xid.setter
    def xid(self, xid):
        """Sets the xid of this ThreeDSecureData.

        Transaction Id in PaRes  # noqa: E501

        :param xid: The xid of this ThreeDSecureData.  # noqa: E501
        :type: str
        """

        self._xid = xid

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
        if issubclass(ThreeDSecureData, dict):
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
        if not isinstance(other, ThreeDSecureData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other