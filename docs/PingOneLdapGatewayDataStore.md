# PingOneLdapGatewayDataStore

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The data store name with a unique value across all data sources. Omitting this attribute will set the value to a combination of the hostname(s) and the principal. | [optional] 
**ldap_type** | **str** | A type that allows PingFederate to configure many provisioning settings automatically. The value is validated against the LDAP gateway configuration in PingOne unless the header &#39;X-BypassExternalValidation&#39; is set to true. | 
**ping_one_connection_ref** | [**ResourceLink**](ResourceLink.md) | Reference to the PingOne connection this gateway uses. | 
**ping_one_environment_id** | **str** | The environment ID that the gateway belongs to. | 
**ping_one_ldap_gateway_id** | **str** | The ID of the PingOne LDAP Gateway this data store uses. | 
**use_ssl** | **bool** | Connects to the LDAP data store using secure SSL/TLS encryption (LDAPS). The default value is false. The value is validated against the LDAP gateway configuration in PingOne unless the header &#39;X-BypassExternalValidation&#39; is set to true. | [optional] 
**binary_attributes** | **list[str]** | The list of LDAP attributes to be handled as binary data. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


