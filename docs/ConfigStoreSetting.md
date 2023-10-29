# ConfigStoreSetting

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The id of the configuration setting. | 
**string_value** | **str** | The value of the configuration setting. This is used when the setting has a single string value. | [optional] 
**list_value** | **list[str]** | The list of values for the configuration setting. This is used when the setting has a list of string values. | [optional] 
**map_value** | **dict(str, str)** | The map of key/value pairs for the configuration setting. This is used when the setting has a map of string keys and values. | [optional] 
**type** | **str** | The type of configuration setting. This could be a single string, list of strings, or map of string keys and values. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


