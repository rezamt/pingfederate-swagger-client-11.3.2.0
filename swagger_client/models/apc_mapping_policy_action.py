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


class ApcMappingPolicyAction(object):
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
        'authentication_policy_contract_ref': 'ResourceLink',
        'attribute_mapping': 'AttributeMapping'
    }

    attribute_map = {
        'authentication_policy_contract_ref': 'authenticationPolicyContractRef',
        'attribute_mapping': 'attributeMapping'
    }

    def __init__(self, authentication_policy_contract_ref=None, attribute_mapping=None, _configuration=None):  # noqa: E501
        """ApcMappingPolicyAction - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._authentication_policy_contract_ref = None
        self._attribute_mapping = None
        self.discriminator = None

        self.authentication_policy_contract_ref = authentication_policy_contract_ref
        self.attribute_mapping = attribute_mapping

    @property
    def authentication_policy_contract_ref(self):
        """Gets the authentication_policy_contract_ref of this ApcMappingPolicyAction.  # noqa: E501

        Reference to the associated authentication policy contract.  # noqa: E501

        :return: The authentication_policy_contract_ref of this ApcMappingPolicyAction.  # noqa: E501
        :rtype: ResourceLink
        """
        return self._authentication_policy_contract_ref

    @authentication_policy_contract_ref.setter
    def authentication_policy_contract_ref(self, authentication_policy_contract_ref):
        """Sets the authentication_policy_contract_ref of this ApcMappingPolicyAction.

        Reference to the associated authentication policy contract.  # noqa: E501

        :param authentication_policy_contract_ref: The authentication_policy_contract_ref of this ApcMappingPolicyAction.  # noqa: E501
        :type: ResourceLink
        """
        if self._configuration.client_side_validation and authentication_policy_contract_ref is None:
            raise ValueError("Invalid value for `authentication_policy_contract_ref`, must not be `None`")  # noqa: E501

        self._authentication_policy_contract_ref = authentication_policy_contract_ref

    @property
    def attribute_mapping(self):
        """Gets the attribute_mapping of this ApcMappingPolicyAction.  # noqa: E501

        Contract fulfillment with the authentication policy contract's default values, and additional attributes retrieved from local data stores.  # noqa: E501

        :return: The attribute_mapping of this ApcMappingPolicyAction.  # noqa: E501
        :rtype: AttributeMapping
        """
        return self._attribute_mapping

    @attribute_mapping.setter
    def attribute_mapping(self, attribute_mapping):
        """Sets the attribute_mapping of this ApcMappingPolicyAction.

        Contract fulfillment with the authentication policy contract's default values, and additional attributes retrieved from local data stores.  # noqa: E501

        :param attribute_mapping: The attribute_mapping of this ApcMappingPolicyAction.  # noqa: E501
        :type: AttributeMapping
        """
        if self._configuration.client_side_validation and attribute_mapping is None:
            raise ValueError("Invalid value for `attribute_mapping`, must not be `None`")  # noqa: E501

        self._attribute_mapping = attribute_mapping

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
        if issubclass(ApcMappingPolicyAction, dict):
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
        if not isinstance(other, ApcMappingPolicyAction):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ApcMappingPolicyAction):
            return True

        return self.to_dict() != other.to_dict()
