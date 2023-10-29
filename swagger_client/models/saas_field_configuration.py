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


class SaasFieldConfiguration(object):
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
        'attribute_names': 'list[str]',
        'default_value': 'str',
        'expression': 'str',
        'create_only': 'bool',
        'trim': 'bool',
        'character_case': 'str',
        'parser': 'str',
        'masked': 'bool'
    }

    attribute_map = {
        'attribute_names': 'attributeNames',
        'default_value': 'defaultValue',
        'expression': 'expression',
        'create_only': 'createOnly',
        'trim': 'trim',
        'character_case': 'characterCase',
        'parser': 'parser',
        'masked': 'masked'
    }

    def __init__(self, attribute_names=None, default_value=None, expression=None, create_only=None, trim=None, character_case=None, parser=None, masked=None, _configuration=None):  # noqa: E501
        """SaasFieldConfiguration - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._attribute_names = None
        self._default_value = None
        self._expression = None
        self._create_only = None
        self._trim = None
        self._character_case = None
        self._parser = None
        self._masked = None
        self.discriminator = None

        if attribute_names is not None:
            self.attribute_names = attribute_names
        if default_value is not None:
            self.default_value = default_value
        if expression is not None:
            self.expression = expression
        if create_only is not None:
            self.create_only = create_only
        if trim is not None:
            self.trim = trim
        if character_case is not None:
            self.character_case = character_case
        if parser is not None:
            self.parser = parser
        if masked is not None:
            self.masked = masked

    @property
    def attribute_names(self):
        """Gets the attribute_names of this SaasFieldConfiguration.  # noqa: E501

        The list of source attribute names used to generate or map to a target field  # noqa: E501

        :return: The attribute_names of this SaasFieldConfiguration.  # noqa: E501
        :rtype: list[str]
        """
        return self._attribute_names

    @attribute_names.setter
    def attribute_names(self, attribute_names):
        """Sets the attribute_names of this SaasFieldConfiguration.

        The list of source attribute names used to generate or map to a target field  # noqa: E501

        :param attribute_names: The attribute_names of this SaasFieldConfiguration.  # noqa: E501
        :type: list[str]
        """

        self._attribute_names = attribute_names

    @property
    def default_value(self):
        """Gets the default_value of this SaasFieldConfiguration.  # noqa: E501

        The default value for the target field  # noqa: E501

        :return: The default_value of this SaasFieldConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._default_value

    @default_value.setter
    def default_value(self, default_value):
        """Sets the default_value of this SaasFieldConfiguration.

        The default value for the target field  # noqa: E501

        :param default_value: The default_value of this SaasFieldConfiguration.  # noqa: E501
        :type: str
        """

        self._default_value = default_value

    @property
    def expression(self):
        """Gets the expression of this SaasFieldConfiguration.  # noqa: E501

        An OGNL expression to obtain a value.  # noqa: E501

        :return: The expression of this SaasFieldConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._expression

    @expression.setter
    def expression(self, expression):
        """Sets the expression of this SaasFieldConfiguration.

        An OGNL expression to obtain a value.  # noqa: E501

        :param expression: The expression of this SaasFieldConfiguration.  # noqa: E501
        :type: str
        """

        self._expression = expression

    @property
    def create_only(self):
        """Gets the create_only of this SaasFieldConfiguration.  # noqa: E501

        Indicates whether this field is a create only field and cannot be updated.  # noqa: E501

        :return: The create_only of this SaasFieldConfiguration.  # noqa: E501
        :rtype: bool
        """
        return self._create_only

    @create_only.setter
    def create_only(self, create_only):
        """Sets the create_only of this SaasFieldConfiguration.

        Indicates whether this field is a create only field and cannot be updated.  # noqa: E501

        :param create_only: The create_only of this SaasFieldConfiguration.  # noqa: E501
        :type: bool
        """

        self._create_only = create_only

    @property
    def trim(self):
        """Gets the trim of this SaasFieldConfiguration.  # noqa: E501

        Indicates whether field should be trimmed before provisioning.  # noqa: E501

        :return: The trim of this SaasFieldConfiguration.  # noqa: E501
        :rtype: bool
        """
        return self._trim

    @trim.setter
    def trim(self, trim):
        """Sets the trim of this SaasFieldConfiguration.

        Indicates whether field should be trimmed before provisioning.  # noqa: E501

        :param trim: The trim of this SaasFieldConfiguration.  # noqa: E501
        :type: bool
        """

        self._trim = trim

    @property
    def character_case(self):
        """Gets the character_case of this SaasFieldConfiguration.  # noqa: E501

        The character case of the field value.  # noqa: E501

        :return: The character_case of this SaasFieldConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._character_case

    @character_case.setter
    def character_case(self, character_case):
        """Sets the character_case of this SaasFieldConfiguration.

        The character case of the field value.  # noqa: E501

        :param character_case: The character_case of this SaasFieldConfiguration.  # noqa: E501
        :type: str
        """
        allowed_values = ["LOWER", "UPPER", "NONE"]  # noqa: E501
        if (self._configuration.client_side_validation and
                character_case not in allowed_values):
            raise ValueError(
                "Invalid value for `character_case` ({0}), must be one of {1}"  # noqa: E501
                .format(character_case, allowed_values)
            )

        self._character_case = character_case

    @property
    def parser(self):
        """Gets the parser of this SaasFieldConfiguration.  # noqa: E501

        Indicates how the field shall be parsed.  # noqa: E501

        :return: The parser of this SaasFieldConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._parser

    @parser.setter
    def parser(self, parser):
        """Sets the parser of this SaasFieldConfiguration.

        Indicates how the field shall be parsed.  # noqa: E501

        :param parser: The parser of this SaasFieldConfiguration.  # noqa: E501
        :type: str
        """
        allowed_values = ["EXTRACT_CN_FROM_DN", "EXTRACT_USERNAME_FROM_EMAIL", "NONE"]  # noqa: E501
        if (self._configuration.client_side_validation and
                parser not in allowed_values):
            raise ValueError(
                "Invalid value for `parser` ({0}), must be one of {1}"  # noqa: E501
                .format(parser, allowed_values)
            )

        self._parser = parser

    @property
    def masked(self):
        """Gets the masked of this SaasFieldConfiguration.  # noqa: E501

        Indicates whether the attribute should be masked in server logs.  # noqa: E501

        :return: The masked of this SaasFieldConfiguration.  # noqa: E501
        :rtype: bool
        """
        return self._masked

    @masked.setter
    def masked(self, masked):
        """Sets the masked of this SaasFieldConfiguration.

        Indicates whether the attribute should be masked in server logs.  # noqa: E501

        :param masked: The masked of this SaasFieldConfiguration.  # noqa: E501
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
        if issubclass(SaasFieldConfiguration, dict):
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
        if not isinstance(other, SaasFieldConfiguration):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SaasFieldConfiguration):
            return True

        return self.to_dict() != other.to_dict()