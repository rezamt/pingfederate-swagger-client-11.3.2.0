# ClientAuth

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Client authentication type.&lt;br&gt;The required field for type SECRET is secret.&lt;br&gt;The required fields for type CERTIFICATE are clientCertIssuerDn and clientCertSubjectDn.&lt;br&gt;The required field for type PRIVATE_KEY_JWT is: either jwks or jwksUrl. | [optional] 
**secret** | **str** | Client secret for Basic Authentication.  To update the client secret, specify the plaintext value in this field.  This field will not be populated for GET requests. | [optional] 
**encrypted_secret** | **str** | For GET requests, this field contains the encrypted client secret, if one exists.  For POST and PUT requests, if you wish to reuse the existing secret, this field should be passed back unchanged. | [optional] 
**secondary_secrets** | [**list[SecondarySecret]**](SecondarySecret.md) | The list of secondary client secrets that are temporarily retained. | [optional] 
**client_cert_issuer_dn** | **str** | Client TLS Certificate Issuer DN. | [optional] 
**client_cert_subject_dn** | **str** | Client TLS Certificate Subject DN. | [optional] 
**enforce_replay_prevention** | **bool** | Enforce replay prevention on JSON Web Tokens. This field is applicable only for Private Key JWT Client and Client Secret JWT Authentication. | [optional] 
**token_endpoint_auth_signing_algorithm** | **str** | The JSON Web Signature [JWS] algorithm that must be used to sign the JSON Web Tokens. This field is applicable only for Private Key JWT and Client Secret JWT Client Authentication. All asymmetric signing algorithms are allowed for Private Key JWT if value is not present.All symmetric signing algorithms are allowed for Client Secret JWT if value is not present &lt;br&gt;RS256 - RSA using SHA-256&lt;br&gt;RS384 - RSA using SHA-384&lt;br&gt;RS512 - RSA using SHA-512&lt;br&gt;ES256 - ECDSA using P256 Curve and SHA-256&lt;br&gt;ES384 - ECDSA using P384 Curve and SHA-384&lt;br&gt;ES512 - ECDSA using P521 Curve and SHA-512&lt;br&gt;PS256 - RSASSA-PSS using SHA-256 and MGF1 padding with SHA-256&lt;br&gt;PS384 - RSASSA-PSS using SHA-384 and MGF1 padding with SHA-384&lt;br&gt;PS512 - RSASSA-PSS using SHA-512 and MGF1 padding with SHA-512&lt;br&gt;RSASSA-PSS is only supported with SafeNet Luna, Thales nCipher or Java 11.&lt;br&gt;HS256 - HMAC using SHA-256&lt;br&gt;HS384 - HMAC using SHA-384&lt;br&gt;HS512 - HMAC using SHA-512. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


