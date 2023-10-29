# OIDCProviderSettings

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scopes** | **str** | Space separated scope values that the OpenID Provider supports. | 
**authorization_endpoint** | **str** | URL of the OpenID Provider&#39;s OAuth 2.0 Authorization Endpoint. | 
**pushed_authorization_request_endpoint** | **str** | URL of the OpenID Provider&#39;s OAuth 2.0 Pushed Authorization Request Endpoint. | [optional] 
**login_type** | **str** | The OpenID Connect login type. These values maps to: &lt;br&gt;  CODE: Authentication using Code Flow &lt;br&gt; POST: Authentication using Form Post &lt;br&gt; POST_AT: Authentication using Form Post with Access Token | 
**authentication_scheme** | **str** | The OpenID Connect Authentication Scheme. This is required for Authentication using Code Flow.  | [optional] 
**authentication_signing_algorithm** | **str** | The authentication signing algorithm for token endpoint PRIVATE_KEY_JWT or CLIENT_SECRET_JWT authentication. Asymmetric algorithms are allowed for PRIVATE_KEY_JWT and symmetric algorithms are allowed for CLIENT_SECRET_JWT. For RSASSA-PSS signing algorithm, PingFederate must be integrated with a hardware security module (HSM) or Java 11. | [optional] 
**request_signing_algorithm** | **str** | The request signing algorithm. Required only if you wish to use signed requests. Only asymmetric algorithms are allowed. For RSASSA-PSS signing algorithm, PingFederate must be integrated with a hardware security module (HSM) or Java 11. | [optional] 
**enable_pkce** | **bool** | Enable Proof Key for Code Exchange (PKCE). When enabled, the client sends an SHA-256 code challenge and corresponding code verifier to the OpenID Provider during the authorization code flow. | [optional] 
**token_endpoint** | **str** | URL of the OpenID Provider&#39;s OAuth 2.0 Token Endpoint. | [optional] 
**user_info_endpoint** | **str** | URL of the OpenID Provider&#39;s UserInfo Endpoint. | [optional] 
**jwks_url** | **str** | URL of the OpenID Provider&#39;s JSON Web Key Set [JWK] document. | 
**track_user_sessions_for_logout** | **bool** | Determines whether PingFederate tracks a logout entry when a user signs in, so that the user session can later be terminated via back-channel logout. | [optional] 
**request_parameters** | [**list[OIDCRequestParameter]**](OIDCRequestParameter.md) | A list of request parameters. Request parameters with same name but different attribute values are treated as a multi-valued request parameter. | [optional] 
**redirect_uri** | **str** | The redirect URI. This is a read-only parameter. | [optional] 
**back_channel_logout_uri** | **str** | The Back-Channel Logout URI. This read-only parameter is available when user sessions are tracked for logout. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


