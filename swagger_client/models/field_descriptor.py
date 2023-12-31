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


class FieldDescriptor(object):
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
        'type': 'str',
        'name': 'str',
        'description': 'str',
        'default_value': 'str',
        'default_for_legacy_config': 'str',
        'advanced': 'bool',
        'required': 'bool',
        'label': 'str'
    }

    attribute_map = {
        'type': 'type',
        'name': 'name',
        'description': 'description',
        'default_value': 'defaultValue',
        'default_for_legacy_config': 'defaultForLegacyConfig',
        'advanced': 'advanced',
        'required': 'required',
        'label': 'label'
    }

    discriminator_value_class_map = {
        'UploadFileFieldDescriptor': 'UploadFileFieldDescriptor',
        'SelectFieldDescriptor': 'SelectFieldDescriptor',
        'CheckBoxFieldDescriptor': 'CheckBoxFieldDescriptor',
        'RadioGroupFieldDescriptor': 'RadioGroupFieldDescriptor',
        'BaseSelectionFieldDescriptor': 'BaseSelectionFieldDescriptor',
        'HashedTextFieldDescriptor': 'HashedTextFieldDescriptor',
        'TextAreaFieldDescriptor': 'TextAreaFieldDescriptor',
        'TextFieldDescriptor': 'TextFieldDescriptor'
    }

    def __init__(self, type=None, name=None, description=None, default_value=None, default_for_legacy_config=None, advanced=None, required=None, label=None, _configuration=None):  # noqa: E501
        """FieldDescriptor - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._type = None
        self._name = None
        self._description = None
        self._default_value = None
        self._default_for_legacy_config = None
        self._advanced = None
        self._required = None
        self._label = None
        self.discriminator = 'type'

        if type is not None:
            self.type = type
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if default_value is not None:
            self.default_value = default_value
        if default_for_legacy_config is not None:
            self.default_for_legacy_config = default_for_legacy_config
        if advanced is not None:
            self.advanced = advanced
        if required is not None:
            self.required = required
        if label is not None:
            self.label = label

    @property
    def type(self):
        """Gets the type of this FieldDescriptor.  # noqa: E501

        The type of field descriptor.  # noqa: E501

        :return: The type of this FieldDescriptor.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this FieldDescriptor.

        The type of field descriptor.  # noqa: E501

        :param type: The type of this FieldDescriptor.  # noqa: E501
        :type: str
        """
        allowed_values = ["RADIO_GROUP", "SELECT", "FILTERABLE_SELECT", "CHECK_BOX", "TEXT_AREA", "TEXT", "UPLOAD_FILE", "HASHED_TEXT"]  # noqa: E501
        if (self._configuration.client_side_validation and
                type not in allowed_values):
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def name(self):
        """Gets the name of this FieldDescriptor.  # noqa: E501

        Name of the field.  # noqa: E501

        :return: The name of this FieldDescriptor.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this FieldDescriptor.

        Name of the field.  # noqa: E501

        :param name: The name of this FieldDescriptor.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this FieldDescriptor.  # noqa: E501

        Description of the field.  # noqa: E501

        :return: The description of this FieldDescriptor.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this FieldDescriptor.

        Description of the field.  # noqa: E501

        :param description: The description of this FieldDescriptor.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def default_value(self):
        """Gets the default_value of this FieldDescriptor.  # noqa: E501

        Default value of the field. This is the value pre-populated in the UI on new plugin instance configuration. This is also the value used to populate the field if it is missing in a POST or PUT request and no 'defaultForLegacyConfig' is defined.  # noqa: E501

        :return: The default_value of this FieldDescriptor.  # noqa: E501
        :rtype: str
        """
        return self._default_value

    @default_value.setter
    def default_value(self, default_value):
        """Sets the default_value of this FieldDescriptor.

        Default value of the field. This is the value pre-populated in the UI on new plugin instance configuration. This is also the value used to populate the field if it is missing in a POST or PUT request and no 'defaultForLegacyConfig' is defined.  # noqa: E501

        :param default_value: The default_value of this FieldDescriptor.  # noqa: E501
        :type: str
        """

        self._default_value = default_value

    @property
    def default_for_legacy_config(self):
        """Gets the default_for_legacy_config of this FieldDescriptor.  # noqa: E501

        Default value of the field when it is missing from the configuration (e.g. in upgrade scenarios). This is the value pre-populated in the UI for existing plugin configurations without values for the field. This is also the value used to populate the field if it is missing in a POST or PUT request. If 'defaultForLegacyConfig' is not defined, PingFederate will fall back to applying the 'defaultValue' to the field.  # noqa: E501

        :return: The default_for_legacy_config of this FieldDescriptor.  # noqa: E501
        :rtype: str
        """
        return self._default_for_legacy_config

    @default_for_legacy_config.setter
    def default_for_legacy_config(self, default_for_legacy_config):
        """Sets the default_for_legacy_config of this FieldDescriptor.

        Default value of the field when it is missing from the configuration (e.g. in upgrade scenarios). This is the value pre-populated in the UI for existing plugin configurations without values for the field. This is also the value used to populate the field if it is missing in a POST or PUT request. If 'defaultForLegacyConfig' is not defined, PingFederate will fall back to applying the 'defaultValue' to the field.  # noqa: E501

        :param default_for_legacy_config: The default_for_legacy_config of this FieldDescriptor.  # noqa: E501
        :type: str
        """

        self._default_for_legacy_config = default_for_legacy_config

    @property
    def advanced(self):
        """Gets the advanced of this FieldDescriptor.  # noqa: E501

        Whether this is an advanced field or not.  # noqa: E501

        :return: The advanced of this FieldDescriptor.  # noqa: E501
        :rtype: bool
        """
        return self._advanced

    @advanced.setter
    def advanced(self, advanced):
        """Sets the advanced of this FieldDescriptor.

        Whether this is an advanced field or not.  # noqa: E501

        :param advanced: The advanced of this FieldDescriptor.  # noqa: E501
        :type: bool
        """

        self._advanced = advanced

    @property
    def required(self):
        """Gets the required of this FieldDescriptor.  # noqa: E501

        Whether a value is required for this field or not.  # noqa: E501

        :return: The required of this FieldDescriptor.  # noqa: E501
        :rtype: bool
        """
        return self._required

    @required.setter
    def required(self, required):
        """Sets the required of this FieldDescriptor.

        Whether a value is required for this field or not.  # noqa: E501

        :param required: The required of this FieldDescriptor.  # noqa: E501
        :type: bool
        """

        self._required = required

    @property
    def label(self):
        """Gets the label of this FieldDescriptor.  # noqa: E501

        Label of the field to be displayed in the administrative console.  # noqa: E501

        :return: The label of this FieldDescriptor.  # noqa: E501
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this FieldDescriptor.

        Label of the field to be displayed in the administrative console.  # noqa: E501

        :param label: The label of this FieldDescriptor.  # noqa: E501
        :type: str
        """

        self._label = label

    def get_real_child_model(self, data):
        """Returns the real base class specified by the discriminator"""
        discriminator_value = data[self.discriminator].lower()
        return self.discriminator_value_class_map.get(discriminator_value)

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
        if issubclass(FieldDescriptor, dict):
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
        if not isinstance(other, FieldDescriptor):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FieldDescriptor):
            return True

        return self.to_dict() != other.to_dict()
