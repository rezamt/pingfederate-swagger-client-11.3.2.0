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


class UrlWhitelistEntry(object):
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
        'valid_domain': 'str',
        'valid_path': 'str',
        'allow_query_and_fragment': 'bool',
        'require_https': 'bool'
    }

    attribute_map = {
        'valid_domain': 'validDomain',
        'valid_path': 'validPath',
        'allow_query_and_fragment': 'allowQueryAndFragment',
        'require_https': 'requireHttps'
    }

    def __init__(self, valid_domain=None, valid_path=None, allow_query_and_fragment=None, require_https=None, _configuration=None):  # noqa: E501
        """UrlWhitelistEntry - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._valid_domain = None
        self._valid_path = None
        self._allow_query_and_fragment = None
        self._require_https = None
        self.discriminator = None

        if valid_domain is not None:
            self.valid_domain = valid_domain
        if valid_path is not None:
            self.valid_path = valid_path
        if allow_query_and_fragment is not None:
            self.allow_query_and_fragment = allow_query_and_fragment
        if require_https is not None:
            self.require_https = require_https

    @property
    def valid_domain(self):
        """Gets the valid_domain of this UrlWhitelistEntry.  # noqa: E501

        Valid Domain Name (leading wildcard '*.' allowed)  # noqa: E501

        :return: The valid_domain of this UrlWhitelistEntry.  # noqa: E501
        :rtype: str
        """
        return self._valid_domain

    @valid_domain.setter
    def valid_domain(self, valid_domain):
        """Sets the valid_domain of this UrlWhitelistEntry.

        Valid Domain Name (leading wildcard '*.' allowed)  # noqa: E501

        :param valid_domain: The valid_domain of this UrlWhitelistEntry.  # noqa: E501
        :type: str
        """

        self._valid_domain = valid_domain

    @property
    def valid_path(self):
        """Gets the valid_path of this UrlWhitelistEntry.  # noqa: E501

        Valid Path (leave blank to allow any path)  # noqa: E501

        :return: The valid_path of this UrlWhitelistEntry.  # noqa: E501
        :rtype: str
        """
        return self._valid_path

    @valid_path.setter
    def valid_path(self, valid_path):
        """Sets the valid_path of this UrlWhitelistEntry.

        Valid Path (leave blank to allow any path)  # noqa: E501

        :param valid_path: The valid_path of this UrlWhitelistEntry.  # noqa: E501
        :type: str
        """

        self._valid_path = valid_path

    @property
    def allow_query_and_fragment(self):
        """Gets the allow_query_and_fragment of this UrlWhitelistEntry.  # noqa: E501

        Allow Any Query/Fragment  # noqa: E501

        :return: The allow_query_and_fragment of this UrlWhitelistEntry.  # noqa: E501
        :rtype: bool
        """
        return self._allow_query_and_fragment

    @allow_query_and_fragment.setter
    def allow_query_and_fragment(self, allow_query_and_fragment):
        """Sets the allow_query_and_fragment of this UrlWhitelistEntry.

        Allow Any Query/Fragment  # noqa: E501

        :param allow_query_and_fragment: The allow_query_and_fragment of this UrlWhitelistEntry.  # noqa: E501
        :type: bool
        """

        self._allow_query_and_fragment = allow_query_and_fragment

    @property
    def require_https(self):
        """Gets the require_https of this UrlWhitelistEntry.  # noqa: E501

        Require HTTPS  # noqa: E501

        :return: The require_https of this UrlWhitelistEntry.  # noqa: E501
        :rtype: bool
        """
        return self._require_https

    @require_https.setter
    def require_https(self, require_https):
        """Sets the require_https of this UrlWhitelistEntry.

        Require HTTPS  # noqa: E501

        :param require_https: The require_https of this UrlWhitelistEntry.  # noqa: E501
        :type: bool
        """

        self._require_https = require_https

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
        if issubclass(UrlWhitelistEntry, dict):
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
        if not isinstance(other, UrlWhitelistEntry):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UrlWhitelistEntry):
            return True

        return self.to_dict() != other.to_dict()
