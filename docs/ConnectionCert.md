# ConnectionCert

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cert_view** | [**CertView**](CertView.md) | Certificate details. This property is read-only and is always ignored on a POST or PUT. | [optional] 
**x509_file** | [**X509File**](X509File.md) | The certificate data. This property must always be supplied on a POST or PUT. | 
**active_verification_cert** | **bool** | Indicates whether this is an active signature verification certificate. | [optional] 
**primary_verification_cert** | **bool** | Indicates whether this is the primary signature verification certificate. Only one certificate in the collection can have this flag set. | [optional] 
**secondary_verification_cert** | **bool** | Indicates whether this is the secondary signature verification certificate. Only one certificate in the collection can have this flag set. | [optional] 
**encryption_cert** | **bool** | Indicates whether to use this cert to encrypt outgoing assertions. Only one certificate in the collection can have this flag set. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


