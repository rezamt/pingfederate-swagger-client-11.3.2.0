# swagger_client.OauthauthorizationDetailProcessorsApi

All URIs are relative to *https://localhost:9999/pf-admin-api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_authorization_detail_processor**](OauthauthorizationDetailProcessorsApi.md#create_authorization_detail_processor) | **POST** /oauth/authorizationDetailProcessors | Create an authorization detail processor plugin instance.
[**delete_authorization_detail_processor**](OauthauthorizationDetailProcessorsApi.md#delete_authorization_detail_processor) | **DELETE** /oauth/authorizationDetailProcessors/{id} | Delete an authorization detail processor plugin instance.
[**get_authorization_detail_processor**](OauthauthorizationDetailProcessorsApi.md#get_authorization_detail_processor) | **GET** /oauth/authorizationDetailProcessors/{id} | Get a specific authorization detail processor plugin instance.
[**get_authorization_detail_processor_plugin_descriptor**](OauthauthorizationDetailProcessorsApi.md#get_authorization_detail_processor_plugin_descriptor) | **GET** /oauth/authorizationDetailProcessors/descriptors/{id} | Get an authorization detail processor plugin descriptor.
[**get_authorization_detail_processor_plugin_descriptors**](OauthauthorizationDetailProcessorsApi.md#get_authorization_detail_processor_plugin_descriptors) | **GET** /oauth/authorizationDetailProcessors/descriptors | Get a list of available authorization detail processor plugin descriptors.
[**get_authorization_detail_processors**](OauthauthorizationDetailProcessorsApi.md#get_authorization_detail_processors) | **GET** /oauth/authorizationDetailProcessors | Get a list of authorization detail processor plugin instances.
[**update_authorization_detail_processor**](OauthauthorizationDetailProcessorsApi.md#update_authorization_detail_processor) | **PUT** /oauth/authorizationDetailProcessors/{id} | Update an authorization detail processor plugin instance.


# **create_authorization_detail_processor**
> AuthorizationDetailProcessor create_authorization_detail_processor(body)

Create an authorization detail processor plugin instance.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OauthauthorizationDetailProcessorsApi()
body = swagger_client.AuthorizationDetailProcessor() # AuthorizationDetailProcessor | Configuration for a authorization detail processor plugin instance.

try:
    # Create an authorization detail processor plugin instance.
    api_response = api_instance.create_authorization_detail_processor(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OauthauthorizationDetailProcessorsApi->create_authorization_detail_processor: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AuthorizationDetailProcessor**](AuthorizationDetailProcessor.md)| Configuration for a authorization detail processor plugin instance. | 

### Return type

[**AuthorizationDetailProcessor**](AuthorizationDetailProcessor.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_authorization_detail_processor**
> delete_authorization_detail_processor(id)

Delete an authorization detail processor plugin instance.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OauthauthorizationDetailProcessorsApi()
id = 'id_example' # str | ID of an authorization detail processor plugin instance.

try:
    # Delete an authorization detail processor plugin instance.
    api_instance.delete_authorization_detail_processor(id)
except ApiException as e:
    print("Exception when calling OauthauthorizationDetailProcessorsApi->delete_authorization_detail_processor: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of an authorization detail processor plugin instance. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_authorization_detail_processor**
> AuthorizationDetailProcessor get_authorization_detail_processor(id)

Get a specific authorization detail processor plugin instance.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OauthauthorizationDetailProcessorsApi()
id = 'id_example' # str | ID of an authorization detail processor plugin instance.

try:
    # Get a specific authorization detail processor plugin instance.
    api_response = api_instance.get_authorization_detail_processor(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OauthauthorizationDetailProcessorsApi->get_authorization_detail_processor: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of an authorization detail processor plugin instance. | 

### Return type

[**AuthorizationDetailProcessor**](AuthorizationDetailProcessor.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_authorization_detail_processor_plugin_descriptor**
> AuthorizationDetailProcessorDescriptor get_authorization_detail_processor_plugin_descriptor(id)

Get an authorization detail processor plugin descriptor.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OauthauthorizationDetailProcessorsApi()
id = 'id_example' # str | ID of authorization detail processor plugin descriptor.

try:
    # Get an authorization detail processor plugin descriptor.
    api_response = api_instance.get_authorization_detail_processor_plugin_descriptor(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OauthauthorizationDetailProcessorsApi->get_authorization_detail_processor_plugin_descriptor: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of authorization detail processor plugin descriptor. | 

### Return type

[**AuthorizationDetailProcessorDescriptor**](AuthorizationDetailProcessorDescriptor.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_authorization_detail_processor_plugin_descriptors**
> AuthorizationDetailProcessorDescriptors get_authorization_detail_processor_plugin_descriptors()

Get a list of available authorization detail processor plugin descriptors.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OauthauthorizationDetailProcessorsApi()

try:
    # Get a list of available authorization detail processor plugin descriptors.
    api_response = api_instance.get_authorization_detail_processor_plugin_descriptors()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OauthauthorizationDetailProcessorsApi->get_authorization_detail_processor_plugin_descriptors: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AuthorizationDetailProcessorDescriptors**](AuthorizationDetailProcessorDescriptors.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_authorization_detail_processors**
> AuthorizationDetailProcessors get_authorization_detail_processors()

Get a list of authorization detail processor plugin instances.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OauthauthorizationDetailProcessorsApi()

try:
    # Get a list of authorization detail processor plugin instances.
    api_response = api_instance.get_authorization_detail_processors()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OauthauthorizationDetailProcessorsApi->get_authorization_detail_processors: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AuthorizationDetailProcessors**](AuthorizationDetailProcessors.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_authorization_detail_processor**
> AuthorizationDetailProcessor update_authorization_detail_processor(id, body)

Update an authorization detail processor plugin instance.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OauthauthorizationDetailProcessorsApi()
id = 'id_example' # str | ID of an authorization detail processor plugin instance.
body = swagger_client.AuthorizationDetailProcessor() # AuthorizationDetailProcessor | Configuration for a authorization detail processor plugin instance.

try:
    # Update an authorization detail processor plugin instance.
    api_response = api_instance.update_authorization_detail_processor(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OauthauthorizationDetailProcessorsApi->update_authorization_detail_processor: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of an authorization detail processor plugin instance. | 
 **body** | [**AuthorizationDetailProcessor**](AuthorizationDetailProcessor.md)| Configuration for a authorization detail processor plugin instance. | 

### Return type

[**AuthorizationDetailProcessor**](AuthorizationDetailProcessor.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

