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


class AuthenticationPolicyContract(object):
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
        'id': 'str',
        'name': 'str',
        'core_attributes': 'list[AuthenticationPolicyContractAttribute]',
        'extended_attributes': 'list[AuthenticationPolicyContractAttribute]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'core_attributes': 'coreAttributes',
        'extended_attributes': 'extendedAttributes'
    }

    def __init__(self, id=None, name=None, core_attributes=None, extended_attributes=None, _configuration=None):  # noqa: E501
        """AuthenticationPolicyContract - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._name = None
        self._core_attributes = None
        self._extended_attributes = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if core_attributes is not None:
            self.core_attributes = core_attributes
        if extended_attributes is not None:
            self.extended_attributes = extended_attributes

    @property
    def id(self):
        """Gets the id of this AuthenticationPolicyContract.  # noqa: E501

        The persistent, unique ID for the authentication policy contract. It can be any combination of [a-zA-Z0-9._-]. This property is system-assigned if not specified.  # noqa: E501

        :return: The id of this AuthenticationPolicyContract.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AuthenticationPolicyContract.

        The persistent, unique ID for the authentication policy contract. It can be any combination of [a-zA-Z0-9._-]. This property is system-assigned if not specified.  # noqa: E501

        :param id: The id of this AuthenticationPolicyContract.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this AuthenticationPolicyContract.  # noqa: E501

        The Authentication Policy Contract Name. Name is unique.  # noqa: E501

        :return: The name of this AuthenticationPolicyContract.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AuthenticationPolicyContract.

        The Authentication Policy Contract Name. Name is unique.  # noqa: E501

        :param name: The name of this AuthenticationPolicyContract.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def core_attributes(self):
        """Gets the core_attributes of this AuthenticationPolicyContract.  # noqa: E501

        A list of read-only assertion attributes (for example, subject) that are automatically populated by PingFederate.  # noqa: E501

        :return: The core_attributes of this AuthenticationPolicyContract.  # noqa: E501
        :rtype: list[AuthenticationPolicyContractAttribute]
        """
        return self._core_attributes

    @core_attributes.setter
    def core_attributes(self, core_attributes):
        """Sets the core_attributes of this AuthenticationPolicyContract.

        A list of read-only assertion attributes (for example, subject) that are automatically populated by PingFederate.  # noqa: E501

        :param core_attributes: The core_attributes of this AuthenticationPolicyContract.  # noqa: E501
        :type: list[AuthenticationPolicyContractAttribute]
        """

        self._core_attributes = core_attributes

    @property
    def extended_attributes(self):
        """Gets the extended_attributes of this AuthenticationPolicyContract.  # noqa: E501

        A list of additional attributes as needed.  # noqa: E501

        :return: The extended_attributes of this AuthenticationPolicyContract.  # noqa: E501
        :rtype: list[AuthenticationPolicyContractAttribute]
        """
        return self._extended_attributes

    @extended_attributes.setter
    def extended_attributes(self, extended_attributes):
        """Sets the extended_attributes of this AuthenticationPolicyContract.

        A list of additional attributes as needed.  # noqa: E501

        :param extended_attributes: The extended_attributes of this AuthenticationPolicyContract.  # noqa: E501
        :type: list[AuthenticationPolicyContractAttribute]
        """

        self._extended_attributes = extended_attributes

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
        if issubclass(AuthenticationPolicyContract, dict):
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
        if not isinstance(other, AuthenticationPolicyContract):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AuthenticationPolicyContract):
            return True

        return self.to_dict() != other.to_dict()
