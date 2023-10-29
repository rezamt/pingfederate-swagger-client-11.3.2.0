# MetadataSigningSettings

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**signing_key_ref** | [**ResourceLink**](ResourceLink.md) | Reference to the key used for metadata signing. Refer to /keyPair/signing to get the list of available signing key pairs. | [optional] 
**signature_algorithm** | **str** | Signature algorithm. If this property is unset, the default signature algorithm for the key algorithm will be used. Supported signature algorithms are available through the /keyPairs/keyAlgorithms endpoint. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


