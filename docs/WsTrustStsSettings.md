# WsTrustStsSettings

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**basic_authn_enabled** | **bool** | Require the use of HTTP Basic Authentication to access WS-Trust STS endpoints. Requires users be populated. | [optional] 
**client_cert_authn_enabled** | **bool** | Require the use of Client Cert Authentication to access WS-Trust STS endpoints. Requires either restrictBySubjectDn and/or restrictByIssuerCert be enabled. | [optional] 
**restrict_by_subject_dn** | **bool** | Restrict Access by Subject DN. Ignored if clientCertAuthnEnabled is disabled. | [optional] 
**restrict_by_issuer_cert** | **bool** | Restrict Access by Issuer Certificate. Ignored if clientCertAuthnEnabled is disabled. | [optional] 
**subject_dns** | **list[str]** | List of Subject DNs for certificates that are allowed to authenticate to WS-Trust STS endpoints. Required if restrictBySubjectDn is enabled. | [optional] 
**users** | [**list[UsernamePasswordCredentials]**](UsernamePasswordCredentials.md) | List of users authorized to access WS-Trust STS endpoints when basicAuthnEnabled is enabled. At least one users entry is required if basicAuthnEnabled is enabled. | [optional] 
**issuer_certs** | [**list[ResourceLink]**](ResourceLink.md) | List of certificate Issuers that are used to validate certificates for access to the WS-Trust STS endpoints. Required if restrictByIssuerCert is enabled. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


