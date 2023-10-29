# SpAttributeQuery

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | **list[str]** | The list of attributes that may be returned to the SP in the response to an attribute request. | 
**attribute_contract_fulfillment** | [**dict(str, AttributeFulfillmentValue)**](AttributeFulfillmentValue.md) | A list of mappings from attribute names to their fulfillment values. | 
**issuance_criteria** | [**IssuanceCriteria**](IssuanceCriteria.md) | The issuance criteria that this transaction must meet before the corresponding attribute contract is fulfilled. | [optional] 
**policy** | [**SpAttributeQueryPolicy**](SpAttributeQueryPolicy.md) | The attribute query profile&#39;s security policy. | [optional] 
**attribute_sources** | [**list[AttributeSource]**](AttributeSource.md) | A list of configured data stores to look up attributes from. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


