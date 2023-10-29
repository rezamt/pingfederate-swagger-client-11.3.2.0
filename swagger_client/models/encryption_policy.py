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


class EncryptionPolicy(object):
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
        'encrypt_assertion': 'bool',
        'encrypted_attributes': 'list[str]',
        'encrypt_slo_subject_name_id': 'bool',
        'slo_subject_name_id_encrypted': 'bool'
    }

    attribute_map = {
        'encrypt_assertion': 'encryptAssertion',
        'encrypted_attributes': 'encryptedAttributes',
        'encrypt_slo_subject_name_id': 'encryptSloSubjectNameId',
        'slo_subject_name_id_encrypted': 'sloSubjectNameIDEncrypted'
    }

    def __init__(self, encrypt_assertion=None, encrypted_attributes=None, encrypt_slo_subject_name_id=None, slo_subject_name_id_encrypted=None, _configuration=None):  # noqa: E501
        """EncryptionPolicy - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._encrypt_assertion = None
        self._encrypted_attributes = None
        self._encrypt_slo_subject_name_id = None
        self._slo_subject_name_id_encrypted = None
        self.discriminator = None

        if encrypt_assertion is not None:
            self.encrypt_assertion = encrypt_assertion
        if encrypted_attributes is not None:
            self.encrypted_attributes = encrypted_attributes
        if encrypt_slo_subject_name_id is not None:
            self.encrypt_slo_subject_name_id = encrypt_slo_subject_name_id
        if slo_subject_name_id_encrypted is not None:
            self.slo_subject_name_id_encrypted = slo_subject_name_id_encrypted

    @property
    def encrypt_assertion(self):
        """Gets the encrypt_assertion of this EncryptionPolicy.  # noqa: E501

        Whether the outgoing SAML assertion will be encrypted.  # noqa: E501

        :return: The encrypt_assertion of this EncryptionPolicy.  # noqa: E501
        :rtype: bool
        """
        return self._encrypt_assertion

    @encrypt_assertion.setter
    def encrypt_assertion(self, encrypt_assertion):
        """Sets the encrypt_assertion of this EncryptionPolicy.

        Whether the outgoing SAML assertion will be encrypted.  # noqa: E501

        :param encrypt_assertion: The encrypt_assertion of this EncryptionPolicy.  # noqa: E501
        :type: bool
        """

        self._encrypt_assertion = encrypt_assertion

    @property
    def encrypted_attributes(self):
        """Gets the encrypted_attributes of this EncryptionPolicy.  # noqa: E501

        The list of outgoing SAML assertion attributes that will be encrypted. The 'encryptAssertion' property takes precedence over this.  # noqa: E501

        :return: The encrypted_attributes of this EncryptionPolicy.  # noqa: E501
        :rtype: list[str]
        """
        return self._encrypted_attributes

    @encrypted_attributes.setter
    def encrypted_attributes(self, encrypted_attributes):
        """Sets the encrypted_attributes of this EncryptionPolicy.

        The list of outgoing SAML assertion attributes that will be encrypted. The 'encryptAssertion' property takes precedence over this.  # noqa: E501

        :param encrypted_attributes: The encrypted_attributes of this EncryptionPolicy.  # noqa: E501
        :type: list[str]
        """

        self._encrypted_attributes = encrypted_attributes

    @property
    def encrypt_slo_subject_name_id(self):
        """Gets the encrypt_slo_subject_name_id of this EncryptionPolicy.  # noqa: E501

        Encrypt the name-identifier attribute in outbound SLO messages.  This can be set if the name id is encrypted.  # noqa: E501

        :return: The encrypt_slo_subject_name_id of this EncryptionPolicy.  # noqa: E501
        :rtype: bool
        """
        return self._encrypt_slo_subject_name_id

    @encrypt_slo_subject_name_id.setter
    def encrypt_slo_subject_name_id(self, encrypt_slo_subject_name_id):
        """Sets the encrypt_slo_subject_name_id of this EncryptionPolicy.

        Encrypt the name-identifier attribute in outbound SLO messages.  This can be set if the name id is encrypted.  # noqa: E501

        :param encrypt_slo_subject_name_id: The encrypt_slo_subject_name_id of this EncryptionPolicy.  # noqa: E501
        :type: bool
        """

        self._encrypt_slo_subject_name_id = encrypt_slo_subject_name_id

    @property
    def slo_subject_name_id_encrypted(self):
        """Gets the slo_subject_name_id_encrypted of this EncryptionPolicy.  # noqa: E501

        Allow the encryption of the name-identifier attribute for inbound SLO messages. This can be set if SP initiated SLO is enabled.  # noqa: E501

        :return: The slo_subject_name_id_encrypted of this EncryptionPolicy.  # noqa: E501
        :rtype: bool
        """
        return self._slo_subject_name_id_encrypted

    @slo_subject_name_id_encrypted.setter
    def slo_subject_name_id_encrypted(self, slo_subject_name_id_encrypted):
        """Sets the slo_subject_name_id_encrypted of this EncryptionPolicy.

        Allow the encryption of the name-identifier attribute for inbound SLO messages. This can be set if SP initiated SLO is enabled.  # noqa: E501

        :param slo_subject_name_id_encrypted: The slo_subject_name_id_encrypted of this EncryptionPolicy.  # noqa: E501
        :type: bool
        """

        self._slo_subject_name_id_encrypted = slo_subject_name_id_encrypted

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
        if issubclass(EncryptionPolicy, dict):
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
        if not isinstance(other, EncryptionPolicy):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EncryptionPolicy):
            return True

        return self.to_dict() != other.to_dict()
