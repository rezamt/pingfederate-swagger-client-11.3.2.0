# SpAdapterAttributeContract

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**core_attributes** | [**list[SpAdapterAttribute]**](SpAdapterAttribute.md) | A list of read-only attributes that are automatically populated by the SP adapter descriptor. | [optional] 
**extended_attributes** | [**list[SpAdapterAttribute]**](SpAdapterAttribute.md) | A list of additional attributes that can be returned by the SP adapter. The extended attributes are only used if the adapter supports them. | [optional] 
**inherited** | **bool** | Whether this attribute contract is inherited from its parent instance. If true, the rest of the properties in this model become read-only. The default value is false. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


