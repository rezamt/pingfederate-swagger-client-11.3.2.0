# coding: utf-8

"""
    Administrative API Documentation

    The PingFederate Administrative API is a REST-based interface that provides a programmatic way to make configuration changes to PingFederate as an alternative to using the administrative console.<br/><br/>Expand the resources below to display implementation details on that resource such as the available endpoints, the parameter and response models for the operation, and the model structure of the resources themselves. Each resource operation comes with the ability to interact with the API. You are prompted for proper administration credentials when you try to perform an API operation.  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from swagger_client.configuration import Configuration


class BackChannelAuth(object):
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
        'type': 'str',
        'http_basic_credentials': 'UsernamePasswordCredentials',
        'digital_signature': 'bool'
    }

    attribute_map = {
        'type': 'type',
        'http_basic_credentials': 'httpBasicCredentials',
        'digital_signature': 'digitalSignature'
    }

    discriminator_value_class_map = {
        'OutboundBackChannelAuth': 'OutboundBackChannelAuth',
        'InboundBackChannelAuth': 'InboundBackChannelAuth'
    }

    def __init__(self, type=None, http_basic_credentials=None, digital_signature=None, _configuration=None):  # noqa: E501
        """BackChannelAuth - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._type = None
        self._http_basic_credentials = None
        self._digital_signature = None
        self.discriminator = 'type'

        self.type = type
        if http_basic_credentials is not None:
            self.http_basic_credentials = http_basic_credentials
        if digital_signature is not None:
            self.digital_signature = digital_signature

    @property
    def type(self):
        """Gets the type of this BackChannelAuth.  # noqa: E501

        The back channel authentication type.  # noqa: E501

        :return: The type of this BackChannelAuth.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this BackChannelAuth.

        The back channel authentication type.  # noqa: E501

        :param type: The type of this BackChannelAuth.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["INBOUND", "OUTBOUND"]  # noqa: E501
        if (self._configuration.client_side_validation and
                type not in allowed_values):
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def http_basic_credentials(self):
        """Gets the http_basic_credentials of this BackChannelAuth.  # noqa: E501

        The credentials to use when you authenticate with the SOAP endpoint.  # noqa: E501

        :return: The http_basic_credentials of this BackChannelAuth.  # noqa: E501
        :rtype: UsernamePasswordCredentials
        """
        return self._http_basic_credentials

    @http_basic_credentials.setter
    def http_basic_credentials(self, http_basic_credentials):
        """Sets the http_basic_credentials of this BackChannelAuth.

        The credentials to use when you authenticate with the SOAP endpoint.  # noqa: E501

        :param http_basic_credentials: The http_basic_credentials of this BackChannelAuth.  # noqa: E501
        :type: UsernamePasswordCredentials
        """

        self._http_basic_credentials = http_basic_credentials

    @property
    def digital_signature(self):
        """Gets the digital_signature of this BackChannelAuth.  # noqa: E501

        If incoming or outgoing messages must be signed.  # noqa: E501

        :return: The digital_signature of this BackChannelAuth.  # noqa: E501
        :rtype: bool
        """
        return self._digital_signature

    @digital_signature.setter
    def digital_signature(self, digital_signature):
        """Sets the digital_signature of this BackChannelAuth.

        If incoming or outgoing messages must be signed.  # noqa: E501

        :param digital_signature: The digital_signature of this BackChannelAuth.  # noqa: E501
        :type: bool
        """

        self._digital_signature = digital_signature

    def get_real_child_model(self, data):
        """Returns the real base class specified by the discriminator"""
        discriminator_value = data[self.discriminator].lower()
        return self.discriminator_value_class_map.get(discriminator_value)

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
                result[attr] = value
        if issubclass(BackChannelAuth, dict):
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
        if not isinstance(other, BackChannelAuth):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BackChannelAuth):
            return True

        return self.to_dict() != other.to_dict()