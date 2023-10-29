# swagger_client.TokenProcessorToTokenGeneratorMappingsApi

All URIs are relative to *https://localhost:9999/pf-admin-api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_token_to_token_mapping**](TokenProcessorToTokenGeneratorMappingsApi.md#create_token_to_token_mapping) | **POST** /tokenProcessorToTokenGeneratorMappings | Create a new Token Processor to Token Generator Mapping.
[**delete_token_to_token_mapping_by_id**](TokenProcessorToTokenGeneratorMappingsApi.md#delete_token_to_token_mapping_by_id) | **DELETE** /tokenProcessorToTokenGeneratorMappings/{id} | Delete a Token Processor to Token Generator Mapping.
[**get_token_to_token_mapping_by_id**](TokenProcessorToTokenGeneratorMappingsApi.md#get_token_to_token_mapping_by_id) | **GET** /tokenProcessorToTokenGeneratorMappings/{id} | Get a Token Processor to Token Generator Mapping.
[**get_token_to_token_mappings**](TokenProcessorToTokenGeneratorMappingsApi.md#get_token_to_token_mappings) | **GET** /tokenProcessorToTokenGeneratorMappings | Get the list of Token Processor to Token Generator Mappings.
[**update_token_to_token_mapping_by_id**](TokenProcessorToTokenGeneratorMappingsApi.md#update_token_to_token_mapping_by_id) | **PUT** /tokenProcessorToTokenGeneratorMappings/{id} | Update a Token Processor to Token Generator Mapping.


# **create_token_to_token_mapping**
> TokenToTokenMapping create_token_to_token_mapping(body, x_bypass_external_validation=x_bypass_external_validation)

Create a new Token Processor to Token Generator Mapping.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TokenProcessorToTokenGeneratorMappingsApi()
body = swagger_client.TokenToTokenMapping() # TokenToTokenMapping | Configuration for a new Token Processor to Token Generator Mapping.
x_bypass_external_validation = false # bool | External validation will be bypassed when set to true. Default to false. (optional) (default to false)

try:
    # Create a new Token Processor to Token Generator Mapping.
    api_response = api_instance.create_token_to_token_mapping(body, x_bypass_external_validation=x_bypass_external_validation)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TokenProcessorToTokenGeneratorMappingsApi->create_token_to_token_mapping: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TokenToTokenMapping**](TokenToTokenMapping.md)| Configuration for a new Token Processor to Token Generator Mapping. | 
 **x_bypass_external_validation** | **bool**| External validation will be bypassed when set to true. Default to false. | [optional] [default to false]

### Return type

[**TokenToTokenMapping**](TokenToTokenMapping.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_token_to_token_mapping_by_id**
> delete_token_to_token_mapping_by_id(id)

Delete a Token Processor to Token Generator Mapping.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TokenProcessorToTokenGeneratorMappingsApi()
id = 'id_example' # str | ID of Token Processor to Token Generator Mapping to delete.

try:
    # Delete a Token Processor to Token Generator Mapping.
    api_instance.delete_token_to_token_mapping_by_id(id)
except ApiException as e:
    print("Exception when calling TokenProcessorToTokenGeneratorMappingsApi->delete_token_to_token_mapping_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of Token Processor to Token Generator Mapping to delete. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_token_to_token_mapping_by_id**
> TokenToTokenMapping get_token_to_token_mapping_by_id(id)

Get a Token Processor to Token Generator Mapping.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TokenProcessorToTokenGeneratorMappingsApi()
id = 'id_example' # str | ID of Token Processor to Token Generator Mapping to fetch.

try:
    # Get a Token Processor to Token Generator Mapping.
    api_response = api_instance.get_token_to_token_mapping_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TokenProcessorToTokenGeneratorMappingsApi->get_token_to_token_mapping_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of Token Processor to Token Generator Mapping to fetch. | 

### Return type

[**TokenToTokenMapping**](TokenToTokenMapping.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_token_to_token_mappings**
> TokenToTokenMappings get_token_to_token_mappings()

Get the list of Token Processor to Token Generator Mappings.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TokenProcessorToTokenGeneratorMappingsApi()

try:
    # Get the list of Token Processor to Token Generator Mappings.
    api_response = api_instance.get_token_to_token_mappings()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TokenProcessorToTokenGeneratorMappingsApi->get_token_to_token_mappings: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**TokenToTokenMappings**](TokenToTokenMappings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_token_to_token_mapping_by_id**
> TokenToTokenMapping update_token_to_token_mapping_by_id(id, body, x_bypass_external_validation=x_bypass_external_validation)

Update a Token Processor to Token Generator Mapping.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TokenProcessorToTokenGeneratorMappingsApi()
id = 'id_example' # str | ID of Token Processor to Token Generator Mapping to update.
body = swagger_client.TokenToTokenMapping() # TokenToTokenMapping | Configuration for updated Token Processor to Token Generator Mapping.
x_bypass_external_validation = false # bool | External validation will be bypassed when set to true. Default to false. (optional) (default to false)

try:
    # Update a Token Processor to Token Generator Mapping.
    api_response = api_instance.update_token_to_token_mapping_by_id(id, body, x_bypass_external_validation=x_bypass_external_validation)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TokenProcessorToTokenGeneratorMappingsApi->update_token_to_token_mapping_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of Token Processor to Token Generator Mapping to update. | 
 **body** | [**TokenToTokenMapping**](TokenToTokenMapping.md)| Configuration for updated Token Processor to Token Generator Mapping. | 
 **x_bypass_external_validation** | **bool**| External validation will be bypassed when set to true. Default to false. | [optional] [default to false]

### Return type

[**TokenToTokenMapping**](TokenToTokenMapping.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

