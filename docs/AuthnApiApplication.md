# AuthnApiApplication

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The persistent, unique ID for the Authentication API application. It can be any combination of [a-zA-Z0-9._-]. This property is system-assigned if not specified. | 
**name** | **str** | The Authentication API Application Name. Name must be unique. | 
**url** | **str** | The Authentication API Application redirect URL. | 
**description** | **str** | The Authentication API Application description. | [optional] 
**additional_allowed_origins** | **list[str]** | The domain in the redirect URL is always whitelisted. This field contains a list of additional allowed origin URL&#39;s for cross-origin resource sharing. | [optional] 
**client_for_redirectless_mode_ref** | [**ResourceLink**](ResourceLink.md) | The client this application must use if it invokes the authentication API in redirectless mode. No client may be specified if restrictAccessToRedirectlessMode is false under /authenticationApi/settings. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


