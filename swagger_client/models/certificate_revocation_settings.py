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


class CertificateRevocationSettings(object):
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
        'ocsp_settings': 'OcspSettings',
        'crl_settings': 'CrlSettings',
        'proxy_settings': 'ProxySettings'
    }

    attribute_map = {
        'ocsp_settings': 'ocspSettings',
        'crl_settings': 'crlSettings',
        'proxy_settings': 'proxySettings'
    }

    def __init__(self, ocsp_settings=None, crl_settings=None, proxy_settings=None, _configuration=None):  # noqa: E501
        """CertificateRevocationSettings - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._ocsp_settings = None
        self._crl_settings = None
        self._proxy_settings = None
        self.discriminator = None

        if ocsp_settings is not None:
            self.ocsp_settings = ocsp_settings
        if crl_settings is not None:
            self.crl_settings = crl_settings
        if proxy_settings is not None:
            self.proxy_settings = proxy_settings

    @property
    def ocsp_settings(self):
        """Gets the ocsp_settings of this CertificateRevocationSettings.  # noqa: E501

        Certificate revocation OCSP settings. If this attribute is omitted, OCSP checks are disabled.  # noqa: E501

        :return: The ocsp_settings of this CertificateRevocationSettings.  # noqa: E501
        :rtype: OcspSettings
        """
        return self._ocsp_settings

    @ocsp_settings.setter
    def ocsp_settings(self, ocsp_settings):
        """Sets the ocsp_settings of this CertificateRevocationSettings.

        Certificate revocation OCSP settings. If this attribute is omitted, OCSP checks are disabled.  # noqa: E501

        :param ocsp_settings: The ocsp_settings of this CertificateRevocationSettings.  # noqa: E501
        :type: OcspSettings
        """

        self._ocsp_settings = ocsp_settings

    @property
    def crl_settings(self):
        """Gets the crl_settings of this CertificateRevocationSettings.  # noqa: E501

        Certificate revocation CRL settings. If this attribute is omitted, CRL checks are disabled.  # noqa: E501

        :return: The crl_settings of this CertificateRevocationSettings.  # noqa: E501
        :rtype: CrlSettings
        """
        return self._crl_settings

    @crl_settings.setter
    def crl_settings(self, crl_settings):
        """Sets the crl_settings of this CertificateRevocationSettings.

        Certificate revocation CRL settings. If this attribute is omitted, CRL checks are disabled.  # noqa: E501

        :param crl_settings: The crl_settings of this CertificateRevocationSettings.  # noqa: E501
        :type: CrlSettings
        """

        self._crl_settings = crl_settings

    @property
    def proxy_settings(self):
        """Gets the proxy_settings of this CertificateRevocationSettings.  # noqa: E501

        If OCSP messaging is routed through a proxy server, specify the server's host (DNS name or IP address) and the port number. The same proxy information applies to CRL checking, when CRL is enabled for failover.  # noqa: E501

        :return: The proxy_settings of this CertificateRevocationSettings.  # noqa: E501
        :rtype: ProxySettings
        """
        return self._proxy_settings

    @proxy_settings.setter
    def proxy_settings(self, proxy_settings):
        """Sets the proxy_settings of this CertificateRevocationSettings.

        If OCSP messaging is routed through a proxy server, specify the server's host (DNS name or IP address) and the port number. The same proxy information applies to CRL checking, when CRL is enabled for failover.  # noqa: E501

        :param proxy_settings: The proxy_settings of this CertificateRevocationSettings.  # noqa: E501
        :type: ProxySettings
        """

        self._proxy_settings = proxy_settings

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
        if issubclass(CertificateRevocationSettings, dict):
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
        if not isinstance(other, CertificateRevocationSettings):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CertificateRevocationSettings):
            return True

        return self.to_dict() != other.to_dict()
