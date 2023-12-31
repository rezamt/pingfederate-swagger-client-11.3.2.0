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


class ServiceAssociation(object):
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
        'component_name': 'str',
        'service_names': 'list[str]',
        'configured': 'bool'
    }

    attribute_map = {
        'component_name': 'componentName',
        'service_names': 'serviceNames',
        'configured': 'configured'
    }

    def __init__(self, component_name=None, service_names=None, configured=None, _configuration=None):  # noqa: E501
        """ServiceAssociation - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._component_name = None
        self._service_names = None
        self._configured = None
        self.discriminator = None

        if component_name is not None:
            self.component_name = component_name
        if service_names is not None:
            self.service_names = service_names
        if configured is not None:
            self.configured = configured

    @property
    def component_name(self):
        """Gets the component_name of this ServiceAssociation.  # noqa: E501

        The display name for the component.  # noqa: E501

        :return: The component_name of this ServiceAssociation.  # noqa: E501
        :rtype: str
        """
        return self._component_name

    @component_name.setter
    def component_name(self, component_name):
        """Sets the component_name of this ServiceAssociation.

        The display name for the component.  # noqa: E501

        :param component_name: The component_name of this ServiceAssociation.  # noqa: E501
        :type: str
        """

        self._component_name = component_name

    @property
    def service_names(self):
        """Gets the service_names of this ServiceAssociation.  # noqa: E501

        The list of PingOne services consumed by the plugin. The first service represents the primary service consumed by the plugin.  # noqa: E501

        :return: The service_names of this ServiceAssociation.  # noqa: E501
        :rtype: list[str]
        """
        return self._service_names

    @service_names.setter
    def service_names(self, service_names):
        """Sets the service_names of this ServiceAssociation.

        The list of PingOne services consumed by the plugin. The first service represents the primary service consumed by the plugin.  # noqa: E501

        :param service_names: The service_names of this ServiceAssociation.  # noqa: E501
        :type: list[str]
        """

        self._service_names = service_names

    @property
    def configured(self):
        """Gets the configured of this ServiceAssociation.  # noqa: E501

        Indicates whether one or more instances of the plugin are configured for a given PingOne connection.  # noqa: E501

        :return: The configured of this ServiceAssociation.  # noqa: E501
        :rtype: bool
        """
        return self._configured

    @configured.setter
    def configured(self, configured):
        """Sets the configured of this ServiceAssociation.

        Indicates whether one or more instances of the plugin are configured for a given PingOne connection.  # noqa: E501

        :param configured: The configured of this ServiceAssociation.  # noqa: E501
        :type: bool
        """

        self._configured = configured

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
        if issubclass(ServiceAssociation, dict):
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
        if not isinstance(other, ServiceAssociation):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ServiceAssociation):
            return True

        return self.to_dict() != other.to_dict()
