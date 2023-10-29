# IdpAdapterAttributeContract

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**core_attributes** | [**list[IdpAdapterAttribute]**](IdpAdapterAttribute.md) | A list of IdP adapter attributes that correspond to the attributes exposed by the IdP adapter type. | 
**extended_attributes** | [**list[IdpAdapterAttribute]**](IdpAdapterAttribute.md) | A list of additional attributes that can be returned by the IdP adapter. The extended attributes are only used if the adapter supports them. | [optional] 
**unique_user_key_attribute** | **str** | The attribute to use for uniquely identify a user&#39;s authentication sessions. | [optional] 
**mask_ognl_values** | **bool** | Whether or not all OGNL expressions used to fulfill an outgoing assertion contract should be masked in the logs. Defaults to false. | [optional] 
**inherited** | **bool** | Whether this attribute contract is inherited from its parent instance. If true, the rest of the properties in this model become read-only. The default value is false. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


