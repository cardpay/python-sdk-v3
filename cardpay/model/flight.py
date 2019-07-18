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


class Flight(object):
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
        'carrier_code': 'str',
        'destination_code': 'str',
        'fare_basis_code': 'str',
        'index': 'int',
        'number': 'str',
        'service_class_code': 'int',
        'stop_over_code': 'str'
    }

    attribute_map = {
        'carrier_code': 'carrier_code',
        'destination_code': 'destination_code',
        'fare_basis_code': 'fare_basis_code',
        'index': 'index',
        'number': 'number',
        'service_class_code': 'service_class_code',
        'stop_over_code': 'stop_over_code'
    }

    def __init__(self, carrier_code=None, destination_code=None, fare_basis_code=None, index=None, number=None, service_class_code=None, stop_over_code=None):  # noqa: E501
        """Flight - a model defined in Swagger"""  # noqa: E501

        self._carrier_code = None
        self._destination_code = None
        self._fare_basis_code = None
        self._index = None
        self._number = None
        self._service_class_code = None
        self._stop_over_code = None
        self.discriminator = None

        if carrier_code is not None:
            self.carrier_code = carrier_code
        if destination_code is not None:
            self.destination_code = destination_code
        if fare_basis_code is not None:
            self.fare_basis_code = fare_basis_code
        if index is not None:
            self.index = index
        if number is not None:
            self.number = number
        if service_class_code is not None:
            self.service_class_code = service_class_code
        if stop_over_code is not None:
            self.stop_over_code = stop_over_code

    @property
    def carrier_code(self):
        """Gets the carrier_code of this Flight.  # noqa: E501

        Carrier code  # noqa: E501

        :return: The carrier_code of this Flight.  # noqa: E501
        :rtype: str
        """
        return self._carrier_code

    @carrier_code.setter
    def carrier_code(self, carrier_code):
        """Sets the carrier_code of this Flight.

        Carrier code  # noqa: E501

        :param carrier_code: The carrier_code of this Flight.  # noqa: E501
        :type: str
        """
        if carrier_code is not None and len(carrier_code) > 2:
            raise ValueError("Invalid value for `carrier_code`, length must be less than or equal to `2`")  # noqa: E501
        if carrier_code is not None and len(carrier_code) < 2:
            raise ValueError("Invalid value for `carrier_code`, length must be greater than or equal to `2`")  # noqa: E501

        self._carrier_code = carrier_code

    @property
    def destination_code(self):
        """Gets the destination_code of this Flight.  # noqa: E501

        Code of airport of destination, IATA code  # noqa: E501

        :return: The destination_code of this Flight.  # noqa: E501
        :rtype: str
        """
        return self._destination_code

    @destination_code.setter
    def destination_code(self, destination_code):
        """Sets the destination_code of this Flight.

        Code of airport of destination, IATA code  # noqa: E501

        :param destination_code: The destination_code of this Flight.  # noqa: E501
        :type: str
        """
        if destination_code is not None and len(destination_code) > 3:
            raise ValueError("Invalid value for `destination_code`, length must be less than or equal to `3`")  # noqa: E501
        if destination_code is not None and len(destination_code) < 3:
            raise ValueError("Invalid value for `destination_code`, length must be greater than or equal to `3`")  # noqa: E501

        self._destination_code = destination_code

    @property
    def fare_basis_code(self):
        """Gets the fare_basis_code of this Flight.  # noqa: E501

        Fare basis code  # noqa: E501

        :return: The fare_basis_code of this Flight.  # noqa: E501
        :rtype: str
        """
        return self._fare_basis_code

    @fare_basis_code.setter
    def fare_basis_code(self, fare_basis_code):
        """Sets the fare_basis_code of this Flight.

        Fare basis code  # noqa: E501

        :param fare_basis_code: The fare_basis_code of this Flight.  # noqa: E501
        :type: str
        """
        if fare_basis_code is not None and len(fare_basis_code) > 6:
            raise ValueError("Invalid value for `fare_basis_code`, length must be less than or equal to `6`")  # noqa: E501
        if fare_basis_code is not None and len(fare_basis_code) < 0:
            raise ValueError("Invalid value for `fare_basis_code`, length must be greater than or equal to `0`")  # noqa: E501

        self._fare_basis_code = fare_basis_code

    @property
    def index(self):
        """Gets the index of this Flight.  # noqa: E501

        Sequence number (index) of the flight, each index number must be unique in one flights section  # noqa: E501

        :return: The index of this Flight.  # noqa: E501
        :rtype: int
        """
        return self._index

    @index.setter
    def index(self, index):
        """Sets the index of this Flight.

        Sequence number (index) of the flight, each index number must be unique in one flights section  # noqa: E501

        :param index: The index of this Flight.  # noqa: E501
        :type: int
        """

        self._index = index

    @property
    def number(self):
        """Gets the number of this Flight.  # noqa: E501

        IATA or ICAO flight number  # noqa: E501

        :return: The number of this Flight.  # noqa: E501
        :rtype: str
        """
        return self._number

    @number.setter
    def number(self, number):
        """Sets the number of this Flight.

        IATA or ICAO flight number  # noqa: E501

        :param number: The number of this Flight.  # noqa: E501
        :type: str
        """
        if number is not None and len(number) > 5:
            raise ValueError("Invalid value for `number`, length must be less than or equal to `5`")  # noqa: E501
        if number is not None and len(number) < 0:
            raise ValueError("Invalid value for `number`, length must be greater than or equal to `0`")  # noqa: E501

        self._number = number

    @property
    def service_class_code(self):
        """Gets the service_class_code of this Flight.  # noqa: E501

        Code of service class  # noqa: E501

        :return: The service_class_code of this Flight.  # noqa: E501
        :rtype: int
        """
        return self._service_class_code

    @service_class_code.setter
    def service_class_code(self, service_class_code):
        """Sets the service_class_code of this Flight.

        Code of service class  # noqa: E501

        :param service_class_code: The service_class_code of this Flight.  # noqa: E501
        :type: int
        """

        self._service_class_code = service_class_code

    @property
    def stop_over_code(self):
        """Gets the stop_over_code of this Flight.  # noqa: E501

        Stop over code  # noqa: E501

        :return: The stop_over_code of this Flight.  # noqa: E501
        :rtype: str
        """
        return self._stop_over_code

    @stop_over_code.setter
    def stop_over_code(self, stop_over_code):
        """Sets the stop_over_code of this Flight.

        Stop over code  # noqa: E501

        :param stop_over_code: The stop_over_code of this Flight.  # noqa: E501
        :type: str
        """
        if stop_over_code is not None and len(stop_over_code) > 1:
            raise ValueError("Invalid value for `stop_over_code`, length must be less than or equal to `1`")  # noqa: E501
        if stop_over_code is not None and len(stop_over_code) < 1:
            raise ValueError("Invalid value for `stop_over_code`, length must be greater than or equal to `1`")  # noqa: E501

        self._stop_over_code = stop_over_code

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
        if issubclass(Flight, dict):
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
        if not isinstance(other, Flight):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
