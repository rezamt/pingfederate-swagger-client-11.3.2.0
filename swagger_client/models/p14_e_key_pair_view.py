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


class P14EKeyPairView(object):
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
        'current_authentication_key': 'bool',
        'previous_authentication_key': 'bool',
        'key_pair_view': 'CertView',
        'creation_time': 'datetime'
    }

    attribute_map = {
        'current_authentication_key': 'currentAuthenticationKey',
        'previous_authentication_key': 'previousAuthenticationKey',
        'key_pair_view': 'keyPairView',
        'creation_time': 'creationTime'
    }

    def __init__(self, current_authentication_key=None, previous_authentication_key=None, key_pair_view=None, creation_time=None, _configuration=None):  # noqa: E501
        """P14EKeyPairView - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._current_authentication_key = None
        self._previous_authentication_key = None
        self._key_pair_view = None
        self._creation_time = None
        self.discriminator = None

        if current_authentication_key is not None:
            self.current_authentication_key = current_authentication_key
        if previous_authentication_key is not None:
            self.previous_authentication_key = previous_authentication_key
        if key_pair_view is not None:
            self.key_pair_view = key_pair_view
        if creation_time is not None:
            self.creation_time = creation_time

    @property
    def current_authentication_key(self):
        """Gets the current_authentication_key of this P14EKeyPairView.  # noqa: E501

        Indicates whether this is the current key used to authenticate with PingOne.  # noqa: E501

        :return: The current_authentication_key of this P14EKeyPairView.  # noqa: E501
        :rtype: bool
        """
        return self._current_authentication_key

    @current_authentication_key.setter
    def current_authentication_key(self, current_authentication_key):
        """Sets the current_authentication_key of this P14EKeyPairView.

        Indicates whether this is the current key used to authenticate with PingOne.  # noqa: E501

        :param current_authentication_key: The current_authentication_key of this P14EKeyPairView.  # noqa: E501
        :type: bool
        """

        self._current_authentication_key = current_authentication_key

    @property
    def previous_authentication_key(self):
        """Gets the previous_authentication_key of this P14EKeyPairView.  # noqa: E501

        Indicates whether this is the previous key used to authenticate with PingOne.  # noqa: E501

        :return: The previous_authentication_key of this P14EKeyPairView.  # noqa: E501
        :rtype: bool
        """
        return self._previous_authentication_key

    @previous_authentication_key.setter
    def previous_authentication_key(self, previous_authentication_key):
        """Sets the previous_authentication_key of this P14EKeyPairView.

        Indicates whether this is the previous key used to authenticate with PingOne.  # noqa: E501

        :param previous_authentication_key: The previous_authentication_key of this P14EKeyPairView.  # noqa: E501
        :type: bool
        """

        self._previous_authentication_key = previous_authentication_key

    @property
    def key_pair_view(self):
        """Gets the key_pair_view of this P14EKeyPairView.  # noqa: E501

        The PingOne for Enterprise key pair details.  # noqa: E501

        :return: The key_pair_view of this P14EKeyPairView.  # noqa: E501
        :rtype: CertView
        """
        return self._key_pair_view

    @key_pair_view.setter
    def key_pair_view(self, key_pair_view):
        """Sets the key_pair_view of this P14EKeyPairView.

        The PingOne for Enterprise key pair details.  # noqa: E501

        :param key_pair_view: The key_pair_view of this P14EKeyPairView.  # noqa: E501
        :type: CertView
        """

        self._key_pair_view = key_pair_view

    @property
    def creation_time(self):
        """Gets the creation_time of this P14EKeyPairView.  # noqa: E501

        The creation time of the key.  # noqa: E501

        :return: The creation_time of this P14EKeyPairView.  # noqa: E501
        :rtype: datetime
        """
        return self._creation_time

    @creation_time.setter
    def creation_time(self, creation_time):
        """Sets the creation_time of this P14EKeyPairView.

        The creation time of the key.  # noqa: E501

        :param creation_time: The creation_time of this P14EKeyPairView.  # noqa: E501
        :type: datetime
        """

        self._creation_time = creation_time

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
        if issubclass(P14EKeyPairView, dict):
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
        if not isinstance(other, P14EKeyPairView):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, P14EKeyPairView):
            return True

        return self.to_dict() != other.to_dict()