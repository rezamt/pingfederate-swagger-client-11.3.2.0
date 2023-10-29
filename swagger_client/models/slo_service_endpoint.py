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


class SloServiceEndpoint(object):
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
        'binding': 'str',
        'url': 'str',
        'response_url': 'str'
    }

    attribute_map = {
        'binding': 'binding',
        'url': 'url',
        'response_url': 'responseUrl'
    }

    def __init__(self, binding=None, url=None, response_url=None, _configuration=None):  # noqa: E501
        """SloServiceEndpoint - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._binding = None
        self._url = None
        self._response_url = None
        self.discriminator = None

        self.binding = binding
        self.url = url
        if response_url is not None:
            self.response_url = response_url

    @property
    def binding(self):
        """Gets the binding of this SloServiceEndpoint.  # noqa: E501

        The binding of this endpoint, if applicable - usually only required for SAML 2.0 endpoints.  # noqa: E501

        :return: The binding of this SloServiceEndpoint.  # noqa: E501
        :rtype: str
        """
        return self._binding

    @binding.setter
    def binding(self, binding):
        """Sets the binding of this SloServiceEndpoint.

        The binding of this endpoint, if applicable - usually only required for SAML 2.0 endpoints.  # noqa: E501

        :param binding: The binding of this SloServiceEndpoint.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and binding is None:
            raise ValueError("Invalid value for `binding`, must not be `None`")  # noqa: E501
        allowed_values = ["ARTIFACT", "POST", "REDIRECT", "SOAP"]  # noqa: E501
        if (self._configuration.client_side_validation and
                binding not in allowed_values):
            raise ValueError(
                "Invalid value for `binding` ({0}), must be one of {1}"  # noqa: E501
                .format(binding, allowed_values)
            )

        self._binding = binding

    @property
    def url(self):
        """Gets the url of this SloServiceEndpoint.  # noqa: E501

        The absolute or relative URL of the endpoint. A relative URL can be specified if a base URL for the connection has been defined.  # noqa: E501

        :return: The url of this SloServiceEndpoint.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this SloServiceEndpoint.

        The absolute or relative URL of the endpoint. A relative URL can be specified if a base URL for the connection has been defined.  # noqa: E501

        :param url: The url of this SloServiceEndpoint.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and url is None:
            raise ValueError("Invalid value for `url`, must not be `None`")  # noqa: E501

        self._url = url

    @property
    def response_url(self):
        """Gets the response_url of this SloServiceEndpoint.  # noqa: E501

        The absolute or relative URL to which logout responses are sent. A relative URL can be specified if a base URL for the connection has been defined.  # noqa: E501

        :return: The response_url of this SloServiceEndpoint.  # noqa: E501
        :rtype: str
        """
        return self._response_url

    @response_url.setter
    def response_url(self, response_url):
        """Sets the response_url of this SloServiceEndpoint.

        The absolute or relative URL to which logout responses are sent. A relative URL can be specified if a base URL for the connection has been defined.  # noqa: E501

        :param response_url: The response_url of this SloServiceEndpoint.  # noqa: E501
        :type: str
        """

        self._response_url = response_url

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
        if issubclass(SloServiceEndpoint, dict):
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
        if not isinstance(other, SloServiceEndpoint):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SloServiceEndpoint):
            return True

        return self.to_dict() != other.to_dict()