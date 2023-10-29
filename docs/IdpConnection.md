# IdpConnection

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**oidc_client_credentials** | [**OIDCClientCredentials**](OIDCClientCredentials.md) | The OIDC client credentials. This is required for an OIDC connection. | [optional] 
**idp_browser_sso** | [**IdpBrowserSso**](IdpBrowserSso.md) | The browser-based SSO settings used to communicate with your IdP. | [optional] 
**attribute_query** | [**IdpAttributeQuery**](IdpAttributeQuery.md) | The attribute query settings for requesting user attributes from an attribute authority. | [optional] 
**idp_o_auth_grant_attribute_mapping** | [**IdpOAuthGrantAttributeMapping**](IdpOAuthGrantAttributeMapping.md) | The OAuth Assertion Grant settings used to map from your IdP. | [optional] 
**ws_trust** | [**IdpWsTrust**](IdpWsTrust.md) | The Ws-Trust settings. | [optional] 
**inbound_provisioning** | [**IdpInboundProvisioning**](IdpInboundProvisioning.md) | The Inbound Provisioning settings used to provision user accounts and groups. | [optional] 
**error_page_msg_id** | **str** | Identifier that specifies the message displayed on a user-facing error page. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


