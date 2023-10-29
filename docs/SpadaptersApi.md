# swagger_client.SpadaptersApi

All URIs are relative to *https://localhost:9999/pf-admin-api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_sp_adapter**](SpadaptersApi.md#create_sp_adapter) | **POST** /sp/adapters | Create a new SP adapter instance.
[**delete_sp_adapter**](SpadaptersApi.md#delete_sp_adapter) | **DELETE** /sp/adapters/{id} | Delete an SP adapter instance.
[**get_action**](SpadaptersApi.md#get_action) | **GET** /sp/adapters/{id}/actions/{actionId} | Find an SP adapter instance&#39;s action by ID.
[**get_actions**](SpadaptersApi.md#get_actions) | **GET** /sp/adapters/{id}/actions | List the actions for an SP adapter instance.
[**get_sp_adapter**](SpadaptersApi.md#get_sp_adapter) | **GET** /sp/adapters/{id} | Find an SP adapter instance by ID.
[**get_sp_adapter_descriptors**](SpadaptersApi.md#get_sp_adapter_descriptors) | **GET** /sp/adapters/descriptors | Get the list of available SP adapter descriptors.
[**get_sp_adapter_descriptors_by_id**](SpadaptersApi.md#get_sp_adapter_descriptors_by_id) | **GET** /sp/adapters/descriptors/{id} | Get the description of an SP adapter plugin by ID.
[**get_sp_adapters**](SpadaptersApi.md#get_sp_adapters) | **GET** /sp/adapters | Get the list of configured SP adapter instances.
[**get_url_mappings**](SpadaptersApi.md#get_url_mappings) | **GET** /sp/adapters/urlMappings | (Deprecated) List the mappings between URLs and adapter instances.
[**invoke_action_with_options**](SpadaptersApi.md#invoke_action_with_options) | **POST** /sp/adapters/{id}/actions/{actionId}/invokeAction | Invokes an action for an SP adapter instance.
[**update_sp_adapter**](SpadaptersApi.md#update_sp_adapter) | **PUT** /sp/adapters/{id} | Update an SP adapter instance.
[**update_url_mappings**](SpadaptersApi.md#update_url_mappings) | **PUT** /sp/adapters/urlMappings | (Deprecated) Update the mappings between URLs and adapters instances.


# **create_sp_adapter**
> SpAdapter create_sp_adapter(body)

Create a new SP adapter instance.

Create a new SP adapter instance. If the SP adapter is not properly configured, a 422 status code is returned along with a list of validation errors that must be corrected.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SpadaptersApi()
body = swagger_client.SpAdapter() # SpAdapter | Configuration for the SP adapter instance.

try:
    # Create a new SP adapter instance.
    api_response = api_instance.create_sp_adapter(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpadaptersApi->create_sp_adapter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SpAdapter**](SpAdapter.md)| Configuration for the SP adapter instance. | 

### Return type

[**SpAdapter**](SpAdapter.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_sp_adapter**
> delete_sp_adapter(id)

Delete an SP adapter instance.

Delete an SP adapter instance with the specified ID. A 404 status code is returned for nonexistent IDs. Note: Only adapters not in use can be deleted. If the request succeeds, the response body is empty. If the request fails, an ApiResult is returned with details of the error.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SpadaptersApi()
id = 'id_example' # str | ID of SP adapter instance.

try:
    # Delete an SP adapter instance.
    api_instance.delete_sp_adapter(id)
except ApiException as e:
    print("Exception when calling SpadaptersApi->delete_sp_adapter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of SP adapter instance. | 

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

Find an SP adapter instance's action by ID.

Find an SP adapter instance's action by ID. A 404 status code is returned for nonexistent IDs.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SpadaptersApi()
id = 'id_example' # str | ID of the SP adapter instance to which this action belongs to.
action_id = 'action_id_example' # str | ID of the action.

try:
    # Find an SP adapter instance's action by ID.
    api_response = api_instance.get_action(id, action_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpadaptersApi->get_action: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the SP adapter instance to which this action belongs to. | 
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

List the actions for an SP adapter instance.

List the actions for an SP adapter instance. A 404 status code is returned for nonexistent IDs.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SpadaptersApi()
id = 'id_example' # str | ID of the SP adapter instance to which this action belongs to.

try:
    # List the actions for an SP adapter instance.
    api_response = api_instance.get_actions(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpadaptersApi->get_actions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the SP adapter instance to which this action belongs to. | 

### Return type

[**Actions**](Actions.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sp_adapter**
> SpAdapter get_sp_adapter(id)

Find an SP adapter instance by ID.

Get the configured SP adapter instance with the specified ID. A 404 status code is returned for nonexistent IDs.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SpadaptersApi()
id = 'id_example' # str | ID of SP adapter instance.

try:
    # Find an SP adapter instance by ID.
    api_response = api_instance.get_sp_adapter(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpadaptersApi->get_sp_adapter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of SP adapter instance. | 

### Return type

[**SpAdapter**](SpAdapter.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sp_adapter_descriptors**
> SpAdapterDescriptors get_sp_adapter_descriptors()

Get the list of available SP adapter descriptors.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SpadaptersApi()

try:
    # Get the list of available SP adapter descriptors.
    api_response = api_instance.get_sp_adapter_descriptors()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpadaptersApi->get_sp_adapter_descriptors: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SpAdapterDescriptors**](SpAdapterDescriptors.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sp_adapter_descriptors_by_id**
> SpAdapterDescriptor get_sp_adapter_descriptors_by_id(id)

Get the description of an SP adapter plugin by ID.

Get the description of an SP adapter plugin by ID. A 404 status code is returned for nonexistent IDs.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SpadaptersApi()
id = 'id_example' # str | ID of SP adapter descriptor to fetch.

try:
    # Get the description of an SP adapter plugin by ID.
    api_response = api_instance.get_sp_adapter_descriptors_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpadaptersApi->get_sp_adapter_descriptors_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of SP adapter descriptor to fetch. | 

### Return type

[**SpAdapterDescriptor**](SpAdapterDescriptor.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sp_adapters**
> SpAdapters get_sp_adapters(page=page, number_per_page=number_per_page, filter=filter)

Get the list of configured SP adapter instances.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SpadaptersApi()
page = 56 # int | Page number to retrieve. (optional)
number_per_page = 56 # int | Number of adapters per page. (optional)
filter = 'filter_example' # str | Filter criteria limits the SP adapters that are returned to only those that match it. The filter criteria is compared to the SP adapter instance name and ID fields. The comparison is a case-insensitive partial match. No additional pattern based matching is supported. (optional)

try:
    # Get the list of configured SP adapter instances.
    api_response = api_instance.get_sp_adapters(page=page, number_per_page=number_per_page, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpadaptersApi->get_sp_adapters: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number to retrieve. | [optional] 
 **number_per_page** | **int**| Number of adapters per page. | [optional] 
 **filter** | **str**| Filter criteria limits the SP adapters that are returned to only those that match it. The filter criteria is compared to the SP adapter instance name and ID fields. The comparison is a case-insensitive partial match. No additional pattern based matching is supported. | [optional] 

### Return type

[**SpAdapters**](SpAdapters.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_url_mappings**
> SpAdapterUrlMappings get_url_mappings()

(Deprecated) List the mappings between URLs and adapter instances.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SpadaptersApi()

try:
    # (Deprecated) List the mappings between URLs and adapter instances.
    api_response = api_instance.get_url_mappings()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpadaptersApi->get_url_mappings: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SpAdapterUrlMappings**](SpAdapterUrlMappings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invoke_action_with_options**
> ActionResult invoke_action_with_options(id, action_id, body=body)

Invokes an action for an SP adapter instance.

Invokes an action for an SP adapter instance. A 404 status code is returned for nonexistent IDs. If the action produces a download file, the file will be returned directly in the response. Otherwise an ActionResult will be returned.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SpadaptersApi()
id = 'id_example' # str | ID of the SP adapter instance to which this action belongs to.
action_id = 'action_id_example' # str | ID of the action.
body = swagger_client.ActionOptions() # ActionOptions | Action options for action invoked. (optional)

try:
    # Invokes an action for an SP adapter instance.
    api_response = api_instance.invoke_action_with_options(id, action_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpadaptersApi->invoke_action_with_options: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the SP adapter instance to which this action belongs to. | 
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

# **update_sp_adapter**
> SpAdapter update_sp_adapter(id, body)

Update an SP adapter instance.

Update an SP adapter instance.If the SP adapter is not properly configured, a 422 status code is returned along with a list of validation errors that must be corrected.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SpadaptersApi()
id = 'id_example' # str | ID of SP adapter instance.
body = swagger_client.SpAdapter() # SpAdapter | Configuration for the SP adapter instance.

try:
    # Update an SP adapter instance.
    api_response = api_instance.update_sp_adapter(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpadaptersApi->update_sp_adapter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of SP adapter instance. | 
 **body** | [**SpAdapter**](SpAdapter.md)| Configuration for the SP adapter instance. | 

### Return type

[**SpAdapter**](SpAdapter.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_url_mappings**
> SpAdapterUrlMappings update_url_mappings(body)

(Deprecated) Update the mappings between URLs and adapters instances.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SpadaptersApi()
body = swagger_client.SpAdapterUrlMappings() # SpAdapterUrlMappings | The SP adapter URL mappings to update.

try:
    # (Deprecated) Update the mappings between URLs and adapters instances.
    api_response = api_instance.update_url_mappings(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpadaptersApi->update_url_mappings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SpAdapterUrlMappings**](SpAdapterUrlMappings.md)| The SP adapter URL mappings to update. | 

### Return type

[**SpAdapterUrlMappings**](SpAdapterUrlMappings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

