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


class JitProvisioningUserAttributes(object):
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
        'attribute_contract': 'list[IdpBrowserSsoAttribute]',
        'do_attribute_query': 'bool'
    }

    attribute_map = {
        'attribute_contract': 'attributeContract',
        'do_attribute_query': 'doAttributeQuery'
    }

    def __init__(self, attribute_contract=None, do_attribute_query=None, _configuration=None):  # noqa: E501
        """JitProvisioningUserAttributes - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._attribute_contract = None
        self._do_attribute_query = None
        self.discriminator = None

        if attribute_contract is not None:
            self.attribute_contract = attribute_contract
        if do_attribute_query is not None:
            self.do_attribute_query = do_attribute_query

    @property
    def attribute_contract(self):
        """Gets the attribute_contract of this JitProvisioningUserAttributes.  # noqa: E501

        A list of user attributes that the IdP sends in the SAML assertion.  # noqa: E501

        :return: The attribute_contract of this JitProvisioningUserAttributes.  # noqa: E501
        :rtype: list[IdpBrowserSsoAttribute]
        """
        return self._attribute_contract

    @attribute_contract.setter
    def attribute_contract(self, attribute_contract):
        """Sets the attribute_contract of this JitProvisioningUserAttributes.

        A list of user attributes that the IdP sends in the SAML assertion.  # noqa: E501

        :param attribute_contract: The attribute_contract of this JitProvisioningUserAttributes.  # noqa: E501
        :type: list[IdpBrowserSsoAttribute]
        """

        self._attribute_contract = attribute_contract

    @property
    def do_attribute_query(self):
        """Gets the do_attribute_query of this JitProvisioningUserAttributes.  # noqa: E501

        Specify whether to use only attributes from the SAML Assertion or retrieve additional attributes from the IdP. The default is false.  # noqa: E501

        :return: The do_attribute_query of this JitProvisioningUserAttributes.  # noqa: E501
        :rtype: bool
        """
        return self._do_attribute_query

    @do_attribute_query.setter
    def do_attribute_query(self, do_attribute_query):
        """Sets the do_attribute_query of this JitProvisioningUserAttributes.

        Specify whether to use only attributes from the SAML Assertion or retrieve additional attributes from the IdP. The default is false.  # noqa: E501

        :param do_attribute_query: The do_attribute_query of this JitProvisioningUserAttributes.  # noqa: E501
        :type: bool
        """

        self._do_attribute_query = do_attribute_query

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
        if issubclass(JitProvisioningUserAttributes, dict):
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
        if not isinstance(other, JitProvisioningUserAttributes):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, JitProvisioningUserAttributes):
            return True

        return self.to_dict() != other.to_dict()