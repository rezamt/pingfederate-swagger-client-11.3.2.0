# TokenExchangeProcessorPolicy

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The Token Exchange processor policy ID. ID is unique. | 
**name** | **str** | The Token Exchange processor policy name. Name is unique. | 
**actor_token_required** | **bool** | Require an Actor token on a OAuth 2.0 Token Exchange request. | [optional] 
**attribute_contract** | [**TokenExchangeProcessorAttributeContract**](TokenExchangeProcessorAttributeContract.md) | A set of attributes exposed by an OAuth 2.0 Token Exchange Processor policy. | 
**processor_mappings** | [**list[TokenExchangeProcessorMapping]**](TokenExchangeProcessorMapping.md) | A list of Token Processor(s) mappings into an OAuth 2.0 Token Exchange Processor policy. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


