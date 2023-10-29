# SpWsTrust

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**partner_service_ids** | **list[str]** | The partner service identifiers. | 
**o_auth_assertion_profiles** | **bool** | When selected, four additional token-type requests become available. | [optional] 
**default_token_type** | **str** | The default token type when a web service client (WSC) does not specify in the token request which token type the STS should issue. Defaults to SAML 2.0. | [optional] 
**generate_key** | **bool** | When selected, the STS generates a symmetric key to be used in conjunction with the \&quot;Holder of Key\&quot; (HoK) designation for the assertion&#39;s Subject Confirmation Method.  This option does not apply to OAuth assertion profiles. | [optional] 
**encrypt_saml2_assertion** | **bool** | When selected, the STS encrypts the SAML 2.0 assertion. Applicable only to SAML 2.0 security token.  This option does not apply to OAuth assertion profiles. | [optional] 
**minutes_before** | **int** | The amount of time before the SAML token was issued during which it is to be considered valid. The default value is 5. | [optional] 
**minutes_after** | **int** | The amount of time after the SAML token was issued during which it is to be considered valid. The default value is 30. | [optional] 
**attribute_contract** | [**SpWsTrustAttributeContract**](SpWsTrustAttributeContract.md) | A set of user attributes that the IdP sends in the token. | 
**token_processor_mappings** | [**list[IdpTokenProcessorMapping]**](IdpTokenProcessorMapping.md) | A list of token processors to validate incoming tokens. | 
**abort_if_not_fulfilled_from_request** | **bool** | If the attribute contract cannot be fulfilled using data from the Request, abort the transaction. | [optional] 
**request_contract_ref** | [**ResourceLink**](ResourceLink.md) | Request Contract to be used to map attribute values into the security token. | [optional] 
**message_customizations** | [**list[ProtocolMessageCustomization]**](ProtocolMessageCustomization.md) | The message customizations for WS-Trust. Depending on server settings, connection type, and protocol this may or may not be supported. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


