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


class ArtifactSettings(object):
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
        'lifetime': 'int',
        'resolver_locations': 'list[ArtifactResolverLocation]',
        'source_id': 'str'
    }

    attribute_map = {
        'lifetime': 'lifetime',
        'resolver_locations': 'resolverLocations',
        'source_id': 'sourceId'
    }

    def __init__(self, lifetime=None, resolver_locations=None, source_id=None, _configuration=None):  # noqa: E501
        """ArtifactSettings - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._lifetime = None
        self._resolver_locations = None
        self._source_id = None
        self.discriminator = None

        self.lifetime = lifetime
        self.resolver_locations = resolver_locations
        if source_id is not None:
            self.source_id = source_id

    @property
    def lifetime(self):
        """Gets the lifetime of this ArtifactSettings.  # noqa: E501

        The lifetime of the artifact in seconds.  # noqa: E501

        :return: The lifetime of this ArtifactSettings.  # noqa: E501
        :rtype: int
        """
        return self._lifetime

    @lifetime.setter
    def lifetime(self, lifetime):
        """Sets the lifetime of this ArtifactSettings.

        The lifetime of the artifact in seconds.  # noqa: E501

        :param lifetime: The lifetime of this ArtifactSettings.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and lifetime is None:
            raise ValueError("Invalid value for `lifetime`, must not be `None`")  # noqa: E501

        self._lifetime = lifetime

    @property
    def resolver_locations(self):
        """Gets the resolver_locations of this ArtifactSettings.  # noqa: E501

        Remote party URLs that you will use to resolve/translate the artifact and get the actual protocol message  # noqa: E501

        :return: The resolver_locations of this ArtifactSettings.  # noqa: E501
        :rtype: list[ArtifactResolverLocation]
        """
        return self._resolver_locations

    @resolver_locations.setter
    def resolver_locations(self, resolver_locations):
        """Sets the resolver_locations of this ArtifactSettings.

        Remote party URLs that you will use to resolve/translate the artifact and get the actual protocol message  # noqa: E501

        :param resolver_locations: The resolver_locations of this ArtifactSettings.  # noqa: E501
        :type: list[ArtifactResolverLocation]
        """
        if self._configuration.client_side_validation and resolver_locations is None:
            raise ValueError("Invalid value for `resolver_locations`, must not be `None`")  # noqa: E501

        self._resolver_locations = resolver_locations

    @property
    def source_id(self):
        """Gets the source_id of this ArtifactSettings.  # noqa: E501

        Source ID for SAML1.x connections  # noqa: E501

        :return: The source_id of this ArtifactSettings.  # noqa: E501
        :rtype: str
        """
        return self._source_id

    @source_id.setter
    def source_id(self, source_id):
        """Sets the source_id of this ArtifactSettings.

        Source ID for SAML1.x connections  # noqa: E501

        :param source_id: The source_id of this ArtifactSettings.  # noqa: E501
        :type: str
        """

        self._source_id = source_id

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
        if issubclass(ArtifactSettings, dict):
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
        if not isinstance(other, ArtifactSettings):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ArtifactSettings):
            return True

        return self.to_dict() != other.to_dict()
