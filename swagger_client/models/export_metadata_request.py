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


class ExportMetadataRequest(object):
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
        'connection_type': 'str',
        'connection_id': 'str',
        'virtual_server_id': 'str',
        'signing_settings': 'BaseSigningSettings',
        'use_secondary_port_for_soap': 'bool',
        'virtual_host_name': 'str'
    }

    attribute_map = {
        'connection_type': 'connectionType',
        'connection_id': 'connectionId',
        'virtual_server_id': 'virtualServerId',
        'signing_settings': 'signingSettings',
        'use_secondary_port_for_soap': 'useSecondaryPortForSoap',
        'virtual_host_name': 'virtualHostName'
    }

    def __init__(self, connection_type=None, connection_id=None, virtual_server_id=None, signing_settings=None, use_secondary_port_for_soap=None, virtual_host_name=None, _configuration=None):  # noqa: E501
        """ExportMetadataRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._connection_type = None
        self._connection_id = None
        self._virtual_server_id = None
        self._signing_settings = None
        self._use_secondary_port_for_soap = None
        self._virtual_host_name = None
        self.discriminator = None

        self.connection_type = connection_type
        self.connection_id = connection_id
        if virtual_server_id is not None:
            self.virtual_server_id = virtual_server_id
        if signing_settings is not None:
            self.signing_settings = signing_settings
        if use_secondary_port_for_soap is not None:
            self.use_secondary_port_for_soap = use_secondary_port_for_soap
        if virtual_host_name is not None:
            self.virtual_host_name = virtual_host_name

    @property
    def connection_type(self):
        """Gets the connection_type of this ExportMetadataRequest.  # noqa: E501

        The type of connection to export.  # noqa: E501

        :return: The connection_type of this ExportMetadataRequest.  # noqa: E501
        :rtype: str
        """
        return self._connection_type

    @connection_type.setter
    def connection_type(self, connection_type):
        """Sets the connection_type of this ExportMetadataRequest.

        The type of connection to export.  # noqa: E501

        :param connection_type: The connection_type of this ExportMetadataRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and connection_type is None:
            raise ValueError("Invalid value for `connection_type`, must not be `None`")  # noqa: E501
        allowed_values = ["IDP", "SP"]  # noqa: E501
        if (self._configuration.client_side_validation and
                connection_type not in allowed_values):
            raise ValueError(
                "Invalid value for `connection_type` ({0}), must be one of {1}"  # noqa: E501
                .format(connection_type, allowed_values)
            )

        self._connection_type = connection_type

    @property
    def connection_id(self):
        """Gets the connection_id of this ExportMetadataRequest.  # noqa: E501

        The ID of the connection to export.  # noqa: E501

        :return: The connection_id of this ExportMetadataRequest.  # noqa: E501
        :rtype: str
        """
        return self._connection_id

    @connection_id.setter
    def connection_id(self, connection_id):
        """Sets the connection_id of this ExportMetadataRequest.

        The ID of the connection to export.  # noqa: E501

        :param connection_id: The connection_id of this ExportMetadataRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and connection_id is None:
            raise ValueError("Invalid value for `connection_id`, must not be `None`")  # noqa: E501

        self._connection_id = connection_id

    @property
    def virtual_server_id(self):
        """Gets the virtual_server_id of this ExportMetadataRequest.  # noqa: E501

        The virtual server ID to export the metadata with. If null, the connection's default will be used.  # noqa: E501

        :return: The virtual_server_id of this ExportMetadataRequest.  # noqa: E501
        :rtype: str
        """
        return self._virtual_server_id

    @virtual_server_id.setter
    def virtual_server_id(self, virtual_server_id):
        """Sets the virtual_server_id of this ExportMetadataRequest.

        The virtual server ID to export the metadata with. If null, the connection's default will be used.  # noqa: E501

        :param virtual_server_id: The virtual_server_id of this ExportMetadataRequest.  # noqa: E501
        :type: str
        """

        self._virtual_server_id = virtual_server_id

    @property
    def signing_settings(self):
        """Gets the signing_settings of this ExportMetadataRequest.  # noqa: E501

        The signing settings to sign the metadata with. If null, the metadata will not be signed  # noqa: E501

        :return: The signing_settings of this ExportMetadataRequest.  # noqa: E501
        :rtype: BaseSigningSettings
        """
        return self._signing_settings

    @signing_settings.setter
    def signing_settings(self, signing_settings):
        """Sets the signing_settings of this ExportMetadataRequest.

        The signing settings to sign the metadata with. If null, the metadata will not be signed  # noqa: E501

        :param signing_settings: The signing_settings of this ExportMetadataRequest.  # noqa: E501
        :type: BaseSigningSettings
        """

        self._signing_settings = signing_settings

    @property
    def use_secondary_port_for_soap(self):
        """Gets the use_secondary_port_for_soap of this ExportMetadataRequest.  # noqa: E501

        If PingFederate's secondary SSL port is configured and you want to use it for the SOAP channel, set to true. If client-certificate authentication is configured for the SOAP channel, the secondary port is required and this must be set to true.  # noqa: E501

        :return: The use_secondary_port_for_soap of this ExportMetadataRequest.  # noqa: E501
        :rtype: bool
        """
        return self._use_secondary_port_for_soap

    @use_secondary_port_for_soap.setter
    def use_secondary_port_for_soap(self, use_secondary_port_for_soap):
        """Sets the use_secondary_port_for_soap of this ExportMetadataRequest.

        If PingFederate's secondary SSL port is configured and you want to use it for the SOAP channel, set to true. If client-certificate authentication is configured for the SOAP channel, the secondary port is required and this must be set to true.  # noqa: E501

        :param use_secondary_port_for_soap: The use_secondary_port_for_soap of this ExportMetadataRequest.  # noqa: E501
        :type: bool
        """

        self._use_secondary_port_for_soap = use_secondary_port_for_soap

    @property
    def virtual_host_name(self):
        """Gets the virtual_host_name of this ExportMetadataRequest.  # noqa: E501

        The virtual host name to be used as the base url.  # noqa: E501

        :return: The virtual_host_name of this ExportMetadataRequest.  # noqa: E501
        :rtype: str
        """
        return self._virtual_host_name

    @virtual_host_name.setter
    def virtual_host_name(self, virtual_host_name):
        """Sets the virtual_host_name of this ExportMetadataRequest.

        The virtual host name to be used as the base url.  # noqa: E501

        :param virtual_host_name: The virtual_host_name of this ExportMetadataRequest.  # noqa: E501
        :type: str
        """

        self._virtual_host_name = virtual_host_name

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
        if issubclass(ExportMetadataRequest, dict):
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
        if not isinstance(other, ExportMetadataRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ExportMetadataRequest):
            return True

        return self.to_dict() != other.to_dict()
