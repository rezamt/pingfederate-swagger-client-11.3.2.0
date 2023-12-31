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


class SpWsTrust(object):
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
        'partner_service_ids': 'list[str]',
        'o_auth_assertion_profiles': 'bool',
        'default_token_type': 'str',
        'generate_key': 'bool',
        'encrypt_saml2_assertion': 'bool',
        'minutes_before': 'int',
        'minutes_after': 'int',
        'attribute_contract': 'SpWsTrustAttributeContract',
        'token_processor_mappings': 'list[IdpTokenProcessorMapping]',
        'abort_if_not_fulfilled_from_request': 'bool',
        'request_contract_ref': 'ResourceLink',
        'message_customizations': 'list[ProtocolMessageCustomization]'
    }

    attribute_map = {
        'partner_service_ids': 'partnerServiceIds',
        'o_auth_assertion_profiles': 'oAuthAssertionProfiles',
        'default_token_type': 'defaultTokenType',
        'generate_key': 'generateKey',
        'encrypt_saml2_assertion': 'encryptSaml2Assertion',
        'minutes_before': 'minutesBefore',
        'minutes_after': 'minutesAfter',
        'attribute_contract': 'attributeContract',
        'token_processor_mappings': 'tokenProcessorMappings',
        'abort_if_not_fulfilled_from_request': 'abortIfNotFulfilledFromRequest',
        'request_contract_ref': 'requestContractRef',
        'message_customizations': 'messageCustomizations'
    }

    def __init__(self, partner_service_ids=None, o_auth_assertion_profiles=None, default_token_type=None, generate_key=None, encrypt_saml2_assertion=None, minutes_before=None, minutes_after=None, attribute_contract=None, token_processor_mappings=None, abort_if_not_fulfilled_from_request=None, request_contract_ref=None, message_customizations=None, _configuration=None):  # noqa: E501
        """SpWsTrust - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._partner_service_ids = None
        self._o_auth_assertion_profiles = None
        self._default_token_type = None
        self._generate_key = None
        self._encrypt_saml2_assertion = None
        self._minutes_before = None
        self._minutes_after = None
        self._attribute_contract = None
        self._token_processor_mappings = None
        self._abort_if_not_fulfilled_from_request = None
        self._request_contract_ref = None
        self._message_customizations = None
        self.discriminator = None

        self.partner_service_ids = partner_service_ids
        if o_auth_assertion_profiles is not None:
            self.o_auth_assertion_profiles = o_auth_assertion_profiles
        if default_token_type is not None:
            self.default_token_type = default_token_type
        if generate_key is not None:
            self.generate_key = generate_key
        if encrypt_saml2_assertion is not None:
            self.encrypt_saml2_assertion = encrypt_saml2_assertion
        if minutes_before is not None:
            self.minutes_before = minutes_before
        if minutes_after is not None:
            self.minutes_after = minutes_after
        self.attribute_contract = attribute_contract
        self.token_processor_mappings = token_processor_mappings
        if abort_if_not_fulfilled_from_request is not None:
            self.abort_if_not_fulfilled_from_request = abort_if_not_fulfilled_from_request
        if request_contract_ref is not None:
            self.request_contract_ref = request_contract_ref
        if message_customizations is not None:
            self.message_customizations = message_customizations

    @property
    def partner_service_ids(self):
        """Gets the partner_service_ids of this SpWsTrust.  # noqa: E501

        The partner service identifiers.  # noqa: E501

        :return: The partner_service_ids of this SpWsTrust.  # noqa: E501
        :rtype: list[str]
        """
        return self._partner_service_ids

    @partner_service_ids.setter
    def partner_service_ids(self, partner_service_ids):
        """Sets the partner_service_ids of this SpWsTrust.

        The partner service identifiers.  # noqa: E501

        :param partner_service_ids: The partner_service_ids of this SpWsTrust.  # noqa: E501
        :type: list[str]
        """
        if self._configuration.client_side_validation and partner_service_ids is None:
            raise ValueError("Invalid value for `partner_service_ids`, must not be `None`")  # noqa: E501

        self._partner_service_ids = partner_service_ids

    @property
    def o_auth_assertion_profiles(self):
        """Gets the o_auth_assertion_profiles of this SpWsTrust.  # noqa: E501

        When selected, four additional token-type requests become available.  # noqa: E501

        :return: The o_auth_assertion_profiles of this SpWsTrust.  # noqa: E501
        :rtype: bool
        """
        return self._o_auth_assertion_profiles

    @o_auth_assertion_profiles.setter
    def o_auth_assertion_profiles(self, o_auth_assertion_profiles):
        """Sets the o_auth_assertion_profiles of this SpWsTrust.

        When selected, four additional token-type requests become available.  # noqa: E501

        :param o_auth_assertion_profiles: The o_auth_assertion_profiles of this SpWsTrust.  # noqa: E501
        :type: bool
        """

        self._o_auth_assertion_profiles = o_auth_assertion_profiles

    @property
    def default_token_type(self):
        """Gets the default_token_type of this SpWsTrust.  # noqa: E501

        The default token type when a web service client (WSC) does not specify in the token request which token type the STS should issue. Defaults to SAML 2.0.  # noqa: E501

        :return: The default_token_type of this SpWsTrust.  # noqa: E501
        :rtype: str
        """
        return self._default_token_type

    @default_token_type.setter
    def default_token_type(self, default_token_type):
        """Sets the default_token_type of this SpWsTrust.

        The default token type when a web service client (WSC) does not specify in the token request which token type the STS should issue. Defaults to SAML 2.0.  # noqa: E501

        :param default_token_type: The default_token_type of this SpWsTrust.  # noqa: E501
        :type: str
        """
        allowed_values = ["SAML20", "SAML11", "SAML11_O365"]  # noqa: E501
        if (self._configuration.client_side_validation and
                default_token_type not in allowed_values):
            raise ValueError(
                "Invalid value for `default_token_type` ({0}), must be one of {1}"  # noqa: E501
                .format(default_token_type, allowed_values)
            )

        self._default_token_type = default_token_type

    @property
    def generate_key(self):
        """Gets the generate_key of this SpWsTrust.  # noqa: E501

        When selected, the STS generates a symmetric key to be used in conjunction with the \"Holder of Key\" (HoK) designation for the assertion's Subject Confirmation Method.  This option does not apply to OAuth assertion profiles.  # noqa: E501

        :return: The generate_key of this SpWsTrust.  # noqa: E501
        :rtype: bool
        """
        return self._generate_key

    @generate_key.setter
    def generate_key(self, generate_key):
        """Sets the generate_key of this SpWsTrust.

        When selected, the STS generates a symmetric key to be used in conjunction with the \"Holder of Key\" (HoK) designation for the assertion's Subject Confirmation Method.  This option does not apply to OAuth assertion profiles.  # noqa: E501

        :param generate_key: The generate_key of this SpWsTrust.  # noqa: E501
        :type: bool
        """

        self._generate_key = generate_key

    @property
    def encrypt_saml2_assertion(self):
        """Gets the encrypt_saml2_assertion of this SpWsTrust.  # noqa: E501

        When selected, the STS encrypts the SAML 2.0 assertion. Applicable only to SAML 2.0 security token.  This option does not apply to OAuth assertion profiles.  # noqa: E501

        :return: The encrypt_saml2_assertion of this SpWsTrust.  # noqa: E501
        :rtype: bool
        """
        return self._encrypt_saml2_assertion

    @encrypt_saml2_assertion.setter
    def encrypt_saml2_assertion(self, encrypt_saml2_assertion):
        """Sets the encrypt_saml2_assertion of this SpWsTrust.

        When selected, the STS encrypts the SAML 2.0 assertion. Applicable only to SAML 2.0 security token.  This option does not apply to OAuth assertion profiles.  # noqa: E501

        :param encrypt_saml2_assertion: The encrypt_saml2_assertion of this SpWsTrust.  # noqa: E501
        :type: bool
        """

        self._encrypt_saml2_assertion = encrypt_saml2_assertion

    @property
    def minutes_before(self):
        """Gets the minutes_before of this SpWsTrust.  # noqa: E501

        The amount of time before the SAML token was issued during which it is to be considered valid. The default value is 5.  # noqa: E501

        :return: The minutes_before of this SpWsTrust.  # noqa: E501
        :rtype: int
        """
        return self._minutes_before

    @minutes_before.setter
    def minutes_before(self, minutes_before):
        """Sets the minutes_before of this SpWsTrust.

        The amount of time before the SAML token was issued during which it is to be considered valid. The default value is 5.  # noqa: E501

        :param minutes_before: The minutes_before of this SpWsTrust.  # noqa: E501
        :type: int
        """

        self._minutes_before = minutes_before

    @property
    def minutes_after(self):
        """Gets the minutes_after of this SpWsTrust.  # noqa: E501

        The amount of time after the SAML token was issued during which it is to be considered valid. The default value is 30.  # noqa: E501

        :return: The minutes_after of this SpWsTrust.  # noqa: E501
        :rtype: int
        """
        return self._minutes_after

    @minutes_after.setter
    def minutes_after(self, minutes_after):
        """Sets the minutes_after of this SpWsTrust.

        The amount of time after the SAML token was issued during which it is to be considered valid. The default value is 30.  # noqa: E501

        :param minutes_after: The minutes_after of this SpWsTrust.  # noqa: E501
        :type: int
        """

        self._minutes_after = minutes_after

    @property
    def attribute_contract(self):
        """Gets the attribute_contract of this SpWsTrust.  # noqa: E501

        A set of user attributes that the IdP sends in the token.  # noqa: E501

        :return: The attribute_contract of this SpWsTrust.  # noqa: E501
        :rtype: SpWsTrustAttributeContract
        """
        return self._attribute_contract

    @attribute_contract.setter
    def attribute_contract(self, attribute_contract):
        """Sets the attribute_contract of this SpWsTrust.

        A set of user attributes that the IdP sends in the token.  # noqa: E501

        :param attribute_contract: The attribute_contract of this SpWsTrust.  # noqa: E501
        :type: SpWsTrustAttributeContract
        """
        if self._configuration.client_side_validation and attribute_contract is None:
            raise ValueError("Invalid value for `attribute_contract`, must not be `None`")  # noqa: E501

        self._attribute_contract = attribute_contract

    @property
    def token_processor_mappings(self):
        """Gets the token_processor_mappings of this SpWsTrust.  # noqa: E501

        A list of token processors to validate incoming tokens.  # noqa: E501

        :return: The token_processor_mappings of this SpWsTrust.  # noqa: E501
        :rtype: list[IdpTokenProcessorMapping]
        """
        return self._token_processor_mappings

    @token_processor_mappings.setter
    def token_processor_mappings(self, token_processor_mappings):
        """Sets the token_processor_mappings of this SpWsTrust.

        A list of token processors to validate incoming tokens.  # noqa: E501

        :param token_processor_mappings: The token_processor_mappings of this SpWsTrust.  # noqa: E501
        :type: list[IdpTokenProcessorMapping]
        """
        if self._configuration.client_side_validation and token_processor_mappings is None:
            raise ValueError("Invalid value for `token_processor_mappings`, must not be `None`")  # noqa: E501

        self._token_processor_mappings = token_processor_mappings

    @property
    def abort_if_not_fulfilled_from_request(self):
        """Gets the abort_if_not_fulfilled_from_request of this SpWsTrust.  # noqa: E501

        If the attribute contract cannot be fulfilled using data from the Request, abort the transaction.  # noqa: E501

        :return: The abort_if_not_fulfilled_from_request of this SpWsTrust.  # noqa: E501
        :rtype: bool
        """
        return self._abort_if_not_fulfilled_from_request

    @abort_if_not_fulfilled_from_request.setter
    def abort_if_not_fulfilled_from_request(self, abort_if_not_fulfilled_from_request):
        """Sets the abort_if_not_fulfilled_from_request of this SpWsTrust.

        If the attribute contract cannot be fulfilled using data from the Request, abort the transaction.  # noqa: E501

        :param abort_if_not_fulfilled_from_request: The abort_if_not_fulfilled_from_request of this SpWsTrust.  # noqa: E501
        :type: bool
        """

        self._abort_if_not_fulfilled_from_request = abort_if_not_fulfilled_from_request

    @property
    def request_contract_ref(self):
        """Gets the request_contract_ref of this SpWsTrust.  # noqa: E501

        Request Contract to be used to map attribute values into the security token.  # noqa: E501

        :return: The request_contract_ref of this SpWsTrust.  # noqa: E501
        :rtype: ResourceLink
        """
        return self._request_contract_ref

    @request_contract_ref.setter
    def request_contract_ref(self, request_contract_ref):
        """Sets the request_contract_ref of this SpWsTrust.

        Request Contract to be used to map attribute values into the security token.  # noqa: E501

        :param request_contract_ref: The request_contract_ref of this SpWsTrust.  # noqa: E501
        :type: ResourceLink
        """

        self._request_contract_ref = request_contract_ref

    @property
    def message_customizations(self):
        """Gets the message_customizations of this SpWsTrust.  # noqa: E501

        The message customizations for WS-Trust. Depending on server settings, connection type, and protocol this may or may not be supported.  # noqa: E501

        :return: The message_customizations of this SpWsTrust.  # noqa: E501
        :rtype: list[ProtocolMessageCustomization]
        """
        return self._message_customizations

    @message_customizations.setter
    def message_customizations(self, message_customizations):
        """Sets the message_customizations of this SpWsTrust.

        The message customizations for WS-Trust. Depending on server settings, connection type, and protocol this may or may not be supported.  # noqa: E501

        :param message_customizations: The message_customizations of this SpWsTrust.  # noqa: E501
        :type: list[ProtocolMessageCustomization]
        """

        self._message_customizations = message_customizations

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
        if issubclass(SpWsTrust, dict):
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
        if not isinstance(other, SpWsTrust):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SpWsTrust):
            return True

        return self.to_dict() != other.to_dict()
