# AttributeSource

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The data store type of this attribute source. | 
**data_store_ref** | [**ResourceLink**](ResourceLink.md) | Reference to the associated data store. | 
**id** | **str** | The ID that defines this attribute source. Only alphanumeric characters allowed.&lt;br&gt;Note: Required for OpenID Connect policy attribute sources, OAuth IdP adapter mappings, OAuth access token mappings and APC-to-SP Adapter Mappings. IdP Connections will ignore this property since it only allows one attribute source to be defined per mapping. IdP-to-SP Adapter Mappings can contain multiple attribute sources. | [optional] 
**description** | **str** | The description of this attribute source. The description needs to be unique amongst the attribute sources for the mapping.&lt;br&gt;Note: Required for APC-to-SP Adapter Mappings | [optional] 
**attribute_contract_fulfillment** | [**dict(str, AttributeFulfillmentValue)**](AttributeFulfillmentValue.md) | A list of mappings from attribute names to their fulfillment values. This field is only valid for the SP Connection&#39;s Browser SSO mappings | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


