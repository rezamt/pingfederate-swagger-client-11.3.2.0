# swagger_client.OauthcibaServerPolicyApi

All URIs are relative to *https://localhost:9999/pf-admin-api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_policy**](OauthcibaServerPolicyApi.md#create_policy) | **POST** /oauth/cibaServerPolicy/requestPolicies | Create a new request policy.
[**delete_policy**](OauthcibaServerPolicyApi.md#delete_policy) | **DELETE** /oauth/cibaServerPolicy/requestPolicies/{id} | Delete a request policy.
[**get_policies**](OauthcibaServerPolicyApi.md#get_policies) | **GET** /oauth/cibaServerPolicy/requestPolicies | Get list of request policies.
[**get_policy**](OauthcibaServerPolicyApi.md#get_policy) | **GET** /oauth/cibaServerPolicy/requestPolicies/{id} | Find request policy by ID.
[**get_settings**](OauthcibaServerPolicyApi.md#get_settings) | **GET** /oauth/cibaServerPolicy/settings | Get general ciba server request policy settings.
[**update_policy**](OauthcibaServerPolicyApi.md#update_policy) | **PUT** /oauth/cibaServerPolicy/requestPolicies/{id} | Update a request policy.
[**update_settings**](OauthcibaServerPolicyApi.md#update_settings) | **PUT** /oauth/cibaServerPolicy/settings | Update general ciba server request policy settings.


# **create_policy**
> RequestPolicy create_policy(body, x_bypass_external_validation=x_bypass_external_validation)

Create a new request policy.

Create a new request policy. If the request policy is not properly configured, a 422 status code is returned along with a list of validation errors that must be corrected.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OauthcibaServerPolicyApi()
body = swagger_client.RequestPolicy() # RequestPolicy | Configuration for new policy.
x_bypass_external_validation = false # bool | External validation will be bypassed when set to true. Default to false. (optional) (default to false)

try:
    # Create a new request policy.
    api_response = api_instance.create_policy(body, x_bypass_external_validation=x_bypass_external_validation)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OauthcibaServerPolicyApi->create_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RequestPolicy**](RequestPolicy.md)| Configuration for new policy. | 
 **x_bypass_external_validation** | **bool**| External validation will be bypassed when set to true. Default to false. | [optional] [default to false]

### Return type

[**RequestPolicy**](RequestPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_policy**
> delete_policy(id)

Delete a request policy.

Delete a request policy with the specified ID. A 404 status code is returned for nonexistent IDs. Note: If the request succeeds, the response body is empty. If the request fails, an ApiResult is returned with details of the error.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OauthcibaServerPolicyApi()
id = 'id_example' # str | ID of request policy to delete.

try:
    # Delete a request policy.
    api_instance.delete_policy(id)
except ApiException as e:
    print("Exception when calling OauthcibaServerPolicyApi->delete_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of request policy to delete. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_policies**
> RequestPolicies get_policies()

Get list of request policies.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OauthcibaServerPolicyApi()

try:
    # Get list of request policies.
    api_response = api_instance.get_policies()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OauthcibaServerPolicyApi->get_policies: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**RequestPolicies**](RequestPolicies.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_policy**
> RequestPolicy get_policy(id)

Find request policy by ID.

Get a request policy with the specified ID. A 404 status code is returned for nonexistent IDs.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OauthcibaServerPolicyApi()
id = 'id_example' # str | ID of the request policy to fetch.

try:
    # Find request policy by ID.
    api_response = api_instance.get_policy(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OauthcibaServerPolicyApi->get_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the request policy to fetch. | 

### Return type

[**RequestPolicy**](RequestPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_settings**
> CibaServerPolicySettings get_settings()

Get general ciba server request policy settings.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OauthcibaServerPolicyApi()

try:
    # Get general ciba server request policy settings.
    api_response = api_instance.get_settings()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OauthcibaServerPolicyApi->get_settings: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**CibaServerPolicySettings**](CibaServerPolicySettings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_policy**
> RequestPolicy update_policy(id, body, x_bypass_external_validation=x_bypass_external_validation)

Update a request policy.

Update a request policy with the matching ID. If the policy is not properly configured, a 422 status code is returned along with a list of validation errors that must be corrected. Note: A 404 status code is returned for nonexistent IDs.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OauthcibaServerPolicyApi()
id = 'id_example' # str | ID of the request policy to update.
body = swagger_client.RequestPolicy() # RequestPolicy | Configuration for updated policy.
x_bypass_external_validation = false # bool | External validation will be bypassed when set to true. Default to false. (optional) (default to false)

try:
    # Update a request policy.
    api_response = api_instance.update_policy(id, body, x_bypass_external_validation=x_bypass_external_validation)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OauthcibaServerPolicyApi->update_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the request policy to update. | 
 **body** | [**RequestPolicy**](RequestPolicy.md)| Configuration for updated policy. | 
 **x_bypass_external_validation** | **bool**| External validation will be bypassed when set to true. Default to false. | [optional] [default to false]

### Return type

[**RequestPolicy**](RequestPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_settings**
> CibaServerPolicySettings update_settings(body, x_bypass_external_validation=x_bypass_external_validation)

Update general ciba server request policy settings.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OauthcibaServerPolicyApi()
body = swagger_client.CibaServerPolicySettings() # CibaServerPolicySettings | Ciba server request policy settings.
x_bypass_external_validation = false # bool | External validation will be bypassed when set to true. Default to false. (optional) (default to false)

try:
    # Update general ciba server request policy settings.
    api_response = api_instance.update_settings(body, x_bypass_external_validation=x_bypass_external_validation)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OauthcibaServerPolicyApi->update_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CibaServerPolicySettings**](CibaServerPolicySettings.md)| Ciba server request policy settings. | 
 **x_bypass_external_validation** | **bool**| External validation will be bypassed when set to true. Default to false. | [optional] [default to false]

### Return type

[**CibaServerPolicySettings**](CibaServerPolicySettings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

