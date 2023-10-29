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


class ServiceAuthentication(object):
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
        'attribute_query': 'ServiceModel',
        'jmx': 'ServiceModel',
        'connection_management': 'ServiceModel',
        'sso_directory_service': 'ServiceModel'
    }

    attribute_map = {
        'attribute_query': 'attributeQuery',
        'jmx': 'jmx',
        'connection_management': 'connectionManagement',
        'sso_directory_service': 'ssoDirectoryService'
    }

    def __init__(self, attribute_query=None, jmx=None, connection_management=None, sso_directory_service=None, _configuration=None):  # noqa: E501
        """ServiceAuthentication - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._attribute_query = None
        self._jmx = None
        self._connection_management = None
        self._sso_directory_service = None
        self.discriminator = None

        if attribute_query is not None:
            self.attribute_query = attribute_query
        if jmx is not None:
            self.jmx = jmx
        if connection_management is not None:
            self.connection_management = connection_management
        if sso_directory_service is not None:
            self.sso_directory_service = sso_directory_service

    @property
    def attribute_query(self):
        """Gets the attribute_query of this ServiceAuthentication.  # noqa: E501

        SAML2.0 attribute query service. Remove the JSON field to deactivate the attribute query service.  # noqa: E501

        :return: The attribute_query of this ServiceAuthentication.  # noqa: E501
        :rtype: ServiceModel
        """
        return self._attribute_query

    @attribute_query.setter
    def attribute_query(self, attribute_query):
        """Sets the attribute_query of this ServiceAuthentication.

        SAML2.0 attribute query service. Remove the JSON field to deactivate the attribute query service.  # noqa: E501

        :param attribute_query: The attribute_query of this ServiceAuthentication.  # noqa: E501
        :type: ServiceModel
        """

        self._attribute_query = attribute_query

    @property
    def jmx(self):
        """Gets the jmx of this ServiceAuthentication.  # noqa: E501

        JMX application management and monitoring service. Remove the JSON field to deactivate the JMX service.  # noqa: E501

        :return: The jmx of this ServiceAuthentication.  # noqa: E501
        :rtype: ServiceModel
        """
        return self._jmx

    @jmx.setter
    def jmx(self, jmx):
        """Sets the jmx of this ServiceAuthentication.

        JMX application management and monitoring service. Remove the JSON field to deactivate the JMX service.  # noqa: E501

        :param jmx: The jmx of this ServiceAuthentication.  # noqa: E501
        :type: ServiceModel
        """

        self._jmx = jmx

    @property
    def connection_management(self):
        """Gets the connection_management of this ServiceAuthentication.  # noqa: E501

        (Deprecated) Connection management service. Remove the JSON field to deactivate the connection management service.  # noqa: E501

        :return: The connection_management of this ServiceAuthentication.  # noqa: E501
        :rtype: ServiceModel
        """
        return self._connection_management

    @connection_management.setter
    def connection_management(self, connection_management):
        """Sets the connection_management of this ServiceAuthentication.

        (Deprecated) Connection management service. Remove the JSON field to deactivate the connection management service.  # noqa: E501

        :param connection_management: The connection_management of this ServiceAuthentication.  # noqa: E501
        :type: ServiceModel
        """

        self._connection_management = connection_management

    @property
    def sso_directory_service(self):
        """Gets the sso_directory_service of this ServiceAuthentication.  # noqa: E501

        (Deprecated) SSO directory service. Remove the JSON field to deactivate the SSO Directory service.  # noqa: E501

        :return: The sso_directory_service of this ServiceAuthentication.  # noqa: E501
        :rtype: ServiceModel
        """
        return self._sso_directory_service

    @sso_directory_service.setter
    def sso_directory_service(self, sso_directory_service):
        """Sets the sso_directory_service of this ServiceAuthentication.

        (Deprecated) SSO directory service. Remove the JSON field to deactivate the SSO Directory service.  # noqa: E501

        :param sso_directory_service: The sso_directory_service of this ServiceAuthentication.  # noqa: E501
        :type: ServiceModel
        """

        self._sso_directory_service = sso_directory_service

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
        if issubclass(ServiceAuthentication, dict):
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
        if not isinstance(other, ServiceAuthentication):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ServiceAuthentication):
            return True

        return self.to_dict() != other.to_dict()
