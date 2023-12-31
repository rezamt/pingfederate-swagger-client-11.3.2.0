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


class ResourceUsage(object):
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
        'category_id': 'str',
        'type': 'str',
        'ref': 'ResourceLink'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'category_id': 'categoryId',
        'type': 'type',
        'ref': 'ref'
    }

    def __init__(self, id=None, name=None, category_id=None, type=None, ref=None, _configuration=None):  # noqa: E501
        """ResourceUsage - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._name = None
        self._category_id = None
        self._type = None
        self._ref = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if category_id is not None:
            self.category_id = category_id
        if type is not None:
            self.type = type
        if ref is not None:
            self.ref = ref

    @property
    def id(self):
        """Gets the id of this ResourceUsage.  # noqa: E501

        The ID of the referencing resource.  # noqa: E501

        :return: The id of this ResourceUsage.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ResourceUsage.

        The ID of the referencing resource.  # noqa: E501

        :param id: The id of this ResourceUsage.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this ResourceUsage.  # noqa: E501

        The name of the referencing resource.  # noqa: E501

        :return: The name of this ResourceUsage.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ResourceUsage.

        The name of the referencing resource.  # noqa: E501

        :param name: The name of this ResourceUsage.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def category_id(self):
        """Gets the category_id of this ResourceUsage.  # noqa: E501

        The category of the referencing resource.  # noqa: E501

        :return: The category_id of this ResourceUsage.  # noqa: E501
        :rtype: str
        """
        return self._category_id

    @category_id.setter
    def category_id(self, category_id):
        """Sets the category_id of this ResourceUsage.

        The category of the referencing resource.  # noqa: E501

        :param category_id: The category_id of this ResourceUsage.  # noqa: E501
        :type: str
        """
        allowed_values = ["IDP_CONNECTION", "SP_CONNECTION", "PASSWORD_CREDENTIAL_VALIDATOR", "AUTHENTICATION_SELECTOR", "IDP_ADAPTER", "SP_ADAPTER", "ACCESS_TOKEN_MGMT_PLUGIN", "TOKEN_PROCESSOR", "TOKEN_GENERATOR", "NOTIFICATION_PUBLISHER", "OOB_AUTH_PLUGIN", "DATA_STORE", "DYNAMIC_CLIENT_REGISTRATION_PLUGIN", "RISK_PROVIDER", "IDENTITY_STORE_PROVISIONER"]  # noqa: E501
        if (self._configuration.client_side_validation and
                category_id not in allowed_values):
            raise ValueError(
                "Invalid value for `category_id` ({0}), must be one of {1}"  # noqa: E501
                .format(category_id, allowed_values)
            )

        self._category_id = category_id

    @property
    def type(self):
        """Gets the type of this ResourceUsage.  # noqa: E501

        The type of the referencing resource. In the case of plugins, this is the plugin type. Otherwise, it is usually the same as the name of the category.  # noqa: E501

        :return: The type of this ResourceUsage.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ResourceUsage.

        The type of the referencing resource. In the case of plugins, this is the plugin type. Otherwise, it is usually the same as the name of the category.  # noqa: E501

        :param type: The type of this ResourceUsage.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def ref(self):
        """Gets the ref of this ResourceUsage.  # noqa: E501

        A link to the referencing resource.  # noqa: E501

        :return: The ref of this ResourceUsage.  # noqa: E501
        :rtype: ResourceLink
        """
        return self._ref

    @ref.setter
    def ref(self, ref):
        """Sets the ref of this ResourceUsage.

        A link to the referencing resource.  # noqa: E501

        :param ref: The ref of this ResourceUsage.  # noqa: E501
        :type: ResourceLink
        """

        self._ref = ref

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
        if issubclass(ResourceUsage, dict):
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
        if not isinstance(other, ResourceUsage):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ResourceUsage):
            return True

        return self.to_dict() != other.to_dict()
