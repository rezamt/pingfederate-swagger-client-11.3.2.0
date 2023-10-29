# AuthenticationPolicyTree

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The authentication policy ID. ID is unique. | [optional] 
**name** | **str** | The authentication policy name. Name is unique. | [optional] 
**description** | **str** | A description for the authentication policy. | [optional] 
**authentication_api_application_ref** | [**ResourceLink**](ResourceLink.md) | Authentication API Application Id to be used in this policy branch. If the value is not specified, no Authentication API Application will be used. | [optional] 
**enabled** | **bool** | Whether or not this authentication policy tree is enabled. Default is true. | [optional] 
**root_node** | [**AuthenticationPolicyTreeNode**](AuthenticationPolicyTreeNode.md) | A node inside the authentication policy tree. | [optional] 
**handle_failures_locally** | **bool** | If a policy ends in failure keep the user local. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


