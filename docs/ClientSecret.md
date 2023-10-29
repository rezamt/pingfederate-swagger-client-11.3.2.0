# ClientSecret

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**secret** | **str** | Client secret for Basic Authentication.  To update the client secret, specify the plaintext value in this field.  This field will not be populated for GET requests. | [optional] 
**encrypted_secret** | **str** | For GET requests, this field contains the encrypted client secret, if one exists.  For POST and PUT requests, if you wish to reuse the existing secret, this field should be passed back unchanged. | [optional] 
**secondary_secrets** | [**list[SecondarySecret]**](SecondarySecret.md) | The list of secondary client secrets that are temporarily retained. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


