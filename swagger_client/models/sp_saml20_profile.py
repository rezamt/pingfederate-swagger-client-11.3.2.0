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


class SpSAML20Profile(object):
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
        'enable_xasp': 'bool'
    }

    attribute_map = {
        'enable_xasp': 'enableXASP'
    }

    def __init__(self, enable_xasp=None, _configuration=None):  # noqa: E501
        """SpSAML20Profile - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._enable_xasp = None
        self.discriminator = None

        if enable_xasp is not None:
            self.enable_xasp = enable_xasp

    @property
    def enable_xasp(self):
        """Gets the enable_xasp of this SpSAML20Profile.  # noqa: E501

        Enable Attribute Requester Mapping for X.509 Attribute Sharing Profile (XASP)  # noqa: E501

        :return: The enable_xasp of this SpSAML20Profile.  # noqa: E501
        :rtype: bool
        """
        return self._enable_xasp

    @enable_xasp.setter
    def enable_xasp(self, enable_xasp):
        """Sets the enable_xasp of this SpSAML20Profile.

        Enable Attribute Requester Mapping for X.509 Attribute Sharing Profile (XASP)  # noqa: E501

        :param enable_xasp: The enable_xasp of this SpSAML20Profile.  # noqa: E501
        :type: bool
        """

        self._enable_xasp = enable_xasp

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
        if issubclass(SpSAML20Profile, dict):
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
        if not isinstance(other, SpSAML20Profile):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SpSAML20Profile):
            return True

        return self.to_dict() != other.to_dict()
