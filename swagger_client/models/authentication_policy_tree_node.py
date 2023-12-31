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


class AuthenticationPolicyTreeNode(object):
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
        'action': 'PolicyAction',
        'children': 'list[AuthenticationPolicyTreeNode]'
    }

    attribute_map = {
        'action': 'action',
        'children': 'children'
    }

    def __init__(self, action=None, children=None, _configuration=None):  # noqa: E501
        """AuthenticationPolicyTreeNode - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._action = None
        self._children = None
        self.discriminator = None

        self.action = action
        if children is not None:
            self.children = children

    @property
    def action(self):
        """Gets the action of this AuthenticationPolicyTreeNode.  # noqa: E501

        The result action.  # noqa: E501

        :return: The action of this AuthenticationPolicyTreeNode.  # noqa: E501
        :rtype: PolicyAction
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this AuthenticationPolicyTreeNode.

        The result action.  # noqa: E501

        :param action: The action of this AuthenticationPolicyTreeNode.  # noqa: E501
        :type: PolicyAction
        """
        if self._configuration.client_side_validation and action is None:
            raise ValueError("Invalid value for `action`, must not be `None`")  # noqa: E501

        self._action = action

    @property
    def children(self):
        """Gets the children of this AuthenticationPolicyTreeNode.  # noqa: E501

        The nodes inside the authentication policy tree node of type AuthenticationPolicyTreeNode.  # noqa: E501

        :return: The children of this AuthenticationPolicyTreeNode.  # noqa: E501
        :rtype: list[AuthenticationPolicyTreeNode]
        """
        return self._children

    @children.setter
    def children(self, children):
        """Sets the children of this AuthenticationPolicyTreeNode.

        The nodes inside the authentication policy tree node of type AuthenticationPolicyTreeNode.  # noqa: E501

        :param children: The children of this AuthenticationPolicyTreeNode.  # noqa: E501
        :type: list[AuthenticationPolicyTreeNode]
        """

        self._children = children

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
        if issubclass(AuthenticationPolicyTreeNode, dict):
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
        if not isinstance(other, AuthenticationPolicyTreeNode):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AuthenticationPolicyTreeNode):
            return True

        return self.to_dict() != other.to_dict()
