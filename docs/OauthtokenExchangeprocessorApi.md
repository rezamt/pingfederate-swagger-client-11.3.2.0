# swagger_client.OauthtokenExchangeprocessorApi

All URIs are relative to *https://localhost:9999/pf-admin-api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_policy**](OauthtokenExchangeprocessorApi.md#create_policy) | **POST** /oauth/tokenExchange/processor/policies | Create a new OAuth 2.0 Token Exchange Processor policy.
[**delete_policy**](OauthtokenExchangeprocessorApi.md#delete_policy) | **DELETE** /oauth/tokenExchange/processor/policies/{id} | Delete an OAuth 2.0 Token Exchange Processor policy.
[**get_policies**](OauthtokenExchangeprocessorApi.md#get_policies) | **GET** /oauth/tokenExchange/processor/policies | Get list of OAuth 2.0 Token Exchange Processor policies.
[**get_policy**](OauthtokenExchangeprocessorApi.md#get_policy) | **GET** /oauth/tokenExchange/processor/policies/{id} | Find an OAuth 2.0 Token Exchange Processor policy by ID.
[**get_settings**](OauthtokenExchangeprocessorApi.md#get_settings) | **GET** /oauth/tokenExchange/processor/settings | Get general OAuth 2.0 Token Exchange Processor settings.
[**update_policy**](OauthtokenExchangeprocessorApi.md#update_policy) | **PUT** /oauth/tokenExchange/processor/policies/{id} | Update an OAuth 2.0 Token Exchange Processor policy.
[**update_settings**](OauthtokenExchangeprocessorApi.md#update_settings) | **PUT** /oauth/tokenExchange/processor/settings | Update general OAuth 2.0 Token Exchange Processor settings.


# **create_policy**
> TokenExchangeProcessorPolicy create_policy(body, bypass_external_validation=bypass_external_validation)

Create a new OAuth 2.0 Token Exchange Processor policy.

Create a new OAuth 2.0 Token Exchange Processor policy. If the OAuth 2.0 Token Exchange Processor policy is not properly configured, a 422 status code is returned along with a list of validation errors that must be corrected.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OauthtokenExchangeprocessorApi()
body = swagger_client.TokenExchangeProcessorPolicy() # TokenExchangeProcessorPolicy | Configuration for new OAuth 2.0 Token Exchange Processor.
bypass_external_validation = true # bool | External validation will be bypassed when set to true. Default to false. (optional)

try:
    # Create a new OAuth 2.0 Token Exchange Processor policy.
    api_response = api_instance.create_policy(body, bypass_external_validation=bypass_external_validation)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OauthtokenExchangeprocessorApi->create_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TokenExchangeProcessorPolicy**](TokenExchangeProcessorPolicy.md)| Configuration for new OAuth 2.0 Token Exchange Processor. | 
 **bypass_external_validation** | **bool**| External validation will be bypassed when set to true. Default to false. | [optional] 

### Return type

[**TokenExchangeProcessorPolicy**](TokenExchangeProcessorPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_policy**
> delete_policy(id)

Delete an OAuth 2.0 Token Exchange Processor policy.

Delete an OAuth 2.0 Token Exchange Processor policy with the specified ID. A 404 status code is returned for nonexistent IDs. Note: If the request succeeds, the response body is empty. If the request fails, an ApiResult is returned with details of the error.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OauthtokenExchangeprocessorApi()
id = 'id_example' # str | ID of OAuth 2.0 Token Exchange Processor policy to delete.

try:
    # Delete an OAuth 2.0 Token Exchange Processor policy.
    api_instance.delete_policy(id)
except ApiException as e:
    print("Exception when calling OauthtokenExchangeprocessorApi->delete_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of OAuth 2.0 Token Exchange Processor policy to delete. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_policies**
> TokenExchangeProcessorPolicies get_policies()

Get list of OAuth 2.0 Token Exchange Processor policies.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OauthtokenExchangeprocessorApi()

try:
    # Get list of OAuth 2.0 Token Exchange Processor policies.
    api_response = api_instance.get_policies()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OauthtokenExchangeprocessorApi->get_policies: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**TokenExchangeProcessorPolicies**](TokenExchangeProcessorPolicies.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_policy**
> TokenExchangeProcessorPolicy get_policy(id)

Find an OAuth 2.0 Token Exchange Processor policy by ID.

Get an OAuth 2.0 Token Exchange Processor policy with the specified ID. A 404 status code is returned for nonexistent IDs.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OauthtokenExchangeprocessorApi()
id = 'id_example' # str | ID of the OAuth 2.0 Token Exchange Processor policy to fetch.

try:
    # Find an OAuth 2.0 Token Exchange Processor policy by ID.
    api_response = api_instance.get_policy(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OauthtokenExchangeprocessorApi->get_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the OAuth 2.0 Token Exchange Processor policy to fetch. | 

### Return type

[**TokenExchangeProcessorPolicy**](TokenExchangeProcessorPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_settings**
> TokenExchangeProcessorSettings get_settings()

Get general OAuth 2.0 Token Exchange Processor settings.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OauthtokenExchangeprocessorApi()

try:
    # Get general OAuth 2.0 Token Exchange Processor settings.
    api_response = api_instance.get_settings()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OauthtokenExchangeprocessorApi->get_settings: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**TokenExchangeProcessorSettings**](TokenExchangeProcessorSettings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_policy**
> TokenExchangeProcessorPolicy update_policy(id, body, bypass_external_validation=bypass_external_validation)

Update an OAuth 2.0 Token Exchange Processor policy.

Update an OAuth 2.0 Token Exchange Processor policy with the matching ID. If the policy is not properly configured, a 422 status code is returned along with a list of validation errors that must be corrected. Note: A 404 status code is returned for nonexistent IDs.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OauthtokenExchangeprocessorApi()
id = 'id_example' # str | ID of the OAuth 2.0 Token Exchange Processor policy to update.
body = swagger_client.TokenExchangeProcessorPolicy() # TokenExchangeProcessorPolicy | Configuration for updated OAuth 2.0 Token Exchange Processor policy.
bypass_external_validation = true # bool | External validation will be bypassed when set to true. Default to false. (optional)

try:
    # Update an OAuth 2.0 Token Exchange Processor policy.
    api_response = api_instance.update_policy(id, body, bypass_external_validation=bypass_external_validation)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OauthtokenExchangeprocessorApi->update_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the OAuth 2.0 Token Exchange Processor policy to update. | 
 **body** | [**TokenExchangeProcessorPolicy**](TokenExchangeProcessorPolicy.md)| Configuration for updated OAuth 2.0 Token Exchange Processor policy. | 
 **bypass_external_validation** | **bool**| External validation will be bypassed when set to true. Default to false. | [optional] 

### Return type

[**TokenExchangeProcessorPolicy**](TokenExchangeProcessorPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_settings**
> TokenExchangeProcessorSettings update_settings(body, bypass_external_validation=bypass_external_validation)

Update general OAuth 2.0 Token Exchange Processor settings.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OauthtokenExchangeprocessorApi()
body = swagger_client.TokenExchangeProcessorSettings() # TokenExchangeProcessorSettings | OAuth 2.0 Token Exchange Processor settings.
bypass_external_validation = true # bool | External validation will be bypassed when set to true. Default to false. (optional)

try:
    # Update general OAuth 2.0 Token Exchange Processor settings.
    api_response = api_instance.update_settings(body, bypass_external_validation=bypass_external_validation)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OauthtokenExchangeprocessorApi->update_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TokenExchangeProcessorSettings**](TokenExchangeProcessorSettings.md)| OAuth 2.0 Token Exchange Processor settings. | 
 **bypass_external_validation** | **bool**| External validation will be bypassed when set to true. Default to false. | [optional] 

### Return type

[**TokenExchangeProcessorSettings**](TokenExchangeProcessorSettings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

