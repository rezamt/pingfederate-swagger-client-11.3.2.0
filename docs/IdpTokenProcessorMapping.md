# IdpTokenProcessorMapping

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**idp_token_processor_ref** | [**ResourceLink**](ResourceLink.md) | Reference to the associated token processor. | 
**restricted_virtual_entity_ids** | **list[str]** | The list of virtual server IDs that this mapping is restricted to. | [optional] 
**attribute_sources** | [**list[AttributeSource]**](AttributeSource.md) | A list of configured data stores to look up attributes from. | [optional] 
**attribute_contract_fulfillment** | [**dict(str, AttributeFulfillmentValue)**](AttributeFulfillmentValue.md) | A list of mappings from attribute names to their fulfillment values. | 
**issuance_criteria** | [**IssuanceCriteria**](IssuanceCriteria.md) | The issuance criteria that this transaction must meet before the corresponding attribute contract is fulfilled. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


