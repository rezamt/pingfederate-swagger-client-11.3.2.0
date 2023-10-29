# swagger_client.IncomingProxySettingsApi

All URIs are relative to *https://localhost:9999/pf-admin-api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_incoming_proxy_settings**](IncomingProxySettingsApi.md#get_incoming_proxy_settings) | **GET** /incomingProxySettings | Get incoming proxy settings.
[**update_incoming_proxy_settings**](IncomingProxySettingsApi.md#update_incoming_proxy_settings) | **PUT** /incomingProxySettings | Update incoming proxy settings.


# **get_incoming_proxy_settings**
> IncomingProxySettings get_incoming_proxy_settings()

Get incoming proxy settings.

When PingFederate is deployed behind a proxy server or load balancer, use information in HTTP headers added by the proxy server to construct correct responses.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IncomingProxySettingsApi()

try:
    # Get incoming proxy settings.
    api_response = api_instance.get_incoming_proxy_settings()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IncomingProxySettingsApi->get_incoming_proxy_settings: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**IncomingProxySettings**](IncomingProxySettings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_incoming_proxy_settings**
> IncomingProxySettings update_incoming_proxy_settings(body)

Update incoming proxy settings.

When PingFederate is deployed behind a proxy server or load balancer, use information in HTTP headers added by the proxy server to construct correct responses.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IncomingProxySettingsApi()
body = swagger_client.IncomingProxySettings() # IncomingProxySettings | Incoming proxy settings.

try:
    # Update incoming proxy settings.
    api_response = api_instance.update_incoming_proxy_settings(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IncomingProxySettingsApi->update_incoming_proxy_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**IncomingProxySettings**](IncomingProxySettings.md)| Incoming proxy settings. | 

### Return type

[**IncomingProxySettings**](IncomingProxySettings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

