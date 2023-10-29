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


class AdditionalAllowedEntitiesConfiguration(object):
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
        'allow_additional_entities': 'bool',
        'allow_all_entities': 'bool',
        'additional_allowed_entities': 'list[Entity]'
    }

    attribute_map = {
        'allow_additional_entities': 'allowAdditionalEntities',
        'allow_all_entities': 'allowAllEntities',
        'additional_allowed_entities': 'additionalAllowedEntities'
    }

    def __init__(self, allow_additional_entities=None, allow_all_entities=None, additional_allowed_entities=None, _configuration=None):  # noqa: E501
        """AdditionalAllowedEntitiesConfiguration - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._allow_additional_entities = None
        self._allow_all_entities = None
        self._additional_allowed_entities = None
        self.discriminator = None

        if allow_additional_entities is not None:
            self.allow_additional_entities = allow_additional_entities
        if allow_all_entities is not None:
            self.allow_all_entities = allow_all_entities
        if additional_allowed_entities is not None:
            self.additional_allowed_entities = additional_allowed_entities

    @property
    def allow_additional_entities(self):
        """Gets the allow_additional_entities of this AdditionalAllowedEntitiesConfiguration.  # noqa: E501

        Set to true to configure additional entities or issuers to be accepted during entity or issuer validation.  # noqa: E501

        :return: The allow_additional_entities of this AdditionalAllowedEntitiesConfiguration.  # noqa: E501
        :rtype: bool
        """
        return self._allow_additional_entities

    @allow_additional_entities.setter
    def allow_additional_entities(self, allow_additional_entities):
        """Sets the allow_additional_entities of this AdditionalAllowedEntitiesConfiguration.

        Set to true to configure additional entities or issuers to be accepted during entity or issuer validation.  # noqa: E501

        :param allow_additional_entities: The allow_additional_entities of this AdditionalAllowedEntitiesConfiguration.  # noqa: E501
        :type: bool
        """

        self._allow_additional_entities = allow_additional_entities

    @property
    def allow_all_entities(self):
        """Gets the allow_all_entities of this AdditionalAllowedEntitiesConfiguration.  # noqa: E501

        Set to true to accept any entity or issuer during entity or issuer validation. (Not Recommended)  # noqa: E501

        :return: The allow_all_entities of this AdditionalAllowedEntitiesConfiguration.  # noqa: E501
        :rtype: bool
        """
        return self._allow_all_entities

    @allow_all_entities.setter
    def allow_all_entities(self, allow_all_entities):
        """Sets the allow_all_entities of this AdditionalAllowedEntitiesConfiguration.

        Set to true to accept any entity or issuer during entity or issuer validation. (Not Recommended)  # noqa: E501

        :param allow_all_entities: The allow_all_entities of this AdditionalAllowedEntitiesConfiguration.  # noqa: E501
        :type: bool
        """

        self._allow_all_entities = allow_all_entities

    @property
    def additional_allowed_entities(self):
        """Gets the additional_allowed_entities of this AdditionalAllowedEntitiesConfiguration.  # noqa: E501

        An array of additional allowed entities or issuers to be accepted during entity or issuer validation.  # noqa: E501

        :return: The additional_allowed_entities of this AdditionalAllowedEntitiesConfiguration.  # noqa: E501
        :rtype: list[Entity]
        """
        return self._additional_allowed_entities

    @additional_allowed_entities.setter
    def additional_allowed_entities(self, additional_allowed_entities):
        """Sets the additional_allowed_entities of this AdditionalAllowedEntitiesConfiguration.

        An array of additional allowed entities or issuers to be accepted during entity or issuer validation.  # noqa: E501

        :param additional_allowed_entities: The additional_allowed_entities of this AdditionalAllowedEntitiesConfiguration.  # noqa: E501
        :type: list[Entity]
        """

        self._additional_allowed_entities = additional_allowed_entities

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
        if issubclass(AdditionalAllowedEntitiesConfiguration, dict):
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
        if not isinstance(other, AdditionalAllowedEntitiesConfiguration):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AdditionalAllowedEntitiesConfiguration):
            return True

        return self.to_dict() != other.to_dict()