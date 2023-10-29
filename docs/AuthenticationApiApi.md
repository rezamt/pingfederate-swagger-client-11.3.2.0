# swagger_client.AuthenticationApiApi

All URIs are relative to *https://localhost:9999/pf-admin-api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_application**](AuthenticationApiApi.md#create_application) | **POST** /authenticationApi/applications | Create a new Authentication API Application.
[**delete_application**](AuthenticationApiApi.md#delete_application) | **DELETE** /authenticationApi/applications/{id} | Delete an Authentication API Application.
[**get_application**](AuthenticationApiApi.md#get_application) | **GET** /authenticationApi/applications/{id} | Find Authentication API Application by ID.
[**get_authentication_api_applications**](AuthenticationApiApi.md#get_authentication_api_applications) | **GET** /authenticationApi/applications | Get the collection of Authentication API Applications.
[**get_authentication_api_settings**](AuthenticationApiApi.md#get_authentication_api_settings) | **GET** /authenticationApi/settings | Get the Authentication API settings.
[**update_application**](AuthenticationApiApi.md#update_application) | **PUT** /authenticationApi/applications/{id} | Update an Authentication API Application.
[**update_authentication_api_settings**](AuthenticationApiApi.md#update_authentication_api_settings) | **PUT** /authenticationApi/settings | Set the Authentication API settings.


# **create_application**
> AuthnApiApplication create_application(body)

Create a new Authentication API Application.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AuthenticationApiApi()
body = swagger_client.AuthnApiApplication() # AuthnApiApplication | Configuration for new Authentication API Application.

try:
    # Create a new Authentication API Application.
    api_response = api_instance.create_application(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationApiApi->create_application: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AuthnApiApplication**](AuthnApiApplication.md)| Configuration for new Authentication API Application. | 

### Return type

[**AuthnApiApplication**](AuthnApiApplication.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_application**
> delete_application(id)

Delete an Authentication API Application.

Delete an Authentication API Application with the specified ID. A 404 status code is returned for nonexistent IDs. Note: If the request succeeds, the response body is empty. If the request fails, an ApiResult is returned with details of the error.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AuthenticationApiApi()
id = 'id_example' # str | ID of Authentication API Application to delete.

try:
    # Delete an Authentication API Application.
    api_instance.delete_application(id)
except ApiException as e:
    print("Exception when calling AuthenticationApiApi->delete_application: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of Authentication API Application to delete. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_application**
> AuthnApiApplication get_application(id)

Find Authentication API Application by ID.

Get an Authentication API Application with the specified ID. A 404 status code is returned for nonexistent IDs.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AuthenticationApiApi()
id = 'id_example' # str | ID of the Authentication API Application to fetch.

try:
    # Find Authentication API Application by ID.
    api_response = api_instance.get_application(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationApiApi->get_application: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the Authentication API Application to fetch. | 

### Return type

[**AuthnApiApplication**](AuthnApiApplication.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_authentication_api_applications**
> AuthnApiApplications get_authentication_api_applications()

Get the collection of Authentication API Applications.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AuthenticationApiApi()

try:
    # Get the collection of Authentication API Applications.
    api_response = api_instance.get_authentication_api_applications()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationApiApi->get_authentication_api_applications: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AuthnApiApplications**](AuthnApiApplications.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_authentication_api_settings**
> AuthnApiSettings get_authentication_api_settings()

Get the Authentication API settings.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AuthenticationApiApi()

try:
    # Get the Authentication API settings.
    api_response = api_instance.get_authentication_api_settings()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationApiApi->get_authentication_api_settings: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AuthnApiSettings**](AuthnApiSettings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_application**
> AuthnApiApplication update_application(id, body)

Update an Authentication API Application.

Update an Authentication API Application with the matching ID. If the application is not properly configured, a 422 status code is returned along with a list of validation errors that must be corrected. Note: A 404 status code is returned for nonexistent IDs.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AuthenticationApiApi()
id = 'id_example' # str | ID of the Authentication API Application to update.
body = swagger_client.AuthnApiApplication() # AuthnApiApplication | Configuration for updated application.

try:
    # Update an Authentication API Application.
    api_response = api_instance.update_application(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationApiApi->update_application: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the Authentication API Application to update. | 
 **body** | [**AuthnApiApplication**](AuthnApiApplication.md)| Configuration for updated application. | 

### Return type

[**AuthnApiApplication**](AuthnApiApplication.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_authentication_api_settings**
> AuthnApiSettings update_authentication_api_settings(body)

Set the Authentication API settings.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AuthenticationApiApi()
body = swagger_client.AuthnApiSettings() # AuthnApiSettings | Authentication API Settings

try:
    # Set the Authentication API settings.
    api_response = api_instance.update_authentication_api_settings(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationApiApi->update_authentication_api_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AuthnApiSettings**](AuthnApiSettings.md)| Authentication API Settings | 

### Return type

[**AuthnApiSettings**](AuthnApiSettings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

