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


class ProcessorPolicyToGeneratorMapping(object):
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
        'attribute_sources': 'list[AttributeSource]',
        'attribute_contract_fulfillment': 'dict(str, AttributeFulfillmentValue)',
        'issuance_criteria': 'IssuanceCriteria',
        'id': 'str',
        'source_id': 'str',
        'target_id': 'str',
        'license_connection_group_assignment': 'str'
    }

    attribute_map = {
        'attribute_sources': 'attributeSources',
        'attribute_contract_fulfillment': 'attributeContractFulfillment',
        'issuance_criteria': 'issuanceCriteria',
        'id': 'id',
        'source_id': 'sourceId',
        'target_id': 'targetId',
        'license_connection_group_assignment': 'licenseConnectionGroupAssignment'
    }

    def __init__(self, attribute_sources=None, attribute_contract_fulfillment=None, issuance_criteria=None, id=None, source_id=None, target_id=None, license_connection_group_assignment=None, _configuration=None):  # noqa: E501
        """ProcessorPolicyToGeneratorMapping - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._attribute_sources = None
        self._attribute_contract_fulfillment = None
        self._issuance_criteria = None
        self._id = None
        self._source_id = None
        self._target_id = None
        self._license_connection_group_assignment = None
        self.discriminator = None

        if attribute_sources is not None:
            self.attribute_sources = attribute_sources
        self.attribute_contract_fulfillment = attribute_contract_fulfillment
        if issuance_criteria is not None:
            self.issuance_criteria = issuance_criteria
        if id is not None:
            self.id = id
        self.source_id = source_id
        self.target_id = target_id
        if license_connection_group_assignment is not None:
            self.license_connection_group_assignment = license_connection_group_assignment

    @property
    def attribute_sources(self):
        """Gets the attribute_sources of this ProcessorPolicyToGeneratorMapping.  # noqa: E501

        A list of configured data stores to look up attributes from.  # noqa: E501

        :return: The attribute_sources of this ProcessorPolicyToGeneratorMapping.  # noqa: E501
        :rtype: list[AttributeSource]
        """
        return self._attribute_sources

    @attribute_sources.setter
    def attribute_sources(self, attribute_sources):
        """Sets the attribute_sources of this ProcessorPolicyToGeneratorMapping.

        A list of configured data stores to look up attributes from.  # noqa: E501

        :param attribute_sources: The attribute_sources of this ProcessorPolicyToGeneratorMapping.  # noqa: E501
        :type: list[AttributeSource]
        """

        self._attribute_sources = attribute_sources

    @property
    def attribute_contract_fulfillment(self):
        """Gets the attribute_contract_fulfillment of this ProcessorPolicyToGeneratorMapping.  # noqa: E501

        A list of mappings from attribute names to their fulfillment values.  # noqa: E501

        :return: The attribute_contract_fulfillment of this ProcessorPolicyToGeneratorMapping.  # noqa: E501
        :rtype: dict(str, AttributeFulfillmentValue)
        """
        return self._attribute_contract_fulfillment

    @attribute_contract_fulfillment.setter
    def attribute_contract_fulfillment(self, attribute_contract_fulfillment):
        """Sets the attribute_contract_fulfillment of this ProcessorPolicyToGeneratorMapping.

        A list of mappings from attribute names to their fulfillment values.  # noqa: E501

        :param attribute_contract_fulfillment: The attribute_contract_fulfillment of this ProcessorPolicyToGeneratorMapping.  # noqa: E501
        :type: dict(str, AttributeFulfillmentValue)
        """
        if self._configuration.client_side_validation and attribute_contract_fulfillment is None:
            raise ValueError("Invalid value for `attribute_contract_fulfillment`, must not be `None`")  # noqa: E501

        self._attribute_contract_fulfillment = attribute_contract_fulfillment

    @property
    def issuance_criteria(self):
        """Gets the issuance_criteria of this ProcessorPolicyToGeneratorMapping.  # noqa: E501

        The issuance criteria that this transaction must meet before the corresponding attribute contract is fulfilled.  # noqa: E501

        :return: The issuance_criteria of this ProcessorPolicyToGeneratorMapping.  # noqa: E501
        :rtype: IssuanceCriteria
        """
        return self._issuance_criteria

    @issuance_criteria.setter
    def issuance_criteria(self, issuance_criteria):
        """Sets the issuance_criteria of this ProcessorPolicyToGeneratorMapping.

        The issuance criteria that this transaction must meet before the corresponding attribute contract is fulfilled.  # noqa: E501

        :param issuance_criteria: The issuance_criteria of this ProcessorPolicyToGeneratorMapping.  # noqa: E501
        :type: IssuanceCriteria
        """

        self._issuance_criteria = issuance_criteria

    @property
    def id(self):
        """Gets the id of this ProcessorPolicyToGeneratorMapping.  # noqa: E501

        The id of the Token Exchange Processor policy to Token Generator mapping. This field is read-only and is ignored when passed in with the payload.  # noqa: E501

        :return: The id of this ProcessorPolicyToGeneratorMapping.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ProcessorPolicyToGeneratorMapping.

        The id of the Token Exchange Processor policy to Token Generator mapping. This field is read-only and is ignored when passed in with the payload.  # noqa: E501

        :param id: The id of this ProcessorPolicyToGeneratorMapping.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def source_id(self):
        """Gets the source_id of this ProcessorPolicyToGeneratorMapping.  # noqa: E501

        The id of the Token Exchange Processor policy.  # noqa: E501

        :return: The source_id of this ProcessorPolicyToGeneratorMapping.  # noqa: E501
        :rtype: str
        """
        return self._source_id

    @source_id.setter
    def source_id(self, source_id):
        """Sets the source_id of this ProcessorPolicyToGeneratorMapping.

        The id of the Token Exchange Processor policy.  # noqa: E501

        :param source_id: The source_id of this ProcessorPolicyToGeneratorMapping.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and source_id is None:
            raise ValueError("Invalid value for `source_id`, must not be `None`")  # noqa: E501

        self._source_id = source_id

    @property
    def target_id(self):
        """Gets the target_id of this ProcessorPolicyToGeneratorMapping.  # noqa: E501

        The id of the Token Generator.  # noqa: E501

        :return: The target_id of this ProcessorPolicyToGeneratorMapping.  # noqa: E501
        :rtype: str
        """
        return self._target_id

    @target_id.setter
    def target_id(self, target_id):
        """Sets the target_id of this ProcessorPolicyToGeneratorMapping.

        The id of the Token Generator.  # noqa: E501

        :param target_id: The target_id of this ProcessorPolicyToGeneratorMapping.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and target_id is None:
            raise ValueError("Invalid value for `target_id`, must not be `None`")  # noqa: E501

        self._target_id = target_id

    @property
    def license_connection_group_assignment(self):
        """Gets the license_connection_group_assignment of this ProcessorPolicyToGeneratorMapping.  # noqa: E501

        The license connection group.  # noqa: E501

        :return: The license_connection_group_assignment of this ProcessorPolicyToGeneratorMapping.  # noqa: E501
        :rtype: str
        """
        return self._license_connection_group_assignment

    @license_connection_group_assignment.setter
    def license_connection_group_assignment(self, license_connection_group_assignment):
        """Sets the license_connection_group_assignment of this ProcessorPolicyToGeneratorMapping.

        The license connection group.  # noqa: E501

        :param license_connection_group_assignment: The license_connection_group_assignment of this ProcessorPolicyToGeneratorMapping.  # noqa: E501
        :type: str
        """

        self._license_connection_group_assignment = license_connection_group_assignment

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
        if issubclass(ProcessorPolicyToGeneratorMapping, dict):
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
        if not isinstance(other, ProcessorPolicyToGeneratorMapping):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ProcessorPolicyToGeneratorMapping):
            return True

        return self.to_dict() != other.to_dict()
