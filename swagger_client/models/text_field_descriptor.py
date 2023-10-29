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


class TextFieldDescriptor(object):
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
        'encrypted': 'bool',
        'size': 'int'
    }

    attribute_map = {
        'encrypted': 'encrypted',
        'size': 'size'
    }

    def __init__(self, encrypted=None, size=None, _configuration=None):  # noqa: E501
        """TextFieldDescriptor - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._encrypted = None
        self._size = None
        self.discriminator = None

        if encrypted is not None:
            self.encrypted = encrypted
        if size is not None:
            self.size = size

    @property
    def encrypted(self):
        """Gets the encrypted of this TextFieldDescriptor.  # noqa: E501

        Determines whether the field value should be masked in the UI and encrypted on disk.  # noqa: E501

        :return: The encrypted of this TextFieldDescriptor.  # noqa: E501
        :rtype: bool
        """
        return self._encrypted

    @encrypted.setter
    def encrypted(self, encrypted):
        """Sets the encrypted of this TextFieldDescriptor.

        Determines whether the field value should be masked in the UI and encrypted on disk.  # noqa: E501

        :param encrypted: The encrypted of this TextFieldDescriptor.  # noqa: E501
        :type: bool
        """

        self._encrypted = encrypted

    @property
    def size(self):
        """Gets the size of this TextFieldDescriptor.  # noqa: E501

        The size of the text field.  # noqa: E501

        :return: The size of this TextFieldDescriptor.  # noqa: E501
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this TextFieldDescriptor.

        The size of the text field.  # noqa: E501

        :param size: The size of this TextFieldDescriptor.  # noqa: E501
        :type: int
        """

        self._size = size

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
        if issubclass(TextFieldDescriptor, dict):
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
        if not isinstance(other, TextFieldDescriptor):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TextFieldDescriptor):
            return True

        return self.to_dict() != other.to_dict()
