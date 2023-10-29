# swagger_client.AuthenticationSelectorsApi

All URIs are relative to *https://localhost:9999/pf-admin-api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_authentication_selector**](AuthenticationSelectorsApi.md#create_authentication_selector) | **POST** /authenticationSelectors | Create a new authentication selector instance.
[**delete_authentication_selector**](AuthenticationSelectorsApi.md#delete_authentication_selector) | **DELETE** /authenticationSelectors/{id} | Delete an Authentication Selector instance.
[**get_authentication_selector**](AuthenticationSelectorsApi.md#get_authentication_selector) | **GET** /authenticationSelectors/{id} | Get an Authentication Selector instance by ID.
[**get_authentication_selector_descriptors**](AuthenticationSelectorsApi.md#get_authentication_selector_descriptors) | **GET** /authenticationSelectors/descriptors | Get the list of available Authentication Selector descriptors.
[**get_authentication_selector_descriptors_by_id**](AuthenticationSelectorsApi.md#get_authentication_selector_descriptors_by_id) | **GET** /authenticationSelectors/descriptors/{id} | Get the description of an Authentication Selector plugin by ID.
[**get_authentication_selectors**](AuthenticationSelectorsApi.md#get_authentication_selectors) | **GET** /authenticationSelectors | Get the list of configured Authentication Selector instances.
[**update_authentication_selector**](AuthenticationSelectorsApi.md#update_authentication_selector) | **PUT** /authenticationSelectors/{id} | Update an authentication selector instance.


# **create_authentication_selector**
> AuthenticationSelector create_authentication_selector(body)

Create a new authentication selector instance.

Create a new authentication selector instance. If the authentication selector is not properly configured, a 422 status code is returned along with a list of validation errors that must be corrected.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AuthenticationSelectorsApi()
body = swagger_client.AuthenticationSelector() # AuthenticationSelector | Configuration for a new authentication selector instance.

try:
    # Create a new authentication selector instance.
    api_response = api_instance.create_authentication_selector(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationSelectorsApi->create_authentication_selector: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AuthenticationSelector**](AuthenticationSelector.md)| Configuration for a new authentication selector instance. | 

### Return type

[**AuthenticationSelector**](AuthenticationSelector.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_authentication_selector**
> delete_authentication_selector(id)

Delete an Authentication Selector instance.

Delete an Authentication Selector instance with the specified ID. A 404 status code is returned for nonexistent IDs. Note: Only selectors not in use can be deleted. If the request succeeds, the response body is empty. If the request fails, an ApiResult is returned with details of the error.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AuthenticationSelectorsApi()
id = 'id_example' # str | ID of Authentication Selector to delete.

try:
    # Delete an Authentication Selector instance.
    api_instance.delete_authentication_selector(id)
except ApiException as e:
    print("Exception when calling AuthenticationSelectorsApi->delete_authentication_selector: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of Authentication Selector to delete. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_authentication_selector**
> AuthenticationSelector get_authentication_selector(id)

Get an Authentication Selector instance by ID.

Get the configured Authentication Selector instance with the specified ID. A 404 status code is returned for nonexistent IDs.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AuthenticationSelectorsApi()
id = 'id_example' # str | ID of Authentication Selector instance to fetch.

try:
    # Get an Authentication Selector instance by ID.
    api_response = api_instance.get_authentication_selector(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationSelectorsApi->get_authentication_selector: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of Authentication Selector instance to fetch. | 

### Return type

[**AuthenticationSelector**](AuthenticationSelector.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_authentication_selector_descriptors**
> AuthenticationSelectorDescriptors get_authentication_selector_descriptors()

Get the list of available Authentication Selector descriptors.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AuthenticationSelectorsApi()

try:
    # Get the list of available Authentication Selector descriptors.
    api_response = api_instance.get_authentication_selector_descriptors()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationSelectorsApi->get_authentication_selector_descriptors: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AuthenticationSelectorDescriptors**](AuthenticationSelectorDescriptors.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_authentication_selector_descriptors_by_id**
> AuthenticationSelectorDescriptor get_authentication_selector_descriptors_by_id(id)

Get the description of an Authentication Selector plugin by ID.

Get the description of an Authentication Selector plugin by ID. A 404 status code is returned for nonexistent IDs.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AuthenticationSelectorsApi()
id = 'id_example' # str | ID of Authentication Selector descriptor to fetch.

try:
    # Get the description of an Authentication Selector plugin by ID.
    api_response = api_instance.get_authentication_selector_descriptors_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationSelectorsApi->get_authentication_selector_descriptors_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of Authentication Selector descriptor to fetch. | 

### Return type

[**AuthenticationSelectorDescriptor**](AuthenticationSelectorDescriptor.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_authentication_selectors**
> AuthenticationSelectors get_authentication_selectors(page=page, number_per_page=number_per_page, filter=filter)

Get the list of configured Authentication Selector instances.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AuthenticationSelectorsApi()
page = 56 # int | Page number to retrieve. (optional)
number_per_page = 56 # int | Number of selectors per page. (optional)
filter = 'filter_example' # str | Filter criteria limits the authentication selector instances that are returned to only those that match it. The filter criteria is compared to the authentication selector instance name and ID fields. The comparison is a case-insensitive partial match. No additional pattern based matching is supported. (optional)

try:
    # Get the list of configured Authentication Selector instances.
    api_response = api_instance.get_authentication_selectors(page=page, number_per_page=number_per_page, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationSelectorsApi->get_authentication_selectors: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number to retrieve. | [optional] 
 **number_per_page** | **int**| Number of selectors per page. | [optional] 
 **filter** | **str**| Filter criteria limits the authentication selector instances that are returned to only those that match it. The filter criteria is compared to the authentication selector instance name and ID fields. The comparison is a case-insensitive partial match. No additional pattern based matching is supported. | [optional] 

### Return type

[**AuthenticationSelectors**](AuthenticationSelectors.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_authentication_selector**
> AuthenticationSelector update_authentication_selector(id, body)

Update an authentication selector instance.

Update an authentication selector instance. If the authentication selector is not properly configured, a 422 status code is returned along with a list of validation errors that must be corrected.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AuthenticationSelectorsApi()
id = 'id_example' # str | ID of the authentication selector instance.
body = swagger_client.AuthenticationSelector() # AuthenticationSelector | Configuration for updated authentication selector instance.

try:
    # Update an authentication selector instance.
    api_response = api_instance.update_authentication_selector(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationSelectorsApi->update_authentication_selector: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the authentication selector instance. | 
 **body** | [**AuthenticationSelector**](AuthenticationSelector.md)| Configuration for updated authentication selector instance. | 

### Return type

[**AuthenticationSelector**](AuthenticationSelector.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

