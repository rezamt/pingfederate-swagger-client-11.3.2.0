# LdapTagConfig

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hostnames** | **list[str]** | The LDAP host names. Failover can be configured by providing multiple host names. | 
**tags** | **str** | Tags associated with the host names. At runtime, nodes will use the first LdapTagConfig that has a tag that matches with node.tags in run.properties. | [optional] 
**default_source** | **bool** | Whether this is the default connection. Defaults to false if not specified. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


