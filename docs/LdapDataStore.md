# LdapDataStore

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hostnames_tags** | [**list[LdapTagConfig]**](LdapTagConfig.md) | The set of host names and associated tags for this LDAP data store. This is required if &#39;hostnames&#39; is not provided. | [optional] 
**hostnames** | **list[str]** | The default LDAP host names. This field is required if no mapping for host names and tags is specified. Failover can be configured by providing multiple host names. | [optional] 
**name** | **str** | The data store name with a unique value across all data sources. Omitting this attribute will set the value to a combination of the hostname(s) and the principal. | [optional] 
**ldap_type** | **str** | A type that allows PingFederate to configure many provisioning settings automatically. The &#39;UNBOUNDID_DS&#39; type has been deprecated, please use the &#39;PING_DIRECTORY&#39; type instead. | 
**bind_anonymously** | **bool** | Whether username and password are required. If true, no other authentication fields should be provided. The default value is false. | [optional] 
**user_dn** | **str** | The username credential required to access the data store. If specified, no other authentication fields should be provided. | [optional] 
**password** | **str** | The password credential required to access the data store. GETs will not return this attribute. To update this field, specify the new value in this attribute. | [optional] 
**encrypted_password** | **str** | The encrypted password credential required to access the data store.  If you do not want to update the stored value, this attribute should be passed back unchanged. Secret Reference may be provided in this field with format &#39;OBF:MGR:{secretManagerId}:{secretId}&#39;. | [optional] 
**client_tls_certificate_ref** | [**ResourceLink**](ResourceLink.md) | The client TLS certificate used to access the data store. If specified, authentication to the data store will be done using mutual TLS and no other authentication fields should be provided. See &#39;/keyPairs/sslClient&#39; to manage certificates. | [optional] 
**use_ssl** | **bool** | Connects to the LDAP data store using secure SSL/TLS encryption (LDAPS). The default value is false. | [optional] 
**use_dns_srv_records** | **bool** | Use DNS SRV Records to discover LDAP server information. The default value is false. | [optional] 
**follow_ldap_referrals** | **bool** | Follow LDAP Referrals in the domain tree. The default value is false. This property does not apply to PingDirectory as this functionality is configured in PingDirectory. | [optional] 
**retry_failed_operations** | **bool** | Indicates whether failed operations should be retried. The default is false. | [optional] 
**test_on_borrow** | **bool** | Indicates whether objects are validated before being borrowed from the pool. | [optional] 
**test_on_return** | **bool** | Indicates whether objects are validated before being returned to the pool. | [optional] 
**create_if_necessary** | **bool** | Indicates whether temporary connections can be created when the Maximum Connections threshold is reached. | [optional] 
**verify_host** | **bool** | Verifies that the presented server certificate includes the address to which the client intended to establish a connection. Omitting this attribute will set the value to true. | [optional] 
**min_connections** | **int** | The smallest number of connections that can remain in each pool, without creating extra ones. Omitting this attribute will set the value to the default value. | [optional] 
**max_connections** | **int** | The largest number of active connections that can remain in each pool without releasing extra ones. Omitting this attribute will set the value to the default value. | [optional] 
**max_wait** | **int** | The maximum number of milliseconds the pool waits for a connection to become available when trying to obtain a connection from the pool. Omitting this attribute or setting a value of -1 causes the pool not to wait at all and to either create a new connection or produce an error (when no connections are available). | [optional] 
**time_between_evictions** | **int** | The frequency, in milliseconds, that the evictor cleans up the connections in the pool. A value of -1 disables the evictor. Omitting this attribute will set the value to the default value. | [optional] 
**read_timeout** | **int** | The maximum number of milliseconds a connection waits for a response to be returned before producing an error. A value of -1 causes the connection to wait indefinitely. Omitting this attribute will set the value to the default value. | [optional] 
**connection_timeout** | **int** | The maximum number of milliseconds that a connection attempt should be allowed to continue before returning an error. A value of -1 causes the pool to wait indefinitely. Omitting this attribute will set the value to the default value. | [optional] 
**dns_ttl** | **int** | The maximum time in milliseconds that DNS information are cached. Omitting this attribute will set the value to the default value. | [optional] 
**ldap_dns_srv_prefix** | **str** | The prefix value used to discover LDAP DNS SRV record. Omitting this attribute will set the value to the default value. | [optional] 
**ldaps_dns_srv_prefix** | **str** | The prefix value used to discover LDAPs DNS SRV record. Omitting this attribute will set the value to the default value. | [optional] 
**binary_attributes** | **list[str]** | The list of LDAP attributes to be handled as binary data. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


