# swagger_client.ExtendedPropertiesApi

All URIs are relative to *https://localhost:9999/pf-admin-api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_extended_properties**](ExtendedPropertiesApi.md#get_extended_properties) | **GET** /extendedProperties | Get the defined Extended Properties.
[**update_extended_properties**](ExtendedPropertiesApi.md#update_extended_properties) | **PUT** /extendedProperties | Update the Extended Properties.


# **get_extended_properties**
> ExtendedProperties get_extended_properties()

Get the defined Extended Properties.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ExtendedPropertiesApi()

try:
    # Get the defined Extended Properties.
    api_response = api_instance.get_extended_properties()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExtendedPropertiesApi->get_extended_properties: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ExtendedProperties**](ExtendedProperties.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_extended_properties**
> ExtendedProperties update_extended_properties(body)

Update the Extended Properties.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ExtendedPropertiesApi()
body = swagger_client.ExtendedProperties() # ExtendedProperties | Definition of extended properties.

try:
    # Update the Extended Properties.
    api_response = api_instance.update_extended_properties(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExtendedPropertiesApi->update_extended_properties: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ExtendedProperties**](ExtendedProperties.md)| Definition of extended properties. | 

### Return type

[**ExtendedProperties**](ExtendedProperties.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

