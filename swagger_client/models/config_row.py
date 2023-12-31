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


class ConfigRow(object):
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
        'fields': 'list[ConfigField]',
        'default_row': 'bool'
    }

    attribute_map = {
        'fields': 'fields',
        'default_row': 'defaultRow'
    }

    def __init__(self, fields=None, default_row=None, _configuration=None):  # noqa: E501
        """ConfigRow - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._fields = None
        self._default_row = None
        self.discriminator = None

        self.fields = fields
        if default_row is not None:
            self.default_row = default_row

    @property
    def fields(self):
        """Gets the fields of this ConfigRow.  # noqa: E501

        The configuration fields in the row.  # noqa: E501

        :return: The fields of this ConfigRow.  # noqa: E501
        :rtype: list[ConfigField]
        """
        return self._fields

    @fields.setter
    def fields(self, fields):
        """Sets the fields of this ConfigRow.

        The configuration fields in the row.  # noqa: E501

        :param fields: The fields of this ConfigRow.  # noqa: E501
        :type: list[ConfigField]
        """
        if self._configuration.client_side_validation and fields is None:
            raise ValueError("Invalid value for `fields`, must not be `None`")  # noqa: E501

        self._fields = fields

    @property
    def default_row(self):
        """Gets the default_row of this ConfigRow.  # noqa: E501

        Whether this row is the default.  # noqa: E501

        :return: The default_row of this ConfigRow.  # noqa: E501
        :rtype: bool
        """
        return self._default_row

    @default_row.setter
    def default_row(self, default_row):
        """Sets the default_row of this ConfigRow.

        Whether this row is the default.  # noqa: E501

        :param default_row: The default_row of this ConfigRow.  # noqa: E501
        :type: bool
        """

        self._default_row = default_row

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
        if issubclass(ConfigRow, dict):
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
        if not isinstance(other, ConfigRow):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ConfigRow):
            return True

        return self.to_dict() != other.to_dict()
