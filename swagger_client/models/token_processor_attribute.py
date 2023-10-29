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


class TokenProcessorAttribute(object):
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
        'name': 'str',
        'masked': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'masked': 'masked'
    }

    def __init__(self, name=None, masked=None, _configuration=None):  # noqa: E501
        """TokenProcessorAttribute - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._name = None
        self._masked = None
        self.discriminator = None

        self.name = name
        if masked is not None:
            self.masked = masked

    @property
    def name(self):
        """Gets the name of this TokenProcessorAttribute.  # noqa: E501

        The name of this attribute.  # noqa: E501

        :return: The name of this TokenProcessorAttribute.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TokenProcessorAttribute.

        The name of this attribute.  # noqa: E501

        :param name: The name of this TokenProcessorAttribute.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def masked(self):
        """Gets the masked of this TokenProcessorAttribute.  # noqa: E501

        Specifies whether this attribute is masked in PingFederate logs. Defaults to false.  # noqa: E501

        :return: The masked of this TokenProcessorAttribute.  # noqa: E501
        :rtype: bool
        """
        return self._masked

    @masked.setter
    def masked(self, masked):
        """Sets the masked of this TokenProcessorAttribute.

        Specifies whether this attribute is masked in PingFederate logs. Defaults to false.  # noqa: E501

        :param masked: The masked of this TokenProcessorAttribute.  # noqa: E501
        :type: bool
        """

        self._masked = masked

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
        if issubclass(TokenProcessorAttribute, dict):
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
        if not isinstance(other, TokenProcessorAttribute):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TokenProcessorAttribute):
            return True

        return self.to_dict() != other.to_dict()
