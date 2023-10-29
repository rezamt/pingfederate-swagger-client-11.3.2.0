# swagger_client.OauthresourceOwnerCredentialsMappingsApi

All URIs are relative to *https://localhost:9999/pf-admin-api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_resource_owner_credentials_mapping**](OauthresourceOwnerCredentialsMappingsApi.md#create_resource_owner_credentials_mapping) | **POST** /oauth/resourceOwnerCredentialsMappings | Create a new Resource Owner Credentials mapping.
[**delete_resource_owner_credentials_mapping**](OauthresourceOwnerCredentialsMappingsApi.md#delete_resource_owner_credentials_mapping) | **DELETE** /oauth/resourceOwnerCredentialsMappings/{id} | Delete a Resource Owner Credentials mapping.
[**get_resource_owner_credentials_mapping**](OauthresourceOwnerCredentialsMappingsApi.md#get_resource_owner_credentials_mapping) | **GET** /oauth/resourceOwnerCredentialsMappings/{id} | Find the Resource Owner Credentials mapping by the ID.
[**get_resource_owner_credentials_mappings**](OauthresourceOwnerCredentialsMappingsApi.md#get_resource_owner_credentials_mappings) | **GET** /oauth/resourceOwnerCredentialsMappings | Get the list of Resource Owner Credentials Grant Mapping.
[**update_resource_owner_credentials_mapping**](OauthresourceOwnerCredentialsMappingsApi.md#update_resource_owner_credentials_mapping) | **PUT** /oauth/resourceOwnerCredentialsMappings/{id} | Update a Resource Owner Credentials mapping.


# **create_resource_owner_credentials_mapping**
> ResourceOwnerCredentialsMapping create_resource_owner_credentials_mapping(body, x_bypass_external_validation=x_bypass_external_validation)

Create a new Resource Owner Credentials mapping.

Create a new Resource Owner Credentials mapping. If a Resource Owner Credentials mapping can't be created, a 422 status code is returned along with a list of validation errors that must be corrected.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OauthresourceOwnerCredentialsMappingsApi()
body = swagger_client.ResourceOwnerCredentialsMapping() # ResourceOwnerCredentialsMapping | Configuration for Resource Owner Credentials mapping.
x_bypass_external_validation = false # bool | External validation will be bypassed when set to true. Default to false. (optional) (default to false)

try:
    # Create a new Resource Owner Credentials mapping.
    api_response = api_instance.create_resource_owner_credentials_mapping(body, x_bypass_external_validation=x_bypass_external_validation)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OauthresourceOwnerCredentialsMappingsApi->create_resource_owner_credentials_mapping: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ResourceOwnerCredentialsMapping**](ResourceOwnerCredentialsMapping.md)| Configuration for Resource Owner Credentials mapping. | 
 **x_bypass_external_validation** | **bool**| External validation will be bypassed when set to true. Default to false. | [optional] [default to false]

### Return type

[**ResourceOwnerCredentialsMapping**](ResourceOwnerCredentialsMapping.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_resource_owner_credentials_mapping**
> delete_resource_owner_credentials_mapping(id)

Delete a Resource Owner Credentials mapping.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OauthresourceOwnerCredentialsMappingsApi()
id = 'id_example' # str | ID of the Resource Owner Credentials mapping.

try:
    # Delete a Resource Owner Credentials mapping.
    api_instance.delete_resource_owner_credentials_mapping(id)
except ApiException as e:
    print("Exception when calling OauthresourceOwnerCredentialsMappingsApi->delete_resource_owner_credentials_mapping: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the Resource Owner Credentials mapping. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_resource_owner_credentials_mapping**
> ResourceOwnerCredentialsMapping get_resource_owner_credentials_mapping(id)

Find the Resource Owner Credentials mapping by the ID.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OauthresourceOwnerCredentialsMappingsApi()
id = 'id_example' # str | ID of the Resource Owner Credentials mapping.

try:
    # Find the Resource Owner Credentials mapping by the ID.
    api_response = api_instance.get_resource_owner_credentials_mapping(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OauthresourceOwnerCredentialsMappingsApi->get_resource_owner_credentials_mapping: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the Resource Owner Credentials mapping. | 

### Return type

[**ResourceOwnerCredentialsMapping**](ResourceOwnerCredentialsMapping.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_resource_owner_credentials_mappings**
> ResourceOwnerCredentialsMappings get_resource_owner_credentials_mappings()

Get the list of Resource Owner Credentials Grant Mapping.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OauthresourceOwnerCredentialsMappingsApi()

try:
    # Get the list of Resource Owner Credentials Grant Mapping.
    api_response = api_instance.get_resource_owner_credentials_mappings()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OauthresourceOwnerCredentialsMappingsApi->get_resource_owner_credentials_mappings: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ResourceOwnerCredentialsMappings**](ResourceOwnerCredentialsMappings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_resource_owner_credentials_mapping**
> ResourceOwnerCredentialsMapping update_resource_owner_credentials_mapping(id, body, x_bypass_external_validation=x_bypass_external_validation)

Update a Resource Owner Credentials mapping.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OauthresourceOwnerCredentialsMappingsApi()
id = 'id_example' # str | ID of the Resource Owner Credentials mapping to update.
body = swagger_client.ResourceOwnerCredentialsMapping() # ResourceOwnerCredentialsMapping | Configuration for Resource Owner Credentials mapping.
x_bypass_external_validation = false # bool | External validation will be bypassed when set to true. Default to false. (optional) (default to false)

try:
    # Update a Resource Owner Credentials mapping.
    api_response = api_instance.update_resource_owner_credentials_mapping(id, body, x_bypass_external_validation=x_bypass_external_validation)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OauthresourceOwnerCredentialsMappingsApi->update_resource_owner_credentials_mapping: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the Resource Owner Credentials mapping to update. | 
 **body** | [**ResourceOwnerCredentialsMapping**](ResourceOwnerCredentialsMapping.md)| Configuration for Resource Owner Credentials mapping. | 
 **x_bypass_external_validation** | **bool**| External validation will be bypassed when set to true. Default to false. | [optional] [default to false]

### Return type

[**ResourceOwnerCredentialsMapping**](ResourceOwnerCredentialsMapping.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

