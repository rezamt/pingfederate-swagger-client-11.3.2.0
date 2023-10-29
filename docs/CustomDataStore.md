# CustomDataStore

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The data store type. | 
**id** | **str** | The persistent, unique ID for the data store. It can be any combination of [a-zA-Z0-9._-]. This property is system-assigned if not specified. | [optional] 
**mask_attribute_values** | **bool** | Whether attribute values should be masked in the log. | [optional] 
**name** | **str** | The plugin instance name. | 
**plugin_descriptor_ref** | [**ResourceLink**](ResourceLink.md) | Reference to the plugin descriptor for this instance. The plugin descriptor cannot be modified once the instance is created.&lt;br&gt;Note: Ignored when specifying a connection&#39;s adapter override. | 
**parent_ref** | [**ResourceLink**](ResourceLink.md) | The reference to this plugin&#39;s parent instance. The parent reference is only accepted if the plugin type supports parent instances.&lt;br&gt;Note: This parent reference is required if this plugin instance is used as an overriding plugin (e.g. connection adapter overrides) | [optional] 
**configuration** | [**PluginConfiguration**](PluginConfiguration.md) | Plugin instance configuration. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


