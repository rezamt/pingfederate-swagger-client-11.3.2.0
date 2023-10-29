# AccessTokenAttributeContract

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**core_attributes** | [**list[AccessTokenAttribute]**](AccessTokenAttribute.md) | A list of core token attributes that are associated with the access token management plugin type. This field is read-only and is ignored on POST/PUT. | [optional] 
**extended_attributes** | [**list[AccessTokenAttribute]**](AccessTokenAttribute.md) | A list of additional token attributes that are associated with this access token management plugin instance. | [optional] 
**inherited** | **bool** | Whether this attribute contract is inherited from its parent instance. If true, the rest of the properties in this model become read-only. The default value is false. | [optional] 
**default_subject_attribute** | **str** | Default subject attribute to use for audit logging when validating the access token. Blank value means to use USER_KEY attribute value after grant lookup. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


