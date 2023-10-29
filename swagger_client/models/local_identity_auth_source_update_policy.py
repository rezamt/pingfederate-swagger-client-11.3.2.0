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


class LocalIdentityAuthSourceUpdatePolicy(object):
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
        'store_attributes': 'bool',
        'retain_attributes': 'bool',
        'update_attributes': 'bool',
        'update_interval': 'float'
    }

    attribute_map = {
        'store_attributes': 'storeAttributes',
        'retain_attributes': 'retainAttributes',
        'update_attributes': 'updateAttributes',
        'update_interval': 'updateInterval'
    }

    def __init__(self, store_attributes=None, retain_attributes=None, update_attributes=None, update_interval=None, _configuration=None):  # noqa: E501
        """LocalIdentityAuthSourceUpdatePolicy - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._store_attributes = None
        self._retain_attributes = None
        self._update_attributes = None
        self._update_interval = None
        self.discriminator = None

        if store_attributes is not None:
            self.store_attributes = store_attributes
        if retain_attributes is not None:
            self.retain_attributes = retain_attributes
        if update_attributes is not None:
            self.update_attributes = update_attributes
        if update_interval is not None:
            self.update_interval = update_interval

    @property
    def store_attributes(self):
        """Gets the store_attributes of this LocalIdentityAuthSourceUpdatePolicy.  # noqa: E501

        Whether or not to store attributes that came from authentication sources.  # noqa: E501

        :return: The store_attributes of this LocalIdentityAuthSourceUpdatePolicy.  # noqa: E501
        :rtype: bool
        """
        return self._store_attributes

    @store_attributes.setter
    def store_attributes(self, store_attributes):
        """Sets the store_attributes of this LocalIdentityAuthSourceUpdatePolicy.

        Whether or not to store attributes that came from authentication sources.  # noqa: E501

        :param store_attributes: The store_attributes of this LocalIdentityAuthSourceUpdatePolicy.  # noqa: E501
        :type: bool
        """

        self._store_attributes = store_attributes

    @property
    def retain_attributes(self):
        """Gets the retain_attributes of this LocalIdentityAuthSourceUpdatePolicy.  # noqa: E501

        Whether or not to keep attributes after user disconnects.  # noqa: E501

        :return: The retain_attributes of this LocalIdentityAuthSourceUpdatePolicy.  # noqa: E501
        :rtype: bool
        """
        return self._retain_attributes

    @retain_attributes.setter
    def retain_attributes(self, retain_attributes):
        """Sets the retain_attributes of this LocalIdentityAuthSourceUpdatePolicy.

        Whether or not to keep attributes after user disconnects.  # noqa: E501

        :param retain_attributes: The retain_attributes of this LocalIdentityAuthSourceUpdatePolicy.  # noqa: E501
        :type: bool
        """

        self._retain_attributes = retain_attributes

    @property
    def update_attributes(self):
        """Gets the update_attributes of this LocalIdentityAuthSourceUpdatePolicy.  # noqa: E501

        Whether or not to update attributes when users authenticate.  # noqa: E501

        :return: The update_attributes of this LocalIdentityAuthSourceUpdatePolicy.  # noqa: E501
        :rtype: bool
        """
        return self._update_attributes

    @update_attributes.setter
    def update_attributes(self, update_attributes):
        """Sets the update_attributes of this LocalIdentityAuthSourceUpdatePolicy.

        Whether or not to update attributes when users authenticate.  # noqa: E501

        :param update_attributes: The update_attributes of this LocalIdentityAuthSourceUpdatePolicy.  # noqa: E501
        :type: bool
        """

        self._update_attributes = update_attributes

    @property
    def update_interval(self):
        """Gets the update_interval of this LocalIdentityAuthSourceUpdatePolicy.  # noqa: E501

        The minimum number of days between updates.  # noqa: E501

        :return: The update_interval of this LocalIdentityAuthSourceUpdatePolicy.  # noqa: E501
        :rtype: float
        """
        return self._update_interval

    @update_interval.setter
    def update_interval(self, update_interval):
        """Sets the update_interval of this LocalIdentityAuthSourceUpdatePolicy.

        The minimum number of days between updates.  # noqa: E501

        :param update_interval: The update_interval of this LocalIdentityAuthSourceUpdatePolicy.  # noqa: E501
        :type: float
        """

        self._update_interval = update_interval

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
        if issubclass(LocalIdentityAuthSourceUpdatePolicy, dict):
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
        if not isinstance(other, LocalIdentityAuthSourceUpdatePolicy):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, LocalIdentityAuthSourceUpdatePolicy):
            return True

        return self.to_dict() != other.to_dict()
