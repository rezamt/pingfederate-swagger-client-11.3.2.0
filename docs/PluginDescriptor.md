# PluginDescriptor

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique ID of the plugin. | [optional] 
**name** | **str** | Friendly name for the plugin. | [optional] 
**class_name** | **str** | Full class name of the class that implements this plugin. | [optional] 
**attribute_contract** | **list[str]** | The attribute contract for this plugin. | [optional] 
**supports_extended_contract** | **bool** | Determines whether this plugin supports extending the attribute contract. | [optional] 
**config_descriptor** | [**PluginConfigDescriptor**](PluginConfigDescriptor.md) | The descriptor which defines the configuration fields available for this plugin. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


