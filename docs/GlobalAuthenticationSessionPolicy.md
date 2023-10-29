# GlobalAuthenticationSessionPolicy

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable_sessions** | **bool** | Determines whether authentication sessions are enabled globally. | 
**persistent_sessions** | **bool** | Determines whether authentication sessions are persistent by default. Persistent sessions are linked to a persistent cookie and stored in a data store. This field is ignored if enableSessions is false. | [optional] 
**hash_unique_user_key_attribute** | **bool** | Determines whether to hash the value of the unique user key attribute. | [optional] 
**idle_timeout_mins** | **int** | The idle timeout period, in minutes. If set to -1, the idle timeout will be set to the maximum timeout. The default is 60. | [optional] 
**idle_timeout_display_unit** | **str** | The display unit for the idle timeout period in the PingFederate administrative console. When the display unit is HOURS or DAYS, the timeout value in minutes must correspond to a whole number value for the specified unit. | [optional] 
**max_timeout_mins** | **int** | The maximum timeout period, in minutes. If set to -1, sessions do not expire. The default is 480. | [optional] 
**max_timeout_display_unit** | **str** | The display unit for the maximum timeout period in the PingFederate administrative console. When the display unit is HOURS or DAYS, the timeout value in minutes must correspond to a whole number value for the specified unit. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


