# KerberosRealm

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The persistent, unique ID for the Kerberos Realm. It can be any combination of [a-z0-9._-]. This property is system-assigned if not specified. | [optional] 
**kerberos_realm_name** | **str** | The Domain/Realm name used for display in UI screens. | 
**connection_type** | **str** | Controls how PingFederate connects to the Active Directory/Kerberos Realm. The default is: \&quot;DIRECT\&quot;. | [optional] 
**key_distribution_centers** | **list[str]** | The Domain Controller/Key Distribution Center Host Action Names. Only applicable when &#39;connectionType&#39; is \&quot;DIRECT\&quot;. | [optional] 
**kerberos_username** | **str** | The Domain/Realm username. Only required when &#39;connectionType&#39; is \&quot;DIRECT\&quot;. | [optional] 
**kerberos_password** | **str** | The Domain/Realm password. GETs will not return this attribute. To update this field, specify the new value in this attribute. Only applicable when &#39;connectionType&#39; is \&quot;DIRECT\&quot;. | [optional] 
**kerberos_encrypted_password** | **str** | For GET requests, this field contains the encrypted Domain/Realm password, if one exists. For POST and PUT requests, if you wish to reuse the existing password, this field should be passed back unchanged. Only applicable when &#39;connectionType&#39; is \&quot;DIRECT\&quot;. | [optional] 
**key_sets** | [**list[KerberosKeySet]**](KerberosKeySet.md) | A list of key sets for validating Kerberos tickets. On POST or PUT, if &#39;retainPreviousKeysOnPasswordChange&#39; is true, PingFederate automatically adds the key set for the current password to this list and removes expired key sets. If &#39;retainPreviousKeysOnPasswordChange&#39; is false, this list is cleared. Only applicable when &#39;connectionType&#39; is \&quot;DIRECT\&quot;. | [optional] 
**retain_previous_keys_on_password_change** | **bool** | Determines whether the previous encryption keys are retained when the password is updated. Retaining the previous keys allows existing Kerberos tickets to continue to be validated. The default is false. Only applicable when &#39;connectionType&#39; is \&quot;DIRECT\&quot;. | [optional] 
**suppress_domain_name_concatenation** | **bool** | Controls whether the KDC hostnames and the realm name are concatenated in the auto-generated krb5.conf file. Default is false. Only applicable when &#39;connectionType&#39; is \&quot;DIRECT\&quot;. | [optional] 
**ldap_gateway_data_store_ref** | [**ResourceLink**](ResourceLink.md) | The LDAP gateway used by PingFederate to communicate with the Active Directory. Only required when &#39;connectionType&#39; is \&quot;LDAP_GATEWAY\&quot;. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


