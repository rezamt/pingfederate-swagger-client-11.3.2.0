# SessionValidationSettings

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inherited** | **bool** | If this token manager has a parent, this flag determines whether session validation settings, such as checkValidAuthnSession, are inherited from the parent. When set to true, the other fields in this model become read-only. The default value is false. | [optional] 
**include_session_id** | **bool** | Include the session identifier in the access token. Note that if any of the session validation features is enabled, the session identifier will already be included in the access tokens. | [optional] 
**check_valid_authn_session** | **bool** | Check for a valid authentication session when validating the access token. | [optional] 
**check_session_revocation_status** | **bool** | Check the session revocation status when validating the access token. | [optional] 
**update_authn_session_activity** | **bool** | Update authentication session activity when validating the access token. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


