# JdbcTagConfig

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connection_url** | **str** | The location of the JDBC database.  | 
**tags** | **str** | Tags associated with the connection URL. At runtime, nodes will use the first JdbcTagConfig that has a tag that matches with node.tags in run.properties. | [optional] 
**default_source** | **bool** | Whether this is the default connection. Defaults to false if not specified. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


