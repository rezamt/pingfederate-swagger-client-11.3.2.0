# swagger_client.OauthidpAdapterMappingsApi

All URIs are relative to *https://localhost:9999/pf-admin-api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_idp_adapter_mapping**](OauthidpAdapterMappingsApi.md#create_idp_adapter_mapping) | **POST** /oauth/idpAdapterMappings | Create a new IdP adapter mapping.
[**delete_idp_adapter_mapping**](OauthidpAdapterMappingsApi.md#delete_idp_adapter_mapping) | **DELETE** /oauth/idpAdapterMappings/{id} | Delete an IdP adapter mapping.
[**get_idp_adapter_mapping**](OauthidpAdapterMappingsApi.md#get_idp_adapter_mapping) | **GET** /oauth/idpAdapterMappings/{id} | Find the IdP adapter mapping by the ID.
[**get_idp_adapter_mappings**](OauthidpAdapterMappingsApi.md#get_idp_adapter_mappings) | **GET** /oauth/idpAdapterMappings | Get the list of IdP adapter mappings.
[**update_idp_adapter_mapping**](OauthidpAdapterMappingsApi.md#update_idp_adapter_mapping) | **PUT** /oauth/idpAdapterMappings/{id} | Update an IdP adapter mapping.


# **create_idp_adapter_mapping**
> IdpAdapterMapping create_idp_adapter_mapping(body, x_bypass_external_validation=x_bypass_external_validation)

Create a new IdP adapter mapping.

Create a new IdP adapter mapping. If an IdP adapter mapping can't be created, a 422 status code is returned along with a list of validation errors that must be corrected.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OauthidpAdapterMappingsApi()
body = swagger_client.IdpAdapterMapping() # IdpAdapterMapping | Configuration for IdP adapter mapping.
x_bypass_external_validation = false # bool | External validation will be bypassed when set to true. Default to false. (optional) (default to false)

try:
    # Create a new IdP adapter mapping.
    api_response = api_instance.create_idp_adapter_mapping(body, x_bypass_external_validation=x_bypass_external_validation)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OauthidpAdapterMappingsApi->create_idp_adapter_mapping: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**IdpAdapterMapping**](IdpAdapterMapping.md)| Configuration for IdP adapter mapping. | 
 **x_bypass_external_validation** | **bool**| External validation will be bypassed when set to true. Default to false. | [optional] [default to false]

### Return type

[**IdpAdapterMapping**](IdpAdapterMapping.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_idp_adapter_mapping**
> delete_idp_adapter_mapping(id)

Delete an IdP adapter mapping.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OauthidpAdapterMappingsApi()
id = 'id_example' # str | ID of the IdP adapter mapping.

try:
    # Delete an IdP adapter mapping.
    api_instance.delete_idp_adapter_mapping(id)
except ApiException as e:
    print("Exception when calling OauthidpAdapterMappingsApi->delete_idp_adapter_mapping: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the IdP adapter mapping. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_idp_adapter_mapping**
> IdpAdapterMapping get_idp_adapter_mapping(id)

Find the IdP adapter mapping by the ID.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OauthidpAdapterMappingsApi()
id = 'id_example' # str | ID of the adapter mapping.

try:
    # Find the IdP adapter mapping by the ID.
    api_response = api_instance.get_idp_adapter_mapping(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OauthidpAdapterMappingsApi->get_idp_adapter_mapping: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the adapter mapping. | 

### Return type

[**IdpAdapterMapping**](IdpAdapterMapping.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_idp_adapter_mappings**
> IdpAdapterMappings get_idp_adapter_mappings()

Get the list of IdP adapter mappings.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OauthidpAdapterMappingsApi()

try:
    # Get the list of IdP adapter mappings.
    api_response = api_instance.get_idp_adapter_mappings()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OauthidpAdapterMappingsApi->get_idp_adapter_mappings: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**IdpAdapterMappings**](IdpAdapterMappings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_idp_adapter_mapping**
> IdpAdapterMapping update_idp_adapter_mapping(id, body, x_bypass_external_validation=x_bypass_external_validation)

Update an IdP adapter mapping.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OauthidpAdapterMappingsApi()
id = 'id_example' # str | ID of the IdP adapter mapping to update.
body = swagger_client.IdpAdapterMapping() # IdpAdapterMapping | Configuration for IdP adapter mapping.
x_bypass_external_validation = false # bool | External validation will be bypassed when set to true. Default to false. (optional) (default to false)

try:
    # Update an IdP adapter mapping.
    api_response = api_instance.update_idp_adapter_mapping(id, body, x_bypass_external_validation=x_bypass_external_validation)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OauthidpAdapterMappingsApi->update_idp_adapter_mapping: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the IdP adapter mapping to update. | 
 **body** | [**IdpAdapterMapping**](IdpAdapterMapping.md)| Configuration for IdP adapter mapping. | 
 **x_bypass_external_validation** | **bool**| External validation will be bypassed when set to true. Default to false. | [optional] [default to false]

### Return type

[**IdpAdapterMapping**](IdpAdapterMapping.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

