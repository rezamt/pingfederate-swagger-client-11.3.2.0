# CertificateRevocationSettings

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ocsp_settings** | [**OcspSettings**](OcspSettings.md) | Certificate revocation OCSP settings. If this attribute is omitted, OCSP checks are disabled. | [optional] 
**crl_settings** | [**CrlSettings**](CrlSettings.md) | Certificate revocation CRL settings. If this attribute is omitted, CRL checks are disabled. | [optional] 
**proxy_settings** | [**ProxySettings**](ProxySettings.md) | If OCSP messaging is routed through a proxy server, specify the server&#39;s host (DNS name or IP address) and the port number. The same proxy information applies to CRL checking, when CRL is enabled for failover. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


