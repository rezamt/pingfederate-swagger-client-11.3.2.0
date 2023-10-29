# LdapAttributeSource

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_dn** | **str** | The base DN to search from. If not specified, the search will start at the LDAP&#39;s root. | [optional] 
**search_scope** | **str** | Determines the node depth of the query. | 
**search_filter** | **str** | The LDAP filter that will be used to lookup the objects from the directory. | 
**search_attributes** | **list[str]** | A list of LDAP attributes returned from search and available for mapping. | [optional] 
**binary_attribute_settings** | [**dict(str, BinaryLdapAttributeSettings)**](BinaryLdapAttributeSettings.md) | The advanced settings for binary LDAP attributes. | [optional] 
**member_of_nested_group** | **bool** | Set this to true to return transitive group memberships for the &#39;memberOf&#39; attribute.  This only applies for Active Directory data sources.  All other data sources will be set to false. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


