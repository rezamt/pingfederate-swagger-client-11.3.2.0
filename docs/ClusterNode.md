# ClusterNode

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | The IP address and port this node is running on. | [optional] 
**index** | **int** | Index of the node within the cluster, or -1 if an index is not assigned. | [optional] 
**mode** | **str** | The deployment mode of this node, from a clustering standpoint. CLUSTERED_DUAL is not supported. | [optional] 
**node_group** | **str** | The node group for this node. This field is only populated if adaptive clustering is enabled. | [optional] 
**version** | **str** | The PingFederate version this node is running on. | [optional] 
**node_tags** | **str** | The node tags for this node. This field is only populated for engine nodes. | [optional] 
**configuration_timestamp** | **datetime** | The time stamp of the configuration data retrieved by this node. | [optional] 
**replication_status** | **str** | The replication status of the node. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


