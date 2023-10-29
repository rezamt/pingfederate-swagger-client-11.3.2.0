# swagger_client.DataStoresApi

All URIs are relative to *https://localhost:9999/pf-admin-api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_data_store**](DataStoresApi.md#create_data_store) | **POST** /dataStores | Create a new data store.
[**delete_data_store**](DataStoresApi.md#delete_data_store) | **DELETE** /dataStores/{id} | Delete a data store.
[**get_action**](DataStoresApi.md#get_action) | **GET** /dataStores/{id}/actions/{actionId} | Find a data store instance&#39;s action by ID.
[**get_actions**](DataStoresApi.md#get_actions) | **GET** /dataStores/{id}/actions | List the actions for a data store instance.
[**get_custom_data_store_descriptor**](DataStoresApi.md#get_custom_data_store_descriptor) | **GET** /dataStores/descriptors/{id} | Get the description of a custom data store plugin by ID.
[**get_custom_data_store_descriptors**](DataStoresApi.md#get_custom_data_store_descriptors) | **GET** /dataStores/descriptors | Get the list of available custom data store descriptors.
[**get_data_store**](DataStoresApi.md#get_data_store) | **GET** /dataStores/{id} | Find data store by ID.
[**get_data_stores**](DataStoresApi.md#get_data_stores) | **GET** /dataStores | Get list of all data stores.
[**invoke_action_with_options**](DataStoresApi.md#invoke_action_with_options) | **POST** /dataStores/{id}/actions/{actionId}/invokeAction | Invokes an action for a data source instance.
[**update_data_store**](DataStoresApi.md#update_data_store) | **PUT** /dataStores/{id} | Update a data store.


# **create_data_store**
> DataStore create_data_store(body, x_bypass_external_validation=x_bypass_external_validation)

Create a new data store.

Create a new data store. If the data store is not properly configured, a 422 status code is returned along with a list of validation errors that must be corrected.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DataStoresApi()
body = swagger_client.DataStore() # DataStore | Configuration for new data store.
x_bypass_external_validation = false # bool | Connection test will be bypassed when set to true. Default to false. (optional) (default to false)

try:
    # Create a new data store.
    api_response = api_instance.create_data_store(body, x_bypass_external_validation=x_bypass_external_validation)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataStoresApi->create_data_store: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DataStore**](DataStore.md)| Configuration for new data store. | 
 **x_bypass_external_validation** | **bool**| Connection test will be bypassed when set to true. Default to false. | [optional] [default to false]

### Return type

[**DataStore**](DataStore.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_data_store**
> delete_data_store(id)

Delete a data store.

Delete a data store with the specified ID. A 404 status code is returned for nonexistent IDs. Note: Only unused data stores can be deleted. If the request succeeds, the response body is empty. If the request fails, an ApiResult is returned with details of the error.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DataStoresApi()
id = 'id_example' # str | ID of data store instance.

try:
    # Delete a data store.
    api_instance.delete_data_store(id)
except ApiException as e:
    print("Exception when calling DataStoresApi->delete_data_store: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of data store instance. | 

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

Find a data store instance's action by ID.

Find a data store instance's action by ID. A 404 status code is returned for nonexistent IDs.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DataStoresApi()
id = 'id_example' # str | ID of data store to which these actions belong to.
action_id = 'action_id_example' # str | ID of the action.

try:
    # Find a data store instance's action by ID.
    api_response = api_instance.get_action(id, action_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataStoresApi->get_action: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of data store to which these actions belong to. | 
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

List the actions for a data store instance.

List the actions for a data store instance. A 404 status code is returned for nonexistent IDs.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DataStoresApi()
id = 'id_example' # str | ID of data store to which these actions belong to.

try:
    # List the actions for a data store instance.
    api_response = api_instance.get_actions(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataStoresApi->get_actions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of data store to which these actions belong to. | 

### Return type

[**Actions**](Actions.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_custom_data_store_descriptor**
> CustomDataStoreDescriptor get_custom_data_store_descriptor(id)

Get the description of a custom data store plugin by ID.

Get the description of a custom data store plugin by ID. A 404 status code is returned for nonexistent IDs.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DataStoresApi()
id = 'id_example' # str | ID of custom data store descriptor to fetch.

try:
    # Get the description of a custom data store plugin by ID.
    api_response = api_instance.get_custom_data_store_descriptor(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataStoresApi->get_custom_data_store_descriptor: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of custom data store descriptor to fetch. | 

### Return type

[**CustomDataStoreDescriptor**](CustomDataStoreDescriptor.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_custom_data_store_descriptors**
> CustomDataStoreDescriptors get_custom_data_store_descriptors()

Get the list of available custom data store descriptors.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DataStoresApi()

try:
    # Get the list of available custom data store descriptors.
    api_response = api_instance.get_custom_data_store_descriptors()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataStoresApi->get_custom_data_store_descriptors: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**CustomDataStoreDescriptors**](CustomDataStoreDescriptors.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_data_store**
> DataStore get_data_store(id)

Find data store by ID.

Get a data store with the specified ID. A 404 status code is returned for nonexistent IDs.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DataStoresApi()
id = 'id_example' # str | ID of data store instance.

try:
    # Find data store by ID.
    api_response = api_instance.get_data_store(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataStoresApi->get_data_store: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of data store instance. | 

### Return type

[**DataStore**](DataStore.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_data_stores**
> DataStores get_data_stores()

Get list of all data stores.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DataStoresApi()

try:
    # Get list of all data stores.
    api_response = api_instance.get_data_stores()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataStoresApi->get_data_stores: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**DataStores**](DataStores.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invoke_action_with_options**
> ActionResult invoke_action_with_options(id, action_id, body=body)

Invokes an action for a data source instance.

Invokes an action for a data source instance. A 404 status code is returned for nonexistent IDs. If the action produces a download file, the file will be returned directly in the response. Otherwise an ActionResult will be returned.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DataStoresApi()
id = 'id_example' # str | ID of data store to which these actions belong to.
action_id = 'action_id_example' # str | ID of the action.
body = swagger_client.ActionOptions() # ActionOptions | Action options for action invoked. (optional)

try:
    # Invokes an action for a data source instance.
    api_response = api_instance.invoke_action_with_options(id, action_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataStoresApi->invoke_action_with_options: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of data store to which these actions belong to. | 
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

# **update_data_store**
> DataStore update_data_store(id, body, x_bypass_external_validation=x_bypass_external_validation)

Update a data store.

Update a data store with the matching ID. If the data store is not properly configured, a 422 status code is returned along with a list of validation errors that must be corrected. Note: A 404 status code is returned for nonexistent IDs.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DataStoresApi()
id = 'id_example' # str | ID of data store instance.
body = swagger_client.DataStore() # DataStore | Configuration for the data store.
x_bypass_external_validation = false # bool | Connection test will be bypassed when set to true. Default to false. (optional) (default to false)

try:
    # Update a data store.
    api_response = api_instance.update_data_store(id, body, x_bypass_external_validation=x_bypass_external_validation)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataStoresApi->update_data_store: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of data store instance. | 
 **body** | [**DataStore**](DataStore.md)| Configuration for the data store. | 
 **x_bypass_external_validation** | **bool**| Connection test will be bypassed when set to true. Default to false. | [optional] [default to false]

### Return type

[**DataStore**](DataStore.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

