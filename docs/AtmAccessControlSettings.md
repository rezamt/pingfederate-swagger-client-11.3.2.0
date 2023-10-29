# AtmAccessControlSettings

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inherited** | **bool** | If this token manager has a parent, this flag determines whether access control settings are inherited from the parent. When set to true, the other fields in this model become read-only. The default value is false. | [optional] 
**restrict_clients** | **bool** | Determines whether access to this token manager is restricted to specific OAuth clients. If false, the &#39;allowedClients&#39; field is ignored. The default value is false. | [optional] 
**allowed_clients** | [**list[ResourceLink]**](ResourceLink.md) | If &#39;restrictClients&#39; is true, this field defines the list of OAuth clients that are allowed to access the token manager. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


