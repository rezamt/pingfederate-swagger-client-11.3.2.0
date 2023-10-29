# ExportMetadataRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connection_type** | **str** | The type of connection to export. | 
**connection_id** | **str** | The ID of the connection to export. | 
**virtual_server_id** | **str** | The virtual server ID to export the metadata with. If null, the connection&#39;s default will be used. | [optional] 
**signing_settings** | [**BaseSigningSettings**](BaseSigningSettings.md) | The signing settings to sign the metadata with. If null, the metadata will not be signed | [optional] 
**use_secondary_port_for_soap** | **bool** | If PingFederate&#39;s secondary SSL port is configured and you want to use it for the SOAP channel, set to true. If client-certificate authentication is configured for the SOAP channel, the secondary port is required and this must be set to true. | [optional] 
**virtual_host_name** | **str** | The virtual host name to be used as the base url. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


