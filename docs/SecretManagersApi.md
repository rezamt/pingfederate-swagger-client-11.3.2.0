# swagger_client.SecretManagersApi

All URIs are relative to *https://localhost:9999/pf-admin-api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_secret_manager**](SecretManagersApi.md#create_secret_manager) | **POST** /secretManagers | Create a secret manager plugin instance.
[**delete_secret_manager**](SecretManagersApi.md#delete_secret_manager) | **DELETE** /secretManagers/{id} | Delete a secret manager plugin instance.
[**get_action**](SecretManagersApi.md#get_action) | **GET** /secretManagers/{id}/actions/{actionId} | Get a secret manager plugin instance&#39;s action by ID.
[**get_actions**](SecretManagersApi.md#get_actions) | **GET** /secretManagers/{id}/actions | Get a list of actions for a secret manager plugin instance.
[**get_secret_manager**](SecretManagersApi.md#get_secret_manager) | **GET** /secretManagers/{id} | Get a specific secret manager plugin instance.
[**get_secret_manager_plugin_descriptor**](SecretManagersApi.md#get_secret_manager_plugin_descriptor) | **GET** /secretManagers/descriptors/{id} | Get a secret manager plugin descriptor.
[**get_secret_manager_plugin_descriptors**](SecretManagersApi.md#get_secret_manager_plugin_descriptors) | **GET** /secretManagers/descriptors | Get a list of available secret manager plugin descriptors.
[**get_secret_managers**](SecretManagersApi.md#get_secret_managers) | **GET** /secretManagers | Get a list of secret manager plugin instances.
[**invoke_action_with_options**](SecretManagersApi.md#invoke_action_with_options) | **POST** /secretManagers/{id}/actions/{actionId}/invokeAction | Invokes an action for secret manager plugin instance.
[**update_secret_manager**](SecretManagersApi.md#update_secret_manager) | **PUT** /secretManagers/{id} | Update a secret manager plugin instance.


# **create_secret_manager**
> SecretManager create_secret_manager(body)

Create a secret manager plugin instance.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SecretManagersApi()
body = swagger_client.SecretManager() # SecretManager | Configuration for a secret manager plugin instance.

try:
    # Create a secret manager plugin instance.
    api_response = api_instance.create_secret_manager(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SecretManagersApi->create_secret_manager: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SecretManager**](SecretManager.md)| Configuration for a secret manager plugin instance. | 

### Return type

[**SecretManager**](SecretManager.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_secret_manager**
> delete_secret_manager(id)

Delete a secret manager plugin instance.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SecretManagersApi()
id = 'id_example' # str | ID of a secret manager plugin instance.

try:
    # Delete a secret manager plugin instance.
    api_instance.delete_secret_manager(id)
except ApiException as e:
    print("Exception when calling SecretManagersApi->delete_secret_manager: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of a secret manager plugin instance. | 

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

Get a secret manager plugin instance's action by ID.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SecretManagersApi()
id = 'id_example' # str | ID of a secret manager plugin instance.
action_id = 'action_id_example' # str | ID of the action.

try:
    # Get a secret manager plugin instance's action by ID.
    api_response = api_instance.get_action(id, action_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SecretManagersApi->get_action: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of a secret manager plugin instance. | 
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

Get a list of actions for a secret manager plugin instance.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SecretManagersApi()
id = 'id_example' # str | ID of a secret manager plugin instance.

try:
    # Get a list of actions for a secret manager plugin instance.
    api_response = api_instance.get_actions(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SecretManagersApi->get_actions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of a secret manager plugin instance. | 

### Return type

[**Actions**](Actions.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_secret_manager**
> SecretManager get_secret_manager(id)

Get a specific secret manager plugin instance.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SecretManagersApi()
id = 'id_example' # str | ID of a secret manager plugin instance.

try:
    # Get a specific secret manager plugin instance.
    api_response = api_instance.get_secret_manager(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SecretManagersApi->get_secret_manager: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of a secret manager plugin instance. | 

### Return type

[**SecretManager**](SecretManager.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_secret_manager_plugin_descriptor**
> SecretManagerDescriptor get_secret_manager_plugin_descriptor(id)

Get a secret manager plugin descriptor.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SecretManagersApi()
id = 'id_example' # str | ID of secret manager plugin descriptor.

try:
    # Get a secret manager plugin descriptor.
    api_response = api_instance.get_secret_manager_plugin_descriptor(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SecretManagersApi->get_secret_manager_plugin_descriptor: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of secret manager plugin descriptor. | 

### Return type

[**SecretManagerDescriptor**](SecretManagerDescriptor.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_secret_manager_plugin_descriptors**
> SecretManagerDescriptors get_secret_manager_plugin_descriptors()

Get a list of available secret manager plugin descriptors.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SecretManagersApi()

try:
    # Get a list of available secret manager plugin descriptors.
    api_response = api_instance.get_secret_manager_plugin_descriptors()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SecretManagersApi->get_secret_manager_plugin_descriptors: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SecretManagerDescriptors**](SecretManagerDescriptors.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_secret_managers**
> SecretManagers get_secret_managers()

Get a list of secret manager plugin instances.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SecretManagersApi()

try:
    # Get a list of secret manager plugin instances.
    api_response = api_instance.get_secret_managers()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SecretManagersApi->get_secret_managers: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SecretManagers**](SecretManagers.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invoke_action_with_options**
> ActionResult invoke_action_with_options(id, action_id, body=body)

Invokes an action for secret manager plugin instance.

Invokes an action for secret manager plugin instance. A 404 status code is returned for nonexistent IDs. If the action produces a download file, the file will be returned directly in the response. Otherwise an ActionResult will be returned.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SecretManagersApi()
id = 'id_example' # str | ID of a secret manager plugin instance.
action_id = 'action_id_example' # str | ID of the action.
body = swagger_client.ActionOptions() # ActionOptions | Action options for action invoked. (optional)

try:
    # Invokes an action for secret manager plugin instance.
    api_response = api_instance.invoke_action_with_options(id, action_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SecretManagersApi->invoke_action_with_options: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of a secret manager plugin instance. | 
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

# **update_secret_manager**
> SecretManager update_secret_manager(id, body)

Update a secret manager plugin instance.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SecretManagersApi()
id = 'id_example' # str | ID of a secret manager plugin instance.
body = swagger_client.SecretManager() # SecretManager | Configuration for a secret manager plugin instance.

try:
    # Update a secret manager plugin instance.
    api_response = api_instance.update_secret_manager(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SecretManagersApi->update_secret_manager: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of a secret manager plugin instance. | 
 **body** | [**SecretManager**](SecretManager.md)| Configuration for a secret manager plugin instance. | 

### Return type

[**SecretManager**](SecretManager.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

