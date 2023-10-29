# swagger_client.OauthoutOfBandAuthPluginsApi

All URIs are relative to *https://localhost:9999/pf-admin-api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_oob_authenticator**](OauthoutOfBandAuthPluginsApi.md#create_oob_authenticator) | **POST** /oauth/outOfBandAuthPlugins | Create an Out of Band authenticator plugin instance.
[**delete_oob_authenticator**](OauthoutOfBandAuthPluginsApi.md#delete_oob_authenticator) | **DELETE** /oauth/outOfBandAuthPlugins/{id} | Delete an Out of Band authenticator plugin instance.
[**get_action**](OauthoutOfBandAuthPluginsApi.md#get_action) | **GET** /oauth/outOfBandAuthPlugins/{id}/actions/{actionId} | Find an Out of Band authenticator plugin instance&#39;s action by ID.
[**get_actions**](OauthoutOfBandAuthPluginsApi.md#get_actions) | **GET** /oauth/outOfBandAuthPlugins/{id}/actions | List of actions for an Out of Band authenticator plugin instance.
[**get_oob_auth_plugin_descriptor**](OauthoutOfBandAuthPluginsApi.md#get_oob_auth_plugin_descriptor) | **GET** /oauth/outOfBandAuthPlugins/descriptors/{id} | Get the descriptor of an Out of Band authenticator plugin.
[**get_oob_auth_plugin_descriptors**](OauthoutOfBandAuthPluginsApi.md#get_oob_auth_plugin_descriptors) | **GET** /oauth/outOfBandAuthPlugins/descriptors | Get the list of available Out of Band authenticator plugin descriptors.
[**get_oob_authenticator**](OauthoutOfBandAuthPluginsApi.md#get_oob_authenticator) | **GET** /oauth/outOfBandAuthPlugins/{id} | Get a specific Out of Band authenticator plugin instance.
[**get_oob_authenticators**](OauthoutOfBandAuthPluginsApi.md#get_oob_authenticators) | **GET** /oauth/outOfBandAuthPlugins | Get a list of Out of Band authenticator plugin instances.
[**invoke_action_with_options**](OauthoutOfBandAuthPluginsApi.md#invoke_action_with_options) | **POST** /oauth/outOfBandAuthPlugins/{id}/actions/{actionId}/invokeAction | Invokes an action for Out of Band authenticator plugin instance.
[**update_oob_authenticator**](OauthoutOfBandAuthPluginsApi.md#update_oob_authenticator) | **PUT** /oauth/outOfBandAuthPlugins/{id} | Update an Out of Band authenticator plugin instance.


# **create_oob_authenticator**
> OutOfBandAuthenticator create_oob_authenticator(body)

Create an Out of Band authenticator plugin instance.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OauthoutOfBandAuthPluginsApi()
body = swagger_client.OutOfBandAuthenticator() # OutOfBandAuthenticator | Configuration for an Out of Band authenticator plugin instance.

try:
    # Create an Out of Band authenticator plugin instance.
    api_response = api_instance.create_oob_authenticator(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OauthoutOfBandAuthPluginsApi->create_oob_authenticator: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OutOfBandAuthenticator**](OutOfBandAuthenticator.md)| Configuration for an Out of Band authenticator plugin instance. | 

### Return type

[**OutOfBandAuthenticator**](OutOfBandAuthenticator.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_oob_authenticator**
> delete_oob_authenticator(id)

Delete an Out of Band authenticator plugin instance.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OauthoutOfBandAuthPluginsApi()
id = 'id_example' # str | ID of Out of Band authenticator plugin instance.

try:
    # Delete an Out of Band authenticator plugin instance.
    api_instance.delete_oob_authenticator(id)
except ApiException as e:
    print("Exception when calling OauthoutOfBandAuthPluginsApi->delete_oob_authenticator: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of Out of Band authenticator plugin instance. | 

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

Find an Out of Band authenticator plugin instance's action by ID.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OauthoutOfBandAuthPluginsApi()
id = 'id_example' # str | ID of the Out of Band authenticator plugin instance to which these actions belongs to.
action_id = 'action_id_example' # str | ID of the action.

try:
    # Find an Out of Band authenticator plugin instance's action by ID.
    api_response = api_instance.get_action(id, action_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OauthoutOfBandAuthPluginsApi->get_action: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the Out of Band authenticator plugin instance to which these actions belongs to. | 
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

List of actions for an Out of Band authenticator plugin instance.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OauthoutOfBandAuthPluginsApi()
id = 'id_example' # str | ID of the Out of Band authenticator plugin instance to which these actions belongs to.

try:
    # List of actions for an Out of Band authenticator plugin instance.
    api_response = api_instance.get_actions(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OauthoutOfBandAuthPluginsApi->get_actions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the Out of Band authenticator plugin instance to which these actions belongs to. | 

### Return type

[**Actions**](Actions.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_oob_auth_plugin_descriptor**
> OutOfBandAuthPluginDescriptor get_oob_auth_plugin_descriptor(id)

Get the descriptor of an Out of Band authenticator plugin.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OauthoutOfBandAuthPluginsApi()
id = 'id_example' # str | ID of an Out of Band authenticator plugin descriptor.

try:
    # Get the descriptor of an Out of Band authenticator plugin.
    api_response = api_instance.get_oob_auth_plugin_descriptor(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OauthoutOfBandAuthPluginsApi->get_oob_auth_plugin_descriptor: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of an Out of Band authenticator plugin descriptor. | 

### Return type

[**OutOfBandAuthPluginDescriptor**](OutOfBandAuthPluginDescriptor.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_oob_auth_plugin_descriptors**
> OutOfBandAuthPluginDescriptors get_oob_auth_plugin_descriptors()

Get the list of available Out of Band authenticator plugin descriptors.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OauthoutOfBandAuthPluginsApi()

try:
    # Get the list of available Out of Band authenticator plugin descriptors.
    api_response = api_instance.get_oob_auth_plugin_descriptors()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OauthoutOfBandAuthPluginsApi->get_oob_auth_plugin_descriptors: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**OutOfBandAuthPluginDescriptors**](OutOfBandAuthPluginDescriptors.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_oob_authenticator**
> OutOfBandAuthenticator get_oob_authenticator(id)

Get a specific Out of Band authenticator plugin instance.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OauthoutOfBandAuthPluginsApi()
id = 'id_example' # str | ID of Out of Band authenticator plugin instance.

try:
    # Get a specific Out of Band authenticator plugin instance.
    api_response = api_instance.get_oob_authenticator(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OauthoutOfBandAuthPluginsApi->get_oob_authenticator: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of Out of Band authenticator plugin instance. | 

### Return type

[**OutOfBandAuthenticator**](OutOfBandAuthenticator.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_oob_authenticators**
> OutOfBandAuthenticators get_oob_authenticators()

Get a list of Out of Band authenticator plugin instances.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OauthoutOfBandAuthPluginsApi()

try:
    # Get a list of Out of Band authenticator plugin instances.
    api_response = api_instance.get_oob_authenticators()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OauthoutOfBandAuthPluginsApi->get_oob_authenticators: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**OutOfBandAuthenticators**](OutOfBandAuthenticators.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invoke_action_with_options**
> ActionResult invoke_action_with_options(id, action_id, body=body)

Invokes an action for Out of Band authenticator plugin instance.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OauthoutOfBandAuthPluginsApi()
id = 'id_example' # str | ID of the Out of Band authenticator plugin instance to which these actions belongs to.
action_id = 'action_id_example' # str | ID of the action.
body = swagger_client.ActionOptions() # ActionOptions | Action options for action invoked. (optional)

try:
    # Invokes an action for Out of Band authenticator plugin instance.
    api_response = api_instance.invoke_action_with_options(id, action_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OauthoutOfBandAuthPluginsApi->invoke_action_with_options: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the Out of Band authenticator plugin instance to which these actions belongs to. | 
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

# **update_oob_authenticator**
> OutOfBandAuthenticator update_oob_authenticator(id, body)

Update an Out of Band authenticator plugin instance.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OauthoutOfBandAuthPluginsApi()
id = 'id_example' # str | ID of Out of Band authenticator plugin instance.
body = swagger_client.OutOfBandAuthenticator() # OutOfBandAuthenticator | Configuration for an Out of Band authenticator plugin instance.

try:
    # Update an Out of Band authenticator plugin instance.
    api_response = api_instance.update_oob_authenticator(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OauthoutOfBandAuthPluginsApi->update_oob_authenticator: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of Out of Band authenticator plugin instance. | 
 **body** | [**OutOfBandAuthenticator**](OutOfBandAuthenticator.md)| Configuration for an Out of Band authenticator plugin instance. | 

### Return type

[**OutOfBandAuthenticator**](OutOfBandAuthenticator.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

