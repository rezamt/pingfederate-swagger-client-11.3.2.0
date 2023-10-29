# NewKeyPairSettings

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The persistent, unique ID for the certificate. It can be any combination of [a-z0-9._-]. This property is system-assigned if not specified. | [optional] 
**common_name** | **str** | Common name for key pair subject. | 
**subject_alternative_names** | **list[str]** | The subject alternative names (SAN). | [optional] 
**organization** | **str** | Organization. | 
**organization_unit** | **str** | Organization unit. | [optional] 
**city** | **str** | City. | [optional] 
**state** | **str** | State. | [optional] 
**country** | **str** | Country. | 
**valid_days** | **int** | Number of days the key pair will be valid for. | 
**key_algorithm** | **str** | Key generation algorithm. Supported algorithms are available through the /keyPairs/keyAlgorithms endpoint. | 
**key_size** | **int** | Key size, in bits. If this property is unset, the default size for the key algorithm will be used. Supported key sizes are available through the /keyPairs/keyAlgorithms endpoint. | [optional] 
**signature_algorithm** | **str** | Signature algorithm. If this property is unset, the default signature algorithm for the key algorithm will be used. Supported signature algorithms are available through the /keyPairs/keyAlgorithms endpoint. | [optional] 
**crypto_provider** | **str** | Cryptographic Provider.  This is only applicable if Hybrid HSM mode is true. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


