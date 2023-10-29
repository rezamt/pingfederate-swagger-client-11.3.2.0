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


class JdbcTagConfig(object):
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
        'connection_url': 'str',
        'tags': 'str',
        'default_source': 'bool'
    }

    attribute_map = {
        'connection_url': 'connectionUrl',
        'tags': 'tags',
        'default_source': 'defaultSource'
    }

    def __init__(self, connection_url=None, tags=None, default_source=None, _configuration=None):  # noqa: E501
        """JdbcTagConfig - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._connection_url = None
        self._tags = None
        self._default_source = None
        self.discriminator = None

        self.connection_url = connection_url
        if tags is not None:
            self.tags = tags
        if default_source is not None:
            self.default_source = default_source

    @property
    def connection_url(self):
        """Gets the connection_url of this JdbcTagConfig.  # noqa: E501

        The location of the JDBC database.   # noqa: E501

        :return: The connection_url of this JdbcTagConfig.  # noqa: E501
        :rtype: str
        """
        return self._connection_url

    @connection_url.setter
    def connection_url(self, connection_url):
        """Sets the connection_url of this JdbcTagConfig.

        The location of the JDBC database.   # noqa: E501

        :param connection_url: The connection_url of this JdbcTagConfig.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and connection_url is None:
            raise ValueError("Invalid value for `connection_url`, must not be `None`")  # noqa: E501

        self._connection_url = connection_url

    @property
    def tags(self):
        """Gets the tags of this JdbcTagConfig.  # noqa: E501

        Tags associated with the connection URL. At runtime, nodes will use the first JdbcTagConfig that has a tag that matches with node.tags in run.properties.  # noqa: E501

        :return: The tags of this JdbcTagConfig.  # noqa: E501
        :rtype: str
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this JdbcTagConfig.

        Tags associated with the connection URL. At runtime, nodes will use the first JdbcTagConfig that has a tag that matches with node.tags in run.properties.  # noqa: E501

        :param tags: The tags of this JdbcTagConfig.  # noqa: E501
        :type: str
        """

        self._tags = tags

    @property
    def default_source(self):
        """Gets the default_source of this JdbcTagConfig.  # noqa: E501

        Whether this is the default connection. Defaults to false if not specified.  # noqa: E501

        :return: The default_source of this JdbcTagConfig.  # noqa: E501
        :rtype: bool
        """
        return self._default_source

    @default_source.setter
    def default_source(self, default_source):
        """Sets the default_source of this JdbcTagConfig.

        Whether this is the default connection. Defaults to false if not specified.  # noqa: E501

        :param default_source: The default_source of this JdbcTagConfig.  # noqa: E501
        :type: bool
        """

        self._default_source = default_source

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
        if issubclass(JdbcTagConfig, dict):
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
        if not isinstance(other, JdbcTagConfig):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, JdbcTagConfig):
            return True

        return self.to_dict() != other.to_dict()
