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


class AlternativeLoginHintTokenIssuer(object):
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
        'issuer': 'str',
        'jwks_url': 'str',
        'jwks': 'str'
    }

    attribute_map = {
        'issuer': 'issuer',
        'jwks_url': 'jwksURL',
        'jwks': 'jwks'
    }

    def __init__(self, issuer=None, jwks_url=None, jwks=None, _configuration=None):  # noqa: E501
        """AlternativeLoginHintTokenIssuer - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._issuer = None
        self._jwks_url = None
        self._jwks = None
        self.discriminator = None

        self.issuer = issuer
        if jwks_url is not None:
            self.jwks_url = jwks_url
        if jwks is not None:
            self.jwks = jwks

    @property
    def issuer(self):
        """Gets the issuer of this AlternativeLoginHintTokenIssuer.  # noqa: E501

        The issuer. Issuer is unique.  # noqa: E501

        :return: The issuer of this AlternativeLoginHintTokenIssuer.  # noqa: E501
        :rtype: str
        """
        return self._issuer

    @issuer.setter
    def issuer(self, issuer):
        """Sets the issuer of this AlternativeLoginHintTokenIssuer.

        The issuer. Issuer is unique.  # noqa: E501

        :param issuer: The issuer of this AlternativeLoginHintTokenIssuer.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and issuer is None:
            raise ValueError("Invalid value for `issuer`, must not be `None`")  # noqa: E501

        self._issuer = issuer

    @property
    def jwks_url(self):
        """Gets the jwks_url of this AlternativeLoginHintTokenIssuer.  # noqa: E501

        The JWKS URL.  # noqa: E501

        :return: The jwks_url of this AlternativeLoginHintTokenIssuer.  # noqa: E501
        :rtype: str
        """
        return self._jwks_url

    @jwks_url.setter
    def jwks_url(self, jwks_url):
        """Sets the jwks_url of this AlternativeLoginHintTokenIssuer.

        The JWKS URL.  # noqa: E501

        :param jwks_url: The jwks_url of this AlternativeLoginHintTokenIssuer.  # noqa: E501
        :type: str
        """

        self._jwks_url = jwks_url

    @property
    def jwks(self):
        """Gets the jwks of this AlternativeLoginHintTokenIssuer.  # noqa: E501

        The JWKS.  # noqa: E501

        :return: The jwks of this AlternativeLoginHintTokenIssuer.  # noqa: E501
        :rtype: str
        """
        return self._jwks

    @jwks.setter
    def jwks(self, jwks):
        """Sets the jwks of this AlternativeLoginHintTokenIssuer.

        The JWKS.  # noqa: E501

        :param jwks: The jwks of this AlternativeLoginHintTokenIssuer.  # noqa: E501
        :type: str
        """

        self._jwks = jwks

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
        if issubclass(AlternativeLoginHintTokenIssuer, dict):
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
        if not isinstance(other, AlternativeLoginHintTokenIssuer):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AlternativeLoginHintTokenIssuer):
            return True

        return self.to_dict() != other.to_dict()