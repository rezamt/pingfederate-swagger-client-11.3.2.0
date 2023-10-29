# IdpToSpAdapterMapping

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attribute_sources** | [**list[AttributeSource]**](AttributeSource.md) | A list of configured data stores to look up attributes from. | [optional] 
**attribute_contract_fulfillment** | [**dict(str, AttributeFulfillmentValue)**](AttributeFulfillmentValue.md) | A list of mappings from attribute names to their fulfillment values. | 
**issuance_criteria** | [**IssuanceCriteria**](IssuanceCriteria.md) | The issuance criteria that this transaction must meet before the corresponding attribute contract is fulfilled. | [optional] 
**source_id** | **str** | The id of the IdP Adapter. | 
**target_id** | **str** | The id of the SP Adapter. | 
**id** | **str** | The id of the IdP-to-SP Adapter mapping. This field is read-only and is ignored when passed in with the payload. | [optional] 
**default_target_resource** | **str** | Default target URL for this adapter-to-adapter mapping configuration. | [optional] 
**license_connection_group_assignment** | **str** | The license connection group. | [optional] 
**application_name** | **str** | The application name. | [optional] 
**application_icon_url** | **str** | The application icon URL. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


