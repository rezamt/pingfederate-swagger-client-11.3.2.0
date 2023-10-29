# swagger_client.SptokenGeneratorsApi

All URIs are relative to *https://localhost:9999/pf-admin-api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_token_generator**](SptokenGeneratorsApi.md#create_token_generator) | **POST** /sp/tokenGenerators | Create a new token generator instance.
[**delete_token_generator**](SptokenGeneratorsApi.md#delete_token_generator) | **DELETE** /sp/tokenGenerators/{id} | Delete a token generator instance.
[**get_token_generator**](SptokenGeneratorsApi.md#get_token_generator) | **GET** /sp/tokenGenerators/{id} | Find a token generator instance by ID.
[**get_token_generator_descriptors**](SptokenGeneratorsApi.md#get_token_generator_descriptors) | **GET** /sp/tokenGenerators/descriptors | Get the list of available token generators.
[**get_token_generator_descriptors_by_id**](SptokenGeneratorsApi.md#get_token_generator_descriptors_by_id) | **GET** /sp/tokenGenerators/descriptors/{id} | Get the description of a token generator plugin by ID.
[**get_token_generators**](SptokenGeneratorsApi.md#get_token_generators) | **GET** /sp/tokenGenerators | Get the list of token generator instances.
[**update_token_generator**](SptokenGeneratorsApi.md#update_token_generator) | **PUT** /sp/tokenGenerators/{id} | Update a token generator instance.


# **create_token_generator**
> TokenGenerator create_token_generator(body)

Create a new token generator instance.

Create a new token generator instance. If the token generator is not properly configured, a 422 status code is returned along with a list of validation errors that must be corrected.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SptokenGeneratorsApi()
body = swagger_client.TokenGenerator() # TokenGenerator | Configuration for a token generator instance.

try:
    # Create a new token generator instance.
    api_response = api_instance.create_token_generator(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SptokenGeneratorsApi->create_token_generator: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TokenGenerator**](TokenGenerator.md)| Configuration for a token generator instance. | 

### Return type

[**TokenGenerator**](TokenGenerator.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_token_generator**
> delete_token_generator(id)

Delete a token generator instance.

Delete a token generator instance with the specified ID. A 404 status code is returned for nonexistent IDs. Note: Only token generators not in use can be deleted. If the request succeeds, the response body is empty. If the request fails, an ApiResult is returned with details of the error.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SptokenGeneratorsApi()
id = 'id_example' # str | ID of the token generator instance to delete.

try:
    # Delete a token generator instance.
    api_instance.delete_token_generator(id)
except ApiException as e:
    print("Exception when calling SptokenGeneratorsApi->delete_token_generator: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the token generator instance to delete. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_token_generator**
> TokenGenerator get_token_generator(id)

Find a token generator instance by ID.

Get the configured token generator instance with the specified ID. A 404 status code is returned for nonexistent IDs.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SptokenGeneratorsApi()
id = 'id_example' # str | ID of the token generator instance to fetch.

try:
    # Find a token generator instance by ID.
    api_response = api_instance.get_token_generator(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SptokenGeneratorsApi->get_token_generator: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the token generator instance to fetch. | 

### Return type

[**TokenGenerator**](TokenGenerator.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_token_generator_descriptors**
> TokenGeneratorDescriptors get_token_generator_descriptors()

Get the list of available token generators.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SptokenGeneratorsApi()

try:
    # Get the list of available token generators.
    api_response = api_instance.get_token_generator_descriptors()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SptokenGeneratorsApi->get_token_generator_descriptors: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**TokenGeneratorDescriptors**](TokenGeneratorDescriptors.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_token_generator_descriptors_by_id**
> TokenGeneratorDescriptor get_token_generator_descriptors_by_id(id)

Get the description of a token generator plugin by ID.

Get the description of a token generator plugin by ID. A 404 status code is returned for nonexistent IDs.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SptokenGeneratorsApi()
id = 'id_example' # str | ID of a token generator descriptor to fetch.

try:
    # Get the description of a token generator plugin by ID.
    api_response = api_instance.get_token_generator_descriptors_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SptokenGeneratorsApi->get_token_generator_descriptors_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of a token generator descriptor to fetch. | 

### Return type

[**TokenGeneratorDescriptor**](TokenGeneratorDescriptor.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_token_generators**
> TokenGenerators get_token_generators()

Get the list of token generator instances.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SptokenGeneratorsApi()

try:
    # Get the list of token generator instances.
    api_response = api_instance.get_token_generators()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SptokenGeneratorsApi->get_token_generators: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**TokenGenerators**](TokenGenerators.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_token_generator**
> TokenGenerator update_token_generator(id, body)

Update a token generator instance.

Update a token generator instance. If the token generator is not properly configured, a 422 status code is returned along with a list of validation errors that must be corrected.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SptokenGeneratorsApi()
id = 'id_example' # str | ID of the token generator instance.
body = swagger_client.TokenGenerator() # TokenGenerator | Configuration for the updated token generator instance.

try:
    # Update a token generator instance.
    api_response = api_instance.update_token_generator(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SptokenGeneratorsApi->update_token_generator: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the token generator instance. | 
 **body** | [**TokenGenerator**](TokenGenerator.md)| Configuration for the updated token generator instance. | 

### Return type

[**TokenGenerator**](TokenGenerator.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

