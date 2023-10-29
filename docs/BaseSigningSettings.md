# BaseSigningSettings

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**signing_key_pair_ref** | [**ResourceLink**](ResourceLink.md) | The ID of the key pair used to sign messages sent to this partner. The ID of the key pair is also known as the alias and can be found by viewing the corresponding certificate under &#39;Signing &amp; Decryption Keys &amp; Certificates&#39; in the PingFederate admin console. | 
**algorithm** | **str** | The algorithm used to sign messages sent to this partner. The default is SHA1withDSA for DSA certs, SHA256withRSA for RSA certs, and SHA256withECDSA for EC certs. For RSA certs, SHA1withRSA, SHA384withRSA, SHA512withRSA, SHA256withRSAandMGF1, SHA384withRSAandMGF1 and SHA512withRSAandMGF1 are also supported. For EC certs, SHA384withECDSA and SHA512withECDSA are also supported. If the connection is WS-Federation with JWT token type, then the possible values are RSA SHA256, RSA SHA384, RSA SHA512, RSASSA-PSS SHA256, RSASSA-PSS SHA384, RSASSA-PSS SHA512, ECDSA SHA256, ECDSA SHA384, ECDSA SHA512 | [optional] 
**include_cert_in_signature** | **bool** | Determines whether the signing certificate is included in the signature &lt;KeyInfo&gt; element. | [optional] 
**include_raw_key_in_signature** | **bool** | Determines whether the &lt;KeyValue&gt; element with the raw public key is included in the signature &lt;KeyInfo&gt; element. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


