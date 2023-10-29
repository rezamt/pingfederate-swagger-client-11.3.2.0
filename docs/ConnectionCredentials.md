# ConnectionCredentials

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**verification_subject_dn** | **str** | If this property is set, the verification trust model is Anchored. The verification certificate must be signed by a trusted CA and included in the incoming message, and the subject DN of the expected certificate is specified in this property. If this property is not set, then a primary verification certificate must be specified in the certs array. | [optional] 
**verification_issuer_dn** | **str** | If a verification Subject DN is provided, you can optionally restrict the issuer to a specific trusted CA by specifying its DN in this field. | [optional] 
**certs** | [**list[ConnectionCert]**](ConnectionCert.md) | The certificates used for signature verification and XML encryption. | [optional] 
**block_encryption_algorithm** | **str** | The algorithm used to encrypt assertions sent to this partner. AES_128, AES_256, AES_128_GCM, AES_192_GCM, AES_256_GCM and Triple_DES are supported. | [optional] 
**key_transport_algorithm** | **str** | The algorithm used to transport keys to this partner. RSA_OAEP, RSA_OAEP_256 and RSA_v15 are supported. | [optional] 
**signing_settings** | [**SigningSettings**](SigningSettings.md) | Settings related to the manner in which messages sent to the partner are digitally signed. Required for SP Connections. | [optional] 
**decryption_key_pair_ref** | [**ResourceLink**](ResourceLink.md) | The ID of the primary key pair used to decrypt message content received from this partner. The ID of the key pair is also known as the alias and can be found by viewing the corresponding certificate under &#39;Signing &amp; Decryption Keys &amp; Certificates&#39; in the PingFederate Administrative Console. | [optional] 
**secondary_decryption_key_pair_ref** | [**ResourceLink**](ResourceLink.md) | The ID of the secondary key pair used to decrypt message content received from this partner.  | [optional] 
**outbound_back_channel_auth** | [**OutboundBackChannelAuth**](OutboundBackChannelAuth.md) | The SOAP authentication method(s) to use when you send a message using SOAP back channel. | [optional] 
**inbound_back_channel_auth** | [**InboundBackChannelAuth**](InboundBackChannelAuth.md) | The SOAP authentication method(s) to use when you receive a message using SOAP back channel. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


