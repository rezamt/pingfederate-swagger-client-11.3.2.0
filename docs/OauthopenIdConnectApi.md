# swagger_client.OauthopenIdConnectApi

All URIs are relative to *https://localhost:9999/pf-admin-api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_policy**](OauthopenIdConnectApi.md#create_policy) | **POST** /oauth/openIdConnect/policies | Create a new OpenID Connect Policy.
[**delete_policy**](OauthopenIdConnectApi.md#delete_policy) | **DELETE** /oauth/openIdConnect/policies/{id} | Delete an OpenID Connect Policy.
[**get_policies**](OauthopenIdConnectApi.md#get_policies) | **GET** /oauth/openIdConnect/policies | Get list of OpenID Connect Policies.
[**get_policy**](OauthopenIdConnectApi.md#get_policy) | **GET** /oauth/openIdConnect/policies/{id} | Find OpenID Connect Policy by ID.
[**get_settings**](OauthopenIdConnectApi.md#get_settings) | **GET** /oauth/openIdConnect/settings | Get the OpenID Connect Settings.
[**update_policy**](OauthopenIdConnectApi.md#update_policy) | **PUT** /oauth/openIdConnect/policies/{id} | Update an OpenID Connect Policy.
[**update_settings**](OauthopenIdConnectApi.md#update_settings) | **PUT** /oauth/openIdConnect/settings | Set the OpenID Connect Settings.


# **create_policy**
> OpenIdConnectPolicy create_policy(body, x_bypass_external_validation=x_bypass_external_validation)

Create a new OpenID Connect Policy.

Create a new OpenID Connect Policy. If the OpenID Connect policy is not properly configured, a 422 status code is returned along with a list of validation errors that must be corrected.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OauthopenIdConnectApi()
body = swagger_client.OpenIdConnectPolicy() # OpenIdConnectPolicy | Configuration for new policy.
x_bypass_external_validation = false # bool | External validation will be bypassed when set to true. Default to false. (optional) (default to false)

try:
    # Create a new OpenID Connect Policy.
    api_response = api_instance.create_policy(body, x_bypass_external_validation=x_bypass_external_validation)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OauthopenIdConnectApi->create_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OpenIdConnectPolicy**](OpenIdConnectPolicy.md)| Configuration for new policy. | 
 **x_bypass_external_validation** | **bool**| External validation will be bypassed when set to true. Default to false. | [optional] [default to false]

### Return type

[**OpenIdConnectPolicy**](OpenIdConnectPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_policy**
> delete_policy(id)

Delete an OpenID Connect Policy.

Delete an OpenID Connect Policy with the specified ID. A 404 status code is returned for nonexistent IDs. Note: If the request succeeds, the response body is empty. If the request fails, an ApiResult is returned with details of the error.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OauthopenIdConnectApi()
id = 'id_example' # str | ID of OpenID Connect Policy to delete.

try:
    # Delete an OpenID Connect Policy.
    api_instance.delete_policy(id)
except ApiException as e:
    print("Exception when calling OauthopenIdConnectApi->delete_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of OpenID Connect Policy to delete. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_policies**
> OpenIdConnectPolicies get_policies()

Get list of OpenID Connect Policies.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OauthopenIdConnectApi()

try:
    # Get list of OpenID Connect Policies.
    api_response = api_instance.get_policies()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OauthopenIdConnectApi->get_policies: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**OpenIdConnectPolicies**](OpenIdConnectPolicies.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_policy**
> OpenIdConnectPolicy get_policy(id)

Find OpenID Connect Policy by ID.

Get an OpenID Connect Policy with the specified ID. A 404 status code is returned for nonexistent IDs.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OauthopenIdConnectApi()
id = 'id_example' # str | ID of the OpenID Connect Policy to fetch.

try:
    # Find OpenID Connect Policy by ID.
    api_response = api_instance.get_policy(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OauthopenIdConnectApi->get_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the OpenID Connect Policy to fetch. | 

### Return type

[**OpenIdConnectPolicy**](OpenIdConnectPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_settings**
> OpenIdConnectSettings get_settings()

Get the OpenID Connect Settings.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OauthopenIdConnectApi()

try:
    # Get the OpenID Connect Settings.
    api_response = api_instance.get_settings()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OauthopenIdConnectApi->get_settings: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**OpenIdConnectSettings**](OpenIdConnectSettings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_policy**
> OpenIdConnectPolicy update_policy(id, body, x_bypass_external_validation=x_bypass_external_validation)

Update an OpenID Connect Policy.

Update an OpenID Connect Policy with the matching ID. If the policy is not properly configured, a 422 status code is returned along with a list of validation errors that must be corrected. Note: A 404 status code is returned for nonexistent IDs.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OauthopenIdConnectApi()
id = 'id_example' # str | ID of the OpenID Connect Policy to update.
body = swagger_client.OpenIdConnectPolicy() # OpenIdConnectPolicy | Configuration for updated policy.
x_bypass_external_validation = false # bool | External validation will be bypassed when set to true. Default to false. (optional) (default to false)

try:
    # Update an OpenID Connect Policy.
    api_response = api_instance.update_policy(id, body, x_bypass_external_validation=x_bypass_external_validation)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OauthopenIdConnectApi->update_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the OpenID Connect Policy to update. | 
 **body** | [**OpenIdConnectPolicy**](OpenIdConnectPolicy.md)| Configuration for updated policy. | 
 **x_bypass_external_validation** | **bool**| External validation will be bypassed when set to true. Default to false. | [optional] [default to false]

### Return type

[**OpenIdConnectPolicy**](OpenIdConnectPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_settings**
> OpenIdConnectSettings update_settings(body)

Set the OpenID Connect Settings.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OauthopenIdConnectApi()
body = swagger_client.OpenIdConnectSettings() # OpenIdConnectSettings | OpenID Connect Settings.

try:
    # Set the OpenID Connect Settings.
    api_response = api_instance.update_settings(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OauthopenIdConnectApi->update_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OpenIdConnectSettings**](OpenIdConnectSettings.md)| OpenID Connect Settings. | 

### Return type

[**OpenIdConnectSettings**](OpenIdConnectSettings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

