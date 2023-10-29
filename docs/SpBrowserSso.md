# SpBrowserSso

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**protocol** | **str** | The browser-based SSO protocol to use. | 
**ws_fed_token_type** | **str** | The WS-Federation Token Type to use. | [optional] 
**ws_trust_version** | **str** | The WS-Trust version for a WS-Federation connection. The default version is WSTRUST12. | [optional] 
**enabled_profiles** | **list[str]** | The profiles that are enabled for browser-based SSO. SAML 2.0 supports all profiles whereas SAML 1.x IdP connections support both IdP and SP (non-standard) initiated SSO. This is required for SAMLx.x Connections.  | [optional] 
**incoming_bindings** | **list[str]** | The SAML bindings that are enabled for browser-based SSO. This is required for SAML 2.0 connections when the enabled profiles contain the SP-initiated SSO profile or either SLO profile. For SAML 1.x based connections, it is not used for SP Connections and it is optional for IdP Connections. | [optional] 
**message_customizations** | [**list[ProtocolMessageCustomization]**](ProtocolMessageCustomization.md) | The message customizations for browser-based SSO. Depending on server settings, connection type, and protocol this may or may not be supported. | [optional] 
**url_whitelist_entries** | [**list[UrlWhitelistEntry]**](UrlWhitelistEntry.md) | For WS-Federation connections, a whitelist of additional allowed domains and paths used to validate wreply for SLO, if enabled. | [optional] 
**artifact** | [**ArtifactSettings**](ArtifactSettings.md) | The settings for an artifact binding. | [optional] 
**slo_service_endpoints** | [**list[SloServiceEndpoint]**](SloServiceEndpoint.md) | A list of possible endpoints to send SLO requests and responses. | [optional] 
**default_target_url** | **str** | Default Target URL for SAML1.x connections. For SP connections, this default URL represents the destination on the SP where the user will be directed. For IdP connections, entering a URL in the Default Target URL field overrides the SP Default URL SSO setting. | [optional] 
**always_sign_artifact_response** | **bool** | Specify to always sign the SAML ArtifactResponse. | [optional] 
**sso_application_endpoint** | **str** | Application endpoint that can be used to invoke single sign-on (SSO) for the connection. This is a read-only parameter. | [optional] 
**sso_service_endpoints** | [**list[SpSsoServiceEndpoint]**](SpSsoServiceEndpoint.md) | A list of possible endpoints to send assertions to. | 
**sp_saml_identity_mapping** | **str** | Process in which users authenticated by the IdP are associated with user accounts local to the SP. | [optional] 
**sp_ws_fed_identity_mapping** | **str** | Process in which users authenticated by the IdP are associated with user accounts local to the SP for WS-Federation connection types. | [optional] 
**sign_response_as_required** | **bool** | Sign SAML Response as required by the associated binding and encryption policy. Applicable to SAML2.0 only and is defaulted to true. It can be set to false only on SAML2.0 connections when signAssertions is set to true. | [optional] 
**sign_assertions** | **bool** | Always sign the SAML Assertion. | [optional] 
**require_signed_authn_requests** | **bool** | Require AuthN requests to be signed when received via the POST or Redirect bindings. | [optional] 
**encryption_policy** | [**EncryptionPolicy**](EncryptionPolicy.md) | The SAML 2.0 encryption policy for browser-based SSO. Required for SAML 2.0 connections. | 
**attribute_contract** | [**SpBrowserSsoAttributeContract**](SpBrowserSsoAttributeContract.md) | A set of user attributes that the IdP sends in the SAML assertion. | 
**adapter_mappings** | [**list[IdpAdapterAssertionMapping]**](IdpAdapterAssertionMapping.md) | A list of adapters that map to outgoing assertions. | 
**authentication_policy_contract_assertion_mappings** | [**list[AuthenticationPolicyContractAssertionMapping]**](AuthenticationPolicyContractAssertionMapping.md) | A list of authentication policy contracts that map to outgoing assertions. | [optional] 
**assertion_lifetime** | [**AssertionLifetime**](AssertionLifetime.md) | The timeframe of validity before and after the issuance of the assertion. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


