# SaasPluginFieldInfoDescriptor

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | The name or code that represents a field. | 
**label** | **str** | The label for a field. | 
**required** | **bool** | Indicates whether a value is required for this field. | [optional] 
**unique** | **bool** | indicates whether the value of this field is unique. | [optional] 
**multi_value** | **bool** | Whether the field can have multiple values. | [optional] 
**options** | [**list[SaasPluginFieldOption]**](SaasPluginFieldOption.md) | List of Option values available for this field. | [optional] 
**min_length** | **int** | Minimum character length for a value. | [optional] 
**max_length** | **int** | Maximum character length for a value. | [optional] 
**pattern** | **str** | Pattern used to validate values of this field. | [optional] 
**notes** | **list[str]** | Description or notes for the field. | [optional] 
**default_value** | **str** | Default value for the field. | [optional] 
**ds_ldap_map** | **bool** | Indicates whether the field can be mapped raw to an LDAP attribute. | [optional] 
**persist_for_membership** | **bool** | The code that represents the field. | [optional] 
**attribute_group** | **bool** | Indicates whether this field belongs to group of attribute such as multivalued or sub-type custom attributes. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


