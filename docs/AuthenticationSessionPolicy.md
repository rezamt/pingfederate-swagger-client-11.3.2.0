# AuthenticationSessionPolicy

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The persistent, unique ID for the session policy. It can be any combination of [a-z0-9._-]. This property is system-assigned if not specified. | [optional] 
**authentication_source** | [**AuthenticationSource**](AuthenticationSource.md) | The authentication source this session policy applies to. This property cannot be changed after the policy is created. | 
**enable_sessions** | **bool** | Determines whether sessions are enabled for the authentication source. This value overrides the enableSessions value from the global authentication session policy. | 
**persistent** | **bool** | Determines whether sessions for the authentication source are persistent. This value overrides the persistentSessions value from the global authentication session policy. This field is ignored if enableSessions is false. | [optional] 
**idle_timeout_mins** | **int** | The idle timeout period, in minutes. If omitted, the value from the global authentication session policy will be used. If set to -1, the idle timeout will be set to the maximum timeout. If a value is provided for this property, a value must also be provided for maxTimeoutMins. | [optional] 
**max_timeout_mins** | **int** | The maximum timeout period, in minutes. If omitted, the value from the global authentication session policy will be used. If set to -1, sessions do not expire. If a value is provided for this property, a value must also be provided for idleTimeoutMins. | [optional] 
**timeout_display_unit** | **str** | The display unit for session timeout periods in the PingFederate administrative console. When the display unit is HOURS or DAYS, the timeout values in minutes must correspond to a whole number value for the specified unit. | [optional] 
**authn_context_sensitive** | **bool** | Determines whether the requested authentication context is considered when deciding whether an existing session is valid for a given request. The default is false. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


