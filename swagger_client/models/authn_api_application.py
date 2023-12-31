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


class AuthnApiApplication(object):
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
        'id': 'str',
        'name': 'str',
        'url': 'str',
        'description': 'str',
        'additional_allowed_origins': 'list[str]',
        'client_for_redirectless_mode_ref': 'ResourceLink'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'url': 'url',
        'description': 'description',
        'additional_allowed_origins': 'additionalAllowedOrigins',
        'client_for_redirectless_mode_ref': 'clientForRedirectlessModeRef'
    }

    def __init__(self, id=None, name=None, url=None, description=None, additional_allowed_origins=None, client_for_redirectless_mode_ref=None, _configuration=None):  # noqa: E501
        """AuthnApiApplication - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._name = None
        self._url = None
        self._description = None
        self._additional_allowed_origins = None
        self._client_for_redirectless_mode_ref = None
        self.discriminator = None

        self.id = id
        self.name = name
        self.url = url
        if description is not None:
            self.description = description
        if additional_allowed_origins is not None:
            self.additional_allowed_origins = additional_allowed_origins
        if client_for_redirectless_mode_ref is not None:
            self.client_for_redirectless_mode_ref = client_for_redirectless_mode_ref

    @property
    def id(self):
        """Gets the id of this AuthnApiApplication.  # noqa: E501

        The persistent, unique ID for the Authentication API application. It can be any combination of [a-zA-Z0-9._-]. This property is system-assigned if not specified.  # noqa: E501

        :return: The id of this AuthnApiApplication.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AuthnApiApplication.

        The persistent, unique ID for the Authentication API application. It can be any combination of [a-zA-Z0-9._-]. This property is system-assigned if not specified.  # noqa: E501

        :param id: The id of this AuthnApiApplication.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def name(self):
        """Gets the name of this AuthnApiApplication.  # noqa: E501

        The Authentication API Application Name. Name must be unique.  # noqa: E501

        :return: The name of this AuthnApiApplication.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AuthnApiApplication.

        The Authentication API Application Name. Name must be unique.  # noqa: E501

        :param name: The name of this AuthnApiApplication.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def url(self):
        """Gets the url of this AuthnApiApplication.  # noqa: E501

        The Authentication API Application redirect URL.  # noqa: E501

        :return: The url of this AuthnApiApplication.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this AuthnApiApplication.

        The Authentication API Application redirect URL.  # noqa: E501

        :param url: The url of this AuthnApiApplication.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and url is None:
            raise ValueError("Invalid value for `url`, must not be `None`")  # noqa: E501

        self._url = url

    @property
    def description(self):
        """Gets the description of this AuthnApiApplication.  # noqa: E501

        The Authentication API Application description.  # noqa: E501

        :return: The description of this AuthnApiApplication.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this AuthnApiApplication.

        The Authentication API Application description.  # noqa: E501

        :param description: The description of this AuthnApiApplication.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def additional_allowed_origins(self):
        """Gets the additional_allowed_origins of this AuthnApiApplication.  # noqa: E501

        The domain in the redirect URL is always whitelisted. This field contains a list of additional allowed origin URL's for cross-origin resource sharing.  # noqa: E501

        :return: The additional_allowed_origins of this AuthnApiApplication.  # noqa: E501
        :rtype: list[str]
        """
        return self._additional_allowed_origins

    @additional_allowed_origins.setter
    def additional_allowed_origins(self, additional_allowed_origins):
        """Sets the additional_allowed_origins of this AuthnApiApplication.

        The domain in the redirect URL is always whitelisted. This field contains a list of additional allowed origin URL's for cross-origin resource sharing.  # noqa: E501

        :param additional_allowed_origins: The additional_allowed_origins of this AuthnApiApplication.  # noqa: E501
        :type: list[str]
        """

        self._additional_allowed_origins = additional_allowed_origins

    @property
    def client_for_redirectless_mode_ref(self):
        """Gets the client_for_redirectless_mode_ref of this AuthnApiApplication.  # noqa: E501

        The client this application must use if it invokes the authentication API in redirectless mode. No client may be specified if restrictAccessToRedirectlessMode is false under /authenticationApi/settings.  # noqa: E501

        :return: The client_for_redirectless_mode_ref of this AuthnApiApplication.  # noqa: E501
        :rtype: ResourceLink
        """
        return self._client_for_redirectless_mode_ref

    @client_for_redirectless_mode_ref.setter
    def client_for_redirectless_mode_ref(self, client_for_redirectless_mode_ref):
        """Sets the client_for_redirectless_mode_ref of this AuthnApiApplication.

        The client this application must use if it invokes the authentication API in redirectless mode. No client may be specified if restrictAccessToRedirectlessMode is false under /authenticationApi/settings.  # noqa: E501

        :param client_for_redirectless_mode_ref: The client_for_redirectless_mode_ref of this AuthnApiApplication.  # noqa: E501
        :type: ResourceLink
        """

        self._client_for_redirectless_mode_ref = client_for_redirectless_mode_ref

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
        if issubclass(AuthnApiApplication, dict):
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
        if not isinstance(other, AuthnApiApplication):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AuthnApiApplication):
            return True

        return self.to_dict() != other.to_dict()
