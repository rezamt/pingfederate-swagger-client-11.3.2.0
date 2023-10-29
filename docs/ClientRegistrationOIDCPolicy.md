# ClientRegistrationOIDCPolicy

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id_token_signing_algorithm** | **str** | The JSON Web Signature [JWS] algorithm required for the ID Token.&lt;br&gt;NONE - No signing algorithm&lt;br&gt;HS256 - HMAC using SHA-256&lt;br&gt;HS384 - HMAC using SHA-384&lt;br&gt;HS512 - HMAC using SHA-512&lt;br&gt;RS256 - RSA using SHA-256&lt;br&gt;RS384 - RSA using SHA-384&lt;br&gt;RS512 - RSA using SHA-512&lt;br&gt;ES256 - ECDSA using P256 Curve and SHA-256&lt;br&gt;ES384 - ECDSA using P384 Curve and SHA-384&lt;br&gt;ES512 - ECDSA using P521 Curve and SHA-512&lt;br&gt;PS256 - RSASSA-PSS using SHA-256 and MGF1 padding with SHA-256&lt;br&gt;PS384 - RSASSA-PSS using SHA-384 and MGF1 padding with SHA-384&lt;br&gt;PS512 - RSASSA-PSS using SHA-512 and MGF1 padding with SHA-512&lt;br&gt;A null value will represent the default algorithm which is RS256.&lt;br&gt;RSASSA-PSS is only supported with SafeNet Luna, Thales nCipher or Java 11 | [optional] 
**id_token_encryption_algorithm** | **str** | The JSON Web Encryption [JWE] encryption algorithm used to encrypt the content encryption key for the ID Token.&lt;br&gt;DIR - Direct Encryption with symmetric key&lt;br&gt;A128KW - AES-128 Key Wrap&lt;br&gt;A192KW - AES-192 Key Wrap&lt;br&gt;A256KW - AES-256 Key Wrap&lt;br&gt;A128GCMKW - AES-GCM-128 key encryption&lt;br&gt;A192GCMKW - AES-GCM-192 key encryption&lt;br&gt;A256GCMKW - AES-GCM-256 key encryption&lt;br&gt;ECDH_ES - ECDH-ES&lt;br&gt;ECDH_ES_A128KW - ECDH-ES with AES-128 Key Wrap&lt;br&gt;ECDH_ES_A192KW - ECDH-ES with AES-192 Key Wrap&lt;br&gt;ECDH_ES_A256KW - ECDH-ES with AES-256 Key Wrap&lt;br&gt;RSA_OAEP - RSAES OAEP&lt;br&gt;RSA_OAEP_256 - RSAES OAEP using SHA-256 and MGF1 with SHA-256 | [optional] 
**id_token_content_encryption_algorithm** | **str** | The JSON Web Encryption [JWE] content encryption algorithm for the ID Token.&lt;br&gt;AES_128_CBC_HMAC_SHA_256 - Composite AES-CBC-128 HMAC-SHA-256&lt;br&gt;AES_192_CBC_HMAC_SHA_384 - Composite AES-CBC-192 HMAC-SHA-384&lt;br&gt;AES_256_CBC_HMAC_SHA_512 - Composite AES-CBC-256 HMAC-SHA-512&lt;br&gt;AES_128_GCM - AES-GCM-128&lt;br&gt;AES_192_GCM - AES-GCM-192&lt;br&gt;AES_256_GCM - AES-GCM-256 | [optional] 
**policy_group** | [**ResourceLink**](ResourceLink.md) | The Open ID Connect policy. A null value will represent the default policy group. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


