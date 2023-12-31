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


class UsernamePasswordCredentials(object):
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
        'username': 'str',
        'password': 'str',
        'encrypted_password': 'str'
    }

    attribute_map = {
        'username': 'username',
        'password': 'password',
        'encrypted_password': 'encryptedPassword'
    }

    def __init__(self, username=None, password=None, encrypted_password=None, _configuration=None):  # noqa: E501
        """UsernamePasswordCredentials - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._username = None
        self._password = None
        self._encrypted_password = None
        self.discriminator = None

        if username is not None:
            self.username = username
        if password is not None:
            self.password = password
        if encrypted_password is not None:
            self.encrypted_password = encrypted_password

    @property
    def username(self):
        """Gets the username of this UsernamePasswordCredentials.  # noqa: E501

        The username.  # noqa: E501

        :return: The username of this UsernamePasswordCredentials.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this UsernamePasswordCredentials.

        The username.  # noqa: E501

        :param username: The username of this UsernamePasswordCredentials.  # noqa: E501
        :type: str
        """

        self._username = username

    @property
    def password(self):
        """Gets the password of this UsernamePasswordCredentials.  # noqa: E501

        User password.  To update the password, specify the plaintext value in this field.  This field will not be populated for GET requests.  # noqa: E501

        :return: The password of this UsernamePasswordCredentials.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this UsernamePasswordCredentials.

        User password.  To update the password, specify the plaintext value in this field.  This field will not be populated for GET requests.  # noqa: E501

        :param password: The password of this UsernamePasswordCredentials.  # noqa: E501
        :type: str
        """

        self._password = password

    @property
    def encrypted_password(self):
        """Gets the encrypted_password of this UsernamePasswordCredentials.  # noqa: E501

        For GET requests, this field contains the encrypted password, if one exists.  For POST and PUT requests, if you wish to reuse the existing password, this field should be passed back unchanged.  # noqa: E501

        :return: The encrypted_password of this UsernamePasswordCredentials.  # noqa: E501
        :rtype: str
        """
        return self._encrypted_password

    @encrypted_password.setter
    def encrypted_password(self, encrypted_password):
        """Sets the encrypted_password of this UsernamePasswordCredentials.

        For GET requests, this field contains the encrypted password, if one exists.  For POST and PUT requests, if you wish to reuse the existing password, this field should be passed back unchanged.  # noqa: E501

        :param encrypted_password: The encrypted_password of this UsernamePasswordCredentials.  # noqa: E501
        :type: str
        """

        self._encrypted_password = encrypted_password

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
        if issubclass(UsernamePasswordCredentials, dict):
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
        if not isinstance(other, UsernamePasswordCredentials):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UsernamePasswordCredentials):
            return True

        return self.to_dict() != other.to_dict()
