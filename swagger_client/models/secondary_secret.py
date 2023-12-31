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


class SecondarySecret(object):
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
        'secret': 'str',
        'encrypted_secret': 'str',
        'expiry_time': 'datetime'
    }

    attribute_map = {
        'secret': 'secret',
        'encrypted_secret': 'encryptedSecret',
        'expiry_time': 'expiryTime'
    }

    def __init__(self, secret=None, encrypted_secret=None, expiry_time=None, _configuration=None):  # noqa: E501
        """SecondarySecret - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._secret = None
        self._encrypted_secret = None
        self._expiry_time = None
        self.discriminator = None

        if secret is not None:
            self.secret = secret
        if encrypted_secret is not None:
            self.encrypted_secret = encrypted_secret
        if expiry_time is not None:
            self.expiry_time = expiry_time

    @property
    def secret(self):
        """Gets the secret of this SecondarySecret.  # noqa: E501

        Secondary client secret for Basic Authentication.  To update the secondary client secret, specify the plaintext value in this field.  This field will not be populated for GET requests.  # noqa: E501

        :return: The secret of this SecondarySecret.  # noqa: E501
        :rtype: str
        """
        return self._secret

    @secret.setter
    def secret(self, secret):
        """Sets the secret of this SecondarySecret.

        Secondary client secret for Basic Authentication.  To update the secondary client secret, specify the plaintext value in this field.  This field will not be populated for GET requests.  # noqa: E501

        :param secret: The secret of this SecondarySecret.  # noqa: E501
        :type: str
        """

        self._secret = secret

    @property
    def encrypted_secret(self):
        """Gets the encrypted_secret of this SecondarySecret.  # noqa: E501

        For GET requests, this field contains the encrypted secondary client secret, if one exists.  For POST and PUT requests, if you wish to reuse the existing secret, this field should be passed back unchanged.  # noqa: E501

        :return: The encrypted_secret of this SecondarySecret.  # noqa: E501
        :rtype: str
        """
        return self._encrypted_secret

    @encrypted_secret.setter
    def encrypted_secret(self, encrypted_secret):
        """Sets the encrypted_secret of this SecondarySecret.

        For GET requests, this field contains the encrypted secondary client secret, if one exists.  For POST and PUT requests, if you wish to reuse the existing secret, this field should be passed back unchanged.  # noqa: E501

        :param encrypted_secret: The encrypted_secret of this SecondarySecret.  # noqa: E501
        :type: str
        """

        self._encrypted_secret = encrypted_secret

    @property
    def expiry_time(self):
        """Gets the expiry_time of this SecondarySecret.  # noqa: E501

        The expiry time of the secondary secret.  # noqa: E501

        :return: The expiry_time of this SecondarySecret.  # noqa: E501
        :rtype: datetime
        """
        return self._expiry_time

    @expiry_time.setter
    def expiry_time(self, expiry_time):
        """Sets the expiry_time of this SecondarySecret.

        The expiry time of the secondary secret.  # noqa: E501

        :param expiry_time: The expiry_time of this SecondarySecret.  # noqa: E501
        :type: datetime
        """

        self._expiry_time = expiry_time

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
        if issubclass(SecondarySecret, dict):
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
        if not isinstance(other, SecondarySecret):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SecondarySecret):
            return True

        return self.to_dict() != other.to_dict()
