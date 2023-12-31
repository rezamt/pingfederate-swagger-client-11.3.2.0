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


class AtmSelectionSettings(object):
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
        'inherited': 'bool',
        'resource_uris': 'list[str]'
    }

    attribute_map = {
        'inherited': 'inherited',
        'resource_uris': 'resourceUris'
    }

    def __init__(self, inherited=None, resource_uris=None, _configuration=None):  # noqa: E501
        """AtmSelectionSettings - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._inherited = None
        self._resource_uris = None
        self.discriminator = None

        if inherited is not None:
            self.inherited = inherited
        if resource_uris is not None:
            self.resource_uris = resource_uris

    @property
    def inherited(self):
        """Gets the inherited of this AtmSelectionSettings.  # noqa: E501

        If this token manager has a parent, this flag determines whether selection settings, such as resource URI's, are inherited from the parent. When set to true, the other fields in this model become read-only. The default value is false.  # noqa: E501

        :return: The inherited of this AtmSelectionSettings.  # noqa: E501
        :rtype: bool
        """
        return self._inherited

    @inherited.setter
    def inherited(self, inherited):
        """Sets the inherited of this AtmSelectionSettings.

        If this token manager has a parent, this flag determines whether selection settings, such as resource URI's, are inherited from the parent. When set to true, the other fields in this model become read-only. The default value is false.  # noqa: E501

        :param inherited: The inherited of this AtmSelectionSettings.  # noqa: E501
        :type: bool
        """

        self._inherited = inherited

    @property
    def resource_uris(self):
        """Gets the resource_uris of this AtmSelectionSettings.  # noqa: E501

        The list of base resource URI's which map to this token manager. A resource URI, specified via the 'aud' parameter, can be used to select a specific token manager for an OAuth request.  # noqa: E501

        :return: The resource_uris of this AtmSelectionSettings.  # noqa: E501
        :rtype: list[str]
        """
        return self._resource_uris

    @resource_uris.setter
    def resource_uris(self, resource_uris):
        """Sets the resource_uris of this AtmSelectionSettings.

        The list of base resource URI's which map to this token manager. A resource URI, specified via the 'aud' parameter, can be used to select a specific token manager for an OAuth request.  # noqa: E501

        :param resource_uris: The resource_uris of this AtmSelectionSettings.  # noqa: E501
        :type: list[str]
        """

        self._resource_uris = resource_uris

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
        if issubclass(AtmSelectionSettings, dict):
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
        if not isinstance(other, AtmSelectionSettings):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AtmSelectionSettings):
            return True

        return self.to_dict() != other.to_dict()
