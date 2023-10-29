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


class AccessTokenMapping(object):
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
        'id': 'str',
        'context': 'AccessTokenMappingContext',
        'access_token_manager_ref': 'ResourceLink',
        'attribute_sources': 'list[AttributeSource]',
        'attribute_contract_fulfillment': 'dict(str, AttributeFulfillmentValue)',
        'issuance_criteria': 'IssuanceCriteria'
    }

    attribute_map = {
        'id': 'id',
        'context': 'context',
        'access_token_manager_ref': 'accessTokenManagerRef',
        'attribute_sources': 'attributeSources',
        'attribute_contract_fulfillment': 'attributeContractFulfillment',
        'issuance_criteria': 'issuanceCriteria'
    }

    def __init__(self, id=None, context=None, access_token_manager_ref=None, attribute_sources=None, attribute_contract_fulfillment=None, issuance_criteria=None, _configuration=None):  # noqa: E501
        """AccessTokenMapping - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._context = None
        self._access_token_manager_ref = None
        self._attribute_sources = None
        self._attribute_contract_fulfillment = None
        self._issuance_criteria = None
        self.discriminator = None

        self.id = id
        self.context = context
        self.access_token_manager_ref = access_token_manager_ref
        if attribute_sources is not None:
            self.attribute_sources = attribute_sources
        self.attribute_contract_fulfillment = attribute_contract_fulfillment
        if issuance_criteria is not None:
            self.issuance_criteria = issuance_criteria

    @property
    def id(self):
        """Gets the id of this AccessTokenMapping.  # noqa: E501

        The id of the Access Token Mapping.  # noqa: E501

        :return: The id of this AccessTokenMapping.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AccessTokenMapping.

        The id of the Access Token Mapping.  # noqa: E501

        :param id: The id of this AccessTokenMapping.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def context(self):
        """Gets the context of this AccessTokenMapping.  # noqa: E501

        The context of the Access Token Mapping. This property cannot be changed after the mapping is created.  # noqa: E501

        :return: The context of this AccessTokenMapping.  # noqa: E501
        :rtype: AccessTokenMappingContext
        """
        return self._context

    @context.setter
    def context(self, context):
        """Sets the context of this AccessTokenMapping.

        The context of the Access Token Mapping. This property cannot be changed after the mapping is created.  # noqa: E501

        :param context: The context of this AccessTokenMapping.  # noqa: E501
        :type: AccessTokenMappingContext
        """
        if self._configuration.client_side_validation and context is None:
            raise ValueError("Invalid value for `context`, must not be `None`")  # noqa: E501

        self._context = context

    @property
    def access_token_manager_ref(self):
        """Gets the access_token_manager_ref of this AccessTokenMapping.  # noqa: E501

        Reference to the access token manager this mapping is associated with. This property cannot be changed after the mapping is created.  # noqa: E501

        :return: The access_token_manager_ref of this AccessTokenMapping.  # noqa: E501
        :rtype: ResourceLink
        """
        return self._access_token_manager_ref

    @access_token_manager_ref.setter
    def access_token_manager_ref(self, access_token_manager_ref):
        """Sets the access_token_manager_ref of this AccessTokenMapping.

        Reference to the access token manager this mapping is associated with. This property cannot be changed after the mapping is created.  # noqa: E501

        :param access_token_manager_ref: The access_token_manager_ref of this AccessTokenMapping.  # noqa: E501
        :type: ResourceLink
        """
        if self._configuration.client_side_validation and access_token_manager_ref is None:
            raise ValueError("Invalid value for `access_token_manager_ref`, must not be `None`")  # noqa: E501

        self._access_token_manager_ref = access_token_manager_ref

    @property
    def attribute_sources(self):
        """Gets the attribute_sources of this AccessTokenMapping.  # noqa: E501

        A list of configured data stores to look up attributes from.  # noqa: E501

        :return: The attribute_sources of this AccessTokenMapping.  # noqa: E501
        :rtype: list[AttributeSource]
        """
        return self._attribute_sources

    @attribute_sources.setter
    def attribute_sources(self, attribute_sources):
        """Sets the attribute_sources of this AccessTokenMapping.

        A list of configured data stores to look up attributes from.  # noqa: E501

        :param attribute_sources: The attribute_sources of this AccessTokenMapping.  # noqa: E501
        :type: list[AttributeSource]
        """

        self._attribute_sources = attribute_sources

    @property
    def attribute_contract_fulfillment(self):
        """Gets the attribute_contract_fulfillment of this AccessTokenMapping.  # noqa: E501

        A list of mappings from attribute names to their fulfillment values.  # noqa: E501

        :return: The attribute_contract_fulfillment of this AccessTokenMapping.  # noqa: E501
        :rtype: dict(str, AttributeFulfillmentValue)
        """
        return self._attribute_contract_fulfillment

    @attribute_contract_fulfillment.setter
    def attribute_contract_fulfillment(self, attribute_contract_fulfillment):
        """Sets the attribute_contract_fulfillment of this AccessTokenMapping.

        A list of mappings from attribute names to their fulfillment values.  # noqa: E501

        :param attribute_contract_fulfillment: The attribute_contract_fulfillment of this AccessTokenMapping.  # noqa: E501
        :type: dict(str, AttributeFulfillmentValue)
        """
        if self._configuration.client_side_validation and attribute_contract_fulfillment is None:
            raise ValueError("Invalid value for `attribute_contract_fulfillment`, must not be `None`")  # noqa: E501

        self._attribute_contract_fulfillment = attribute_contract_fulfillment

    @property
    def issuance_criteria(self):
        """Gets the issuance_criteria of this AccessTokenMapping.  # noqa: E501

        The issuance criteria that this transaction must meet before the corresponding attribute contract is fulfilled.  # noqa: E501

        :return: The issuance_criteria of this AccessTokenMapping.  # noqa: E501
        :rtype: IssuanceCriteria
        """
        return self._issuance_criteria

    @issuance_criteria.setter
    def issuance_criteria(self, issuance_criteria):
        """Sets the issuance_criteria of this AccessTokenMapping.

        The issuance criteria that this transaction must meet before the corresponding attribute contract is fulfilled.  # noqa: E501

        :param issuance_criteria: The issuance_criteria of this AccessTokenMapping.  # noqa: E501
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
        if issubclass(AccessTokenMapping, dict):
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
        if not isinstance(other, AccessTokenMapping):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AccessTokenMapping):
            return True

        return self.to_dict() != other.to_dict()
