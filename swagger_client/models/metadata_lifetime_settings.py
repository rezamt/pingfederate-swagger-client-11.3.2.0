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


class MetadataLifetimeSettings(object):
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
        'cache_duration': 'int',
        'reload_delay': 'int'
    }

    attribute_map = {
        'cache_duration': 'cacheDuration',
        'reload_delay': 'reloadDelay'
    }

    def __init__(self, cache_duration=None, reload_delay=None, _configuration=None):  # noqa: E501
        """MetadataLifetimeSettings - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._cache_duration = None
        self._reload_delay = None
        self.discriminator = None

        if cache_duration is not None:
            self.cache_duration = cache_duration
        if reload_delay is not None:
            self.reload_delay = reload_delay

    @property
    def cache_duration(self):
        """Gets the cache_duration of this MetadataLifetimeSettings.  # noqa: E501

        This field adjusts the validity of your metadata in minutes. The default value is 1440 (1 day).  # noqa: E501

        :return: The cache_duration of this MetadataLifetimeSettings.  # noqa: E501
        :rtype: int
        """
        return self._cache_duration

    @cache_duration.setter
    def cache_duration(self, cache_duration):
        """Sets the cache_duration of this MetadataLifetimeSettings.

        This field adjusts the validity of your metadata in minutes. The default value is 1440 (1 day).  # noqa: E501

        :param cache_duration: The cache_duration of this MetadataLifetimeSettings.  # noqa: E501
        :type: int
        """

        self._cache_duration = cache_duration

    @property
    def reload_delay(self):
        """Gets the reload_delay of this MetadataLifetimeSettings.  # noqa: E501

        This field adjusts the frequency of automatic reloading of SAML metadata in minutes. The default value is 1440 (1 day).  # noqa: E501

        :return: The reload_delay of this MetadataLifetimeSettings.  # noqa: E501
        :rtype: int
        """
        return self._reload_delay

    @reload_delay.setter
    def reload_delay(self, reload_delay):
        """Sets the reload_delay of this MetadataLifetimeSettings.

        This field adjusts the frequency of automatic reloading of SAML metadata in minutes. The default value is 1440 (1 day).  # noqa: E501

        :param reload_delay: The reload_delay of this MetadataLifetimeSettings.  # noqa: E501
        :type: int
        """

        self._reload_delay = reload_delay

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
        if issubclass(MetadataLifetimeSettings, dict):
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
        if not isinstance(other, MetadataLifetimeSettings):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MetadataLifetimeSettings):
            return True

        return self.to_dict() != other.to_dict()
