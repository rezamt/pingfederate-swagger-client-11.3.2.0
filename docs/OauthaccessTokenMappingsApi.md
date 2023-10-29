# swagger_client.OauthaccessTokenMappingsApi

All URIs are relative to *https://localhost:9999/pf-admin-api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_mapping**](OauthaccessTokenMappingsApi.md#create_mapping) | **POST** /oauth/accessTokenMappings | Create a new Access Token Mapping.
[**delete_mapping**](OauthaccessTokenMappingsApi.md#delete_mapping) | **DELETE** /oauth/accessTokenMappings/{id} | Delete an Access Token Mapping.
[**get_mapping**](OauthaccessTokenMappingsApi.md#get_mapping) | **GET** /oauth/accessTokenMappings/{id} | Find the Access Token Mapping by its ID.
[**get_mappings**](OauthaccessTokenMappingsApi.md#get_mappings) | **GET** /oauth/accessTokenMappings | Get the list of Access Token Mappings.
[**update_mapping**](OauthaccessTokenMappingsApi.md#update_mapping) | **PUT** /oauth/accessTokenMappings/{id} | Update an Access Token Mapping.


# **create_mapping**
> AccessTokenMapping create_mapping(body, x_bypass_external_validation=x_bypass_external_validation)

Create a new Access Token Mapping.

Create a new Access Token Mapping. If the mapping is not properly configured, a 422 status code is returned along with a list of validation errors that must be corrected.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OauthaccessTokenMappingsApi()
body = swagger_client.AccessTokenMapping() # AccessTokenMapping | Configuration for the new Access Token Mapping.
x_bypass_external_validation = false # bool | External validation will be bypassed when set to true. Default to false. (optional) (default to false)

try:
    # Create a new Access Token Mapping.
    api_response = api_instance.create_mapping(body, x_bypass_external_validation=x_bypass_external_validation)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OauthaccessTokenMappingsApi->create_mapping: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AccessTokenMapping**](AccessTokenMapping.md)| Configuration for the new Access Token Mapping. | 
 **x_bypass_external_validation** | **bool**| External validation will be bypassed when set to true. Default to false. | [optional] [default to false]

### Return type

[**AccessTokenMapping**](AccessTokenMapping.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_mapping**
> delete_mapping(id)

Delete an Access Token Mapping.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OauthaccessTokenMappingsApi()
id = 'id_example' # str | ID of the Access Token Mapping.

try:
    # Delete an Access Token Mapping.
    api_instance.delete_mapping(id)
except ApiException as e:
    print("Exception when calling OauthaccessTokenMappingsApi->delete_mapping: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the Access Token Mapping. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_mapping**
> AccessTokenMapping get_mapping(id)

Find the Access Token Mapping by its ID.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OauthaccessTokenMappingsApi()
id = 'id_example' # str | ID of the Access Token Mapping.

try:
    # Find the Access Token Mapping by its ID.
    api_response = api_instance.get_mapping(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OauthaccessTokenMappingsApi->get_mapping: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the Access Token Mapping. | 

### Return type

[**AccessTokenMapping**](AccessTokenMapping.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_mappings**
> AccessTokenMappings get_mappings()

Get the list of Access Token Mappings.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OauthaccessTokenMappingsApi()

try:
    # Get the list of Access Token Mappings.
    api_response = api_instance.get_mappings()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OauthaccessTokenMappingsApi->get_mappings: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AccessTokenMappings**](AccessTokenMappings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_mapping**
> AccessTokenMapping update_mapping(id, body, x_bypass_external_validation=x_bypass_external_validation)

Update an Access Token Mapping.

Update an Access Token Mapping with the matching ID. If the mapping is not properly configured, a 422 status code is returned along with a list of validation errors that must be corrected. Note: A 404 status code is returned for nonexistent mapping ID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OauthaccessTokenMappingsApi()
id = 'id_example' # str | ID of the Access Token Mapping to update.
body = swagger_client.AccessTokenMapping() # AccessTokenMapping | Configuration for updated mapping.
x_bypass_external_validation = false # bool | External validation will be bypassed when set to true. Default to false. (optional) (default to false)

try:
    # Update an Access Token Mapping.
    api_response = api_instance.update_mapping(id, body, x_bypass_external_validation=x_bypass_external_validation)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OauthaccessTokenMappingsApi->update_mapping: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the Access Token Mapping to update. | 
 **body** | [**AccessTokenMapping**](AccessTokenMapping.md)| Configuration for updated mapping. | 
 **x_bypass_external_validation** | **bool**| External validation will be bypassed when set to true. Default to false. | [optional] [default to false]

### Return type

[**AccessTokenMapping**](AccessTokenMapping.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

