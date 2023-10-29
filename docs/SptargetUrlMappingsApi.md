# swagger_client.SptargetUrlMappingsApi

All URIs are relative to *https://localhost:9999/pf-admin-api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_url_mappings**](SptargetUrlMappingsApi.md#get_url_mappings) | **GET** /sp/targetUrlMappings | List the mappings between URLs and adapter or connection instances.
[**update_url_mappings**](SptargetUrlMappingsApi.md#update_url_mappings) | **PUT** /sp/targetUrlMappings | Update the mappings between URLs and adapters or connections instances.


# **get_url_mappings**
> SpUrlMappings get_url_mappings()

List the mappings between URLs and adapter or connection instances.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SptargetUrlMappingsApi()

try:
    # List the mappings between URLs and adapter or connection instances.
    api_response = api_instance.get_url_mappings()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SptargetUrlMappingsApi->get_url_mappings: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SpUrlMappings**](SpUrlMappings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_url_mappings**
> SpUrlMappings update_url_mappings(body)

Update the mappings between URLs and adapters or connections instances.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SptargetUrlMappingsApi()
body = swagger_client.SpUrlMappings() # SpUrlMappings | The SP adapter URL mappings to update.

try:
    # Update the mappings between URLs and adapters or connections instances.
    api_response = api_instance.update_url_mappings(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SptargetUrlMappingsApi->update_url_mappings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SpUrlMappings**](SpUrlMappings.md)| The SP adapter URL mappings to update. | 

### Return type

[**SpUrlMappings**](SpUrlMappings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

