# InboundBackChannelAuth

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**verification_subject_dn** | **str** | If this property is set, the verification trust model is Anchored. The verification certificate must be signed by a trusted CA and included in the incoming message, and the subject DN of the expected certificate is specified in this property. If this property is not set, then a primary verification certificate must be specified in the certs array. | [optional] 
**verification_issuer_dn** | **str** | If a verification Subject DN is provided, you can optionally restrict the issuer to a specific trusted CA by specifying its DN in this field. | [optional] 
**certs** | [**list[ConnectionCert]**](ConnectionCert.md) | The certificate used for signature verification and XML encryption. | [optional] 
**require_ssl** | **bool** | Incoming HTTP transmissions must use a secure channel. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


