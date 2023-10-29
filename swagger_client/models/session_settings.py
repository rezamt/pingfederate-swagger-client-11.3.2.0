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


class SessionSettings(object):
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
        'track_adapter_sessions_for_logout': 'bool',
        'revoke_user_session_on_logout': 'bool',
        'session_revocation_lifetime': 'int'
    }

    attribute_map = {
        'track_adapter_sessions_for_logout': 'trackAdapterSessionsForLogout',
        'revoke_user_session_on_logout': 'revokeUserSessionOnLogout',
        'session_revocation_lifetime': 'sessionRevocationLifetime'
    }

    def __init__(self, track_adapter_sessions_for_logout=None, revoke_user_session_on_logout=None, session_revocation_lifetime=None, _configuration=None):  # noqa: E501
        """SessionSettings - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._track_adapter_sessions_for_logout = None
        self._revoke_user_session_on_logout = None
        self._session_revocation_lifetime = None
        self.discriminator = None

        if track_adapter_sessions_for_logout is not None:
            self.track_adapter_sessions_for_logout = track_adapter_sessions_for_logout
        if revoke_user_session_on_logout is not None:
            self.revoke_user_session_on_logout = revoke_user_session_on_logout
        if session_revocation_lifetime is not None:
            self.session_revocation_lifetime = session_revocation_lifetime

    @property
    def track_adapter_sessions_for_logout(self):
        """Gets the track_adapter_sessions_for_logout of this SessionSettings.  # noqa: E501

        Determines whether adapter sessions are tracked for cleanup during single logout. The default is false.  # noqa: E501

        :return: The track_adapter_sessions_for_logout of this SessionSettings.  # noqa: E501
        :rtype: bool
        """
        return self._track_adapter_sessions_for_logout

    @track_adapter_sessions_for_logout.setter
    def track_adapter_sessions_for_logout(self, track_adapter_sessions_for_logout):
        """Sets the track_adapter_sessions_for_logout of this SessionSettings.

        Determines whether adapter sessions are tracked for cleanup during single logout. The default is false.  # noqa: E501

        :param track_adapter_sessions_for_logout: The track_adapter_sessions_for_logout of this SessionSettings.  # noqa: E501
        :type: bool
        """

        self._track_adapter_sessions_for_logout = track_adapter_sessions_for_logout

    @property
    def revoke_user_session_on_logout(self):
        """Gets the revoke_user_session_on_logout of this SessionSettings.  # noqa: E501

        Determines whether the user's session is revoked on logout. If this property is not provided on a PUT, the setting is left unchanged.  # noqa: E501

        :return: The revoke_user_session_on_logout of this SessionSettings.  # noqa: E501
        :rtype: bool
        """
        return self._revoke_user_session_on_logout

    @revoke_user_session_on_logout.setter
    def revoke_user_session_on_logout(self, revoke_user_session_on_logout):
        """Sets the revoke_user_session_on_logout of this SessionSettings.

        Determines whether the user's session is revoked on logout. If this property is not provided on a PUT, the setting is left unchanged.  # noqa: E501

        :param revoke_user_session_on_logout: The revoke_user_session_on_logout of this SessionSettings.  # noqa: E501
        :type: bool
        """

        self._revoke_user_session_on_logout = revoke_user_session_on_logout

    @property
    def session_revocation_lifetime(self):
        """Gets the session_revocation_lifetime of this SessionSettings.  # noqa: E501

        How long a session revocation is tracked and stored, in minutes. If this property is not provided on a PUT, the setting is left unchanged.  # noqa: E501

        :return: The session_revocation_lifetime of this SessionSettings.  # noqa: E501
        :rtype: int
        """
        return self._session_revocation_lifetime

    @session_revocation_lifetime.setter
    def session_revocation_lifetime(self, session_revocation_lifetime):
        """Sets the session_revocation_lifetime of this SessionSettings.

        How long a session revocation is tracked and stored, in minutes. If this property is not provided on a PUT, the setting is left unchanged.  # noqa: E501

        :param session_revocation_lifetime: The session_revocation_lifetime of this SessionSettings.  # noqa: E501
        :type: int
        """

        self._session_revocation_lifetime = session_revocation_lifetime

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
        if issubclass(SessionSettings, dict):
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
        if not isinstance(other, SessionSettings):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SessionSettings):
            return True

        return self.to_dict() != other.to_dict()
