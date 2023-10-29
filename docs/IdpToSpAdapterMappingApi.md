# swagger_client.IdpToSpAdapterMappingApi

All URIs are relative to *https://localhost:9999/pf-admin-api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_idp_to_sp_adapter_mapping**](IdpToSpAdapterMappingApi.md#create_idp_to_sp_adapter_mapping) | **POST** /idpToSpAdapterMapping | Create a new IdP-to-SP Adapter mapping.
[**delete_idp_to_sp_adapter_mappings_by_id**](IdpToSpAdapterMappingApi.md#delete_idp_to_sp_adapter_mappings_by_id) | **DELETE** /idpToSpAdapterMapping/{id} | Delete an Adapter to Adapter Mapping.
[**get_idp_to_sp_adapter_mappings**](IdpToSpAdapterMappingApi.md#get_idp_to_sp_adapter_mappings) | **GET** /idpToSpAdapterMapping | Get list of IdP-to-SP Adapter Mappings.
[**get_idp_to_sp_adapter_mappings_by_id**](IdpToSpAdapterMappingApi.md#get_idp_to_sp_adapter_mappings_by_id) | **GET** /idpToSpAdapterMapping/{id} | Get an IdP-to-SP Adapter Mapping.
[**update_idp_to_sp_adapter_mapping**](IdpToSpAdapterMappingApi.md#update_idp_to_sp_adapter_mapping) | **PUT** /idpToSpAdapterMapping/{id} | Update the specified IdP-to-SP Adapter mapping.


# **create_idp_to_sp_adapter_mapping**
> IdpToSpAdapterMapping create_idp_to_sp_adapter_mapping(body, x_bypass_external_validation=x_bypass_external_validation)

Create a new IdP-to-SP Adapter mapping.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IdpToSpAdapterMappingApi()
body = swagger_client.IdpToSpAdapterMapping() # IdpToSpAdapterMapping | Configuration for new IdP-to-SP Adapter Mapping.
x_bypass_external_validation = false # bool | External validation will be bypassed when set to true. Default to false. (optional) (default to false)

try:
    # Create a new IdP-to-SP Adapter mapping.
    api_response = api_instance.create_idp_to_sp_adapter_mapping(body, x_bypass_external_validation=x_bypass_external_validation)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IdpToSpAdapterMappingApi->create_idp_to_sp_adapter_mapping: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**IdpToSpAdapterMapping**](IdpToSpAdapterMapping.md)| Configuration for new IdP-to-SP Adapter Mapping. | 
 **x_bypass_external_validation** | **bool**| External validation will be bypassed when set to true. Default to false. | [optional] [default to false]

### Return type

[**IdpToSpAdapterMapping**](IdpToSpAdapterMapping.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_idp_to_sp_adapter_mappings_by_id**
> delete_idp_to_sp_adapter_mappings_by_id(id)

Delete an Adapter to Adapter Mapping.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IdpToSpAdapterMappingApi()
id = 'id_example' # str | ID of the IdP-to-SP Adapter Mapping to delete.

try:
    # Delete an Adapter to Adapter Mapping.
    api_instance.delete_idp_to_sp_adapter_mappings_by_id(id)
except ApiException as e:
    print("Exception when calling IdpToSpAdapterMappingApi->delete_idp_to_sp_adapter_mappings_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the IdP-to-SP Adapter Mapping to delete. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_idp_to_sp_adapter_mappings**
> IdpToSpAdapterMappings get_idp_to_sp_adapter_mappings()

Get list of IdP-to-SP Adapter Mappings.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IdpToSpAdapterMappingApi()

try:
    # Get list of IdP-to-SP Adapter Mappings.
    api_response = api_instance.get_idp_to_sp_adapter_mappings()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IdpToSpAdapterMappingApi->get_idp_to_sp_adapter_mappings: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**IdpToSpAdapterMappings**](IdpToSpAdapterMappings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_idp_to_sp_adapter_mappings_by_id**
> IdpToSpAdapterMapping get_idp_to_sp_adapter_mappings_by_id(id)

Get an IdP-to-SP Adapter Mapping.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IdpToSpAdapterMappingApi()
id = 'id_example' # str | ID of IdP-to-SP Adapter Mapping to fetch.

try:
    # Get an IdP-to-SP Adapter Mapping.
    api_response = api_instance.get_idp_to_sp_adapter_mappings_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IdpToSpAdapterMappingApi->get_idp_to_sp_adapter_mappings_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of IdP-to-SP Adapter Mapping to fetch. | 

### Return type

[**IdpToSpAdapterMapping**](IdpToSpAdapterMapping.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_idp_to_sp_adapter_mapping**
> IdpToSpAdapterMapping update_idp_to_sp_adapter_mapping(id, body, x_bypass_external_validation=x_bypass_external_validation)

Update the specified IdP-to-SP Adapter mapping.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IdpToSpAdapterMappingApi()
id = 'id_example' # str | ID of source adapter in the IdP-to-SP Adapter Mapping to fetch.
body = swagger_client.IdpToSpAdapterMapping() # IdpToSpAdapterMapping | Configuration for updated IdP-to-SP Adapter Mapping.
x_bypass_external_validation = false # bool | External validation will be bypassed when set to true. Default to false. (optional) (default to false)

try:
    # Update the specified IdP-to-SP Adapter mapping.
    api_response = api_instance.update_idp_to_sp_adapter_mapping(id, body, x_bypass_external_validation=x_bypass_external_validation)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IdpToSpAdapterMappingApi->update_idp_to_sp_adapter_mapping: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of source adapter in the IdP-to-SP Adapter Mapping to fetch. | 
 **body** | [**IdpToSpAdapterMapping**](IdpToSpAdapterMapping.md)| Configuration for updated IdP-to-SP Adapter Mapping. | 
 **x_bypass_external_validation** | **bool**| External validation will be bypassed when set to true. Default to false. | [optional] [default to false]

### Return type

[**IdpToSpAdapterMapping**](IdpToSpAdapterMapping.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

