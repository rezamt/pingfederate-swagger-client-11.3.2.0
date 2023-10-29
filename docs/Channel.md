# Channel

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** | Indicates whether the channel is the active channel for this connection. | 
**channel_source** | [**ChannelSource**](ChannelSource.md) | The LDAP settings that apply to the source user-data store. | 
**attribute_mapping** | [**list[SaasAttributeMapping]**](SaasAttributeMapping.md) | The mapping of attributes from the local data store into Fields specified by the service provider. | 
**name** | **str** | The name of the channel. | 
**max_threads** | **int** | The number of processing threads. The default value is 1. | 
**timeout** | **int** | Timeout, in seconds, for individual user and group provisioning operations on the target service provider. The default value is 60. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


