# swagger_client.VirtualHostNamesApi

All URIs are relative to *https://localhost:9999/pf-admin-api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_virtual_host_names_settings**](VirtualHostNamesApi.md#get_virtual_host_names_settings) | **GET** /virtualHostNames | Retrieve virtual host names settings.
[**update_virtual_host_names_settings**](VirtualHostNamesApi.md#update_virtual_host_names_settings) | **PUT** /virtualHostNames | Update virtual host names settings.


# **get_virtual_host_names_settings**
> VirtualHostNameSettings get_virtual_host_names_settings()

Retrieve virtual host names settings.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VirtualHostNamesApi()

try:
    # Retrieve virtual host names settings.
    api_response = api_instance.get_virtual_host_names_settings()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VirtualHostNamesApi->get_virtual_host_names_settings: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**VirtualHostNameSettings**](VirtualHostNameSettings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_virtual_host_names_settings**
> VirtualHostNameSettings update_virtual_host_names_settings(body)

Update virtual host names settings.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VirtualHostNamesApi()
body = swagger_client.VirtualHostNameSettings() # VirtualHostNameSettings | Virtual host names settings.

try:
    # Update virtual host names settings.
    api_response = api_instance.update_virtual_host_names_settings(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VirtualHostNamesApi->update_virtual_host_names_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**VirtualHostNameSettings**](VirtualHostNameSettings.md)| Virtual host names settings. | 

### Return type

[**VirtualHostNameSettings**](VirtualHostNameSettings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

