# Connection

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of this connection. Default is &#39;IDP&#39;. | [optional] 
**id** | **str** | The persistent, unique ID for the connection. It can be any combination of [a-zA-Z0-9._-]. This property is system-assigned if not specified. | [optional] 
**entity_id** | **str** | The partner&#39;s entity ID (connection ID) or issuer value (for OIDC Connections). | 
**name** | **str** | The connection name. | 
**modification_date** | **datetime** | The time at which the connection was last changed. This property is read only and is ignored on PUT and POST requests. | [optional] 
**creation_date** | **datetime** | The time at which the connection was created. This property is read only and is ignored on PUT and POST requests. | [optional] 
**active** | **bool** | Specifies whether the connection is active and ready to process incoming requests. The default value is false. | [optional] 
**base_url** | **str** | The fully-qualified hostname and port on which your partner&#39;s federation deployment runs. | [optional] 
**default_virtual_entity_id** | **str** | The default alternate entity ID that identifies the local server to this partner. It is required when virtualEntityIds is not empty and must be included in that list. | [optional] 
**virtual_entity_ids** | **list[str]** | List of alternate entity IDs that identifies the local server to this partner. | [optional] 
**metadata_reload_settings** | [**ConnectionMetadataUrl**](ConnectionMetadataUrl.md) | Connection metadata automatic reload settings. | [optional] 
**credentials** | [**ConnectionCredentials**](ConnectionCredentials.md) | The certificates and settings for encryption, signing, and signature verification. It is required for  SAMLx.x and WS-Fed Connections. | [optional] 
**contact_info** | [**ContactInfo**](ContactInfo.md) | The contact information for this partner. | [optional] 
**license_connection_group** | **str** | The license connection group. If your PingFederate license is based on connection groups, each connection must be assigned to a group before it can be used. | [optional] 
**logging_mode** | **str** | The level of transaction logging applicable for this connection. Default is STANDARD. | [optional] 
**additional_allowed_entities_configuration** | [**AdditionalAllowedEntitiesConfiguration**](AdditionalAllowedEntitiesConfiguration.md) | Additional allowed entities or issuers configuration. Currently only used in OIDC IdP (RP) connection. | [optional] 
**extended_properties** | [**dict(str, ParameterValues)**](ParameterValues.md) | Extended Properties allows to store additional information for IdP/SP Connections. The names of these extended properties should be defined in /extendedProperties. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


