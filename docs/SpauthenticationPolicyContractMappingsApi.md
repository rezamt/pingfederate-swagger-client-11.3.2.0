# swagger_client.SpauthenticationPolicyContractMappingsApi

All URIs are relative to *https://localhost:9999/pf-admin-api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_apc_to_sp_adapter_mapping**](SpauthenticationPolicyContractMappingsApi.md#create_apc_to_sp_adapter_mapping) | **POST** /sp/authenticationPolicyContractMappings | Create a new APC-to-SP Adapter Mapping.
[**delete_apc_to_sp_adapter_mapping_by_id**](SpauthenticationPolicyContractMappingsApi.md#delete_apc_to_sp_adapter_mapping_by_id) | **DELETE** /sp/authenticationPolicyContractMappings/{id} | Delete an APC-to-SP Adapter Mapping.
[**get_apc_to_sp_adapter_mapping_by_id**](SpauthenticationPolicyContractMappingsApi.md#get_apc_to_sp_adapter_mapping_by_id) | **GET** /sp/authenticationPolicyContractMappings/{id} | Get an APC-to-SP Adapter Mapping.
[**get_apc_to_sp_adapter_mappings**](SpauthenticationPolicyContractMappingsApi.md#get_apc_to_sp_adapter_mappings) | **GET** /sp/authenticationPolicyContractMappings | Get the list of APC-to-SP Adapter Mappings.
[**update_apc_to_sp_adapter_mapping_by_id**](SpauthenticationPolicyContractMappingsApi.md#update_apc_to_sp_adapter_mapping_by_id) | **PUT** /sp/authenticationPolicyContractMappings/{id} | Update an APC-to-SP Adapter Mapping.


# **create_apc_to_sp_adapter_mapping**
> ApcToSpAdapterMapping create_apc_to_sp_adapter_mapping(body, x_bypass_external_validation=x_bypass_external_validation)

Create a new APC-to-SP Adapter Mapping.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SpauthenticationPolicyContractMappingsApi()
body = swagger_client.ApcToSpAdapterMapping() # ApcToSpAdapterMapping | Configuration for a new APC-to-SP Adapter Mapping.
x_bypass_external_validation = false # bool | External validation will be bypassed when set to true. Default to false. (optional) (default to false)

try:
    # Create a new APC-to-SP Adapter Mapping.
    api_response = api_instance.create_apc_to_sp_adapter_mapping(body, x_bypass_external_validation=x_bypass_external_validation)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpauthenticationPolicyContractMappingsApi->create_apc_to_sp_adapter_mapping: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ApcToSpAdapterMapping**](ApcToSpAdapterMapping.md)| Configuration for a new APC-to-SP Adapter Mapping. | 
 **x_bypass_external_validation** | **bool**| External validation will be bypassed when set to true. Default to false. | [optional] [default to false]

### Return type

[**ApcToSpAdapterMapping**](ApcToSpAdapterMapping.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_apc_to_sp_adapter_mapping_by_id**
> delete_apc_to_sp_adapter_mapping_by_id(id)

Delete an APC-to-SP Adapter Mapping.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SpauthenticationPolicyContractMappingsApi()
id = 'id_example' # str | ID of APC-to-SP Adapter Mapping to delete.

try:
    # Delete an APC-to-SP Adapter Mapping.
    api_instance.delete_apc_to_sp_adapter_mapping_by_id(id)
except ApiException as e:
    print("Exception when calling SpauthenticationPolicyContractMappingsApi->delete_apc_to_sp_adapter_mapping_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of APC-to-SP Adapter Mapping to delete. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_apc_to_sp_adapter_mapping_by_id**
> ApcToSpAdapterMapping get_apc_to_sp_adapter_mapping_by_id(id)

Get an APC-to-SP Adapter Mapping.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SpauthenticationPolicyContractMappingsApi()
id = 'id_example' # str | ID of APC-to-SP Adapter Mapping to fetch.

try:
    # Get an APC-to-SP Adapter Mapping.
    api_response = api_instance.get_apc_to_sp_adapter_mapping_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpauthenticationPolicyContractMappingsApi->get_apc_to_sp_adapter_mapping_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of APC-to-SP Adapter Mapping to fetch. | 

### Return type

[**ApcToSpAdapterMapping**](ApcToSpAdapterMapping.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_apc_to_sp_adapter_mappings**
> ApcToSpAdapterMappings get_apc_to_sp_adapter_mappings()

Get the list of APC-to-SP Adapter Mappings.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SpauthenticationPolicyContractMappingsApi()

try:
    # Get the list of APC-to-SP Adapter Mappings.
    api_response = api_instance.get_apc_to_sp_adapter_mappings()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpauthenticationPolicyContractMappingsApi->get_apc_to_sp_adapter_mappings: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ApcToSpAdapterMappings**](ApcToSpAdapterMappings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_apc_to_sp_adapter_mapping_by_id**
> ApcToSpAdapterMapping update_apc_to_sp_adapter_mapping_by_id(id, body, x_bypass_external_validation=x_bypass_external_validation)

Update an APC-to-SP Adapter Mapping.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SpauthenticationPolicyContractMappingsApi()
id = 'id_example' # str | ID of APC-to-SP Adapter Mapping to update.
body = swagger_client.ApcToSpAdapterMapping() # ApcToSpAdapterMapping | Configuration for updated APC-to-SP Adapter Mapping.
x_bypass_external_validation = false # bool | External validation will be bypassed when set to true. Default to false. (optional) (default to false)

try:
    # Update an APC-to-SP Adapter Mapping.
    api_response = api_instance.update_apc_to_sp_adapter_mapping_by_id(id, body, x_bypass_external_validation=x_bypass_external_validation)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpauthenticationPolicyContractMappingsApi->update_apc_to_sp_adapter_mapping_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of APC-to-SP Adapter Mapping to update. | 
 **body** | [**ApcToSpAdapterMapping**](ApcToSpAdapterMapping.md)| Configuration for updated APC-to-SP Adapter Mapping. | 
 **x_bypass_external_validation** | **bool**| External validation will be bypassed when set to true. Default to false. | [optional] [default to false]

### Return type

[**ApcToSpAdapterMapping**](ApcToSpAdapterMapping.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

