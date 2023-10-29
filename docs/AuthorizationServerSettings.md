# AuthorizationServerSettings

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default_scope_description** | **str** | The default scope description. | 
**scopes** | [**list[ScopeEntry]**](ScopeEntry.md) | The list of common scopes. | [optional] 
**scope_groups** | [**list[ScopeGroupEntry]**](ScopeGroupEntry.md) | The list of common scope groups. | [optional] 
**exclusive_scopes** | [**list[ScopeEntry]**](ScopeEntry.md) | The list of exclusive scopes. | [optional] 
**exclusive_scope_groups** | [**list[ScopeGroupEntry]**](ScopeGroupEntry.md) | The list of exclusive scope groups. | [optional] 
**authorization_code_timeout** | **int** | The authorization code timeout, in seconds. | 
**authorization_code_entropy** | **int** | The authorization code entropy, in bytes. | 
**disallow_plain_pkce** | **bool** | Determines whether PKCE&#39;s &#39;plain&#39; code challenge method will be disallowed. The default value is false. | [optional] 
**include_issuer_in_authorization_response** | **bool** | Determines whether the authorization server&#39;s issuer value is added to the authorization response or not. The default value is false. | [optional] 
**track_user_sessions_for_logout** | **bool** | Determines whether user sessions are tracked for logout. If this property is not provided on a PUT, the setting is left unchanged. | [optional] 
**token_endpoint_base_url** | **str** | The token endpoint base URL used to validate the &#39;aud&#39; claim during Private Key JWT Client Authentication. | [optional] 
**persistent_grant_lifetime** | **int** | The persistent grant lifetime. The default value is indefinite. -1 indicates an indefinite amount of time. | [optional] 
**persistent_grant_lifetime_unit** | **str** | The persistent grant lifetime unit. | [optional] 
**persistent_grant_idle_timeout** | **int** | The persistent grant idle timeout. The default value is 30 (days). -1 indicates an indefinite amount of time. | [optional] 
**persistent_grant_idle_timeout_time_unit** | **str** | The persistent grant idle timeout time unit. | [optional] 
**refresh_token_length** | **int** | The refresh token length in number of characters. | 
**roll_refresh_token_values** | **bool** | The roll refresh token values default policy. The default value is true. | [optional] 
**refresh_token_rolling_grace_period** | **int** | The grace period that a rolled refresh token remains valid in seconds. The default value is 60. | [optional] 
**refresh_rolling_interval** | **int** | The minimum interval to roll refresh tokens, in hours. | 
**persistent_grant_reuse_grant_types** | **list[str]** | The grant types that the OAuth AS can reuse rather than creating a new grant for each request. Only &#39;IMPLICIT&#39; or &#39;AUTHORIZATION_CODE&#39; or &#39;RESOURCE_OWNER_CREDENTIALS&#39; are valid grant types. | [optional] 
**persistent_grant_contract** | [**PersistentGrantContract**](PersistentGrantContract.md) | The persistent grant contract defines attributes that are associated with OAuth persistent grants. | [optional] 
**bypass_authorization_for_approved_grants** | **bool** | Bypass authorization for previously approved persistent grants. The default value is false. | [optional] 
**allow_unidentified_client_ro_creds** | **bool** | Allow unidentified clients to request resource owner password credentials grants. The default value is false. | [optional] 
**allow_unidentified_client_extension_grants** | **bool** | Allow unidentified clients to request extension grants. The default value is false. | [optional] 
**admin_web_service_pcv_ref** | [**ResourceLink**](ResourceLink.md) | The password credential validator reference that is used for authenticating access to the OAuth Administrative Web Service. | [optional] 
**atm_id_for_o_auth_grant_management** | **str** | The ID of the Access Token Manager used for OAuth enabled grant management. | [optional] 
**scope_for_o_auth_grant_management** | **str** | The OAuth scope to validate when accessing grant management service. | [optional] 
**allowed_origins** | **list[str]** | The list of allowed origins. | [optional] 
**user_authorization_url** | **str** | The URL used to generate &#39;verification_url&#39; and &#39;verification_url_complete&#39; values in a Device Authorization request | [optional] 
**registered_authorization_path** | **str** | The Registered Authorization Path is concatenated to PingFederate base URL to generate &#39;verification_url&#39; and &#39;verification_url_complete&#39; values in a Device Authorization request. PingFederate listens to this path if specified | 
**pending_authorization_timeout** | **int** | The &#39;device_code&#39; and &#39;user_code&#39; timeout, in seconds. | 
**device_polling_interval** | **int** | The amount of time client should wait between polling requests, in seconds. | 
**activation_code_check_mode** | **str** | Determines whether the user is prompted to enter or confirm the activation code after authenticating or before. The default is AFTER_AUTHENTICATION. | [optional] 
**bypass_activation_code_confirmation** | **bool** | Indicates if the Activation Code Confirmation page should be bypassed if &#39;verification_url_complete&#39; is used by the end user to authorize a device. | 
**user_authorization_consent_page_setting** | **str** | User Authorization Consent Page setting to use PingFederate&#39;s internal consent page or an external system | [optional] 
**user_authorization_consent_adapter** | **str** | Adapter ID of the external consent adapter to be used for the consent page user interface. | [optional] 
**approved_scopes_attribute** | **str** | Attribute from the external consent adapter&#39;s contract, intended for storing approved scopes returned by the external consent page. | [optional] 
**approved_authorization_detail_attribute** | **str** | Attribute from the external consent adapter&#39;s contract, intended for storing approved authorization details returned by the external consent page. | [optional] 
**par_reference_timeout** | **int** | The timeout, in seconds, of the pushed authorization request reference. The default value is 60. | [optional] 
**par_reference_length** | **int** | The entropy of pushed authorization request references, in bytes. The default value is 24. | [optional] 
**par_status** | **str** | The status of pushed authorization request support. The default value is ENABLED. | [optional] 
**client_secret_retention_period** | **int** | The length of time in minutes that client secrets will be retained as secondary secrets after secret change. The default value is 0, which will disable secondary client secret retention. | [optional] 
**jwt_secured_authorization_response_mode_lifetime** | **int** | The lifetime, in seconds, of the JWT Secured authorization response. The default value is 600. | [optional] 
**dpop_proof_require_nonce** | **bool** | Determines whether nonce is required in the Demonstrating Proof-of-Possession (DPoP) proof JWT. The default value is false. | [optional] 
**dpop_proof_lifetime_seconds** | **int** | The lifetime, in seconds, of the Demonstrating Proof-of-Possession (DPoP) proof JWT. The default value is 120. | [optional] 
**dpop_proof_enforce_replay_prevention** | **bool** | Determines whether Demonstrating Proof-of-Possession (DPoP) proof JWT replay prevention is enforced. The default value is false. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


