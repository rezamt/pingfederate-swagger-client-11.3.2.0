# JdbcAttributeSource

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**schema** | **str** | Lists the table structure that stores information within a database. Some databases, such as Oracle, require a schema for a JDBC query. Other databases, such as MySQL, do not require a schema. | [optional] 
**table** | **str** | The name of the database table. The name is used to construct the SQL query to retrieve data from the data store. | 
**column_names** | **list[str]** | A list of column names used to construct the SQL query to retrieve data from the specified table in the datastore. | [optional] 
**filter** | **str** | The JDBC WHERE clause used to query your data store to locate a user record. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


