# JdbcDataStore

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connection_url_tags** | [**list[JdbcTagConfig]**](JdbcTagConfig.md) | The set of connection URLs and associated tags for this JDBC data store. This is required if &#39;connectionUrl&#39; is not provided. | [optional] 
**connection_url** | **str** | The default location of the JDBC database. This field is required if no mapping for JDBC database location and tags is specified. | [optional] 
**name** | **str** | The data store name with a unique value across all data sources. Omitting this attribute will set the value to a combination of the connection url and the username. | [optional] 
**driver_class** | **str** | The name of the driver class used to communicate with the source database. | 
**user_name** | **str** | The name that identifies the user when connecting to the database. | [optional] 
**password** | **str** | The password needed to access the database. GETs will not return this attribute. To update this field, specify the new value in this attribute. | [optional] 
**encrypted_password** | **str** | The encrypted password needed to access the database. If you do not want to update the stored value, this attribute should be passed back unchanged. Secret Reference may be provided in this field with format &#39;OBF:MGR:{secretManagerId}:{secretId}&#39;. | [optional] 
**validate_connection_sql** | **str** | A simple SQL statement used by PingFederate at runtime to verify that the database connection is still active and to reconnect if needed. | [optional] 
**allow_multi_value_attributes** | **bool** | Indicates that this data store can select more than one record from a column and return the results as a multi-value attribute. | [optional] 
**min_pool_size** | **int** | The smallest number of database connections in the connection pool for the given data store. Omitting this attribute will set the value to the connection pool default. | [optional] 
**max_pool_size** | **int** | The largest number of database connections in the connection pool for the given data store. Omitting this attribute will set the value to the connection pool default. | [optional] 
**blocking_timeout** | **int** | The amount of time in milliseconds a request waits to get a connection from the connection pool before it fails. Omitting this attribute will set the value to the connection pool default. | [optional] 
**idle_timeout** | **int** | The length of time in minutes the connection can be idle in the pool before it is closed. Omitting this attribute will set the value to the connection pool default. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


