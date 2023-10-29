# LdapInboundProvisioningUserRepository

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_store_ref** | [**ResourceLink**](ResourceLink.md) | Reference to the associated data store. | 
**base_dn** | **str** | The base DN to search from. If not specified, the search will start at the LDAP&#39;s root. | [optional] 
**unique_user_id_filter** | **str** | The expression that results in a unique user identifier, when combined with the Base DN. | 
**unique_group_id_filter** | **str** | The expression that results in a unique group identifier, when combined with the Base DN. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


