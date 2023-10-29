# IdentityStoreProvisionerAttributeContract

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**core_attributes** | [**list[Attribute]**](Attribute.md) | A list of identity store provisioner attributes that correspond to the attributes exposed by the identity store provisioner type. | 
**extended_attributes** | [**list[Attribute]**](Attribute.md) | A list of additional attributes that can be returned by the identity store provisioner. The extended attributes are only used if the provisioner supports them. | [optional] 
**inherited** | **bool** | Whether this attribute contract is inherited from its parent instance. If true, the rest of the properties in this model become read-only. The default value is false. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


