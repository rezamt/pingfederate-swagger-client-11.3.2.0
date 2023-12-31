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


class ChannelSource(object):
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
        'data_source': 'ResourceLink',
        'guid_attribute_name': 'str',
        'guid_binary': 'bool',
        'change_detection_settings': 'ChangeDetectionSettings',
        'group_membership_detection': 'GroupMembershipDetection',
        'account_management_settings': 'AccountManagementSettings',
        'base_dn': 'str',
        'user_source_location': 'ChannelSourceLocation',
        'group_source_location': 'ChannelSourceLocation'
    }

    attribute_map = {
        'data_source': 'dataSource',
        'guid_attribute_name': 'guidAttributeName',
        'guid_binary': 'guidBinary',
        'change_detection_settings': 'changeDetectionSettings',
        'group_membership_detection': 'groupMembershipDetection',
        'account_management_settings': 'accountManagementSettings',
        'base_dn': 'baseDn',
        'user_source_location': 'userSourceLocation',
        'group_source_location': 'groupSourceLocation'
    }

    def __init__(self, data_source=None, guid_attribute_name=None, guid_binary=None, change_detection_settings=None, group_membership_detection=None, account_management_settings=None, base_dn=None, user_source_location=None, group_source_location=None, _configuration=None):  # noqa: E501
        """ChannelSource - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._data_source = None
        self._guid_attribute_name = None
        self._guid_binary = None
        self._change_detection_settings = None
        self._group_membership_detection = None
        self._account_management_settings = None
        self._base_dn = None
        self._user_source_location = None
        self._group_source_location = None
        self.discriminator = None

        self.data_source = data_source
        self.guid_attribute_name = guid_attribute_name
        self.guid_binary = guid_binary
        self.change_detection_settings = change_detection_settings
        self.group_membership_detection = group_membership_detection
        self.account_management_settings = account_management_settings
        self.base_dn = base_dn
        self.user_source_location = user_source_location
        if group_source_location is not None:
            self.group_source_location = group_source_location

    @property
    def data_source(self):
        """Gets the data_source of this ChannelSource.  # noqa: E501

        Reference to an LDAP datastore.  # noqa: E501

        :return: The data_source of this ChannelSource.  # noqa: E501
        :rtype: ResourceLink
        """
        return self._data_source

    @data_source.setter
    def data_source(self, data_source):
        """Sets the data_source of this ChannelSource.

        Reference to an LDAP datastore.  # noqa: E501

        :param data_source: The data_source of this ChannelSource.  # noqa: E501
        :type: ResourceLink
        """
        if self._configuration.client_side_validation and data_source is None:
            raise ValueError("Invalid value for `data_source`, must not be `None`")  # noqa: E501

        self._data_source = data_source

    @property
    def guid_attribute_name(self):
        """Gets the guid_attribute_name of this ChannelSource.  # noqa: E501

        the GUID attribute name.  # noqa: E501

        :return: The guid_attribute_name of this ChannelSource.  # noqa: E501
        :rtype: str
        """
        return self._guid_attribute_name

    @guid_attribute_name.setter
    def guid_attribute_name(self, guid_attribute_name):
        """Sets the guid_attribute_name of this ChannelSource.

        the GUID attribute name.  # noqa: E501

        :param guid_attribute_name: The guid_attribute_name of this ChannelSource.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and guid_attribute_name is None:
            raise ValueError("Invalid value for `guid_attribute_name`, must not be `None`")  # noqa: E501

        self._guid_attribute_name = guid_attribute_name

    @property
    def guid_binary(self):
        """Gets the guid_binary of this ChannelSource.  # noqa: E501

        Indicates whether the GUID is stored in binary format.  # noqa: E501

        :return: The guid_binary of this ChannelSource.  # noqa: E501
        :rtype: bool
        """
        return self._guid_binary

    @guid_binary.setter
    def guid_binary(self, guid_binary):
        """Sets the guid_binary of this ChannelSource.

        Indicates whether the GUID is stored in binary format.  # noqa: E501

        :param guid_binary: The guid_binary of this ChannelSource.  # noqa: E501
        :type: bool
        """
        if self._configuration.client_side_validation and guid_binary is None:
            raise ValueError("Invalid value for `guid_binary`, must not be `None`")  # noqa: E501

        self._guid_binary = guid_binary

    @property
    def change_detection_settings(self):
        """Gets the change_detection_settings of this ChannelSource.  # noqa: E501

        Settings to detect a during provisioning.  # noqa: E501

        :return: The change_detection_settings of this ChannelSource.  # noqa: E501
        :rtype: ChangeDetectionSettings
        """
        return self._change_detection_settings

    @change_detection_settings.setter
    def change_detection_settings(self, change_detection_settings):
        """Sets the change_detection_settings of this ChannelSource.

        Settings to detect a during provisioning.  # noqa: E501

        :param change_detection_settings: The change_detection_settings of this ChannelSource.  # noqa: E501
        :type: ChangeDetectionSettings
        """
        if self._configuration.client_side_validation and change_detection_settings is None:
            raise ValueError("Invalid value for `change_detection_settings`, must not be `None`")  # noqa: E501

        self._change_detection_settings = change_detection_settings

    @property
    def group_membership_detection(self):
        """Gets the group_membership_detection of this ChannelSource.  # noqa: E501

        Settings to detect group memberships.  # noqa: E501

        :return: The group_membership_detection of this ChannelSource.  # noqa: E501
        :rtype: GroupMembershipDetection
        """
        return self._group_membership_detection

    @group_membership_detection.setter
    def group_membership_detection(self, group_membership_detection):
        """Sets the group_membership_detection of this ChannelSource.

        Settings to detect group memberships.  # noqa: E501

        :param group_membership_detection: The group_membership_detection of this ChannelSource.  # noqa: E501
        :type: GroupMembershipDetection
        """
        if self._configuration.client_side_validation and group_membership_detection is None:
            raise ValueError("Invalid value for `group_membership_detection`, must not be `None`")  # noqa: E501

        self._group_membership_detection = group_membership_detection

    @property
    def account_management_settings(self):
        """Gets the account_management_settings of this ChannelSource.  # noqa: E501

        Account management settings that includes the status and algorithms.  # noqa: E501

        :return: The account_management_settings of this ChannelSource.  # noqa: E501
        :rtype: AccountManagementSettings
        """
        return self._account_management_settings

    @account_management_settings.setter
    def account_management_settings(self, account_management_settings):
        """Sets the account_management_settings of this ChannelSource.

        Account management settings that includes the status and algorithms.  # noqa: E501

        :param account_management_settings: The account_management_settings of this ChannelSource.  # noqa: E501
        :type: AccountManagementSettings
        """
        if self._configuration.client_side_validation and account_management_settings is None:
            raise ValueError("Invalid value for `account_management_settings`, must not be `None`")  # noqa: E501

        self._account_management_settings = account_management_settings

    @property
    def base_dn(self):
        """Gets the base_dn of this ChannelSource.  # noqa: E501

        The base DN where the user records are located.  # noqa: E501

        :return: The base_dn of this ChannelSource.  # noqa: E501
        :rtype: str
        """
        return self._base_dn

    @base_dn.setter
    def base_dn(self, base_dn):
        """Sets the base_dn of this ChannelSource.

        The base DN where the user records are located.  # noqa: E501

        :param base_dn: The base_dn of this ChannelSource.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and base_dn is None:
            raise ValueError("Invalid value for `base_dn`, must not be `None`")  # noqa: E501

        self._base_dn = base_dn

    @property
    def user_source_location(self):
        """Gets the user_source_location of this ChannelSource.  # noqa: E501

        The user provisioning source location settings.  # noqa: E501

        :return: The user_source_location of this ChannelSource.  # noqa: E501
        :rtype: ChannelSourceLocation
        """
        return self._user_source_location

    @user_source_location.setter
    def user_source_location(self, user_source_location):
        """Sets the user_source_location of this ChannelSource.

        The user provisioning source location settings.  # noqa: E501

        :param user_source_location: The user_source_location of this ChannelSource.  # noqa: E501
        :type: ChannelSourceLocation
        """
        if self._configuration.client_side_validation and user_source_location is None:
            raise ValueError("Invalid value for `user_source_location`, must not be `None`")  # noqa: E501

        self._user_source_location = user_source_location

    @property
    def group_source_location(self):
        """Gets the group_source_location of this ChannelSource.  # noqa: E501

        The group provisioning source location settings.  # noqa: E501

        :return: The group_source_location of this ChannelSource.  # noqa: E501
        :rtype: ChannelSourceLocation
        """
        return self._group_source_location

    @group_source_location.setter
    def group_source_location(self, group_source_location):
        """Sets the group_source_location of this ChannelSource.

        The group provisioning source location settings.  # noqa: E501

        :param group_source_location: The group_source_location of this ChannelSource.  # noqa: E501
        :type: ChannelSourceLocation
        """

        self._group_source_location = group_source_location

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
        if issubclass(ChannelSource, dict):
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
        if not isinstance(other, ChannelSource):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ChannelSource):
            return True

        return self.to_dict() != other.to_dict()
