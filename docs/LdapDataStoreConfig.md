# LdapDataStoreConfig

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_dn** | **str** | The base DN to search from. If not specified, the search will start at the LDAP&#39;s root. | 
**create_pattern** | **str** | The Relative DN Pattern that will be used to create objects in the directory. | 
**object_class** | **str** | The Object Class used by the new objects stored in the LDAP data store. | 
**auxiliary_object_classes** | **list[str]** | The Auxiliary Object Classes used by the new objects stored in the LDAP data store. | [optional] 
**data_store_mapping** | [**dict(str, DataStoreAttribute)**](DataStoreAttribute.md) | The data store mapping. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


