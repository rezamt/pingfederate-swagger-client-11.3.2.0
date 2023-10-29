# AuthenticationPolicy

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fail_if_no_selection** | **bool** | Fail if policy finds no authentication source. | [optional] 
**authn_selection_trees** | [**list[AuthenticationPolicyTree]**](AuthenticationPolicyTree.md) | The list of authentication policy trees. | [optional] 
**default_authentication_sources** | [**list[AuthenticationSource]**](AuthenticationSource.md) | The default authentication sources. | [optional] 
**tracked_http_parameters** | **list[str]** | The HTTP request parameters to track and make available to authentication sources, selectors, and contract mappings throughout the authentication policy. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


