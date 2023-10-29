# ClusterStatus

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nodes** | [**list[ClusterNode]**](ClusterNode.md) | List of nodes in the cluster. | [optional] 
**last_config_update_time** | **datetime** | Time when the configuration of this node was last updated. | [optional] 
**last_replication_time** | **datetime** | Time when configuration changes were last replicated. | [optional] 
**replication_required** | **bool** | Indicates whether a replication is required to propagate config updates. | [optional] 
**mixed_mode** | **bool** | Indicates whether there is more than one version of PingFederate in the cluster. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


