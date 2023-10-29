# KeyPairView

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The persistent, unique ID for the certificate. | [optional] 
**serial_number** | **str** | The serial number assigned by the CA. | [optional] 
**subject_dn** | **str** | The subject&#39;s distinguished name. | [optional] 
**subject_alternative_names** | **list[str]** | The subject alternative names (SAN). | [optional] 
**issuer_dn** | **str** | The issuer&#39;s distinguished name. | [optional] 
**valid_from** | **datetime** | The start date from which the item is valid, in ISO 8601 format (UTC). | [optional] 
**expires** | **datetime** | The end date up until which the item is valid, in ISO 8601 format (UTC). | [optional] 
**key_algorithm** | **str** | The public key algorithm. | [optional] 
**key_size** | **int** | The public key size. | [optional] 
**signature_algorithm** | **str** | The signature algorithm. | [optional] 
**version** | **int** | The X.509 version to which the item conforms. | [optional] 
**sha1_fingerprint** | **str** | SHA-1 fingerprint in Hex encoding. | [optional] 
**sha256_fingerprint** | **str** | SHA-256 fingerprint in Hex encoding. | [optional] 
**status** | **str** | Status of the item. | [optional] 
**crypto_provider** | **str** | Cryptographic Provider. This is only applicable if Hybrid HSM mode is true. | [optional] 
**rotation_settings** | [**KeyPairRotationSettings**](KeyPairRotationSettings.md) | Key pair rotation settings. Only applicable to self-signed signing key pairs. Automatic key rotation is not currently available for SSL client or SSL server key pairs. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


