# KeyPairRotationSettings

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**creation_buffer_days** | **int** | Buffer days before key pair expiration for creation of a new key pair. | 
**activation_buffer_days** | **int** | Buffer days before key pair expiration for activation of the new key pair. | 
**valid_days** | **int** | Valid days for the new key pair to be created. If this property is unset, the validity days of the original key pair will be used. | [optional] 
**key_algorithm** | **str** | Key algorithm to be used while creating a new key pair. If this property is unset, the key algorithm of the original key pair will be used. Supported algorithms are available through the /keyPairs/keyAlgorithms endpoint. | [optional] 
**key_size** | **int** | Key size, in bits. If this property is unset, the key size of the original key pair will be used. Supported key sizes are available through the /keyPairs/keyAlgorithms endpoint. | [optional] 
**signature_algorithm** | **str** | Required if the original key pair used SHA1 algorithm. If this property is unset, the default signature algorithm of the original key pair will be used. Supported signature algorithms are available through the /keyPairs/keyAlgorithms endpoint. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


