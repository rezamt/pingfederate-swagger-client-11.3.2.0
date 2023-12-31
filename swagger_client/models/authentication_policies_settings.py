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


class AuthenticationPoliciesSettings(object):
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
        'enable_idp_authn_selection': 'bool',
        'enable_sp_authn_selection': 'bool'
    }

    attribute_map = {
        'enable_idp_authn_selection': 'enableIdpAuthnSelection',
        'enable_sp_authn_selection': 'enableSpAuthnSelection'
    }

    def __init__(self, enable_idp_authn_selection=None, enable_sp_authn_selection=None, _configuration=None):  # noqa: E501
        """AuthenticationPoliciesSettings - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._enable_idp_authn_selection = None
        self._enable_sp_authn_selection = None
        self.discriminator = None

        if enable_idp_authn_selection is not None:
            self.enable_idp_authn_selection = enable_idp_authn_selection
        if enable_sp_authn_selection is not None:
            self.enable_sp_authn_selection = enable_sp_authn_selection

    @property
    def enable_idp_authn_selection(self):
        """Gets the enable_idp_authn_selection of this AuthenticationPoliciesSettings.  # noqa: E501

        Enable IdP authentication policies.  # noqa: E501

        :return: The enable_idp_authn_selection of this AuthenticationPoliciesSettings.  # noqa: E501
        :rtype: bool
        """
        return self._enable_idp_authn_selection

    @enable_idp_authn_selection.setter
    def enable_idp_authn_selection(self, enable_idp_authn_selection):
        """Sets the enable_idp_authn_selection of this AuthenticationPoliciesSettings.

        Enable IdP authentication policies.  # noqa: E501

        :param enable_idp_authn_selection: The enable_idp_authn_selection of this AuthenticationPoliciesSettings.  # noqa: E501
        :type: bool
        """

        self._enable_idp_authn_selection = enable_idp_authn_selection

    @property
    def enable_sp_authn_selection(self):
        """Gets the enable_sp_authn_selection of this AuthenticationPoliciesSettings.  # noqa: E501

        Enable SP authentication policies.  # noqa: E501

        :return: The enable_sp_authn_selection of this AuthenticationPoliciesSettings.  # noqa: E501
        :rtype: bool
        """
        return self._enable_sp_authn_selection

    @enable_sp_authn_selection.setter
    def enable_sp_authn_selection(self, enable_sp_authn_selection):
        """Sets the enable_sp_authn_selection of this AuthenticationPoliciesSettings.

        Enable SP authentication policies.  # noqa: E501

        :param enable_sp_authn_selection: The enable_sp_authn_selection of this AuthenticationPoliciesSettings.  # noqa: E501
        :type: bool
        """

        self._enable_sp_authn_selection = enable_sp_authn_selection

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
        if issubclass(AuthenticationPoliciesSettings, dict):
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
        if not isinstance(other, AuthenticationPoliciesSettings):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AuthenticationPoliciesSettings):
            return True

        return self.to_dict() != other.to_dict()
