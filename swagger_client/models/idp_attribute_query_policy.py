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


class IdpAttributeQueryPolicy(object):
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
        'require_signed_response': 'bool',
        'require_signed_assertion': 'bool',
        'require_encrypted_assertion': 'bool',
        'sign_attribute_query': 'bool',
        'encrypt_name_id': 'bool',
        'mask_attribute_values': 'bool'
    }

    attribute_map = {
        'require_signed_response': 'requireSignedResponse',
        'require_signed_assertion': 'requireSignedAssertion',
        'require_encrypted_assertion': 'requireEncryptedAssertion',
        'sign_attribute_query': 'signAttributeQuery',
        'encrypt_name_id': 'encryptNameId',
        'mask_attribute_values': 'maskAttributeValues'
    }

    def __init__(self, require_signed_response=None, require_signed_assertion=None, require_encrypted_assertion=None, sign_attribute_query=None, encrypt_name_id=None, mask_attribute_values=None, _configuration=None):  # noqa: E501
        """IdpAttributeQueryPolicy - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._require_signed_response = None
        self._require_signed_assertion = None
        self._require_encrypted_assertion = None
        self._sign_attribute_query = None
        self._encrypt_name_id = None
        self._mask_attribute_values = None
        self.discriminator = None

        if require_signed_response is not None:
            self.require_signed_response = require_signed_response
        if require_signed_assertion is not None:
            self.require_signed_assertion = require_signed_assertion
        if require_encrypted_assertion is not None:
            self.require_encrypted_assertion = require_encrypted_assertion
        if sign_attribute_query is not None:
            self.sign_attribute_query = sign_attribute_query
        if encrypt_name_id is not None:
            self.encrypt_name_id = encrypt_name_id
        if mask_attribute_values is not None:
            self.mask_attribute_values = mask_attribute_values

    @property
    def require_signed_response(self):
        """Gets the require_signed_response of this IdpAttributeQueryPolicy.  # noqa: E501

        Require signed response.  # noqa: E501

        :return: The require_signed_response of this IdpAttributeQueryPolicy.  # noqa: E501
        :rtype: bool
        """
        return self._require_signed_response

    @require_signed_response.setter
    def require_signed_response(self, require_signed_response):
        """Sets the require_signed_response of this IdpAttributeQueryPolicy.

        Require signed response.  # noqa: E501

        :param require_signed_response: The require_signed_response of this IdpAttributeQueryPolicy.  # noqa: E501
        :type: bool
        """

        self._require_signed_response = require_signed_response

    @property
    def require_signed_assertion(self):
        """Gets the require_signed_assertion of this IdpAttributeQueryPolicy.  # noqa: E501

        Require signed assertion.  # noqa: E501

        :return: The require_signed_assertion of this IdpAttributeQueryPolicy.  # noqa: E501
        :rtype: bool
        """
        return self._require_signed_assertion

    @require_signed_assertion.setter
    def require_signed_assertion(self, require_signed_assertion):
        """Sets the require_signed_assertion of this IdpAttributeQueryPolicy.

        Require signed assertion.  # noqa: E501

        :param require_signed_assertion: The require_signed_assertion of this IdpAttributeQueryPolicy.  # noqa: E501
        :type: bool
        """

        self._require_signed_assertion = require_signed_assertion

    @property
    def require_encrypted_assertion(self):
        """Gets the require_encrypted_assertion of this IdpAttributeQueryPolicy.  # noqa: E501

        Require encrypted assertion.  # noqa: E501

        :return: The require_encrypted_assertion of this IdpAttributeQueryPolicy.  # noqa: E501
        :rtype: bool
        """
        return self._require_encrypted_assertion

    @require_encrypted_assertion.setter
    def require_encrypted_assertion(self, require_encrypted_assertion):
        """Sets the require_encrypted_assertion of this IdpAttributeQueryPolicy.

        Require encrypted assertion.  # noqa: E501

        :param require_encrypted_assertion: The require_encrypted_assertion of this IdpAttributeQueryPolicy.  # noqa: E501
        :type: bool
        """

        self._require_encrypted_assertion = require_encrypted_assertion

    @property
    def sign_attribute_query(self):
        """Gets the sign_attribute_query of this IdpAttributeQueryPolicy.  # noqa: E501

        Sign the attribute query.  # noqa: E501

        :return: The sign_attribute_query of this IdpAttributeQueryPolicy.  # noqa: E501
        :rtype: bool
        """
        return self._sign_attribute_query

    @sign_attribute_query.setter
    def sign_attribute_query(self, sign_attribute_query):
        """Sets the sign_attribute_query of this IdpAttributeQueryPolicy.

        Sign the attribute query.  # noqa: E501

        :param sign_attribute_query: The sign_attribute_query of this IdpAttributeQueryPolicy.  # noqa: E501
        :type: bool
        """

        self._sign_attribute_query = sign_attribute_query

    @property
    def encrypt_name_id(self):
        """Gets the encrypt_name_id of this IdpAttributeQueryPolicy.  # noqa: E501

        Encrypt the name identifier.  # noqa: E501

        :return: The encrypt_name_id of this IdpAttributeQueryPolicy.  # noqa: E501
        :rtype: bool
        """
        return self._encrypt_name_id

    @encrypt_name_id.setter
    def encrypt_name_id(self, encrypt_name_id):
        """Sets the encrypt_name_id of this IdpAttributeQueryPolicy.

        Encrypt the name identifier.  # noqa: E501

        :param encrypt_name_id: The encrypt_name_id of this IdpAttributeQueryPolicy.  # noqa: E501
        :type: bool
        """

        self._encrypt_name_id = encrypt_name_id

    @property
    def mask_attribute_values(self):
        """Gets the mask_attribute_values of this IdpAttributeQueryPolicy.  # noqa: E501

        Mask attributes in log files.  # noqa: E501

        :return: The mask_attribute_values of this IdpAttributeQueryPolicy.  # noqa: E501
        :rtype: bool
        """
        return self._mask_attribute_values

    @mask_attribute_values.setter
    def mask_attribute_values(self, mask_attribute_values):
        """Sets the mask_attribute_values of this IdpAttributeQueryPolicy.

        Mask attributes in log files.  # noqa: E501

        :param mask_attribute_values: The mask_attribute_values of this IdpAttributeQueryPolicy.  # noqa: E501
        :type: bool
        """

        self._mask_attribute_values = mask_attribute_values

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
        if issubclass(IdpAttributeQueryPolicy, dict):
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
        if not isinstance(other, IdpAttributeQueryPolicy):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IdpAttributeQueryPolicy):
            return True

        return self.to_dict() != other.to_dict()