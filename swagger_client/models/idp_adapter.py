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


class IdpAdapter(object):
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
        'authn_ctx_class_ref': 'str',
        'attribute_mapping': 'IdpAdapterContractMapping',
        'attribute_contract': 'IdpAdapterAttributeContract'
    }

    attribute_map = {
        'authn_ctx_class_ref': 'authnCtxClassRef',
        'attribute_mapping': 'attributeMapping',
        'attribute_contract': 'attributeContract'
    }

    def __init__(self, authn_ctx_class_ref=None, attribute_mapping=None, attribute_contract=None, _configuration=None):  # noqa: E501
        """IdpAdapter - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._authn_ctx_class_ref = None
        self._attribute_mapping = None
        self._attribute_contract = None
        self.discriminator = None

        if authn_ctx_class_ref is not None:
            self.authn_ctx_class_ref = authn_ctx_class_ref
        if attribute_mapping is not None:
            self.attribute_mapping = attribute_mapping
        if attribute_contract is not None:
            self.attribute_contract = attribute_contract

    @property
    def authn_ctx_class_ref(self):
        """Gets the authn_ctx_class_ref of this IdpAdapter.  # noqa: E501

        The fixed value that indicates how the user was authenticated.  # noqa: E501

        :return: The authn_ctx_class_ref of this IdpAdapter.  # noqa: E501
        :rtype: str
        """
        return self._authn_ctx_class_ref

    @authn_ctx_class_ref.setter
    def authn_ctx_class_ref(self, authn_ctx_class_ref):
        """Sets the authn_ctx_class_ref of this IdpAdapter.

        The fixed value that indicates how the user was authenticated.  # noqa: E501

        :param authn_ctx_class_ref: The authn_ctx_class_ref of this IdpAdapter.  # noqa: E501
        :type: str
        """

        self._authn_ctx_class_ref = authn_ctx_class_ref

    @property
    def attribute_mapping(self):
        """Gets the attribute_mapping of this IdpAdapter.  # noqa: E501

        The attributes mapping from attribute sources to attribute targets.  # noqa: E501

        :return: The attribute_mapping of this IdpAdapter.  # noqa: E501
        :rtype: IdpAdapterContractMapping
        """
        return self._attribute_mapping

    @attribute_mapping.setter
    def attribute_mapping(self, attribute_mapping):
        """Sets the attribute_mapping of this IdpAdapter.

        The attributes mapping from attribute sources to attribute targets.  # noqa: E501

        :param attribute_mapping: The attribute_mapping of this IdpAdapter.  # noqa: E501
        :type: IdpAdapterContractMapping
        """

        self._attribute_mapping = attribute_mapping

    @property
    def attribute_contract(self):
        """Gets the attribute_contract of this IdpAdapter.  # noqa: E501

        The list of attributes that the IdP adapter provides.  # noqa: E501

        :return: The attribute_contract of this IdpAdapter.  # noqa: E501
        :rtype: IdpAdapterAttributeContract
        """
        return self._attribute_contract

    @attribute_contract.setter
    def attribute_contract(self, attribute_contract):
        """Sets the attribute_contract of this IdpAdapter.

        The list of attributes that the IdP adapter provides.  # noqa: E501

        :param attribute_contract: The attribute_contract of this IdpAdapter.  # noqa: E501
        :type: IdpAdapterAttributeContract
        """

        self._attribute_contract = attribute_contract

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
        if issubclass(IdpAdapter, dict):
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
        if not isinstance(other, IdpAdapter):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IdpAdapter):
            return True

        return self.to_dict() != other.to_dict()
