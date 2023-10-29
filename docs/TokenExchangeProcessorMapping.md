# TokenExchangeProcessorMapping

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attribute_sources** | [**list[AttributeSource]**](AttributeSource.md) | A list of configured data stores to look up attributes from. | [optional] 
**attribute_contract_fulfillment** | [**dict(str, AttributeFulfillmentValue)**](AttributeFulfillmentValue.md) | A list of mappings from attribute names to their fulfillment values. | 
**issuance_criteria** | [**IssuanceCriteria**](IssuanceCriteria.md) | The issuance criteria that this transaction must meet before the corresponding attribute contract is fulfilled. | [optional] 
**subject_token_type** | **str** | The Subject token type | 
**subject_token_processor** | [**ResourceLink**](ResourceLink.md) | The Token processor used to process the subject token | 
**actor_token_type** | **str** | The Actor token type | [optional] 
**actor_token_processor** | [**ResourceLink**](ResourceLink.md) | The Token processor used to process the actor token | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


