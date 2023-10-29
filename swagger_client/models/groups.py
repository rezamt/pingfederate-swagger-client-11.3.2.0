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


class Groups(object):
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
        'write_groups': 'WriteGroups',
        'read_groups': 'ReadGroups'
    }

    attribute_map = {
        'write_groups': 'writeGroups',
        'read_groups': 'readGroups'
    }

    def __init__(self, write_groups=None, read_groups=None, _configuration=None):  # noqa: E501
        """Groups - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._write_groups = None
        self._read_groups = None
        self.discriminator = None

        self.write_groups = write_groups
        self.read_groups = read_groups

    @property
    def write_groups(self):
        """Gets the write_groups of this Groups.  # noqa: E501

        Configuration to create a group within the user repository.  # noqa: E501

        :return: The write_groups of this Groups.  # noqa: E501
        :rtype: WriteGroups
        """
        return self._write_groups

    @write_groups.setter
    def write_groups(self, write_groups):
        """Sets the write_groups of this Groups.

        Configuration to create a group within the user repository.  # noqa: E501

        :param write_groups: The write_groups of this Groups.  # noqa: E501
        :type: WriteGroups
        """
        if self._configuration.client_side_validation and write_groups is None:
            raise ValueError("Invalid value for `write_groups`, must not be `None`")  # noqa: E501

        self._write_groups = write_groups

    @property
    def read_groups(self):
        """Gets the read_groups of this Groups.  # noqa: E501

        Configuration to lookup group info within the user repository and respond to incoming SCIM requests.  # noqa: E501

        :return: The read_groups of this Groups.  # noqa: E501
        :rtype: ReadGroups
        """
        return self._read_groups

    @read_groups.setter
    def read_groups(self, read_groups):
        """Sets the read_groups of this Groups.

        Configuration to lookup group info within the user repository and respond to incoming SCIM requests.  # noqa: E501

        :param read_groups: The read_groups of this Groups.  # noqa: E501
        :type: ReadGroups
        """
        if self._configuration.client_side_validation and read_groups is None:
            raise ValueError("Invalid value for `read_groups`, must not be `None`")  # noqa: E501

        self._read_groups = read_groups

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
        if issubclass(Groups, dict):
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
        if not isinstance(other, Groups):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Groups):
            return True

        return self.to_dict() != other.to_dict()
