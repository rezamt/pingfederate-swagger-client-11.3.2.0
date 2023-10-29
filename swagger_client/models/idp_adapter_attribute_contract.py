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


class IdpAdapterAttributeContract(object):
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
        'core_attributes': 'list[IdpAdapterAttribute]',
        'extended_attributes': 'list[IdpAdapterAttribute]',
        'unique_user_key_attribute': 'str',
        'mask_ognl_values': 'bool',
        'inherited': 'bool'
    }

    attribute_map = {
        'core_attributes': 'coreAttributes',
        'extended_attributes': 'extendedAttributes',
        'unique_user_key_attribute': 'uniqueUserKeyAttribute',
        'mask_ognl_values': 'maskOgnlValues',
        'inherited': 'inherited'
    }

    def __init__(self, core_attributes=None, extended_attributes=None, unique_user_key_attribute=None, mask_ognl_values=None, inherited=None, _configuration=None):  # noqa: E501
        """IdpAdapterAttributeContract - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._core_attributes = None
        self._extended_attributes = None
        self._unique_user_key_attribute = None
        self._mask_ognl_values = None
        self._inherited = None
        self.discriminator = None

        self.core_attributes = core_attributes
        if extended_attributes is not None:
            self.extended_attributes = extended_attributes
        if unique_user_key_attribute is not None:
            self.unique_user_key_attribute = unique_user_key_attribute
        if mask_ognl_values is not None:
            self.mask_ognl_values = mask_ognl_values
        if inherited is not None:
            self.inherited = inherited

    @property
    def core_attributes(self):
        """Gets the core_attributes of this IdpAdapterAttributeContract.  # noqa: E501

        A list of IdP adapter attributes that correspond to the attributes exposed by the IdP adapter type.  # noqa: E501

        :return: The core_attributes of this IdpAdapterAttributeContract.  # noqa: E501
        :rtype: list[IdpAdapterAttribute]
        """
        return self._core_attributes

    @core_attributes.setter
    def core_attributes(self, core_attributes):
        """Sets the core_attributes of this IdpAdapterAttributeContract.

        A list of IdP adapter attributes that correspond to the attributes exposed by the IdP adapter type.  # noqa: E501

        :param core_attributes: The core_attributes of this IdpAdapterAttributeContract.  # noqa: E501
        :type: list[IdpAdapterAttribute]
        """
        if self._configuration.client_side_validation and core_attributes is None:
            raise ValueError("Invalid value for `core_attributes`, must not be `None`")  # noqa: E501

        self._core_attributes = core_attributes

    @property
    def extended_attributes(self):
        """Gets the extended_attributes of this IdpAdapterAttributeContract.  # noqa: E501

        A list of additional attributes that can be returned by the IdP adapter. The extended attributes are only used if the adapter supports them.  # noqa: E501

        :return: The extended_attributes of this IdpAdapterAttributeContract.  # noqa: E501
        :rtype: list[IdpAdapterAttribute]
        """
        return self._extended_attributes

    @extended_attributes.setter
    def extended_attributes(self, extended_attributes):
        """Sets the extended_attributes of this IdpAdapterAttributeContract.

        A list of additional attributes that can be returned by the IdP adapter. The extended attributes are only used if the adapter supports them.  # noqa: E501

        :param extended_attributes: The extended_attributes of this IdpAdapterAttributeContract.  # noqa: E501
        :type: list[IdpAdapterAttribute]
        """

        self._extended_attributes = extended_attributes

    @property
    def unique_user_key_attribute(self):
        """Gets the unique_user_key_attribute of this IdpAdapterAttributeContract.  # noqa: E501

        The attribute to use for uniquely identify a user's authentication sessions.  # noqa: E501

        :return: The unique_user_key_attribute of this IdpAdapterAttributeContract.  # noqa: E501
        :rtype: str
        """
        return self._unique_user_key_attribute

    @unique_user_key_attribute.setter
    def unique_user_key_attribute(self, unique_user_key_attribute):
        """Sets the unique_user_key_attribute of this IdpAdapterAttributeContract.

        The attribute to use for uniquely identify a user's authentication sessions.  # noqa: E501

        :param unique_user_key_attribute: The unique_user_key_attribute of this IdpAdapterAttributeContract.  # noqa: E501
        :type: str
        """

        self._unique_user_key_attribute = unique_user_key_attribute

    @property
    def mask_ognl_values(self):
        """Gets the mask_ognl_values of this IdpAdapterAttributeContract.  # noqa: E501

        Whether or not all OGNL expressions used to fulfill an outgoing assertion contract should be masked in the logs. Defaults to false.  # noqa: E501

        :return: The mask_ognl_values of this IdpAdapterAttributeContract.  # noqa: E501
        :rtype: bool
        """
        return self._mask_ognl_values

    @mask_ognl_values.setter
    def mask_ognl_values(self, mask_ognl_values):
        """Sets the mask_ognl_values of this IdpAdapterAttributeContract.

        Whether or not all OGNL expressions used to fulfill an outgoing assertion contract should be masked in the logs. Defaults to false.  # noqa: E501

        :param mask_ognl_values: The mask_ognl_values of this IdpAdapterAttributeContract.  # noqa: E501
        :type: bool
        """

        self._mask_ognl_values = mask_ognl_values

    @property
    def inherited(self):
        """Gets the inherited of this IdpAdapterAttributeContract.  # noqa: E501

        Whether this attribute contract is inherited from its parent instance. If true, the rest of the properties in this model become read-only. The default value is false.  # noqa: E501

        :return: The inherited of this IdpAdapterAttributeContract.  # noqa: E501
        :rtype: bool
        """
        return self._inherited

    @inherited.setter
    def inherited(self, inherited):
        """Sets the inherited of this IdpAdapterAttributeContract.

        Whether this attribute contract is inherited from its parent instance. If true, the rest of the properties in this model become read-only. The default value is false.  # noqa: E501

        :param inherited: The inherited of this IdpAdapterAttributeContract.  # noqa: E501
        :type: bool
        """

        self._inherited = inherited

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
        if issubclass(IdpAdapterAttributeContract, dict):
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
        if not isinstance(other, IdpAdapterAttributeContract):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IdpAdapterAttributeContract):
            return True

        return self.to_dict() != other.to_dict()
