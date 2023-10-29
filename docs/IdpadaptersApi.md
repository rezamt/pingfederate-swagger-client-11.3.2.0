# swagger_client.IdpadaptersApi

All URIs are relative to *https://localhost:9999/pf-admin-api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_idp_adapter**](IdpadaptersApi.md#create_idp_adapter) | **POST** /idp/adapters | Create a new IdP adapter instance.
[**delete_idp_adapter**](IdpadaptersApi.md#delete_idp_adapter) | **DELETE** /idp/adapters/{id} | Delete an IdP adapter instance.
[**get_action**](IdpadaptersApi.md#get_action) | **GET** /idp/adapters/{id}/actions/{actionId} | Find an IdP adapter instance&#39;s action by ID.
[**get_actions**](IdpadaptersApi.md#get_actions) | **GET** /idp/adapters/{id}/actions | List the actions for an IdP adapter instance.
[**get_idp_adapter**](IdpadaptersApi.md#get_idp_adapter) | **GET** /idp/adapters/{id} | Find an IdP adapter instance by ID.
[**get_idp_adapter_descriptors**](IdpadaptersApi.md#get_idp_adapter_descriptors) | **GET** /idp/adapters/descriptors | Get the list of available IdP adapter descriptors.
[**get_idp_adapter_descriptors_by_id**](IdpadaptersApi.md#get_idp_adapter_descriptors_by_id) | **GET** /idp/adapters/descriptors/{id} | Get the description of an IdP adapter plugin by ID.
[**get_idp_adapters**](IdpadaptersApi.md#get_idp_adapters) | **GET** /idp/adapters | Get the list of configured IdP adapter instances.
[**invoke_action_with_options**](IdpadaptersApi.md#invoke_action_with_options) | **POST** /idp/adapters/{id}/actions/{actionId}/invokeAction | Invokes an action for an IdP adapter instance.
[**update_idp_adapter**](IdpadaptersApi.md#update_idp_adapter) | **PUT** /idp/adapters/{id} | Update an IdP adapter instance.


# **create_idp_adapter**
> IdpAdapter create_idp_adapter(body, x_bypass_external_validation=x_bypass_external_validation)

Create a new IdP adapter instance.

Create a new IdP adapter instance. If the IdP adapter is not properly configured, a 422 status code is returned along with a list of validation errors that must be corrected.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IdpadaptersApi()
body = swagger_client.IdpAdapter() # IdpAdapter | Configuration for the IdP adapter instance.
x_bypass_external_validation = false # bool | External validation will be bypassed when set to true. Default to false. (optional) (default to false)

try:
    # Create a new IdP adapter instance.
    api_response = api_instance.create_idp_adapter(body, x_bypass_external_validation=x_bypass_external_validation)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IdpadaptersApi->create_idp_adapter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**IdpAdapter**](IdpAdapter.md)| Configuration for the IdP adapter instance. | 
 **x_bypass_external_validation** | **bool**| External validation will be bypassed when set to true. Default to false. | [optional] [default to false]

### Return type

[**IdpAdapter**](IdpAdapter.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_idp_adapter**
> delete_idp_adapter(id)

Delete an IdP adapter instance.

Delete an IdP adapter instance with the specified ID. A 404 status code is returned for nonexistent IDs. Note: Only adapters not in use can be deleted. If the request succeeds, the response body is empty. If the request fails, an ApiResult is returned with details of the error.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IdpadaptersApi()
id = 'id_example' # str | ID of IdP adapter instance.

try:
    # Delete an IdP adapter instance.
    api_instance.delete_idp_adapter(id)
except ApiException as e:
    print("Exception when calling IdpadaptersApi->delete_idp_adapter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of IdP adapter instance. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_action**
> Action get_action(id, action_id)

Find an IdP adapter instance's action by ID.

Find an IdP adapter instance's action by ID. A 404 status code is returned for nonexistent IDs.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IdpadaptersApi()
id = 'id_example' # str | ID of the IdP adapter instance to which these actions belongs to.
action_id = 'action_id_example' # str | ID of the action.

try:
    # Find an IdP adapter instance's action by ID.
    api_response = api_instance.get_action(id, action_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IdpadaptersApi->get_action: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the IdP adapter instance to which these actions belongs to. | 
 **action_id** | **str**| ID of the action. | 

### Return type

[**Action**](Action.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_actions**
> Actions get_actions(id)

List the actions for an IdP adapter instance.

List the actions for an IdP adapter instance. A 404 status code is returned for nonexistent IDs.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IdpadaptersApi()
id = 'id_example' # str | ID of the IdP adapter instance to which these actions belongs to.

try:
    # List the actions for an IdP adapter instance.
    api_response = api_instance.get_actions(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IdpadaptersApi->get_actions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the IdP adapter instance to which these actions belongs to. | 

### Return type

[**Actions**](Actions.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_idp_adapter**
> IdpAdapter get_idp_adapter(id)

Find an IdP adapter instance by ID.

Get the configured IdP adapter instance with the specified ID. A 404 status code is returned for nonexistent IDs.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IdpadaptersApi()
id = 'id_example' # str | ID of IdP adapter instance.

try:
    # Find an IdP adapter instance by ID.
    api_response = api_instance.get_idp_adapter(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IdpadaptersApi->get_idp_adapter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of IdP adapter instance. | 

### Return type

[**IdpAdapter**](IdpAdapter.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_idp_adapter_descriptors**
> IdpAdapterDescriptors get_idp_adapter_descriptors()

Get the list of available IdP adapter descriptors.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IdpadaptersApi()

try:
    # Get the list of available IdP adapter descriptors.
    api_response = api_instance.get_idp_adapter_descriptors()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IdpadaptersApi->get_idp_adapter_descriptors: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**IdpAdapterDescriptors**](IdpAdapterDescriptors.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_idp_adapter_descriptors_by_id**
> IdpAdapterDescriptor get_idp_adapter_descriptors_by_id(id)

Get the description of an IdP adapter plugin by ID.

Get the description of an IdP adapter plugin by ID. A 404 status code is returned for nonexistent IDs.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IdpadaptersApi()
id = 'id_example' # str | ID of IdP adapter descriptor to fetch.

try:
    # Get the description of an IdP adapter plugin by ID.
    api_response = api_instance.get_idp_adapter_descriptors_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IdpadaptersApi->get_idp_adapter_descriptors_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of IdP adapter descriptor to fetch. | 

### Return type

[**IdpAdapterDescriptor**](IdpAdapterDescriptor.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_idp_adapters**
> IdpAdapters get_idp_adapters(page=page, number_per_page=number_per_page, filter=filter)

Get the list of configured IdP adapter instances.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IdpadaptersApi()
page = 56 # int | Page number to retrieve. (optional)
number_per_page = 56 # int | Number of adapters per page. (optional)
filter = 'filter_example' # str | Filter criteria limits the IdP adapters that are returned to only those that match it. The filter criteria is compared to the IdP adapter instance name and ID fields. The comparison is a case-insensitive partial match. No additional pattern based matching is supported. (optional)

try:
    # Get the list of configured IdP adapter instances.
    api_response = api_instance.get_idp_adapters(page=page, number_per_page=number_per_page, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IdpadaptersApi->get_idp_adapters: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number to retrieve. | [optional] 
 **number_per_page** | **int**| Number of adapters per page. | [optional] 
 **filter** | **str**| Filter criteria limits the IdP adapters that are returned to only those that match it. The filter criteria is compared to the IdP adapter instance name and ID fields. The comparison is a case-insensitive partial match. No additional pattern based matching is supported. | [optional] 

### Return type

[**IdpAdapters**](IdpAdapters.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invoke_action_with_options**
> ActionResult invoke_action_with_options(id, action_id, body=body)

Invokes an action for an IdP adapter instance.

Invokes an action for an IdP adapter instance. A 404 status code is returned for nonexistent IDs. If the action produces a download file, the file will be returned directly in the response. Otherwise an ActionResult will be returned.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IdpadaptersApi()
id = 'id_example' # str | ID of the IdP adapter instance to which these actions belongs to.
action_id = 'action_id_example' # str | ID of the action.
body = swagger_client.ActionOptions() # ActionOptions | Action options for action invoked. (optional)

try:
    # Invokes an action for an IdP adapter instance.
    api_response = api_instance.invoke_action_with_options(id, action_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IdpadaptersApi->invoke_action_with_options: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the IdP adapter instance to which these actions belongs to. | 
 **action_id** | **str**| ID of the action. | 
 **body** | [**ActionOptions**](ActionOptions.md)| Action options for action invoked. | [optional] 

### Return type

[**ActionResult**](ActionResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_idp_adapter**
> IdpAdapter update_idp_adapter(id, body, x_bypass_external_validation=x_bypass_external_validation)

Update an IdP adapter instance.

Update an IdP adapter instance.If the IdP adapter is not properly configured, a 422 status code is returned along with a list of validation errors that must be corrected.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IdpadaptersApi()
id = 'id_example' # str | ID of IdP adapter instance.
body = swagger_client.IdpAdapter() # IdpAdapter | Configuration for the IdP adapter instance.
x_bypass_external_validation = false # bool | External validation will be bypassed when set to true. Default to false. (optional) (default to false)

try:
    # Update an IdP adapter instance.
    api_response = api_instance.update_idp_adapter(id, body, x_bypass_external_validation=x_bypass_external_validation)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IdpadaptersApi->update_idp_adapter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of IdP adapter instance. | 
 **body** | [**IdpAdapter**](IdpAdapter.md)| Configuration for the IdP adapter instance. | 
 **x_bypass_external_validation** | **bool**| External validation will be bypassed when set to true. Default to false. | [optional] [default to false]

### Return type

[**IdpAdapter**](IdpAdapter.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

