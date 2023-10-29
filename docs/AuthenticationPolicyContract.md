# AuthenticationPolicyContract

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The persistent, unique ID for the authentication policy contract. It can be any combination of [a-zA-Z0-9._-]. This property is system-assigned if not specified. | [optional] 
**name** | **str** | The Authentication Policy Contract Name. Name is unique. | [optional] 
**core_attributes** | [**list[AuthenticationPolicyContractAttribute]**](AuthenticationPolicyContractAttribute.md) | A list of read-only assertion attributes (for example, subject) that are automatically populated by PingFederate. | [optional] 
**extended_attributes** | [**list[AuthenticationPolicyContractAttribute]**](AuthenticationPolicyContractAttribute.md) | A list of additional attributes as needed. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


