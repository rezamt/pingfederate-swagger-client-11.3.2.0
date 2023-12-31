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


class AuthorizationDetailType(object):
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
        'description': 'str',
        'type': 'str',
        'authorization_detail_processor_ref': 'ResourceLink',
        'active': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'description': 'description',
        'type': 'type',
        'authorization_detail_processor_ref': 'authorizationDetailProcessorRef',
        'active': 'active'
    }

    def __init__(self, id=None, description=None, type=None, authorization_detail_processor_ref=None, active=None, _configuration=None):  # noqa: E501
        """AuthorizationDetailType - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._description = None
        self._type = None
        self._authorization_detail_processor_ref = None
        self._active = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if description is not None:
            self.description = description
        self.type = type
        self.authorization_detail_processor_ref = authorization_detail_processor_ref
        if active is not None:
            self.active = active

    @property
    def id(self):
        """Gets the id of this AuthorizationDetailType.  # noqa: E501

        The ID of the authorization detail type. The ID will be system-assigned if not specified.  # noqa: E501

        :return: The id of this AuthorizationDetailType.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AuthorizationDetailType.

        The ID of the authorization detail type. The ID will be system-assigned if not specified.  # noqa: E501

        :param id: The id of this AuthorizationDetailType.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def description(self):
        """Gets the description of this AuthorizationDetailType.  # noqa: E501

        The description of the authorization detail type.  # noqa: E501

        :return: The description of this AuthorizationDetailType.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this AuthorizationDetailType.

        The description of the authorization detail type.  # noqa: E501

        :param description: The description of this AuthorizationDetailType.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def type(self):
        """Gets the type of this AuthorizationDetailType.  # noqa: E501

        The authorization detail type.  # noqa: E501

        :return: The type of this AuthorizationDetailType.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this AuthorizationDetailType.

        The authorization detail type.  # noqa: E501

        :param type: The type of this AuthorizationDetailType.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def authorization_detail_processor_ref(self):
        """Gets the authorization_detail_processor_ref of this AuthorizationDetailType.  # noqa: E501

        The authentication detail processor used to process this type.  # noqa: E501

        :return: The authorization_detail_processor_ref of this AuthorizationDetailType.  # noqa: E501
        :rtype: ResourceLink
        """
        return self._authorization_detail_processor_ref

    @authorization_detail_processor_ref.setter
    def authorization_detail_processor_ref(self, authorization_detail_processor_ref):
        """Sets the authorization_detail_processor_ref of this AuthorizationDetailType.

        The authentication detail processor used to process this type.  # noqa: E501

        :param authorization_detail_processor_ref: The authorization_detail_processor_ref of this AuthorizationDetailType.  # noqa: E501
        :type: ResourceLink
        """
        if self._configuration.client_side_validation and authorization_detail_processor_ref is None:
            raise ValueError("Invalid value for `authorization_detail_processor_ref`, must not be `None`")  # noqa: E501

        self._authorization_detail_processor_ref = authorization_detail_processor_ref

    @property
    def active(self):
        """Gets the active of this AuthorizationDetailType.  # noqa: E501

        Whether or not this authorization detail type is active. Defaults to true.  # noqa: E501

        :return: The active of this AuthorizationDetailType.  # noqa: E501
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this AuthorizationDetailType.

        Whether or not this authorization detail type is active. Defaults to true.  # noqa: E501

        :param active: The active of this AuthorizationDetailType.  # noqa: E501
        :type: bool
        """

        self._active = active

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
        if issubclass(AuthorizationDetailType, dict):
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
        if not isinstance(other, AuthorizationDetailType):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AuthorizationDetailType):
            return True

        return self.to_dict() != other.to_dict()
