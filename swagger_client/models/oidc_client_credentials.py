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


class OIDCClientCredentials(object):
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
        'client_id': 'str',
        'client_secret': 'str',
        'encrypted_secret': 'str'
    }

    attribute_map = {
        'client_id': 'clientId',
        'client_secret': 'clientSecret',
        'encrypted_secret': 'encryptedSecret'
    }

    def __init__(self, client_id=None, client_secret=None, encrypted_secret=None, _configuration=None):  # noqa: E501
        """OIDCClientCredentials - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._client_id = None
        self._client_secret = None
        self._encrypted_secret = None
        self.discriminator = None

        self.client_id = client_id
        if client_secret is not None:
            self.client_secret = client_secret
        if encrypted_secret is not None:
            self.encrypted_secret = encrypted_secret

    @property
    def client_id(self):
        """Gets the client_id of this OIDCClientCredentials.  # noqa: E501

        The OpenID Connect client identitification.  # noqa: E501

        :return: The client_id of this OIDCClientCredentials.  # noqa: E501
        :rtype: str
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        """Sets the client_id of this OIDCClientCredentials.

        The OpenID Connect client identitification.  # noqa: E501

        :param client_id: The client_id of this OIDCClientCredentials.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and client_id is None:
            raise ValueError("Invalid value for `client_id`, must not be `None`")  # noqa: E501

        self._client_id = client_id

    @property
    def client_secret(self):
        """Gets the client_secret of this OIDCClientCredentials.  # noqa: E501

        The OpenID Connect client secret. To update the client secret, specify the plaintext value in this field.  This field will not be populated for GET requests.  # noqa: E501

        :return: The client_secret of this OIDCClientCredentials.  # noqa: E501
        :rtype: str
        """
        return self._client_secret

    @client_secret.setter
    def client_secret(self, client_secret):
        """Sets the client_secret of this OIDCClientCredentials.

        The OpenID Connect client secret. To update the client secret, specify the plaintext value in this field.  This field will not be populated for GET requests.  # noqa: E501

        :param client_secret: The client_secret of this OIDCClientCredentials.  # noqa: E501
        :type: str
        """

        self._client_secret = client_secret

    @property
    def encrypted_secret(self):
        """Gets the encrypted_secret of this OIDCClientCredentials.  # noqa: E501

        For GET requests, this field contains the encrypted client secret, if one exists.  For POST and PUT requests, if you wish to reuse the existing secret, this field should be passed back unchanged.  # noqa: E501

        :return: The encrypted_secret of this OIDCClientCredentials.  # noqa: E501
        :rtype: str
        """
        return self._encrypted_secret

    @encrypted_secret.setter
    def encrypted_secret(self, encrypted_secret):
        """Sets the encrypted_secret of this OIDCClientCredentials.

        For GET requests, this field contains the encrypted client secret, if one exists.  For POST and PUT requests, if you wish to reuse the existing secret, this field should be passed back unchanged.  # noqa: E501

        :param encrypted_secret: The encrypted_secret of this OIDCClientCredentials.  # noqa: E501
        :type: str
        """

        self._encrypted_secret = encrypted_secret

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
        if issubclass(OIDCClientCredentials, dict):
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
        if not isinstance(other, OIDCClientCredentials):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OIDCClientCredentials):
            return True

        return self.to_dict() != other.to_dict()