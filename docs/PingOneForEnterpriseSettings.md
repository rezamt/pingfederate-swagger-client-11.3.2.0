# PingOneForEnterpriseSettings

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connected_to_ping_one_for_enterprise** | **bool** | A read only field indicating whether PingFederate is connected to PingOne for Enterprise. | [optional] 
**ping_one_sso_connection** | [**ResourceLink**](ResourceLink.md) | A read only reference to the SP connection configured for PingOne SSO. | [optional] 
**company_name** | **str** | A read only field indicating the company name. | [optional] 
**enable_admin_console_sso** | **bool** | Indicates whether single sign on from PingOne for Enterprise to the PingFederate admin console is enabled. The default is false. | [optional] 
**enable_monitoring** | **bool** | Indicates whether monitoring of PingFederate from PingOne for Enterprise is enabled. The default is true. | [optional] 
**current_authn_key_creation_time** | **datetime** | A read only field indicating the creation time of the current authentication key. | [optional] 
**previous_authn_key_creation_time** | **datetime** | A read only field indicating the creation time of the previous authentication key. | [optional] 
**identity_repository_update_required** | **bool** | A read-only field indicating whether changes were made in the current PingFederate configuration that might affect your connection with PingOne for Enterprise. For example, if you modified the attribute contract of your SSO configuration. Update the identity repository to keep your PingFederate and PingOne for Enterprise settings synchronized.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


