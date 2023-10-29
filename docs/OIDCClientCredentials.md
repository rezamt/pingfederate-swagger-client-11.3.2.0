# OIDCClientCredentials

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_id** | **str** | The OpenID Connect client identitification. | 
**client_secret** | **str** | The OpenID Connect client secret. To update the client secret, specify the plaintext value in this field.  This field will not be populated for GET requests. | [optional] 
**encrypted_secret** | **str** | For GET requests, this field contains the encrypted client secret, if one exists.  For POST and PUT requests, if you wish to reuse the existing secret, this field should be passed back unchanged. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


