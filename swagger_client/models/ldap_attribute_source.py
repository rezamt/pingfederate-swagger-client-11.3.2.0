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


class LdapAttributeSource(object):
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
        'base_dn': 'str',
        'search_scope': 'str',
        'search_filter': 'str',
        'search_attributes': 'list[str]',
        'binary_attribute_settings': 'dict(str, BinaryLdapAttributeSettings)',
        'member_of_nested_group': 'bool'
    }

    attribute_map = {
        'base_dn': 'baseDn',
        'search_scope': 'searchScope',
        'search_filter': 'searchFilter',
        'search_attributes': 'searchAttributes',
        'binary_attribute_settings': 'binaryAttributeSettings',
        'member_of_nested_group': 'memberOfNestedGroup'
    }

    def __init__(self, base_dn=None, search_scope=None, search_filter=None, search_attributes=None, binary_attribute_settings=None, member_of_nested_group=None, _configuration=None):  # noqa: E501
        """LdapAttributeSource - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._base_dn = None
        self._search_scope = None
        self._search_filter = None
        self._search_attributes = None
        self._binary_attribute_settings = None
        self._member_of_nested_group = None
        self.discriminator = None

        if base_dn is not None:
            self.base_dn = base_dn
        self.search_scope = search_scope
        self.search_filter = search_filter
        if search_attributes is not None:
            self.search_attributes = search_attributes
        if binary_attribute_settings is not None:
            self.binary_attribute_settings = binary_attribute_settings
        if member_of_nested_group is not None:
            self.member_of_nested_group = member_of_nested_group

    @property
    def base_dn(self):
        """Gets the base_dn of this LdapAttributeSource.  # noqa: E501

        The base DN to search from. If not specified, the search will start at the LDAP's root.  # noqa: E501

        :return: The base_dn of this LdapAttributeSource.  # noqa: E501
        :rtype: str
        """
        return self._base_dn

    @base_dn.setter
    def base_dn(self, base_dn):
        """Sets the base_dn of this LdapAttributeSource.

        The base DN to search from. If not specified, the search will start at the LDAP's root.  # noqa: E501

        :param base_dn: The base_dn of this LdapAttributeSource.  # noqa: E501
        :type: str
        """

        self._base_dn = base_dn

    @property
    def search_scope(self):
        """Gets the search_scope of this LdapAttributeSource.  # noqa: E501

        Determines the node depth of the query.  # noqa: E501

        :return: The search_scope of this LdapAttributeSource.  # noqa: E501
        :rtype: str
        """
        return self._search_scope

    @search_scope.setter
    def search_scope(self, search_scope):
        """Sets the search_scope of this LdapAttributeSource.

        Determines the node depth of the query.  # noqa: E501

        :param search_scope: The search_scope of this LdapAttributeSource.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and search_scope is None:
            raise ValueError("Invalid value for `search_scope`, must not be `None`")  # noqa: E501
        allowed_values = ["OBJECT", "ONE_LEVEL", "SUBTREE"]  # noqa: E501
        if (self._configuration.client_side_validation and
                search_scope not in allowed_values):
            raise ValueError(
                "Invalid value for `search_scope` ({0}), must be one of {1}"  # noqa: E501
                .format(search_scope, allowed_values)
            )

        self._search_scope = search_scope

    @property
    def search_filter(self):
        """Gets the search_filter of this LdapAttributeSource.  # noqa: E501

        The LDAP filter that will be used to lookup the objects from the directory.  # noqa: E501

        :return: The search_filter of this LdapAttributeSource.  # noqa: E501
        :rtype: str
        """
        return self._search_filter

    @search_filter.setter
    def search_filter(self, search_filter):
        """Sets the search_filter of this LdapAttributeSource.

        The LDAP filter that will be used to lookup the objects from the directory.  # noqa: E501

        :param search_filter: The search_filter of this LdapAttributeSource.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and search_filter is None:
            raise ValueError("Invalid value for `search_filter`, must not be `None`")  # noqa: E501

        self._search_filter = search_filter

    @property
    def search_attributes(self):
        """Gets the search_attributes of this LdapAttributeSource.  # noqa: E501

        A list of LDAP attributes returned from search and available for mapping.  # noqa: E501

        :return: The search_attributes of this LdapAttributeSource.  # noqa: E501
        :rtype: list[str]
        """
        return self._search_attributes

    @search_attributes.setter
    def search_attributes(self, search_attributes):
        """Sets the search_attributes of this LdapAttributeSource.

        A list of LDAP attributes returned from search and available for mapping.  # noqa: E501

        :param search_attributes: The search_attributes of this LdapAttributeSource.  # noqa: E501
        :type: list[str]
        """

        self._search_attributes = search_attributes

    @property
    def binary_attribute_settings(self):
        """Gets the binary_attribute_settings of this LdapAttributeSource.  # noqa: E501

        The advanced settings for binary LDAP attributes.  # noqa: E501

        :return: The binary_attribute_settings of this LdapAttributeSource.  # noqa: E501
        :rtype: dict(str, BinaryLdapAttributeSettings)
        """
        return self._binary_attribute_settings

    @binary_attribute_settings.setter
    def binary_attribute_settings(self, binary_attribute_settings):
        """Sets the binary_attribute_settings of this LdapAttributeSource.

        The advanced settings for binary LDAP attributes.  # noqa: E501

        :param binary_attribute_settings: The binary_attribute_settings of this LdapAttributeSource.  # noqa: E501
        :type: dict(str, BinaryLdapAttributeSettings)
        """

        self._binary_attribute_settings = binary_attribute_settings

    @property
    def member_of_nested_group(self):
        """Gets the member_of_nested_group of this LdapAttributeSource.  # noqa: E501

        Set this to true to return transitive group memberships for the 'memberOf' attribute.  This only applies for Active Directory data sources.  All other data sources will be set to false.  # noqa: E501

        :return: The member_of_nested_group of this LdapAttributeSource.  # noqa: E501
        :rtype: bool
        """
        return self._member_of_nested_group

    @member_of_nested_group.setter
    def member_of_nested_group(self, member_of_nested_group):
        """Sets the member_of_nested_group of this LdapAttributeSource.

        Set this to true to return transitive group memberships for the 'memberOf' attribute.  This only applies for Active Directory data sources.  All other data sources will be set to false.  # noqa: E501

        :param member_of_nested_group: The member_of_nested_group of this LdapAttributeSource.  # noqa: E501
        :type: bool
        """

        self._member_of_nested_group = member_of_nested_group

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
        if issubclass(LdapAttributeSource, dict):
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
        if not isinstance(other, LdapAttributeSource):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, LdapAttributeSource):
            return True

        return self.to_dict() != other.to_dict()
