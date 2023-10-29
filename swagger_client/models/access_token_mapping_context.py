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


class AccessTokenMappingContext(object):
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
        'context_ref': 'ResourceLink'
    }

    attribute_map = {
        'type': 'type',
        'context_ref': 'contextRef'
    }

    def __init__(self, type=None, context_ref=None, _configuration=None):  # noqa: E501
        """AccessTokenMappingContext - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._type = None
        self._context_ref = None
        self.discriminator = None

        self.type = type
        self.context_ref = context_ref

    @property
    def type(self):
        """Gets the type of this AccessTokenMappingContext.  # noqa: E501

        The Access Token Mapping Context type.  # noqa: E501

        :return: The type of this AccessTokenMappingContext.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this AccessTokenMappingContext.

        The Access Token Mapping Context type.  # noqa: E501

        :param type: The type of this AccessTokenMappingContext.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["DEFAULT", "PCV", "IDP_CONNECTION", "IDP_ADAPTER", "AUTHENTICATION_POLICY_CONTRACT", "CLIENT_CREDENTIALS", "TOKEN_EXCHANGE_PROCESSOR_POLICY"]  # noqa: E501
        if (self._configuration.client_side_validation and
                type not in allowed_values):
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def context_ref(self):
        """Gets the context_ref of this AccessTokenMappingContext.  # noqa: E501

        Reference to the associated Access Token Mapping Context instance.  # noqa: E501

        :return: The context_ref of this AccessTokenMappingContext.  # noqa: E501
        :rtype: ResourceLink
        """
        return self._context_ref

    @context_ref.setter
    def context_ref(self, context_ref):
        """Sets the context_ref of this AccessTokenMappingContext.

        Reference to the associated Access Token Mapping Context instance.  # noqa: E501

        :param context_ref: The context_ref of this AccessTokenMappingContext.  # noqa: E501
        :type: ResourceLink
        """
        if self._configuration.client_side_validation and context_ref is None:
            raise ValueError("Invalid value for `context_ref`, must not be `None`")  # noqa: E501

        self._context_ref = context_ref

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
        if issubclass(AccessTokenMappingContext, dict):
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
        if not isinstance(other, AccessTokenMappingContext):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AccessTokenMappingContext):
            return True

        return self.to_dict() != other.to_dict()