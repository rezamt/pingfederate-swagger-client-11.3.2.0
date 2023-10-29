# KeyPairFile

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The persistent, unique ID for the certificate. It can be any combination of [a-z0-9._-]. This property is system-assigned if not specified. | [optional] 
**file_data** | **str** | Base-64 encoded PKCS12 or PEM file data. In the case of PEM, the raw (non-base-64) data is also accepted. In BCFIPS mode, only PEM with PBES2 and AES or Triple DES encryption is accepted and 128-bit salt is required. | 
**format** | **str** | Key pair file format. If specified, this field will control what file format is expected, otherwise the format will be auto-detected. In BCFIPS mode, only PEM is supported. | [optional] 
**password** | **str** | Password for the file. In BCFIPS mode, the password must be at least 14 characters. | 
**encrypted_password** | **str** | Encrypted password for the file. Only applicable for bulk export/import operations. For bulk import operation, either password or encrypted password must be set. | [optional] 
**crypto_provider** | **str** | Cryptographic Provider. This is only applicable if Hybrid HSM mode is true. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


