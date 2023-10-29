# SessionSettings

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**track_adapter_sessions_for_logout** | **bool** | Determines whether adapter sessions are tracked for cleanup during single logout. The default is false. | [optional] 
**revoke_user_session_on_logout** | **bool** | Determines whether the user&#39;s session is revoked on logout. If this property is not provided on a PUT, the setting is left unchanged. | [optional] 
**session_revocation_lifetime** | **int** | How long a session revocation is tracked and stored, in minutes. If this property is not provided on a PUT, the setting is left unchanged. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


