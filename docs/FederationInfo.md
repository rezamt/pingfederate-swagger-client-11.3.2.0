# FederationInfo

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_url** | **str** | The fully qualified host name, port, and path (if applicable) on which the PingFederate server runs. | [optional] 
**saml2_entity_id** | **str** | This ID defines your organization as the entity operating the server for SAML 2.0 transactions. It is usually defined as an organization&#39;s URL or a DNS address; for example: pingidentity.com. The SAML SourceID used for artifact resolution is derived from this ID using SHA1. | [optional] 
**auto_connect_entity_id** | **str** | This property has been deprecated and no longer used | [optional] 
**saml1x_issuer_id** | **str** | This ID identifies your federation server for SAML 1.x transactions. As with SAML 2.0, it is usually defined as an organization&#39;s URL or a DNS address. The SourceID used for artifact resolution is derived from this ID using SHA1. | [optional] 
**saml1x_source_id** | **str** | If supplied, the Source ID value entered here is used for SAML 1.x, instead of being derived from the SAML 1.x Issuer/Audience. | [optional] 
**wsfed_realm** | **str** | The URI of the realm associated with the PingFederate server. A realm represents a single unit of security administration or trust. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


