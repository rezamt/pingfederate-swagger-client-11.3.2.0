# swagger_client.OauthaccessTokenManagersApi

All URIs are relative to *https://localhost:9999/pf-admin-api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_token_manager**](OauthaccessTokenManagersApi.md#create_token_manager) | **POST** /oauth/accessTokenManagers | Create a token management plugin instance.
[**delete_token_manager**](OauthaccessTokenManagersApi.md#delete_token_manager) | **DELETE** /oauth/accessTokenManagers/{id} | Delete a token management plugin instance.
[**get_settings**](OauthaccessTokenManagersApi.md#get_settings) | **GET** /oauth/accessTokenManagers/settings | Get general access token management settings.
[**get_token_manager**](OauthaccessTokenManagersApi.md#get_token_manager) | **GET** /oauth/accessTokenManagers/{id} | Get a specific token management plugin instance.
[**get_token_manager_descriptor**](OauthaccessTokenManagersApi.md#get_token_manager_descriptor) | **GET** /oauth/accessTokenManagers/descriptors/{id} | Get the description of a token management plugin descriptor.
[**get_token_manager_descriptors**](OauthaccessTokenManagersApi.md#get_token_manager_descriptors) | **GET** /oauth/accessTokenManagers/descriptors | Get the list of available token management plugin descriptors.
[**get_token_managers**](OauthaccessTokenManagersApi.md#get_token_managers) | **GET** /oauth/accessTokenManagers | Get a list of all token management plugin instances.
[**update_settings**](OauthaccessTokenManagersApi.md#update_settings) | **PUT** /oauth/accessTokenManagers/settings | Update general access token management settings.
[**update_token_manager**](OauthaccessTokenManagersApi.md#update_token_manager) | **PUT** /oauth/accessTokenManagers/{id} | Update a token management plugin instance.


# **create_token_manager**
> AccessTokenManager create_token_manager(body)

Create a token management plugin instance.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OauthaccessTokenManagersApi()
body = swagger_client.AccessTokenManager() # AccessTokenManager | Configuration for plugin instance.

try:
    # Create a token management plugin instance.
    api_response = api_instance.create_token_manager(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OauthaccessTokenManagersApi->create_token_manager: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AccessTokenManager**](AccessTokenManager.md)| Configuration for plugin instance. | 

### Return type

[**AccessTokenManager**](AccessTokenManager.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_token_manager**
> delete_token_manager(id)

Delete a token management plugin instance.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OauthaccessTokenManagersApi()
id = 'id_example' # str | ID of token management plugin instance.

try:
    # Delete a token management plugin instance.
    api_instance.delete_token_manager(id)
except ApiException as e:
    print("Exception when calling OauthaccessTokenManagersApi->delete_token_manager: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of token management plugin instance. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_settings**
> AccessTokenManagementSettings get_settings()

Get general access token management settings.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OauthaccessTokenManagersApi()

try:
    # Get general access token management settings.
    api_response = api_instance.get_settings()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OauthaccessTokenManagersApi->get_settings: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AccessTokenManagementSettings**](AccessTokenManagementSettings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_token_manager**
> AccessTokenManager get_token_manager(id)

Get a specific token management plugin instance.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OauthaccessTokenManagersApi()
id = 'id_example' # str | ID of token management plugin instance.

try:
    # Get a specific token management plugin instance.
    api_response = api_instance.get_token_manager(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OauthaccessTokenManagersApi->get_token_manager: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of token management plugin instance. | 

### Return type

[**AccessTokenManager**](AccessTokenManager.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_token_manager_descriptor**
> AccessTokenManagerDescriptor get_token_manager_descriptor(id)

Get the description of a token management plugin descriptor.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OauthaccessTokenManagersApi()
id = 'id_example' # str | ID of token management plugin descriptor.

try:
    # Get the description of a token management plugin descriptor.
    api_response = api_instance.get_token_manager_descriptor(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OauthaccessTokenManagersApi->get_token_manager_descriptor: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of token management plugin descriptor. | 

### Return type

[**AccessTokenManagerDescriptor**](AccessTokenManagerDescriptor.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_token_manager_descriptors**
> AccessTokenManagerDescriptors get_token_manager_descriptors()

Get the list of available token management plugin descriptors.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OauthaccessTokenManagersApi()

try:
    # Get the list of available token management plugin descriptors.
    api_response = api_instance.get_token_manager_descriptors()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OauthaccessTokenManagersApi->get_token_manager_descriptors: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AccessTokenManagerDescriptors**](AccessTokenManagerDescriptors.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_token_managers**
> AccessTokenManagers get_token_managers()

Get a list of all token management plugin instances.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OauthaccessTokenManagersApi()

try:
    # Get a list of all token management plugin instances.
    api_response = api_instance.get_token_managers()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OauthaccessTokenManagersApi->get_token_managers: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AccessTokenManagers**](AccessTokenManagers.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_settings**
> AccessTokenManagementSettings update_settings(body)

Update general access token management settings.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OauthaccessTokenManagersApi()
body = swagger_client.AccessTokenManagementSettings() # AccessTokenManagementSettings | Access token management settings.

try:
    # Update general access token management settings.
    api_response = api_instance.update_settings(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OauthaccessTokenManagersApi->update_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AccessTokenManagementSettings**](AccessTokenManagementSettings.md)| Access token management settings. | 

### Return type

[**AccessTokenManagementSettings**](AccessTokenManagementSettings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_token_manager**
> AccessTokenManager update_token_manager(id, body)

Update a token management plugin instance.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OauthaccessTokenManagersApi()
id = 'id_example' # str | ID of token management plugin instance.
body = swagger_client.AccessTokenManager() # AccessTokenManager | Configuration for token management plugin instance.

try:
    # Update a token management plugin instance.
    api_response = api_instance.update_token_manager(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OauthaccessTokenManagersApi->update_token_manager: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of token management plugin instance. | 
 **body** | [**AccessTokenManager**](AccessTokenManager.md)| Configuration for token management plugin instance. | 

### Return type

[**AccessTokenManager**](AccessTokenManager.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

