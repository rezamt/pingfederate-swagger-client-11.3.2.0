# SecondarySecret

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**secret** | **str** | Secondary client secret for Basic Authentication.  To update the secondary client secret, specify the plaintext value in this field.  This field will not be populated for GET requests. | [optional] 
**encrypted_secret** | **str** | For GET requests, this field contains the encrypted secondary client secret, if one exists.  For POST and PUT requests, if you wish to reuse the existing secret, this field should be passed back unchanged. | [optional] 
**expiry_time** | **datetime** | The expiry time of the secondary secret. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


