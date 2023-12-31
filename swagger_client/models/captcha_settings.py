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


class CaptchaSettings(object):
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
        'site_key': 'str',
        'secret_key': 'str',
        'encrypted_secret_key': 'str'
    }

    attribute_map = {
        'site_key': 'siteKey',
        'secret_key': 'secretKey',
        'encrypted_secret_key': 'encryptedSecretKey'
    }

    def __init__(self, site_key=None, secret_key=None, encrypted_secret_key=None, _configuration=None):  # noqa: E501
        """CaptchaSettings - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._site_key = None
        self._secret_key = None
        self._encrypted_secret_key = None
        self.discriminator = None

        if site_key is not None:
            self.site_key = site_key
        if secret_key is not None:
            self.secret_key = secret_key
        if encrypted_secret_key is not None:
            self.encrypted_secret_key = encrypted_secret_key

    @property
    def site_key(self):
        """Gets the site_key of this CaptchaSettings.  # noqa: E501

        Site key for reCAPTCHA.  # noqa: E501

        :return: The site_key of this CaptchaSettings.  # noqa: E501
        :rtype: str
        """
        return self._site_key

    @site_key.setter
    def site_key(self, site_key):
        """Sets the site_key of this CaptchaSettings.

        Site key for reCAPTCHA.  # noqa: E501

        :param site_key: The site_key of this CaptchaSettings.  # noqa: E501
        :type: str
        """

        self._site_key = site_key

    @property
    def secret_key(self):
        """Gets the secret_key of this CaptchaSettings.  # noqa: E501

        Secret key for reCAPTCHA. GETs will not return this attribute. To update this field, specify the new value in this attribute.  # noqa: E501

        :return: The secret_key of this CaptchaSettings.  # noqa: E501
        :rtype: str
        """
        return self._secret_key

    @secret_key.setter
    def secret_key(self, secret_key):
        """Sets the secret_key of this CaptchaSettings.

        Secret key for reCAPTCHA. GETs will not return this attribute. To update this field, specify the new value in this attribute.  # noqa: E501

        :param secret_key: The secret_key of this CaptchaSettings.  # noqa: E501
        :type: str
        """

        self._secret_key = secret_key

    @property
    def encrypted_secret_key(self):
        """Gets the encrypted_secret_key of this CaptchaSettings.  # noqa: E501

        The encrypted secret key for reCAPTCHA. If you do not want to update the stored value, this attribute should be passed back unchanged.  # noqa: E501

        :return: The encrypted_secret_key of this CaptchaSettings.  # noqa: E501
        :rtype: str
        """
        return self._encrypted_secret_key

    @encrypted_secret_key.setter
    def encrypted_secret_key(self, encrypted_secret_key):
        """Sets the encrypted_secret_key of this CaptchaSettings.

        The encrypted secret key for reCAPTCHA. If you do not want to update the stored value, this attribute should be passed back unchanged.  # noqa: E501

        :param encrypted_secret_key: The encrypted_secret_key of this CaptchaSettings.  # noqa: E501
        :type: str
        """

        self._encrypted_secret_key = encrypted_secret_key

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
        if issubclass(CaptchaSettings, dict):
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
        if not isinstance(other, CaptchaSettings):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CaptchaSettings):
            return True

        return self.to_dict() != other.to_dict()
