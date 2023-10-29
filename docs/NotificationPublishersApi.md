# swagger_client.NotificationPublishersApi

All URIs are relative to *https://localhost:9999/pf-admin-api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_notification_publisher**](NotificationPublishersApi.md#create_notification_publisher) | **POST** /notificationPublishers | Create a notification publisher plugin instance.
[**delete_notification_publisher**](NotificationPublishersApi.md#delete_notification_publisher) | **DELETE** /notificationPublishers/{id} | Delete a notification publisher plugin instance.
[**get_action**](NotificationPublishersApi.md#get_action) | **GET** /notificationPublishers/{id}/actions/{actionId} | Find an notification publisher plugin instance&#39;s action by ID.
[**get_actions**](NotificationPublishersApi.md#get_actions) | **GET** /notificationPublishers/{id}/actions | List the actions for a notification publisher plugin instance.
[**get_notification_publisher**](NotificationPublishersApi.md#get_notification_publisher) | **GET** /notificationPublishers/{id} | Get a specific notification publisher plugin instance.
[**get_notification_publisher_plugin_descriptor**](NotificationPublishersApi.md#get_notification_publisher_plugin_descriptor) | **GET** /notificationPublishers/descriptors/{id} | Get the description of a notification publisher plugin descriptor.
[**get_notification_publisher_plugin_descriptors**](NotificationPublishersApi.md#get_notification_publisher_plugin_descriptors) | **GET** /notificationPublishers/descriptors | Get the list of available Notification Publisher Plugin descriptors.
[**get_notification_publishers**](NotificationPublishersApi.md#get_notification_publishers) | **GET** /notificationPublishers | Get a list of notification publisher plugin instances.
[**get_settings**](NotificationPublishersApi.md#get_settings) | **GET** /notificationPublishers/settings | Get general notification publisher settings.
[**invoke_action_with_options**](NotificationPublishersApi.md#invoke_action_with_options) | **POST** /notificationPublishers/{id}/actions/{actionId}/invokeAction | Invokes an action for notification publisher plugin instance.
[**update_notification_publisher**](NotificationPublishersApi.md#update_notification_publisher) | **PUT** /notificationPublishers/{id} | Update a notification publisher plugin instance.
[**update_settings**](NotificationPublishersApi.md#update_settings) | **PUT** /notificationPublishers/settings | Update general notification publisher settings.


# **create_notification_publisher**
> NotificationPublisher create_notification_publisher(body)

Create a notification publisher plugin instance.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NotificationPublishersApi()
body = swagger_client.NotificationPublisher() # NotificationPublisher | Configuration for a notification publisher plugin instance.

try:
    # Create a notification publisher plugin instance.
    api_response = api_instance.create_notification_publisher(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificationPublishersApi->create_notification_publisher: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NotificationPublisher**](NotificationPublisher.md)| Configuration for a notification publisher plugin instance. | 

### Return type

[**NotificationPublisher**](NotificationPublisher.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_notification_publisher**
> delete_notification_publisher(id)

Delete a notification publisher plugin instance.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NotificationPublishersApi()
id = 'id_example' # str | ID of a notification publisher plugin instance.

try:
    # Delete a notification publisher plugin instance.
    api_instance.delete_notification_publisher(id)
except ApiException as e:
    print("Exception when calling NotificationPublishersApi->delete_notification_publisher: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of a notification publisher plugin instance. | 

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

Find an notification publisher plugin instance's action by ID.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NotificationPublishersApi()
id = 'id_example' # str | ID of the notification publisher plugin instance to which these actions belongs to.
action_id = 'action_id_example' # str | ID of the action to get.

try:
    # Find an notification publisher plugin instance's action by ID.
    api_response = api_instance.get_action(id, action_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificationPublishersApi->get_action: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the notification publisher plugin instance to which these actions belongs to. | 
 **action_id** | **str**| ID of the action to get. | 

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

List the actions for a notification publisher plugin instance.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NotificationPublishersApi()
id = 'id_example' # str | ID of the notification publisher plugin instance to which these actions belongs to.

try:
    # List the actions for a notification publisher plugin instance.
    api_response = api_instance.get_actions(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificationPublishersApi->get_actions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the notification publisher plugin instance to which these actions belongs to. | 

### Return type

[**Actions**](Actions.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_notification_publisher**
> NotificationPublisher get_notification_publisher(id)

Get a specific notification publisher plugin instance.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NotificationPublishersApi()
id = 'id_example' # str | ID of a notification publisher plugin instance.

try:
    # Get a specific notification publisher plugin instance.
    api_response = api_instance.get_notification_publisher(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificationPublishersApi->get_notification_publisher: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of a notification publisher plugin instance. | 

### Return type

[**NotificationPublisher**](NotificationPublisher.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_notification_publisher_plugin_descriptor**
> NotificationPublisherDescriptor get_notification_publisher_plugin_descriptor(id)

Get the description of a notification publisher plugin descriptor.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NotificationPublishersApi()
id = 'id_example' # str | ID of notification publisher plugin descriptor.

try:
    # Get the description of a notification publisher plugin descriptor.
    api_response = api_instance.get_notification_publisher_plugin_descriptor(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificationPublishersApi->get_notification_publisher_plugin_descriptor: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of notification publisher plugin descriptor. | 

### Return type

[**NotificationPublisherDescriptor**](NotificationPublisherDescriptor.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_notification_publisher_plugin_descriptors**
> NotificationPublisherDescriptors get_notification_publisher_plugin_descriptors()

Get the list of available Notification Publisher Plugin descriptors.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NotificationPublishersApi()

try:
    # Get the list of available Notification Publisher Plugin descriptors.
    api_response = api_instance.get_notification_publisher_plugin_descriptors()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificationPublishersApi->get_notification_publisher_plugin_descriptors: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NotificationPublisherDescriptors**](NotificationPublisherDescriptors.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_notification_publishers**
> NotificationPublishers get_notification_publishers()

Get a list of notification publisher plugin instances.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NotificationPublishersApi()

try:
    # Get a list of notification publisher plugin instances.
    api_response = api_instance.get_notification_publishers()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificationPublishersApi->get_notification_publishers: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NotificationPublishers**](NotificationPublishers.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_settings**
> NotificationPublishersSettings get_settings()

Get general notification publisher settings.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NotificationPublishersApi()

try:
    # Get general notification publisher settings.
    api_response = api_instance.get_settings()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificationPublishersApi->get_settings: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NotificationPublishersSettings**](NotificationPublishersSettings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invoke_action_with_options**
> ActionResult invoke_action_with_options(id, action_id, body=body)

Invokes an action for notification publisher plugin instance.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NotificationPublishersApi()
id = 'id_example' # str | ID of the notification publisher plugin instance to which these actions belongs to.
action_id = 'action_id_example' # str | ID of the action to get.
body = swagger_client.ActionOptions() # ActionOptions | Action options for action invoked. (optional)

try:
    # Invokes an action for notification publisher plugin instance.
    api_response = api_instance.invoke_action_with_options(id, action_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificationPublishersApi->invoke_action_with_options: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the notification publisher plugin instance to which these actions belongs to. | 
 **action_id** | **str**| ID of the action to get. | 
 **body** | [**ActionOptions**](ActionOptions.md)| Action options for action invoked. | [optional] 

### Return type

[**ActionResult**](ActionResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_notification_publisher**
> NotificationPublisher update_notification_publisher(id, body)

Update a notification publisher plugin instance.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NotificationPublishersApi()
id = 'id_example' # str | ID of a notification publisher plugin instance.
body = swagger_client.NotificationPublisher() # NotificationPublisher | Configuration for a notification publisher plugin instance.

try:
    # Update a notification publisher plugin instance.
    api_response = api_instance.update_notification_publisher(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificationPublishersApi->update_notification_publisher: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of a notification publisher plugin instance. | 
 **body** | [**NotificationPublisher**](NotificationPublisher.md)| Configuration for a notification publisher plugin instance. | 

### Return type

[**NotificationPublisher**](NotificationPublisher.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_settings**
> NotificationPublishersSettings update_settings(body)

Update general notification publisher settings.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NotificationPublishersApi()
body = swagger_client.NotificationPublishersSettings() # NotificationPublishersSettings | 

try:
    # Update general notification publisher settings.
    api_response = api_instance.update_settings(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificationPublishersApi->update_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NotificationPublishersSettings**](NotificationPublishersSettings.md)|  | 

### Return type

[**NotificationPublishersSettings**](NotificationPublishersSettings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

