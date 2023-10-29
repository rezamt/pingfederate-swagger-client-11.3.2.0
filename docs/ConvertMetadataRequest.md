# ConvertMetadataRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connection_type** | **str** | The expected connection type to convert. | 
**expected_protocol** | **str** | The expected browser-based SSO protocol to convert. In this case the protocol is restricted to SAML. | 
**expected_entity_id** | **str** | The entity ID of the connection to be obtained from the input SAML Metadata. Required if the SAML Metadata has more than one connection defined. | [optional] 
**saml_metadata** | **str** | The base-64 encoded XML SAML metadata. | 
**verification_certificate** | **str** | The certificate to validate the metadata signature against. The certificate can be in PEM format or base-64 encoded DER format. | [optional] 
**template_connection** | [**Connection**](Connection.md) | The template connection to overlay the metadata on. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


