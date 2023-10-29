# swagger_client.AuthenticationPoliciesApi

All URIs are relative to *https://localhost:9999/pf-admin-api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_fragment**](AuthenticationPoliciesApi.md#create_fragment) | **POST** /authenticationPolicies/fragments | Create an authentication policy fragment.
[**create_policy**](AuthenticationPoliciesApi.md#create_policy) | **POST** /authenticationPolicies/policy | Create a new authentication policy.
[**delete_fragment**](AuthenticationPoliciesApi.md#delete_fragment) | **DELETE** /authenticationPolicies/fragments/{id} | Delete an authentication policy fragment.
[**delete_policy**](AuthenticationPoliciesApi.md#delete_policy) | **DELETE** /authenticationPolicies/policy/{id} | Delete an authentication policy.
[**get_default_authentication_policy**](AuthenticationPoliciesApi.md#get_default_authentication_policy) | **GET** /authenticationPolicies/default | Get the default configured authentication policy.
[**get_fragment**](AuthenticationPoliciesApi.md#get_fragment) | **GET** /authenticationPolicies/fragments/{id} | Get an authentication policy fragment by ID.
[**get_fragments**](AuthenticationPoliciesApi.md#get_fragments) | **GET** /authenticationPolicies/fragments | Get all of the authentication policies fragments.
[**get_policy**](AuthenticationPoliciesApi.md#get_policy) | **GET** /authenticationPolicies/policy/{id} | Get an authentication policy by ID.
[**get_settings**](AuthenticationPoliciesApi.md#get_settings) | **GET** /authenticationPolicies/settings | Get the authentication policies settings.
[**move_policy**](AuthenticationPoliciesApi.md#move_policy) | **POST** /authenticationPolicies/policy/{id}/move | Move an authentication policy to a location within the policy tree.
[**update_default_authentication_policy**](AuthenticationPoliciesApi.md#update_default_authentication_policy) | **PUT** /authenticationPolicies/default | Set the default authentication policy.
[**update_fragment**](AuthenticationPoliciesApi.md#update_fragment) | **PUT** /authenticationPolicies/fragments/{id} | Update an authentication policy fragment.
[**update_policy**](AuthenticationPoliciesApi.md#update_policy) | **PUT** /authenticationPolicies/policy/{id} | Update an authentication policy.
[**update_settings**](AuthenticationPoliciesApi.md#update_settings) | **PUT** /authenticationPolicies/settings | Set the authentication policies settings.


# **create_fragment**
> AuthenticationPolicyFragment create_fragment(body, x_bypass_external_validation=x_bypass_external_validation)

Create an authentication policy fragment.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AuthenticationPoliciesApi()
body = swagger_client.AuthenticationPolicyFragment() # AuthenticationPolicyFragment | Configuration of the authentication policy fragment.
x_bypass_external_validation = false # bool | External validation will be bypassed when set to true. Default to false. (optional) (default to false)

try:
    # Create an authentication policy fragment.
    api_response = api_instance.create_fragment(body, x_bypass_external_validation=x_bypass_external_validation)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationPoliciesApi->create_fragment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AuthenticationPolicyFragment**](AuthenticationPolicyFragment.md)| Configuration of the authentication policy fragment. | 
 **x_bypass_external_validation** | **bool**| External validation will be bypassed when set to true. Default to false. | [optional] [default to false]

### Return type

[**AuthenticationPolicyFragment**](AuthenticationPolicyFragment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_policy**
> AuthenticationPolicyTree create_policy(body, x_bypass_external_validation=x_bypass_external_validation)

Create a new authentication policy.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AuthenticationPoliciesApi()
body = swagger_client.AuthenticationPolicyTree() # AuthenticationPolicyTree | Configuration of the authentication policy.
x_bypass_external_validation = false # bool | External validation will be bypassed when set to true. Default to false. (optional) (default to false)

try:
    # Create a new authentication policy.
    api_response = api_instance.create_policy(body, x_bypass_external_validation=x_bypass_external_validation)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationPoliciesApi->create_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AuthenticationPolicyTree**](AuthenticationPolicyTree.md)| Configuration of the authentication policy. | 
 **x_bypass_external_validation** | **bool**| External validation will be bypassed when set to true. Default to false. | [optional] [default to false]

### Return type

[**AuthenticationPolicyTree**](AuthenticationPolicyTree.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_fragment**
> delete_fragment(id)

Delete an authentication policy fragment.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AuthenticationPoliciesApi()
id = 'id_example' # str | ID of the policy fragment to delete.

try:
    # Delete an authentication policy fragment.
    api_instance.delete_fragment(id)
except ApiException as e:
    print("Exception when calling AuthenticationPoliciesApi->delete_fragment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the policy fragment to delete. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_policy**
> delete_policy(id)

Delete an authentication policy.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AuthenticationPoliciesApi()
id = 'id_example' # str | Authentication policy Id.

try:
    # Delete an authentication policy.
    api_instance.delete_policy(id)
except ApiException as e:
    print("Exception when calling AuthenticationPoliciesApi->delete_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Authentication policy Id. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_default_authentication_policy**
> AuthenticationPolicy get_default_authentication_policy()

Get the default configured authentication policy.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AuthenticationPoliciesApi()

try:
    # Get the default configured authentication policy.
    api_response = api_instance.get_default_authentication_policy()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationPoliciesApi->get_default_authentication_policy: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AuthenticationPolicy**](AuthenticationPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_fragment**
> AuthenticationPolicyFragment get_fragment(id)

Get an authentication policy fragment by ID.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AuthenticationPoliciesApi()
id = 'id_example' # str | ID of the policy fragment to fetch.

try:
    # Get an authentication policy fragment by ID.
    api_response = api_instance.get_fragment(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationPoliciesApi->get_fragment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the policy fragment to fetch. | 

### Return type

[**AuthenticationPolicyFragment**](AuthenticationPolicyFragment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_fragments**
> AuthenticationPolicyFragments get_fragments(page=page, number_per_page=number_per_page, filter=filter)

Get all of the authentication policies fragments.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AuthenticationPoliciesApi()
page = 56 # int | Page number to retrieve. (optional)
number_per_page = 56 # int | Number of fragments per page. (optional)
filter = 'filter_example' # str | Filter criteria limits the fragments that are returned to only those that match it. The filter criteria is compared to the fragment instance name and ID fields. The comparison is a case-insensitive partial match. No additional pattern based matching is supported. (optional)

try:
    # Get all of the authentication policies fragments.
    api_response = api_instance.get_fragments(page=page, number_per_page=number_per_page, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationPoliciesApi->get_fragments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number to retrieve. | [optional] 
 **number_per_page** | **int**| Number of fragments per page. | [optional] 
 **filter** | **str**| Filter criteria limits the fragments that are returned to only those that match it. The filter criteria is compared to the fragment instance name and ID fields. The comparison is a case-insensitive partial match. No additional pattern based matching is supported. | [optional] 

### Return type

[**AuthenticationPolicyFragments**](AuthenticationPolicyFragments.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_policy**
> AuthenticationPolicyTree get_policy(id)

Get an authentication policy by ID.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AuthenticationPoliciesApi()
id = 'id_example' # str | Authentication policy Id.

try:
    # Get an authentication policy by ID.
    api_response = api_instance.get_policy(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationPoliciesApi->get_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Authentication policy Id. | 

### Return type

[**AuthenticationPolicyTree**](AuthenticationPolicyTree.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_settings**
> AuthenticationPoliciesSettings get_settings()

Get the authentication policies settings.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AuthenticationPoliciesApi()

try:
    # Get the authentication policies settings.
    api_response = api_instance.get_settings()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationPoliciesApi->get_settings: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AuthenticationPoliciesSettings**](AuthenticationPoliciesSettings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **move_policy**
> move_policy(id, body)

Move an authentication policy to a location within the policy tree.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AuthenticationPoliciesApi()
id = 'id_example' # str | Authentication policy Id.
body = swagger_client.MoveItemRequest() # MoveItemRequest | Metadata about where to move the policy

try:
    # Move an authentication policy to a location within the policy tree.
    api_instance.move_policy(id, body)
except ApiException as e:
    print("Exception when calling AuthenticationPoliciesApi->move_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Authentication policy Id. | 
 **body** | [**MoveItemRequest**](MoveItemRequest.md)| Metadata about where to move the policy | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_default_authentication_policy**
> AuthenticationPolicy update_default_authentication_policy(body, x_bypass_external_validation=x_bypass_external_validation)

Set the default authentication policy.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AuthenticationPoliciesApi()
body = swagger_client.AuthenticationPolicy() # AuthenticationPolicy | Default authentication policy.
x_bypass_external_validation = false # bool | External validation will be bypassed when set to true. Default to false. (optional) (default to false)

try:
    # Set the default authentication policy.
    api_response = api_instance.update_default_authentication_policy(body, x_bypass_external_validation=x_bypass_external_validation)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationPoliciesApi->update_default_authentication_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AuthenticationPolicy**](AuthenticationPolicy.md)| Default authentication policy. | 
 **x_bypass_external_validation** | **bool**| External validation will be bypassed when set to true. Default to false. | [optional] [default to false]

### Return type

[**AuthenticationPolicy**](AuthenticationPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_fragment**
> AuthenticationPolicyFragment update_fragment(id, body, x_bypass_external_validation=x_bypass_external_validation)

Update an authentication policy fragment.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AuthenticationPoliciesApi()
id = 'id_example' # str | ID of the policy fragment to  update.
body = swagger_client.AuthenticationPolicyFragment() # AuthenticationPolicyFragment | Configuration of the authentication policy fragment.
x_bypass_external_validation = false # bool | External validation will be bypassed when set to true. Default to false. (optional) (default to false)

try:
    # Update an authentication policy fragment.
    api_response = api_instance.update_fragment(id, body, x_bypass_external_validation=x_bypass_external_validation)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationPoliciesApi->update_fragment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the policy fragment to  update. | 
 **body** | [**AuthenticationPolicyFragment**](AuthenticationPolicyFragment.md)| Configuration of the authentication policy fragment. | 
 **x_bypass_external_validation** | **bool**| External validation will be bypassed when set to true. Default to false. | [optional] [default to false]

### Return type

[**AuthenticationPolicyFragment**](AuthenticationPolicyFragment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_policy**
> AuthenticationPolicyTree update_policy(id, body, x_bypass_external_validation=x_bypass_external_validation)

Update an authentication policy.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AuthenticationPoliciesApi()
id = 'id_example' # str | Authentication policy Id.
body = swagger_client.AuthenticationPolicyTree() # AuthenticationPolicyTree | Configuration of the authentication policy.
x_bypass_external_validation = false # bool | External validation will be bypassed when set to true. Default to false. (optional) (default to false)

try:
    # Update an authentication policy.
    api_response = api_instance.update_policy(id, body, x_bypass_external_validation=x_bypass_external_validation)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationPoliciesApi->update_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Authentication policy Id. | 
 **body** | [**AuthenticationPolicyTree**](AuthenticationPolicyTree.md)| Configuration of the authentication policy. | 
 **x_bypass_external_validation** | **bool**| External validation will be bypassed when set to true. Default to false. | [optional] [default to false]

### Return type

[**AuthenticationPolicyTree**](AuthenticationPolicyTree.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_settings**
> AuthenticationPoliciesSettings update_settings(body)

Set the authentication policies settings.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AuthenticationPoliciesApi()
body = swagger_client.AuthenticationPoliciesSettings() # AuthenticationPoliciesSettings | Authentication policies settings.

try:
    # Set the authentication policies settings.
    api_response = api_instance.update_settings(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationPoliciesApi->update_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AuthenticationPoliciesSettings**](AuthenticationPoliciesSettings.md)| Authentication policies settings. | 

### Return type

[**AuthenticationPoliciesSettings**](AuthenticationPoliciesSettings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

