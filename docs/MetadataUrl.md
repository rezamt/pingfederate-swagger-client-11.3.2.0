# MetadataUrl

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The persistent, unique ID for the Metadata Url. It can be any combination of [a-z0-9._-]. This property is system-assigned if not specified. | [optional] 
**name** | **str** | The name for the Metadata URL. | 
**url** | **str** | The Metadata URL. | 
**cert_view** | [**CertView**](CertView.md) | The Signature Verification Certificate details. This property is read-only and is always ignored on a POST or PUT. | [optional] 
**x509_file** | [**X509File**](X509File.md) | Data of the Signature Verification Certificate for the Metadata URL. | [optional] 
**validate_signature** | **bool** | Perform Metadata Signature Validation. The default value is TRUE. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


