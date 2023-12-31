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


class IdpTokenProcessorMapping(object):
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
        'idp_token_processor_ref': 'ResourceLink',
        'restricted_virtual_entity_ids': 'list[str]',
        'attribute_sources': 'list[AttributeSource]',
        'attribute_contract_fulfillment': 'dict(str, AttributeFulfillmentValue)',
        'issuance_criteria': 'IssuanceCriteria'
    }

    attribute_map = {
        'idp_token_processor_ref': 'idpTokenProcessorRef',
        'restricted_virtual_entity_ids': 'restrictedVirtualEntityIds',
        'attribute_sources': 'attributeSources',
        'attribute_contract_fulfillment': 'attributeContractFulfillment',
        'issuance_criteria': 'issuanceCriteria'
    }

    def __init__(self, idp_token_processor_ref=None, restricted_virtual_entity_ids=None, attribute_sources=None, attribute_contract_fulfillment=None, issuance_criteria=None, _configuration=None):  # noqa: E501
        """IdpTokenProcessorMapping - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._idp_token_processor_ref = None
        self._restricted_virtual_entity_ids = None
        self._attribute_sources = None
        self._attribute_contract_fulfillment = None
        self._issuance_criteria = None
        self.discriminator = None

        self.idp_token_processor_ref = idp_token_processor_ref
        if restricted_virtual_entity_ids is not None:
            self.restricted_virtual_entity_ids = restricted_virtual_entity_ids
        if attribute_sources is not None:
            self.attribute_sources = attribute_sources
        self.attribute_contract_fulfillment = attribute_contract_fulfillment
        if issuance_criteria is not None:
            self.issuance_criteria = issuance_criteria

    @property
    def idp_token_processor_ref(self):
        """Gets the idp_token_processor_ref of this IdpTokenProcessorMapping.  # noqa: E501

        Reference to the associated token processor.  # noqa: E501

        :return: The idp_token_processor_ref of this IdpTokenProcessorMapping.  # noqa: E501
        :rtype: ResourceLink
        """
        return self._idp_token_processor_ref

    @idp_token_processor_ref.setter
    def idp_token_processor_ref(self, idp_token_processor_ref):
        """Sets the idp_token_processor_ref of this IdpTokenProcessorMapping.

        Reference to the associated token processor.  # noqa: E501

        :param idp_token_processor_ref: The idp_token_processor_ref of this IdpTokenProcessorMapping.  # noqa: E501
        :type: ResourceLink
        """
        if self._configuration.client_side_validation and idp_token_processor_ref is None:
            raise ValueError("Invalid value for `idp_token_processor_ref`, must not be `None`")  # noqa: E501

        self._idp_token_processor_ref = idp_token_processor_ref

    @property
    def restricted_virtual_entity_ids(self):
        """Gets the restricted_virtual_entity_ids of this IdpTokenProcessorMapping.  # noqa: E501

        The list of virtual server IDs that this mapping is restricted to.  # noqa: E501

        :return: The restricted_virtual_entity_ids of this IdpTokenProcessorMapping.  # noqa: E501
        :rtype: list[str]
        """
        return self._restricted_virtual_entity_ids

    @restricted_virtual_entity_ids.setter
    def restricted_virtual_entity_ids(self, restricted_virtual_entity_ids):
        """Sets the restricted_virtual_entity_ids of this IdpTokenProcessorMapping.

        The list of virtual server IDs that this mapping is restricted to.  # noqa: E501

        :param restricted_virtual_entity_ids: The restricted_virtual_entity_ids of this IdpTokenProcessorMapping.  # noqa: E501
        :type: list[str]
        """

        self._restricted_virtual_entity_ids = restricted_virtual_entity_ids

    @property
    def attribute_sources(self):
        """Gets the attribute_sources of this IdpTokenProcessorMapping.  # noqa: E501

        A list of configured data stores to look up attributes from.  # noqa: E501

        :return: The attribute_sources of this IdpTokenProcessorMapping.  # noqa: E501
        :rtype: list[AttributeSource]
        """
        return self._attribute_sources

    @attribute_sources.setter
    def attribute_sources(self, attribute_sources):
        """Sets the attribute_sources of this IdpTokenProcessorMapping.

        A list of configured data stores to look up attributes from.  # noqa: E501

        :param attribute_sources: The attribute_sources of this IdpTokenProcessorMapping.  # noqa: E501
        :type: list[AttributeSource]
        """

        self._attribute_sources = attribute_sources

    @property
    def attribute_contract_fulfillment(self):
        """Gets the attribute_contract_fulfillment of this IdpTokenProcessorMapping.  # noqa: E501

        A list of mappings from attribute names to their fulfillment values.  # noqa: E501

        :return: The attribute_contract_fulfillment of this IdpTokenProcessorMapping.  # noqa: E501
        :rtype: dict(str, AttributeFulfillmentValue)
        """
        return self._attribute_contract_fulfillment

    @attribute_contract_fulfillment.setter
    def attribute_contract_fulfillment(self, attribute_contract_fulfillment):
        """Sets the attribute_contract_fulfillment of this IdpTokenProcessorMapping.

        A list of mappings from attribute names to their fulfillment values.  # noqa: E501

        :param attribute_contract_fulfillment: The attribute_contract_fulfillment of this IdpTokenProcessorMapping.  # noqa: E501
        :type: dict(str, AttributeFulfillmentValue)
        """
        if self._configuration.client_side_validation and attribute_contract_fulfillment is None:
            raise ValueError("Invalid value for `attribute_contract_fulfillment`, must not be `None`")  # noqa: E501

        self._attribute_contract_fulfillment = attribute_contract_fulfillment

    @property
    def issuance_criteria(self):
        """Gets the issuance_criteria of this IdpTokenProcessorMapping.  # noqa: E501

        The issuance criteria that this transaction must meet before the corresponding attribute contract is fulfilled.  # noqa: E501

        :return: The issuance_criteria of this IdpTokenProcessorMapping.  # noqa: E501
        :rtype: IssuanceCriteria
        """
        return self._issuance_criteria

    @issuance_criteria.setter
    def issuance_criteria(self, issuance_criteria):
        """Sets the issuance_criteria of this IdpTokenProcessorMapping.

        The issuance criteria that this transaction must meet before the corresponding attribute contract is fulfilled.  # noqa: E501

        :param issuance_criteria: The issuance_criteria of this IdpTokenProcessorMapping.  # noqa: E501
        :type: IssuanceCriteria
        """

        self._issuance_criteria = issuance_criteria

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
        if issubclass(IdpTokenProcessorMapping, dict):
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
        if not isinstance(other, IdpTokenProcessorMapping):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IdpTokenProcessorMapping):
            return True

        return self.to_dict() != other.to_dict()
