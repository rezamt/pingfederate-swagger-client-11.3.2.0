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


class SchemaAttribute(object):
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
        'multi_valued': 'bool',
        'types': 'list[str]',
        'sub_attributes': 'list[str]'
    }

    attribute_map = {
        'name': 'name',
        'multi_valued': 'multiValued',
        'types': 'types',
        'sub_attributes': 'subAttributes'
    }

    def __init__(self, name=None, multi_valued=None, types=None, sub_attributes=None, _configuration=None):  # noqa: E501
        """SchemaAttribute - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._name = None
        self._multi_valued = None
        self._types = None
        self._sub_attributes = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if multi_valued is not None:
            self.multi_valued = multi_valued
        if types is not None:
            self.types = types
        if sub_attributes is not None:
            self.sub_attributes = sub_attributes

    @property
    def name(self):
        """Gets the name of this SchemaAttribute.  # noqa: E501

        Name of the attribute.  # noqa: E501

        :return: The name of this SchemaAttribute.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SchemaAttribute.

        Name of the attribute.  # noqa: E501

        :param name: The name of this SchemaAttribute.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def multi_valued(self):
        """Gets the multi_valued of this SchemaAttribute.  # noqa: E501

        Indicates whether the attribute is multi-valued.  # noqa: E501

        :return: The multi_valued of this SchemaAttribute.  # noqa: E501
        :rtype: bool
        """
        return self._multi_valued

    @multi_valued.setter
    def multi_valued(self, multi_valued):
        """Sets the multi_valued of this SchemaAttribute.

        Indicates whether the attribute is multi-valued.  # noqa: E501

        :param multi_valued: The multi_valued of this SchemaAttribute.  # noqa: E501
        :type: bool
        """

        self._multi_valued = multi_valued

    @property
    def types(self):
        """Gets the types of this SchemaAttribute.  # noqa: E501

        Represents the name of each attribute type in case of multi-valued attribute.  # noqa: E501

        :return: The types of this SchemaAttribute.  # noqa: E501
        :rtype: list[str]
        """
        return self._types

    @types.setter
    def types(self, types):
        """Sets the types of this SchemaAttribute.

        Represents the name of each attribute type in case of multi-valued attribute.  # noqa: E501

        :param types: The types of this SchemaAttribute.  # noqa: E501
        :type: list[str]
        """

        self._types = types

    @property
    def sub_attributes(self):
        """Gets the sub_attributes of this SchemaAttribute.  # noqa: E501

        List of sub-attributes for an attribute.  # noqa: E501

        :return: The sub_attributes of this SchemaAttribute.  # noqa: E501
        :rtype: list[str]
        """
        return self._sub_attributes

    @sub_attributes.setter
    def sub_attributes(self, sub_attributes):
        """Sets the sub_attributes of this SchemaAttribute.

        List of sub-attributes for an attribute.  # noqa: E501

        :param sub_attributes: The sub_attributes of this SchemaAttribute.  # noqa: E501
        :type: list[str]
        """

        self._sub_attributes = sub_attributes

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
        if issubclass(SchemaAttribute, dict):
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
        if not isinstance(other, SchemaAttribute):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SchemaAttribute):
            return True

        return self.to_dict() != other.to_dict()
