# IncomingProxySettings

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**forwarded_ip_address_header_name** | **str** | Globally specify the header name (for example, X-Forwarded-For) where PingFederate should attempt to retrieve the client IP address in all HTTP requests. | [optional] 
**forwarded_ip_address_header_index** | **str** | PingFederate combines multiple comma-separated header values into the same order that they are received. Define which IP address you want to use. Default is to use the last address. | [optional] 
**forwarded_host_header_name** | **str** | Globally specify the header name (for example, X-Forwarded-Host) where PingFederate should attempt to retrieve the hostname and port in all HTTP requests. | [optional] 
**forwarded_host_header_index** | **str** | PingFederate combines multiple comma-separated header values into the same order that they are received. Define which hostname you want to use. Default is to use the last hostname. | [optional] 
**client_cert_ssl_header_name** | **str** | While the proxy server is configured to pass client certificates as HTTP request headers, specify the header name here. | [optional] 
**client_cert_chain_ssl_header_name** | **str** | While the proxy server is configured to pass client certificates as HTTP request headers, specify the chain header name here. | [optional] 
**proxy_terminates_https_conns** | **bool** | Allows you to globally specify that connections to the reverse proxy are made over HTTPS even when HTTP is used between the reverse proxy and PingFederate. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


