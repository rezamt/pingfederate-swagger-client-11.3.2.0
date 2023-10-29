# swagger_client.OauthauthServerSettingsApi

All URIs are relative to *https://localhost:9999/pf-admin-api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_common_scope**](OauthauthServerSettingsApi.md#add_common_scope) | **POST** /oauth/authServerSettings/scopes/commonScopes | Add a new common scope.
[**add_common_scope_group**](OauthauthServerSettingsApi.md#add_common_scope_group) | **POST** /oauth/authServerSettings/scopes/commonScopeGroups | Create a new common scope group.
[**add_exclusive_scope**](OauthauthServerSettingsApi.md#add_exclusive_scope) | **POST** /oauth/authServerSettings/scopes/exclusiveScopes | Add a new exclusive scope.
[**add_exclusive_scope_group**](OauthauthServerSettingsApi.md#add_exclusive_scope_group) | **POST** /oauth/authServerSettings/scopes/exclusiveScopeGroups | Create a new exclusive scope group.
[**get_authorization_server_settings**](OauthauthServerSettingsApi.md#get_authorization_server_settings) | **GET** /oauth/authServerSettings | Get the Authorization Server Settings.
[**get_common_scope**](OauthauthServerSettingsApi.md#get_common_scope) | **GET** /oauth/authServerSettings/scopes/commonScopes/{name} | Get an existing common scope.
[**get_common_scope_group**](OauthauthServerSettingsApi.md#get_common_scope_group) | **GET** /oauth/authServerSettings/scopes/commonScopeGroups/{name} | Get an existing common scope group.
[**get_exclusive_scope**](OauthauthServerSettingsApi.md#get_exclusive_scope) | **GET** /oauth/authServerSettings/scopes/exclusiveScopes/{name} | Get an existing exclusive scope.
[**get_exclusive_scope_group**](OauthauthServerSettingsApi.md#get_exclusive_scope_group) | **GET** /oauth/authServerSettings/scopes/exclusiveScopeGroups/{name} | Get an existing exclusive scope group.
[**remove_common_scope**](OauthauthServerSettingsApi.md#remove_common_scope) | **DELETE** /oauth/authServerSettings/scopes/commonScopes/{name} | Remove an existing common scope.
[**remove_common_scope_group**](OauthauthServerSettingsApi.md#remove_common_scope_group) | **DELETE** /oauth/authServerSettings/scopes/commonScopeGroups/{name} | Remove an existing common scope group.
[**remove_exclusive_scope**](OauthauthServerSettingsApi.md#remove_exclusive_scope) | **DELETE** /oauth/authServerSettings/scopes/exclusiveScopes/{name} | Remove an existing exclusive scope.
[**remove_exclusive_scope_group**](OauthauthServerSettingsApi.md#remove_exclusive_scope_group) | **DELETE** /oauth/authServerSettings/scopes/exclusiveScopeGroups/{name} | Remove an existing exclusive scope group.
[**update_authorization_server_settings**](OauthauthServerSettingsApi.md#update_authorization_server_settings) | **PUT** /oauth/authServerSettings | Update the Authorization Server Settings.
[**update_common_scope**](OauthauthServerSettingsApi.md#update_common_scope) | **PUT** /oauth/authServerSettings/scopes/commonScopes/{name} | Update an existing common scope.
[**update_common_scope_group**](OauthauthServerSettingsApi.md#update_common_scope_group) | **PUT** /oauth/authServerSettings/scopes/commonScopeGroups/{name} | Update an existing common scope group.
[**update_exclusive_scope**](OauthauthServerSettingsApi.md#update_exclusive_scope) | **PUT** /oauth/authServerSettings/scopes/exclusiveScopes/{name} | Update an existing exclusive scope.
[**update_exclusive_scope_groups**](OauthauthServerSettingsApi.md#update_exclusive_scope_groups) | **PUT** /oauth/authServerSettings/scopes/exclusiveScopeGroups/{name} | Update an existing exclusive scope group.


# **add_common_scope**
> ScopeEntry add_common_scope(body)

Add a new common scope.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OauthauthServerSettingsApi()
body = swagger_client.ScopeEntry() # ScopeEntry | The scope definition.

try:
    # Add a new common scope.
    api_response = api_instance.add_common_scope(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OauthauthServerSettingsApi->add_common_scope: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ScopeEntry**](ScopeEntry.md)| The scope definition. | 

### Return type

[**ScopeEntry**](ScopeEntry.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_common_scope_group**
> ScopeGroupEntry add_common_scope_group(body)

Create a new common scope group.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OauthauthServerSettingsApi()
body = swagger_client.ScopeGroupEntry() # ScopeGroupEntry | The scope group definition

try:
    # Create a new common scope group.
    api_response = api_instance.add_common_scope_group(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OauthauthServerSettingsApi->add_common_scope_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ScopeGroupEntry**](ScopeGroupEntry.md)| The scope group definition | 

### Return type

[**ScopeGroupEntry**](ScopeGroupEntry.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_exclusive_scope**
> ScopeEntry add_exclusive_scope(body)

Add a new exclusive scope.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OauthauthServerSettingsApi()
body = swagger_client.ScopeEntry() # ScopeEntry | A new exclusive scope

try:
    # Add a new exclusive scope.
    api_response = api_instance.add_exclusive_scope(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OauthauthServerSettingsApi->add_exclusive_scope: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ScopeEntry**](ScopeEntry.md)| A new exclusive scope | 

### Return type

[**ScopeEntry**](ScopeEntry.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_exclusive_scope_group**
> ScopeGroupEntry add_exclusive_scope_group(body)

Create a new exclusive scope group.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OauthauthServerSettingsApi()
body = swagger_client.ScopeGroupEntry() # ScopeGroupEntry | The scope group definition

try:
    # Create a new exclusive scope group.
    api_response = api_instance.add_exclusive_scope_group(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OauthauthServerSettingsApi->add_exclusive_scope_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ScopeGroupEntry**](ScopeGroupEntry.md)| The scope group definition | 

### Return type

[**ScopeGroupEntry**](ScopeGroupEntry.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_authorization_server_settings**
> AuthorizationServerSettings get_authorization_server_settings()

Get the Authorization Server Settings.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OauthauthServerSettingsApi()

try:
    # Get the Authorization Server Settings.
    api_response = api_instance.get_authorization_server_settings()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OauthauthServerSettingsApi->get_authorization_server_settings: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AuthorizationServerSettings**](AuthorizationServerSettings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_common_scope**
> ScopeEntry get_common_scope(name)

Get an existing common scope.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OauthauthServerSettingsApi()
name = 'name_example' # str | Name of the common scope.

try:
    # Get an existing common scope.
    api_response = api_instance.get_common_scope(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OauthauthServerSettingsApi->get_common_scope: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the common scope. | 

### Return type

[**ScopeEntry**](ScopeEntry.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_common_scope_group**
> ScopeGroupEntry get_common_scope_group(name)

Get an existing common scope group.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OauthauthServerSettingsApi()
name = 'name_example' # str | Name of the common scope group.

try:
    # Get an existing common scope group.
    api_response = api_instance.get_common_scope_group(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OauthauthServerSettingsApi->get_common_scope_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the common scope group. | 

### Return type

[**ScopeGroupEntry**](ScopeGroupEntry.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_exclusive_scope**
> ScopeEntry get_exclusive_scope(name)

Get an existing exclusive scope.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OauthauthServerSettingsApi()
name = 'name_example' # str | Name of the exclusive scope.

try:
    # Get an existing exclusive scope.
    api_response = api_instance.get_exclusive_scope(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OauthauthServerSettingsApi->get_exclusive_scope: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the exclusive scope. | 

### Return type

[**ScopeEntry**](ScopeEntry.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_exclusive_scope_group**
> ScopeGroupEntry get_exclusive_scope_group(name)

Get an existing exclusive scope group.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OauthauthServerSettingsApi()
name = 'name_example' # str | Name of the exclusive scope group.

try:
    # Get an existing exclusive scope group.
    api_response = api_instance.get_exclusive_scope_group(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OauthauthServerSettingsApi->get_exclusive_scope_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the exclusive scope group. | 

### Return type

[**ScopeGroupEntry**](ScopeGroupEntry.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_common_scope**
> remove_common_scope(name)

Remove an existing common scope.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OauthauthServerSettingsApi()
name = 'name_example' # str | Name of the common scope.

try:
    # Remove an existing common scope.
    api_instance.remove_common_scope(name)
except ApiException as e:
    print("Exception when calling OauthauthServerSettingsApi->remove_common_scope: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the common scope. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_common_scope_group**
> remove_common_scope_group(name)

Remove an existing common scope group.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OauthauthServerSettingsApi()
name = 'name_example' # str | Name of the common scope group.

try:
    # Remove an existing common scope group.
    api_instance.remove_common_scope_group(name)
except ApiException as e:
    print("Exception when calling OauthauthServerSettingsApi->remove_common_scope_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the common scope group. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_exclusive_scope**
> remove_exclusive_scope(name)

Remove an existing exclusive scope.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OauthauthServerSettingsApi()
name = 'name_example' # str | Name of the exclusive scope.

try:
    # Remove an existing exclusive scope.
    api_instance.remove_exclusive_scope(name)
except ApiException as e:
    print("Exception when calling OauthauthServerSettingsApi->remove_exclusive_scope: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the exclusive scope. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_exclusive_scope_group**
> remove_exclusive_scope_group(name)

Remove an existing exclusive scope group.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OauthauthServerSettingsApi()
name = 'name_example' # str | Name of the exclusive scope group.

try:
    # Remove an existing exclusive scope group.
    api_instance.remove_exclusive_scope_group(name)
except ApiException as e:
    print("Exception when calling OauthauthServerSettingsApi->remove_exclusive_scope_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the exclusive scope group. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_authorization_server_settings**
> AuthorizationServerSettings update_authorization_server_settings(body)

Update the Authorization Server Settings.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OauthauthServerSettingsApi()
body = swagger_client.AuthorizationServerSettings() # AuthorizationServerSettings | Configuration for updated server settings.

try:
    # Update the Authorization Server Settings.
    api_response = api_instance.update_authorization_server_settings(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OauthauthServerSettingsApi->update_authorization_server_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AuthorizationServerSettings**](AuthorizationServerSettings.md)| Configuration for updated server settings. | 

### Return type

[**AuthorizationServerSettings**](AuthorizationServerSettings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_common_scope**
> ScopeEntry update_common_scope(name, body)

Update an existing common scope.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OauthauthServerSettingsApi()
name = 'name_example' # str | Name of the common scope.
body = swagger_client.ScopeEntry() # ScopeEntry | The scope definition

try:
    # Update an existing common scope.
    api_response = api_instance.update_common_scope(name, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OauthauthServerSettingsApi->update_common_scope: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the common scope. | 
 **body** | [**ScopeEntry**](ScopeEntry.md)| The scope definition | 

### Return type

[**ScopeEntry**](ScopeEntry.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_common_scope_group**
> ScopeGroupEntry update_common_scope_group(name, body)

Update an existing common scope group.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OauthauthServerSettingsApi()
name = 'name_example' # str | Name of the common scope group.
body = swagger_client.ScopeGroupEntry() # ScopeGroupEntry | The scope group definition.

try:
    # Update an existing common scope group.
    api_response = api_instance.update_common_scope_group(name, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OauthauthServerSettingsApi->update_common_scope_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the common scope group. | 
 **body** | [**ScopeGroupEntry**](ScopeGroupEntry.md)| The scope group definition. | 

### Return type

[**ScopeGroupEntry**](ScopeGroupEntry.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_exclusive_scope**
> ScopeEntry update_exclusive_scope(name, body)

Update an existing exclusive scope.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OauthauthServerSettingsApi()
name = 'name_example' # str | Name of the exclusive scope.
body = swagger_client.ScopeEntry() # ScopeEntry | The scope definition.

try:
    # Update an existing exclusive scope.
    api_response = api_instance.update_exclusive_scope(name, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OauthauthServerSettingsApi->update_exclusive_scope: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the exclusive scope. | 
 **body** | [**ScopeEntry**](ScopeEntry.md)| The scope definition. | 

### Return type

[**ScopeEntry**](ScopeEntry.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_exclusive_scope_groups**
> ScopeGroupEntry update_exclusive_scope_groups(name, body)

Update an existing exclusive scope group.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OauthauthServerSettingsApi()
name = 'name_example' # str | Name of the exclusive scope group.
body = swagger_client.ScopeGroupEntry() # ScopeGroupEntry | The scope group definition

try:
    # Update an existing exclusive scope group.
    api_response = api_instance.update_exclusive_scope_groups(name, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OauthauthServerSettingsApi->update_exclusive_scope_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the exclusive scope group. | 
 **body** | [**ScopeGroupEntry**](ScopeGroupEntry.md)| The scope group definition | 

### Return type

[**ScopeGroupEntry**](ScopeGroupEntry.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

