# swagger_client.ServiceAuthenticationApi

All URIs are relative to *https://localhost:9999/pf-admin-api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_service_authentication**](ServiceAuthenticationApi.md#get_service_authentication) | **GET** /serviceAuthentication | Get the service authentication settings.
[**update_service_authentication**](ServiceAuthenticationApi.md#update_service_authentication) | **PUT** /serviceAuthentication | Update the service authentication settings.


# **get_service_authentication**
> ServiceAuthentication get_service_authentication()

Get the service authentication settings.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ServiceAuthenticationApi()

try:
    # Get the service authentication settings.
    api_response = api_instance.get_service_authentication()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceAuthenticationApi->get_service_authentication: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ServiceAuthentication**](ServiceAuthentication.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_service_authentication**
> ServiceAuthentication update_service_authentication(body)

Update the service authentication settings.

Manage availability and credentials to services responsible for federation protocol handling, monitoring and administration.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ServiceAuthenticationApi()
body = swagger_client.ServiceAuthentication() # ServiceAuthentication | Service authentication settings.

try:
    # Update the service authentication settings.
    api_response = api_instance.update_service_authentication(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceAuthenticationApi->update_service_authentication: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ServiceAuthentication**](ServiceAuthentication.md)| Service authentication settings. | 

### Return type

[**ServiceAuthentication**](ServiceAuthentication.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

