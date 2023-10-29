# swagger_client.OauthtokenExchangegeneratorApi

All URIs are relative to *https://localhost:9999/pf-admin-api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_group**](OauthtokenExchangegeneratorApi.md#create_group) | **POST** /oauth/tokenExchange/generator/groups | Create a new OAuth 2.0 Token Exchange Generator group.
[**delete_group**](OauthtokenExchangegeneratorApi.md#delete_group) | **DELETE** /oauth/tokenExchange/generator/groups/{id} | Delete an OAuth 2.0 Token Exchange Generator group.
[**get_group**](OauthtokenExchangegeneratorApi.md#get_group) | **GET** /oauth/tokenExchange/generator/groups/{id} | Find an OAuth 2.0 Token Exchange Generator group by ID.
[**get_groups**](OauthtokenExchangegeneratorApi.md#get_groups) | **GET** /oauth/tokenExchange/generator/groups | Get list of OAuth 2.0 Token Exchange Generator groups.
[**get_settings**](OauthtokenExchangegeneratorApi.md#get_settings) | **GET** /oauth/tokenExchange/generator/settings | Get general OAuth 2.0 Token Exchange Generator settings.
[**update_group**](OauthtokenExchangegeneratorApi.md#update_group) | **PUT** /oauth/tokenExchange/generator/groups/{id} | Update an OAuth 2.0 Token Exchange Generator group.
[**update_settings**](OauthtokenExchangegeneratorApi.md#update_settings) | **PUT** /oauth/tokenExchange/generator/settings | Update general OAuth 2.0 Token Exchange Generator settings.


# **create_group**
> TokenExchangeGeneratorGroup create_group(body, bypass_external_validation=bypass_external_validation)

Create a new OAuth 2.0 Token Exchange Generator group.

Create a new OAuth 2.0 Token Exchange Generator group. If the OAuth 2.0 Token Exchange Generator group is not properly configured, a 422 status code is returned along with a list of validation errors that must be corrected.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OauthtokenExchangegeneratorApi()
body = swagger_client.TokenExchangeGeneratorGroup() # TokenExchangeGeneratorGroup | Configuration for new OAuth 2.0 Token Exchange Generator.
bypass_external_validation = true # bool | External validation will be bypassed when set to true. Default to false. (optional)

try:
    # Create a new OAuth 2.0 Token Exchange Generator group.
    api_response = api_instance.create_group(body, bypass_external_validation=bypass_external_validation)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OauthtokenExchangegeneratorApi->create_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TokenExchangeGeneratorGroup**](TokenExchangeGeneratorGroup.md)| Configuration for new OAuth 2.0 Token Exchange Generator. | 
 **bypass_external_validation** | **bool**| External validation will be bypassed when set to true. Default to false. | [optional] 

### Return type

[**TokenExchangeGeneratorGroup**](TokenExchangeGeneratorGroup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_group**
> delete_group(id)

Delete an OAuth 2.0 Token Exchange Generator group.

Delete an OAuth 2.0 Token Exchange Generator group with the specified ID. A 404 status code is returned for nonexistent IDs. Note: If the request succeeds, the response body is empty. If the request fails, an ApiResult is returned with details of the error.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OauthtokenExchangegeneratorApi()
id = 'id_example' # str | ID of OAuth 2.0 Token Exchange Generator group to delete.

try:
    # Delete an OAuth 2.0 Token Exchange Generator group.
    api_instance.delete_group(id)
except ApiException as e:
    print("Exception when calling OauthtokenExchangegeneratorApi->delete_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of OAuth 2.0 Token Exchange Generator group to delete. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_group**
> TokenExchangeGeneratorGroup get_group(id)

Find an OAuth 2.0 Token Exchange Generator group by ID.

Get an OAuth 2.0 Token Exchange Generator group with the specified ID. A 404 status code is returned for nonexistent IDs.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OauthtokenExchangegeneratorApi()
id = 'id_example' # str | ID of the OAuth 2.0 Token Exchange Generator group to fetch.

try:
    # Find an OAuth 2.0 Token Exchange Generator group by ID.
    api_response = api_instance.get_group(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OauthtokenExchangegeneratorApi->get_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the OAuth 2.0 Token Exchange Generator group to fetch. | 

### Return type

[**TokenExchangeGeneratorGroup**](TokenExchangeGeneratorGroup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_groups**
> TokenExchangeGeneratorGroups get_groups()

Get list of OAuth 2.0 Token Exchange Generator groups.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OauthtokenExchangegeneratorApi()

try:
    # Get list of OAuth 2.0 Token Exchange Generator groups.
    api_response = api_instance.get_groups()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OauthtokenExchangegeneratorApi->get_groups: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**TokenExchangeGeneratorGroups**](TokenExchangeGeneratorGroups.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_settings**
> TokenExchangeGeneratorSettings get_settings()

Get general OAuth 2.0 Token Exchange Generator settings.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OauthtokenExchangegeneratorApi()

try:
    # Get general OAuth 2.0 Token Exchange Generator settings.
    api_response = api_instance.get_settings()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OauthtokenExchangegeneratorApi->get_settings: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**TokenExchangeGeneratorSettings**](TokenExchangeGeneratorSettings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_group**
> TokenExchangeGeneratorGroup update_group(id, body, bypass_external_validation=bypass_external_validation)

Update an OAuth 2.0 Token Exchange Generator group.

Update an OAuth 2.0 Token Exchange Generator group with the matching ID. If the group is not properly configured, a 422 status code is returned along with a list of validation errors that must be corrected. Note: A 404 status code is returned for nonexistent IDs.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OauthtokenExchangegeneratorApi()
id = 'id_example' # str | ID of the OAuth 2.0 Token Exchange Generator group to update.
body = swagger_client.TokenExchangeGeneratorGroup() # TokenExchangeGeneratorGroup | Configuration for updated OAuth 2.0 Token Exchange Generator group.
bypass_external_validation = true # bool | External validation will be bypassed when set to true. Default to false. (optional)

try:
    # Update an OAuth 2.0 Token Exchange Generator group.
    api_response = api_instance.update_group(id, body, bypass_external_validation=bypass_external_validation)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OauthtokenExchangegeneratorApi->update_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the OAuth 2.0 Token Exchange Generator group to update. | 
 **body** | [**TokenExchangeGeneratorGroup**](TokenExchangeGeneratorGroup.md)| Configuration for updated OAuth 2.0 Token Exchange Generator group. | 
 **bypass_external_validation** | **bool**| External validation will be bypassed when set to true. Default to false. | [optional] 

### Return type

[**TokenExchangeGeneratorGroup**](TokenExchangeGeneratorGroup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_settings**
> TokenExchangeGeneratorSettings update_settings(body, bypass_external_validation=bypass_external_validation)

Update general OAuth 2.0 Token Exchange Generator settings.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OauthtokenExchangegeneratorApi()
body = swagger_client.TokenExchangeGeneratorSettings() # TokenExchangeGeneratorSettings | OAuth 2.0 Token Exchange Generator settings.
bypass_external_validation = true # bool | External validation will be bypassed when set to true. Default to false. (optional)

try:
    # Update general OAuth 2.0 Token Exchange Generator settings.
    api_response = api_instance.update_settings(body, bypass_external_validation=bypass_external_validation)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OauthtokenExchangegeneratorApi->update_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TokenExchangeGeneratorSettings**](TokenExchangeGeneratorSettings.md)| OAuth 2.0 Token Exchange Generator settings. | 
 **bypass_external_validation** | **bool**| External validation will be bypassed when set to true. Default to false. | [optional] 

### Return type

[**TokenExchangeGeneratorSettings**](TokenExchangeGeneratorSettings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

