# KerberosRealmsSettings

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**force_tcp** | **bool** | Reference to the default security. | [optional] 
**kdc_retries** | **str** | Reference to the default Key Distribution Center Retries. | 
**debug_log_output** | **bool** | Reference to the default logging. | [optional] 
**kdc_timeout** | **str** | Reference to the default Key Distribution Center Timeout (in seconds). | 
**key_set_retention_period_mins** | **int** | The key set retention period in minutes. When &#39;retainPreviousKeysOnPasswordChange&#39; is set to true for a realm, this setting determines how long keys will be retained after a password change occurs. If this field is omitted in a PUT request, the default of 610 minutes is applied. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


