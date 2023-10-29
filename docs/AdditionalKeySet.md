# AdditionalKeySet

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique ID for the key set. It can be any combination of [a-zA-Z0-9._-]. This property is system-assigned if not specified. | [optional] 
**name** | **str** | The key set name. | 
**description** | **str** | A description of the key set. | [optional] 
**signing_keys** | [**SigningKeys**](SigningKeys.md) | A set of references to the keys. | 
**issuers** | [**list[ResourceLink]**](ResourceLink.md) | A list of virtual issuers that will use the current key set. Once assigned to a key set, the same virtual issuer cannot be assigned to another key set instance. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


