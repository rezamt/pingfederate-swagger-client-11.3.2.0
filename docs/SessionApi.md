# swagger_client.SessionApi

All URIs are relative to *https://localhost:9999/pf-admin-api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_source_policy**](SessionApi.md#create_source_policy) | **POST** /session/authenticationSessionPolicies | Create a new session policy.
[**delete_source_policy**](SessionApi.md#delete_source_policy) | **DELETE** /session/authenticationSessionPolicies/{id} | Delete a session policy.
[**get_application_policy**](SessionApi.md#get_application_policy) | **GET** /session/applicationSessionPolicy | Get the application session policy.
[**get_global_policy**](SessionApi.md#get_global_policy) | **GET** /session/authenticationSessionPolicies/global | Get the global authentication session policy.
[**get_session_settings**](SessionApi.md#get_session_settings) | **GET** /session/settings | Get general session management settings.
[**get_source_policies**](SessionApi.md#get_source_policies) | **GET** /session/authenticationSessionPolicies | Get list of session policies.
[**get_source_policy**](SessionApi.md#get_source_policy) | **GET** /session/authenticationSessionPolicies/{id} | Find session policy by ID.
[**update_application_policy**](SessionApi.md#update_application_policy) | **PUT** /session/applicationSessionPolicy | Update the application session policy.
[**update_global_policy**](SessionApi.md#update_global_policy) | **PUT** /session/authenticationSessionPolicies/global | Update the global authentication session policy.
[**update_session_settings**](SessionApi.md#update_session_settings) | **PUT** /session/settings | Update general session management settings.
[**update_source_policy**](SessionApi.md#update_source_policy) | **PUT** /session/authenticationSessionPolicies/{id} | Update a session policy.


# **create_source_policy**
> AuthenticationSessionPolicy create_source_policy(body)

Create a new session policy.

Create a new session policy for a specified authentication source. If the session policy is not properly configured, a 422 status code is returned along with a list of validation errors that must be corrected.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SessionApi()
body = swagger_client.AuthenticationSessionPolicy() # AuthenticationSessionPolicy | Configuration for new policy.

try:
    # Create a new session policy.
    api_response = api_instance.create_source_policy(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SessionApi->create_source_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AuthenticationSessionPolicy**](AuthenticationSessionPolicy.md)| Configuration for new policy. | 

### Return type

[**AuthenticationSessionPolicy**](AuthenticationSessionPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_source_policy**
> delete_source_policy(id)

Delete a session policy.

Delete the session policy with the specified ID. A 404 status code is returned for nonexistent IDs. If the request succeeds, the response body is empty. If the request fails, an ApiResult is returned with details of the error.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SessionApi()
id = 'id_example' # str | ID of session policy to delete.

try:
    # Delete a session policy.
    api_instance.delete_source_policy(id)
except ApiException as e:
    print("Exception when calling SessionApi->delete_source_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of session policy to delete. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_application_policy**
> ApplicationSessionPolicy get_application_policy()

Get the application session policy.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SessionApi()

try:
    # Get the application session policy.
    api_response = api_instance.get_application_policy()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SessionApi->get_application_policy: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ApplicationSessionPolicy**](ApplicationSessionPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_global_policy**
> GlobalAuthenticationSessionPolicy get_global_policy()

Get the global authentication session policy.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SessionApi()

try:
    # Get the global authentication session policy.
    api_response = api_instance.get_global_policy()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SessionApi->get_global_policy: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GlobalAuthenticationSessionPolicy**](GlobalAuthenticationSessionPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_session_settings**
> SessionSettings get_session_settings()

Get general session management settings.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SessionApi()

try:
    # Get general session management settings.
    api_response = api_instance.get_session_settings()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SessionApi->get_session_settings: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SessionSettings**](SessionSettings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_source_policies**
> AuthenticationSessionPolicies get_source_policies()

Get list of session policies.

Get a list of all session policies that are associated with specific authentication sources.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SessionApi()

try:
    # Get list of session policies.
    api_response = api_instance.get_source_policies()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SessionApi->get_source_policies: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AuthenticationSessionPolicies**](AuthenticationSessionPolicies.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_source_policy**
> AuthenticationSessionPolicy get_source_policy(id)

Find session policy by ID.

Get the session policy with the specified ID. A 404 status code is returned for nonexistent IDs.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SessionApi()
id = 'id_example' # str | ID of the session policy to fetch.

try:
    # Find session policy by ID.
    api_response = api_instance.get_source_policy(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SessionApi->get_source_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the session policy to fetch. | 

### Return type

[**AuthenticationSessionPolicy**](AuthenticationSessionPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_application_policy**
> ApplicationSessionPolicy update_application_policy(body)

Update the application session policy.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SessionApi()
body = swagger_client.ApplicationSessionPolicy() # ApplicationSessionPolicy | Application session policy.

try:
    # Update the application session policy.
    api_response = api_instance.update_application_policy(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SessionApi->update_application_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ApplicationSessionPolicy**](ApplicationSessionPolicy.md)| Application session policy. | 

### Return type

[**ApplicationSessionPolicy**](ApplicationSessionPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_global_policy**
> GlobalAuthenticationSessionPolicy update_global_policy(body)

Update the global authentication session policy.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SessionApi()
body = swagger_client.GlobalAuthenticationSessionPolicy() # GlobalAuthenticationSessionPolicy | Global authentication session policy.

try:
    # Update the global authentication session policy.
    api_response = api_instance.update_global_policy(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SessionApi->update_global_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GlobalAuthenticationSessionPolicy**](GlobalAuthenticationSessionPolicy.md)| Global authentication session policy. | 

### Return type

[**GlobalAuthenticationSessionPolicy**](GlobalAuthenticationSessionPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_session_settings**
> SessionSettings update_session_settings(body)

Update general session management settings.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SessionApi()
body = swagger_client.SessionSettings() # SessionSettings | Session settings.

try:
    # Update general session management settings.
    api_response = api_instance.update_session_settings(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SessionApi->update_session_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SessionSettings**](SessionSettings.md)| Session settings. | 

### Return type

[**SessionSettings**](SessionSettings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_source_policy**
> AuthenticationSessionPolicy update_source_policy(id, body)

Update a session policy.

Update the session policy with the matching ID. If the policy is not properly configured, a 422 status code is returned along with a list of validation errors that must be corrected.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SessionApi()
id = 'id_example' # str | ID of the session policy to update.
body = swagger_client.AuthenticationSessionPolicy() # AuthenticationSessionPolicy | Configuration for updated policy.

try:
    # Update a session policy.
    api_response = api_instance.update_source_policy(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SessionApi->update_source_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the session policy to update. | 
 **body** | [**AuthenticationSessionPolicy**](AuthenticationSessionPolicy.md)| Configuration for updated policy. | 

### Return type

[**AuthenticationSessionPolicy**](AuthenticationSessionPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

