# swagger_client.OauthauthenticationPolicyContractMappingsApi

All URIs are relative to *https://localhost:9999/pf-admin-api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_apc_mapping**](OauthauthenticationPolicyContractMappingsApi.md#create_apc_mapping) | **POST** /oauth/authenticationPolicyContractMappings | Create a new authentication policy contract to persistent grant mapping.
[**delete_apc_mapping**](OauthauthenticationPolicyContractMappingsApi.md#delete_apc_mapping) | **DELETE** /oauth/authenticationPolicyContractMappings/{id} | Delete an authentication policy contract to persistent grant mapping.
[**get_apc_mapping**](OauthauthenticationPolicyContractMappingsApi.md#get_apc_mapping) | **GET** /oauth/authenticationPolicyContractMappings/{id} | Find the authentication policy contract to persistent grant mapping by ID.
[**get_apc_mappings**](OauthauthenticationPolicyContractMappingsApi.md#get_apc_mappings) | **GET** /oauth/authenticationPolicyContractMappings | Get the list of authentication policy contract to persistent grant mappings.
[**update_apc_mapping**](OauthauthenticationPolicyContractMappingsApi.md#update_apc_mapping) | **PUT** /oauth/authenticationPolicyContractMappings/{id} | Update an authentication policy contract to persistent grant mapping.


# **create_apc_mapping**
> ApcToPersistentGrantMapping create_apc_mapping(body, x_bypass_external_validation=x_bypass_external_validation)

Create a new authentication policy contract to persistent grant mapping.

Create a new authentication policy contract to persistent grant mapping. If a mapping can't be created, a 422 status code is returned along with a list of validation errors that must be corrected.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OauthauthenticationPolicyContractMappingsApi()
body = swagger_client.ApcToPersistentGrantMapping() # ApcToPersistentGrantMapping | Configuration for an authentication policy contract to persistent grant mapping.
x_bypass_external_validation = false # bool | External validation will be bypassed when set to true. Default to false. (optional) (default to false)

try:
    # Create a new authentication policy contract to persistent grant mapping.
    api_response = api_instance.create_apc_mapping(body, x_bypass_external_validation=x_bypass_external_validation)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OauthauthenticationPolicyContractMappingsApi->create_apc_mapping: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ApcToPersistentGrantMapping**](ApcToPersistentGrantMapping.md)| Configuration for an authentication policy contract to persistent grant mapping. | 
 **x_bypass_external_validation** | **bool**| External validation will be bypassed when set to true. Default to false. | [optional] [default to false]

### Return type

[**ApcToPersistentGrantMapping**](ApcToPersistentGrantMapping.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_apc_mapping**
> delete_apc_mapping(id)

Delete an authentication policy contract to persistent grant mapping.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OauthauthenticationPolicyContractMappingsApi()
id = 'id_example' # str | ID of the authentication policy contract to persistent grant mapping.

try:
    # Delete an authentication policy contract to persistent grant mapping.
    api_instance.delete_apc_mapping(id)
except ApiException as e:
    print("Exception when calling OauthauthenticationPolicyContractMappingsApi->delete_apc_mapping: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the authentication policy contract to persistent grant mapping. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_apc_mapping**
> ApcToPersistentGrantMapping get_apc_mapping(id)

Find the authentication policy contract to persistent grant mapping by ID.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OauthauthenticationPolicyContractMappingsApi()
id = 'id_example' # str | ID of the authentication policy contract to persistent grant mapping.

try:
    # Find the authentication policy contract to persistent grant mapping by ID.
    api_response = api_instance.get_apc_mapping(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OauthauthenticationPolicyContractMappingsApi->get_apc_mapping: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the authentication policy contract to persistent grant mapping. | 

### Return type

[**ApcToPersistentGrantMapping**](ApcToPersistentGrantMapping.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_apc_mappings**
> ApcToPersistentGrantMappings get_apc_mappings()

Get the list of authentication policy contract to persistent grant mappings.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OauthauthenticationPolicyContractMappingsApi()

try:
    # Get the list of authentication policy contract to persistent grant mappings.
    api_response = api_instance.get_apc_mappings()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OauthauthenticationPolicyContractMappingsApi->get_apc_mappings: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ApcToPersistentGrantMappings**](ApcToPersistentGrantMappings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_apc_mapping**
> ApcToPersistentGrantMapping update_apc_mapping(id, body, x_bypass_external_validation=x_bypass_external_validation)

Update an authentication policy contract to persistent grant mapping.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OauthauthenticationPolicyContractMappingsApi()
id = 'id_example' # str | ID of the authentication policy contract to persistent grant mapping to update.
body = swagger_client.ApcToPersistentGrantMapping() # ApcToPersistentGrantMapping | Configuration for an authentication policy contract to persistent grant mapping.
x_bypass_external_validation = false # bool | External validation will be bypassed when set to true. Default to false. (optional) (default to false)

try:
    # Update an authentication policy contract to persistent grant mapping.
    api_response = api_instance.update_apc_mapping(id, body, x_bypass_external_validation=x_bypass_external_validation)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OauthauthenticationPolicyContractMappingsApi->update_apc_mapping: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the authentication policy contract to persistent grant mapping to update. | 
 **body** | [**ApcToPersistentGrantMapping**](ApcToPersistentGrantMapping.md)| Configuration for an authentication policy contract to persistent grant mapping. | 
 **x_bypass_external_validation** | **bool**| External validation will be bypassed when set to true. Default to false. | [optional] [default to false]

### Return type

[**ApcToPersistentGrantMapping**](ApcToPersistentGrantMapping.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

