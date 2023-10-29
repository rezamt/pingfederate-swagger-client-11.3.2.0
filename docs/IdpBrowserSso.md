# IdpBrowserSso

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**protocol** | **str** | The browser-based SSO protocol to use. | 
**oidc_provider_settings** | [**OIDCProviderSettings**](OIDCProviderSettings.md) | The OpenID Provider configuration settings. Required for an OIDC connection. | [optional] 
**enabled_profiles** | **list[str]** | The profiles that are enabled for browser-based SSO. SAML 2.0 supports all profiles whereas SAML 1.x IdP connections support both IdP and SP (non-standard) initiated SSO. This is required for SAMLx.x Connections.  | [optional] 
**incoming_bindings** | **list[str]** | The SAML bindings that are enabled for browser-based SSO. This is required for SAML 2.0 connections when the enabled profiles contain the SP-initiated SSO profile or either SLO profile. For SAML 1.x based connections, it is not used for SP Connections and it is optional for IdP Connections. | [optional] 
**message_customizations** | [**list[ProtocolMessageCustomization]**](ProtocolMessageCustomization.md) | The message customizations for browser-based SSO. Depending on server settings, connection type, and protocol this may or may not be supported. | [optional] 
**url_whitelist_entries** | [**list[UrlWhitelistEntry]**](UrlWhitelistEntry.md) | For WS-Federation connections, a whitelist of additional allowed domains and paths used to validate wreply for SLO, if enabled. | [optional] 
**artifact** | [**ArtifactSettings**](ArtifactSettings.md) | The settings for an artifact binding. | [optional] 
**slo_service_endpoints** | [**list[SloServiceEndpoint]**](SloServiceEndpoint.md) | A list of possible endpoints to send SLO requests and responses. | [optional] 
**always_sign_artifact_response** | **bool** | Specify to always sign the SAML ArtifactResponse. | [optional] 
**sso_application_endpoint** | **str** | Application endpoint that can be used to invoke single sign-on (SSO) for the connection. This is a read-only parameter. | [optional] 
**sso_service_endpoints** | [**list[IdpSsoServiceEndpoint]**](IdpSsoServiceEndpoint.md) | The IdP SSO endpoints that define where to send your authentication requests. Only required for SP initiated SSO. This is required for SAML x.x and WS-FED Connections. | [optional] 
**default_target_url** | **str** | The default target URL for this connection. If defined, this overrides the default URL. | [optional] 
**authn_context_mappings** | [**list[AuthnContextMapping]**](AuthnContextMapping.md) | A list of authentication context mappings between local and remote values. Applicable for SAML 2.0 and OIDC protocol connections. | [optional] 
**assertions_signed** | **bool** | Specify whether the incoming SAML assertions are signed rather than the entire SAML response being signed. | [optional] 
**sign_authn_requests** | **bool** | Determines whether SAML authentication requests should be signed. | [optional] 
**decryption_policy** | [**DecryptionPolicy**](DecryptionPolicy.md) | The SAML 2.0 decryption policy for browser-based SSO. | [optional] 
**idp_identity_mapping** | **str** | Defines the process in which users authenticated by the IdP are associated with user accounts local to the SP. | 
**attribute_contract** | [**IdpBrowserSsoAttributeContract**](IdpBrowserSsoAttributeContract.md) | The list of attributes that the IdP sends in the assertion. | [optional] 
**adapter_mappings** | [**list[SpAdapterMapping]**](SpAdapterMapping.md) | A list of adapters that map to incoming assertions. | [optional] 
**authentication_policy_contract_mappings** | [**list[AuthenticationPolicyContractMapping]**](AuthenticationPolicyContractMapping.md) | A list of Authentication Policy Contracts that map to incoming assertions. | [optional] 
**sso_o_auth_mapping** | [**SsoOAuthMapping**](SsoOAuthMapping.md) | Direct mapping from the IdP connection to the OAuth persistent grant. | [optional] 
**oauth_authentication_policy_contract_ref** | [**ResourceLink**](ResourceLink.md) | The Authentication policy contract to map into for OAuth. The policy contract can subsequently be mapped into the OAuth persistent grant. | [optional] 
**jit_provisioning** | [**JitProvisioning**](JitProvisioning.md) | JIT Provisioning of user accounts. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


