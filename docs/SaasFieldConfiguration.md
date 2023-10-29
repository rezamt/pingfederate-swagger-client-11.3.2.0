# SaasFieldConfiguration

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attribute_names** | **list[str]** | The list of source attribute names used to generate or map to a target field | [optional] 
**default_value** | **str** | The default value for the target field | [optional] 
**expression** | **str** | An OGNL expression to obtain a value. | [optional] 
**create_only** | **bool** | Indicates whether this field is a create only field and cannot be updated. | [optional] 
**trim** | **bool** | Indicates whether field should be trimmed before provisioning. | [optional] 
**character_case** | **str** | The character case of the field value. | [optional] 
**parser** | **str** | Indicates how the field shall be parsed. | [optional] 
**masked** | **bool** | Indicates whether the attribute should be masked in server logs. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


