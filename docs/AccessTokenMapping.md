# AccessTokenMapping

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The id of the Access Token Mapping. | 
**context** | [**AccessTokenMappingContext**](AccessTokenMappingContext.md) | The context of the Access Token Mapping. This property cannot be changed after the mapping is created. | 
**access_token_manager_ref** | [**ResourceLink**](ResourceLink.md) | Reference to the access token manager this mapping is associated with. This property cannot be changed after the mapping is created. | 
**attribute_sources** | [**list[AttributeSource]**](AttributeSource.md) | A list of configured data stores to look up attributes from. | [optional] 
**attribute_contract_fulfillment** | [**dict(str, AttributeFulfillmentValue)**](AttributeFulfillmentValue.md) | A list of mappings from attribute names to their fulfillment values. | 
**issuance_criteria** | [**IssuanceCriteria**](IssuanceCriteria.md) | The issuance criteria that this transaction must meet before the corresponding attribute contract is fulfilled. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


