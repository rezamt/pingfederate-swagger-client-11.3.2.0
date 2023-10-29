# LdapDataStoreRepository

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_dn** | **str** | The base DN to search from. If not specified, the search will start at the LDAP&#39;s root. | [optional] 
**unique_user_id_filter** | **str** | The expression that results in a unique user identifier, when combined with the Base DN. | 
**jit_repository_attribute_mapping** | [**dict(str, AttributeFulfillmentValue)**](AttributeFulfillmentValue.md) | A list of user repository mappings from attribute names to their fulfillment values. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


