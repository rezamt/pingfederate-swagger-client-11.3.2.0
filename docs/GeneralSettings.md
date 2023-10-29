# GeneralSettings

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disable_automatic_connection_validation** | **bool** | Boolean that disables automatic connection validation when set to true. The default is false. | [optional] 
**idp_connection_transaction_logging_override** | **str** | Determines the level of transaction logging for all identity provider connections. The default is DONT_OVERRIDE, in which case the logging level will be determined by each individual IdP connection | [optional] 
**sp_connection_transaction_logging_override** | **str** | Determines the level of transaction logging for all service provider connections. The default is DONT_OVERRIDE, in which case the logging level will be determined by each individual SP connection | [optional] 
**datastore_validation_interval_secs** | **int** | Determines how long (in seconds) the result of testing a datastore connection is cached. The default is 300. | [optional] 
**request_header_for_correlation_id** | **str** | HTTP request header for retrieving correlation ID. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


