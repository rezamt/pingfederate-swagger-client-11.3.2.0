# swagger_client.OauthclientSettingsApi

All URIs are relative to *https://localhost:9999/pf-admin-api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_client_settings**](OauthclientSettingsApi.md#get_client_settings) | **GET** /oauth/clientSettings | Configure the client settings.
[**update_client_settings**](OauthclientSettingsApi.md#update_client_settings) | **PUT** /oauth/clientSettings | Update the client settings.


# **get_client_settings**
> ClientSettings get_client_settings()

Configure the client settings.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OauthclientSettingsApi()

try:
    # Configure the client settings.
    api_response = api_instance.get_client_settings()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OauthclientSettingsApi->get_client_settings: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ClientSettings**](ClientSettings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_client_settings**
> ClientSettings update_client_settings(body)

Update the client settings.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OauthclientSettingsApi()
body = swagger_client.ClientSettings() # ClientSettings | Configuration for client settings.

try:
    # Update the client settings.
    api_response = api_instance.update_client_settings(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OauthclientSettingsApi->update_client_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ClientSettings**](ClientSettings.md)| Configuration for client settings. | 

### Return type

[**ClientSettings**](ClientSettings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

