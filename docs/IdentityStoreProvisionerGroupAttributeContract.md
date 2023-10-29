# IdentityStoreProvisionerGroupAttributeContract

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**core_attributes** | [**list[GroupAttribute]**](GroupAttribute.md) | A list of identity store provisioner group attributes that correspond to the group attributes exposed by the identity store provisioner type. | 
**extended_attributes** | [**list[GroupAttribute]**](GroupAttribute.md) | A list of additional group attributes that can be returned by the identity store provisioner. The extended group attributes are only used if the provisioner supports them. | [optional] 
**inherited** | **bool** | Whether this group attribute contract is inherited from its parent instance. If true, the rest of the properties in this model become read-only. The default value is false. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


