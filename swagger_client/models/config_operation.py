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


class ConfigOperation(object):
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
        'resource_type': 'str',
        'sub_resource': 'str',
        'operation_type': 'str',
        'items': 'list[object]',
        'item_ids': 'list[str]'
    }

    attribute_map = {
        'resource_type': 'resourceType',
        'sub_resource': 'subResource',
        'operation_type': 'operationType',
        'items': 'items',
        'item_ids': 'itemIds'
    }

    def __init__(self, resource_type=None, sub_resource=None, operation_type=None, items=None, item_ids=None, _configuration=None):  # noqa: E501
        """ConfigOperation - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._resource_type = None
        self._sub_resource = None
        self._operation_type = None
        self._items = None
        self._item_ids = None
        self.discriminator = None

        self.resource_type = resource_type
        if sub_resource is not None:
            self.sub_resource = sub_resource
        self.operation_type = operation_type
        if items is not None:
            self.items = items
        if item_ids is not None:
            self.item_ids = item_ids

    @property
    def resource_type(self):
        """Gets the resource_type of this ConfigOperation.  # noqa: E501

        The identifier for the resource type the operation applies to.  # noqa: E501

        :return: The resource_type of this ConfigOperation.  # noqa: E501
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this ConfigOperation.

        The identifier for the resource type the operation applies to.  # noqa: E501

        :param resource_type: The resource_type of this ConfigOperation.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and resource_type is None:
            raise ValueError("Invalid value for `resource_type`, must not be `None`")  # noqa: E501

        self._resource_type = resource_type

    @property
    def sub_resource(self):
        """Gets the sub_resource of this ConfigOperation.  # noqa: E501

        The subresource for the operation.  # noqa: E501

        :return: The sub_resource of this ConfigOperation.  # noqa: E501
        :rtype: str
        """
        return self._sub_resource

    @sub_resource.setter
    def sub_resource(self, sub_resource):
        """Sets the sub_resource of this ConfigOperation.

        The subresource for the operation.  # noqa: E501

        :param sub_resource: The sub_resource of this ConfigOperation.  # noqa: E501
        :type: str
        """

        self._sub_resource = sub_resource

    @property
    def operation_type(self):
        """Gets the operation_type of this ConfigOperation.  # noqa: E501

        The type of operation to be performed.  # noqa: E501

        :return: The operation_type of this ConfigOperation.  # noqa: E501
        :rtype: str
        """
        return self._operation_type

    @operation_type.setter
    def operation_type(self, operation_type):
        """Sets the operation_type of this ConfigOperation.

        The type of operation to be performed.  # noqa: E501

        :param operation_type: The operation_type of this ConfigOperation.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and operation_type is None:
            raise ValueError("Invalid value for `operation_type`, must not be `None`")  # noqa: E501
        allowed_values = ["SAVE", "DELETE"]  # noqa: E501
        if (self._configuration.client_side_validation and
                operation_type not in allowed_values):
            raise ValueError(
                "Invalid value for `operation_type` ({0}), must be one of {1}"  # noqa: E501
                .format(operation_type, allowed_values)
            )

        self._operation_type = operation_type

    @property
    def items(self):
        """Gets the items of this ConfigOperation.  # noqa: E501

        The configuration items for the operation. This field only applies to the SAVE operation type.  # noqa: E501

        :return: The items of this ConfigOperation.  # noqa: E501
        :rtype: list[object]
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this ConfigOperation.

        The configuration items for the operation. This field only applies to the SAVE operation type.  # noqa: E501

        :param items: The items of this ConfigOperation.  # noqa: E501
        :type: list[object]
        """

        self._items = items

    @property
    def item_ids(self):
        """Gets the item_ids of this ConfigOperation.  # noqa: E501

        The item ID's for the operation. This field only applies to the DELETE operation type.  # noqa: E501

        :return: The item_ids of this ConfigOperation.  # noqa: E501
        :rtype: list[str]
        """
        return self._item_ids

    @item_ids.setter
    def item_ids(self, item_ids):
        """Sets the item_ids of this ConfigOperation.

        The item ID's for the operation. This field only applies to the DELETE operation type.  # noqa: E501

        :param item_ids: The item_ids of this ConfigOperation.  # noqa: E501
        :type: list[str]
        """

        self._item_ids = item_ids

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
        if issubclass(ConfigOperation, dict):
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
        if not isinstance(other, ConfigOperation):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ConfigOperation):
            return True

        return self.to_dict() != other.to_dict()
