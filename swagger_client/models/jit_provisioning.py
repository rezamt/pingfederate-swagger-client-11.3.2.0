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


class JitProvisioning(object):
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
        'user_attributes': 'JitProvisioningUserAttributes',
        'user_repository': 'DataStoreRepository',
        'event_trigger': 'str',
        'error_handling': 'str'
    }

    attribute_map = {
        'user_attributes': 'userAttributes',
        'user_repository': 'userRepository',
        'event_trigger': 'eventTrigger',
        'error_handling': 'errorHandling'
    }

    def __init__(self, user_attributes=None, user_repository=None, event_trigger=None, error_handling=None, _configuration=None):  # noqa: E501
        """JitProvisioning - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._user_attributes = None
        self._user_repository = None
        self._event_trigger = None
        self._error_handling = None
        self.discriminator = None

        self.user_attributes = user_attributes
        self.user_repository = user_repository
        if event_trigger is not None:
            self.event_trigger = event_trigger
        if error_handling is not None:
            self.error_handling = error_handling

    @property
    def user_attributes(self):
        """Gets the user_attributes of this JitProvisioning.  # noqa: E501

        Attributes from the SAML Assertion.  # noqa: E501

        :return: The user_attributes of this JitProvisioning.  # noqa: E501
        :rtype: JitProvisioningUserAttributes
        """
        return self._user_attributes

    @user_attributes.setter
    def user_attributes(self, user_attributes):
        """Sets the user_attributes of this JitProvisioning.

        Attributes from the SAML Assertion.  # noqa: E501

        :param user_attributes: The user_attributes of this JitProvisioning.  # noqa: E501
        :type: JitProvisioningUserAttributes
        """
        if self._configuration.client_side_validation and user_attributes is None:
            raise ValueError("Invalid value for `user_attributes`, must not be `None`")  # noqa: E501

        self._user_attributes = user_attributes

    @property
    def user_repository(self):
        """Gets the user_repository of this JitProvisioning.  # noqa: E501

        The data store used as the local repository for user provisioning.  # noqa: E501

        :return: The user_repository of this JitProvisioning.  # noqa: E501
        :rtype: DataStoreRepository
        """
        return self._user_repository

    @user_repository.setter
    def user_repository(self, user_repository):
        """Sets the user_repository of this JitProvisioning.

        The data store used as the local repository for user provisioning.  # noqa: E501

        :param user_repository: The user_repository of this JitProvisioning.  # noqa: E501
        :type: DataStoreRepository
        """
        if self._configuration.client_side_validation and user_repository is None:
            raise ValueError("Invalid value for `user_repository`, must not be `None`")  # noqa: E501

        self._user_repository = user_repository

    @property
    def event_trigger(self):
        """Gets the event_trigger of this JitProvisioning.  # noqa: E501

        Specify when provisioning occurs during assertion processing. The default is 'NEW_USER_ONLY'.  # noqa: E501

        :return: The event_trigger of this JitProvisioning.  # noqa: E501
        :rtype: str
        """
        return self._event_trigger

    @event_trigger.setter
    def event_trigger(self, event_trigger):
        """Sets the event_trigger of this JitProvisioning.

        Specify when provisioning occurs during assertion processing. The default is 'NEW_USER_ONLY'.  # noqa: E501

        :param event_trigger: The event_trigger of this JitProvisioning.  # noqa: E501
        :type: str
        """
        allowed_values = ["NEW_USER_ONLY", "ALL_SAML_ASSERTIONS"]  # noqa: E501
        if (self._configuration.client_side_validation and
                event_trigger not in allowed_values):
            raise ValueError(
                "Invalid value for `event_trigger` ({0}), must be one of {1}"  # noqa: E501
                .format(event_trigger, allowed_values)
            )

        self._event_trigger = event_trigger

    @property
    def error_handling(self):
        """Gets the error_handling of this JitProvisioning.  # noqa: E501

        Specify behavior when provisioning request fails. The default is 'CONTINUE_SSO'.  # noqa: E501

        :return: The error_handling of this JitProvisioning.  # noqa: E501
        :rtype: str
        """
        return self._error_handling

    @error_handling.setter
    def error_handling(self, error_handling):
        """Sets the error_handling of this JitProvisioning.

        Specify behavior when provisioning request fails. The default is 'CONTINUE_SSO'.  # noqa: E501

        :param error_handling: The error_handling of this JitProvisioning.  # noqa: E501
        :type: str
        """
        allowed_values = ["CONTINUE_SSO", "ABORT_SSO"]  # noqa: E501
        if (self._configuration.client_side_validation and
                error_handling not in allowed_values):
            raise ValueError(
                "Invalid value for `error_handling` ({0}), must be one of {1}"  # noqa: E501
                .format(error_handling, allowed_values)
            )

        self._error_handling = error_handling

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
        if issubclass(JitProvisioning, dict):
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
        if not isinstance(other, JitProvisioning):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, JitProvisioning):
            return True

        return self.to_dict() != other.to_dict()