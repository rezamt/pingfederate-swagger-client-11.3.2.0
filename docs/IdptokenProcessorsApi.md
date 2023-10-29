# swagger_client.IdptokenProcessorsApi

All URIs are relative to *https://localhost:9999/pf-admin-api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_token_processor**](IdptokenProcessorsApi.md#create_token_processor) | **POST** /idp/tokenProcessors | Create a new token processor instance.
[**delete_token_processor**](IdptokenProcessorsApi.md#delete_token_processor) | **DELETE** /idp/tokenProcessors/{id} | Delete a token processor instance.
[**get_token_processor**](IdptokenProcessorsApi.md#get_token_processor) | **GET** /idp/tokenProcessors/{id} | Find a token processor instance by ID.
[**get_token_processor_descriptors**](IdptokenProcessorsApi.md#get_token_processor_descriptors) | **GET** /idp/tokenProcessors/descriptors | Get the list of available token processors.
[**get_token_processor_descriptors_by_id**](IdptokenProcessorsApi.md#get_token_processor_descriptors_by_id) | **GET** /idp/tokenProcessors/descriptors/{id} | Get the description of a token processor plugin by ID.
[**get_token_processors**](IdptokenProcessorsApi.md#get_token_processors) | **GET** /idp/tokenProcessors | Get the list of token processor instances.
[**update_token_processor**](IdptokenProcessorsApi.md#update_token_processor) | **PUT** /idp/tokenProcessors/{id} | Update a token processor instance.


# **create_token_processor**
> TokenProcessor create_token_processor(body)

Create a new token processor instance.

Create a new token processor instance. If the token processor is not properly configured, a 422 status code is returned along with a list of validation errors that must be corrected.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IdptokenProcessorsApi()
body = swagger_client.TokenProcessor() # TokenProcessor | Configuration for a token processor instance.

try:
    # Create a new token processor instance.
    api_response = api_instance.create_token_processor(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IdptokenProcessorsApi->create_token_processor: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TokenProcessor**](TokenProcessor.md)| Configuration for a token processor instance. | 

### Return type

[**TokenProcessor**](TokenProcessor.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_token_processor**
> delete_token_processor(id)

Delete a token processor instance.

Delete a token processor instance with the specified ID. A 404 status code is returned for nonexistent IDs. Note: Only token processors not in use can be deleted. If the request succeeds, the response body is empty. If the request fails, an ApiResult is returned with details of the error.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IdptokenProcessorsApi()
id = 'id_example' # str | ID of the token processor instance to delete.

try:
    # Delete a token processor instance.
    api_instance.delete_token_processor(id)
except ApiException as e:
    print("Exception when calling IdptokenProcessorsApi->delete_token_processor: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the token processor instance to delete. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_token_processor**
> TokenProcessor get_token_processor(id)

Find a token processor instance by ID.

Get the configured token processor instance with the specified ID. A 404 status code is returned for nonexistent IDs.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IdptokenProcessorsApi()
id = 'id_example' # str | ID of the token processor instance to fetch.

try:
    # Find a token processor instance by ID.
    api_response = api_instance.get_token_processor(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IdptokenProcessorsApi->get_token_processor: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the token processor instance to fetch. | 

### Return type

[**TokenProcessor**](TokenProcessor.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_token_processor_descriptors**
> TokenProcessorDescriptors get_token_processor_descriptors()

Get the list of available token processors.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IdptokenProcessorsApi()

try:
    # Get the list of available token processors.
    api_response = api_instance.get_token_processor_descriptors()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IdptokenProcessorsApi->get_token_processor_descriptors: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**TokenProcessorDescriptors**](TokenProcessorDescriptors.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_token_processor_descriptors_by_id**
> TokenProcessorDescriptor get_token_processor_descriptors_by_id(id)

Get the description of a token processor plugin by ID.

Get the description of a token processor plugin by ID. A 404 status code is returned for nonexistent IDs.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IdptokenProcessorsApi()
id = 'id_example' # str | ID of a token processor descriptor to fetch.

try:
    # Get the description of a token processor plugin by ID.
    api_response = api_instance.get_token_processor_descriptors_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IdptokenProcessorsApi->get_token_processor_descriptors_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of a token processor descriptor to fetch. | 

### Return type

[**TokenProcessorDescriptor**](TokenProcessorDescriptor.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_token_processors**
> TokenProcessors get_token_processors()

Get the list of token processor instances.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IdptokenProcessorsApi()

try:
    # Get the list of token processor instances.
    api_response = api_instance.get_token_processors()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IdptokenProcessorsApi->get_token_processors: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**TokenProcessors**](TokenProcessors.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_token_processor**
> TokenProcessor update_token_processor(id, body)

Update a token processor instance.

Update a token processor instance. If the token processor is not properly configured, a 422 status code is returned along with a list of validation errors that must be corrected.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IdptokenProcessorsApi()
id = 'id_example' # str | ID of token processor instance.
body = swagger_client.TokenProcessor() # TokenProcessor | Configuration for updated token processor instance.

try:
    # Update a token processor instance.
    api_response = api_instance.update_token_processor(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IdptokenProcessorsApi->update_token_processor: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of token processor instance. | 
 **body** | [**TokenProcessor**](TokenProcessor.md)| Configuration for updated token processor instance. | 

### Return type

[**TokenProcessor**](TokenProcessor.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

