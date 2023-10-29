# OIDCRequestParameter

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Request parameter name. | 
**attribute_value** | [**AttributeFulfillmentValue**](AttributeFulfillmentValue.md) | A request parameter attribute value with source type. | 
**value** | **str** | A request parameter value. A parameter can have either a value or a attribute value but not both. Value set here will be converted to an attribute value of source type TEXT. An empty value will be converted to attribute value of source type NO_MAPPING. | [optional] 
**application_endpoint_override** | **bool** | Indicates whether the parameter value can be overridden by an Application Endpoint parameter | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


