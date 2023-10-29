# swagger_client.IdpconnectorsApi

All URIs are relative to *https://localhost:9999/pf-admin-api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_idp_connector_descriptor_by_id**](IdpconnectorsApi.md#get_idp_connector_descriptor_by_id) | **GET** /idp/connectors/descriptors/{id} | Get the list of available connector descriptors.
[**get_idp_connector_descriptors**](IdpconnectorsApi.md#get_idp_connector_descriptors) | **GET** /idp/connectors/descriptors | Get the list of available IdP connector descriptors.


# **get_idp_connector_descriptor_by_id**
> SaasPluginDescriptor get_idp_connector_descriptor_by_id(id)

Get the list of available connector descriptors.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IdpconnectorsApi()
id = 'id_example' # str | the type of connector descriptor to fetch.

try:
    # Get the list of available connector descriptors.
    api_response = api_instance.get_idp_connector_descriptor_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IdpconnectorsApi->get_idp_connector_descriptor_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| the type of connector descriptor to fetch. | 

### Return type

[**SaasPluginDescriptor**](SaasPluginDescriptor.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_idp_connector_descriptors**
> SaasPluginDescriptors get_idp_connector_descriptors()

Get the list of available IdP connector descriptors.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IdpconnectorsApi()

try:
    # Get the list of available IdP connector descriptors.
    api_response = api_instance.get_idp_connector_descriptors()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IdpconnectorsApi->get_idp_connector_descriptors: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SaasPluginDescriptors**](SaasPluginDescriptors.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

