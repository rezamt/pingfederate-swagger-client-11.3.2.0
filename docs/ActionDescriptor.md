# ActionDescriptor

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of this action | [optional] 
**description** | **str** | The description of this action | [optional] 
**download** | **bool** | Whether this action will trigger a download or invoke an internal action that will return a string result. | [optional] 
**download_content_type** | **str** | If this is a download, this is the Content-Type of the downloaded file. Otherwise, this is null. | [optional] 
**download_file_name** | **str** | If this is a download, this is the suggested file name of the downloaded file. Otherwise, this is null. | [optional] 
**parameters** | [**list[FieldDescriptor]**](FieldDescriptor.md) | List of parameters for this action. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


