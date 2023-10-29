# TokenProcessorAttributeContract

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**core_attributes** | [**list[TokenProcessorAttribute]**](TokenProcessorAttribute.md) | A list of token processor attributes that correspond to the attributes exposed by the token processor type. | 
**extended_attributes** | [**list[TokenProcessorAttribute]**](TokenProcessorAttribute.md) | A list of additional attributes that can be returned by the token processor. The extended attributes are only used if the token processor supports them. | [optional] 
**mask_ognl_values** | **bool** | Whether or not all OGNL expressions used to fulfill an outgoing assertion contract should be masked in the logs. Defaults to false. | [optional] 
**inherited** | **bool** | Whether this attribute contract is inherited from its parent instance. If true, the rest of the properties in this model become read-only. The default value is false. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


