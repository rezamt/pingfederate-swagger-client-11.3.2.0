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


class ConvertMetadataResponse(object):
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
        'signature_status': 'str',
        'cert_trust_status': 'str',
        'cert_subject_dn': 'str',
        'cert_serial_number': 'str',
        'cert_expiration': 'datetime',
        'connection': 'Connection'
    }

    attribute_map = {
        'signature_status': 'signatureStatus',
        'cert_trust_status': 'certTrustStatus',
        'cert_subject_dn': 'certSubjectDn',
        'cert_serial_number': 'certSerialNumber',
        'cert_expiration': 'certExpiration',
        'connection': 'connection'
    }

    def __init__(self, signature_status=None, cert_trust_status=None, cert_subject_dn=None, cert_serial_number=None, cert_expiration=None, connection=None, _configuration=None):  # noqa: E501
        """ConvertMetadataResponse - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._signature_status = None
        self._cert_trust_status = None
        self._cert_subject_dn = None
        self._cert_serial_number = None
        self._cert_expiration = None
        self._connection = None
        self.discriminator = None

        if signature_status is not None:
            self.signature_status = signature_status
        if cert_trust_status is not None:
            self.cert_trust_status = cert_trust_status
        if cert_subject_dn is not None:
            self.cert_subject_dn = cert_subject_dn
        if cert_serial_number is not None:
            self.cert_serial_number = cert_serial_number
        if cert_expiration is not None:
            self.cert_expiration = cert_expiration
        if connection is not None:
            self.connection = connection

    @property
    def signature_status(self):
        """Gets the signature_status of this ConvertMetadataResponse.  # noqa: E501

        The metadata's digital signature status.  # noqa: E501

        :return: The signature_status of this ConvertMetadataResponse.  # noqa: E501
        :rtype: str
        """
        return self._signature_status

    @signature_status.setter
    def signature_status(self, signature_status):
        """Sets the signature_status of this ConvertMetadataResponse.

        The metadata's digital signature status.  # noqa: E501

        :param signature_status: The signature_status of this ConvertMetadataResponse.  # noqa: E501
        :type: str
        """
        allowed_values = ["SIGNED", "UNSIGNED"]  # noqa: E501
        if (self._configuration.client_side_validation and
                signature_status not in allowed_values):
            raise ValueError(
                "Invalid value for `signature_status` ({0}), must be one of {1}"  # noqa: E501
                .format(signature_status, allowed_values)
            )

        self._signature_status = signature_status

    @property
    def cert_trust_status(self):
        """Gets the cert_trust_status of this ConvertMetadataResponse.  # noqa: E501

        The metadata certificate's trust status, i.e. If the partner's certificate can be trusted or not.  # noqa: E501

        :return: The cert_trust_status of this ConvertMetadataResponse.  # noqa: E501
        :rtype: str
        """
        return self._cert_trust_status

    @cert_trust_status.setter
    def cert_trust_status(self, cert_trust_status):
        """Sets the cert_trust_status of this ConvertMetadataResponse.

        The metadata certificate's trust status, i.e. If the partner's certificate can be trusted or not.  # noqa: E501

        :param cert_trust_status: The cert_trust_status of this ConvertMetadataResponse.  # noqa: E501
        :type: str
        """
        allowed_values = ["TRUSTED", "NOT_TRUSTED"]  # noqa: E501
        if (self._configuration.client_side_validation and
                cert_trust_status not in allowed_values):
            raise ValueError(
                "Invalid value for `cert_trust_status` ({0}), must be one of {1}"  # noqa: E501
                .format(cert_trust_status, allowed_values)
            )

        self._cert_trust_status = cert_trust_status

    @property
    def cert_subject_dn(self):
        """Gets the cert_subject_dn of this ConvertMetadataResponse.  # noqa: E501

        The metadata certificate's subject DN.  # noqa: E501

        :return: The cert_subject_dn of this ConvertMetadataResponse.  # noqa: E501
        :rtype: str
        """
        return self._cert_subject_dn

    @cert_subject_dn.setter
    def cert_subject_dn(self, cert_subject_dn):
        """Sets the cert_subject_dn of this ConvertMetadataResponse.

        The metadata certificate's subject DN.  # noqa: E501

        :param cert_subject_dn: The cert_subject_dn of this ConvertMetadataResponse.  # noqa: E501
        :type: str
        """

        self._cert_subject_dn = cert_subject_dn

    @property
    def cert_serial_number(self):
        """Gets the cert_serial_number of this ConvertMetadataResponse.  # noqa: E501

        The metadata certificate's serial number.  # noqa: E501

        :return: The cert_serial_number of this ConvertMetadataResponse.  # noqa: E501
        :rtype: str
        """
        return self._cert_serial_number

    @cert_serial_number.setter
    def cert_serial_number(self, cert_serial_number):
        """Sets the cert_serial_number of this ConvertMetadataResponse.

        The metadata certificate's serial number.  # noqa: E501

        :param cert_serial_number: The cert_serial_number of this ConvertMetadataResponse.  # noqa: E501
        :type: str
        """

        self._cert_serial_number = cert_serial_number

    @property
    def cert_expiration(self):
        """Gets the cert_expiration of this ConvertMetadataResponse.  # noqa: E501

        The metadata certificate's expiry date.  # noqa: E501

        :return: The cert_expiration of this ConvertMetadataResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._cert_expiration

    @cert_expiration.setter
    def cert_expiration(self, cert_expiration):
        """Sets the cert_expiration of this ConvertMetadataResponse.

        The metadata certificate's expiry date.  # noqa: E501

        :param cert_expiration: The cert_expiration of this ConvertMetadataResponse.  # noqa: E501
        :type: datetime
        """

        self._cert_expiration = cert_expiration

    @property
    def connection(self):
        """Gets the connection of this ConvertMetadataResponse.  # noqa: E501

        The converted API connection.  # noqa: E501

        :return: The connection of this ConvertMetadataResponse.  # noqa: E501
        :rtype: Connection
        """
        return self._connection

    @connection.setter
    def connection(self, connection):
        """Sets the connection of this ConvertMetadataResponse.

        The converted API connection.  # noqa: E501

        :param connection: The connection of this ConvertMetadataResponse.  # noqa: E501
        :type: Connection
        """

        self._connection = connection

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
        if issubclass(ConvertMetadataResponse, dict):
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
        if not isinstance(other, ConvertMetadataResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ConvertMetadataResponse):
            return True

        return self.to_dict() != other.to_dict()
