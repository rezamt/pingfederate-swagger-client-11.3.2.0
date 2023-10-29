# JwksSettings

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**jwks_url** | **str** | JSON Web Key Set (JWKS) URL of the OAuth client. Either &#39;jwks&#39; or &#39;jwksUrl&#39; must be provided if private key JWT client authentication or signed requests is enabled.  If the client signs its JWTs using an RSASSA-PSS signing algorithm, PingFederate must either use Java 11 or be integrated with a hardware security module (HSM) to process the digital signatures. | [optional] 
**jwks** | **str** | JSON Web Key Set (JWKS) document of the OAuth client. Either &#39;jwks&#39; or &#39;jwksUrl&#39; must be provided if private key JWT client authentication or signed requests is enabled.  If the client signs its JWTs using an RSASSA-PSS signing algorithm, PingFederate must either use Java 11 or be integrated with a hardware security module (HSM) to process the digital signatures. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


