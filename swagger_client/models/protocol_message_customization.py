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


class ProtocolMessageCustomization(object):
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
        'context_name': 'str',
        'message_expression': 'str'
    }

    attribute_map = {
        'context_name': 'contextName',
        'message_expression': 'messageExpression'
    }

    def __init__(self, context_name=None, message_expression=None, _configuration=None):  # noqa: E501
        """ProtocolMessageCustomization - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._context_name = None
        self._message_expression = None
        self.discriminator = None

        if context_name is not None:
            self.context_name = context_name
        if message_expression is not None:
            self.message_expression = message_expression

    @property
    def context_name(self):
        """Gets the context_name of this ProtocolMessageCustomization.  # noqa: E501

        The context in which the customization will be applied. Depending on the connection type and protocol, this can either be 'assertion', 'authn-response' or 'authn-request'.  # noqa: E501

        :return: The context_name of this ProtocolMessageCustomization.  # noqa: E501
        :rtype: str
        """
        return self._context_name

    @context_name.setter
    def context_name(self, context_name):
        """Sets the context_name of this ProtocolMessageCustomization.

        The context in which the customization will be applied. Depending on the connection type and protocol, this can either be 'assertion', 'authn-response' or 'authn-request'.  # noqa: E501

        :param context_name: The context_name of this ProtocolMessageCustomization.  # noqa: E501
        :type: str
        """

        self._context_name = context_name

    @property
    def message_expression(self):
        """Gets the message_expression of this ProtocolMessageCustomization.  # noqa: E501

        The OGNL expression that will be executed. Refer to the Admin Manual for a list of variables provided by PingFederate.  # noqa: E501

        :return: The message_expression of this ProtocolMessageCustomization.  # noqa: E501
        :rtype: str
        """
        return self._message_expression

    @message_expression.setter
    def message_expression(self, message_expression):
        """Sets the message_expression of this ProtocolMessageCustomization.

        The OGNL expression that will be executed. Refer to the Admin Manual for a list of variables provided by PingFederate.  # noqa: E501

        :param message_expression: The message_expression of this ProtocolMessageCustomization.  # noqa: E501
        :type: str
        """

        self._message_expression = message_expression

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
        if issubclass(ProtocolMessageCustomization, dict):
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
        if not isinstance(other, ProtocolMessageCustomization):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ProtocolMessageCustomization):
            return True

        return self.to_dict() != other.to_dict()
