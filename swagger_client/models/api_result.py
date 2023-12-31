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


class ApiResult(object):
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
        'result_id': 'str',
        'message': 'str',
        'developer_message': 'str',
        'validation_errors': 'list[ValidationError]'
    }

    attribute_map = {
        'result_id': 'resultId',
        'message': 'message',
        'developer_message': 'developerMessage',
        'validation_errors': 'validationErrors'
    }

    def __init__(self, result_id=None, message=None, developer_message=None, validation_errors=None, _configuration=None):  # noqa: E501
        """ApiResult - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._result_id = None
        self._message = None
        self._developer_message = None
        self._validation_errors = None
        self.discriminator = None

        if result_id is not None:
            self.result_id = result_id
        if message is not None:
            self.message = message
        if developer_message is not None:
            self.developer_message = developer_message
        if validation_errors is not None:
            self.validation_errors = validation_errors

    @property
    def result_id(self):
        """Gets the result_id of this ApiResult.  # noqa: E501

        Result identifier.  # noqa: E501

        :return: The result_id of this ApiResult.  # noqa: E501
        :rtype: str
        """
        return self._result_id

    @result_id.setter
    def result_id(self, result_id):
        """Sets the result_id of this ApiResult.

        Result identifier.  # noqa: E501

        :param result_id: The result_id of this ApiResult.  # noqa: E501
        :type: str
        """

        self._result_id = result_id

    @property
    def message(self):
        """Gets the message of this ApiResult.  # noqa: E501

        Success or error message.  # noqa: E501

        :return: The message of this ApiResult.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this ApiResult.

        Success or error message.  # noqa: E501

        :param message: The message of this ApiResult.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def developer_message(self):
        """Gets the developer_message of this ApiResult.  # noqa: E501

        Developer-oriented error message, if available.  # noqa: E501

        :return: The developer_message of this ApiResult.  # noqa: E501
        :rtype: str
        """
        return self._developer_message

    @developer_message.setter
    def developer_message(self, developer_message):
        """Sets the developer_message of this ApiResult.

        Developer-oriented error message, if available.  # noqa: E501

        :param developer_message: The developer_message of this ApiResult.  # noqa: E501
        :type: str
        """

        self._developer_message = developer_message

    @property
    def validation_errors(self):
        """Gets the validation_errors of this ApiResult.  # noqa: E501

        List of validation errors, if any.  # noqa: E501

        :return: The validation_errors of this ApiResult.  # noqa: E501
        :rtype: list[ValidationError]
        """
        return self._validation_errors

    @validation_errors.setter
    def validation_errors(self, validation_errors):
        """Sets the validation_errors of this ApiResult.

        List of validation errors, if any.  # noqa: E501

        :param validation_errors: The validation_errors of this ApiResult.  # noqa: E501
        :type: list[ValidationError]
        """

        self._validation_errors = validation_errors

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
        if issubclass(ApiResult, dict):
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
        if not isinstance(other, ApiResult):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ApiResult):
            return True

        return self.to_dict() != other.to_dict()
