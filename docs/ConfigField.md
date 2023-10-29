# ConfigField

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the configuration field. | 
**value** | **str** | The value for the configuration field. For encrypted or hashed fields, GETs will not return this attribute. To update an encrypted or hashed field, specify the new value in this attribute. | [optional] 
**encrypted_value** | **str** | For encrypted or hashed fields, this attribute contains the encrypted representation of the field&#39;s value, if a value is defined. If you do not want to update the stored value, this attribute should be passed back unchanged. | [optional] 
**inherited** | **bool** | Whether this field is inherited from its parent instance. If true, the value/encrypted value properties become read-only. The default value is false. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


