# swagger_client.OauthauthorizationDetailTypesApi

All URIs are relative to *https://localhost:9999/pf-admin-api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_authorization_detail_type**](OauthauthorizationDetailTypesApi.md#add_authorization_detail_type) | **POST** /oauth/authorizationDetailTypes | Create a new authorization detail type.
[**delete_authorization_detail_type**](OauthauthorizationDetailTypesApi.md#delete_authorization_detail_type) | **DELETE** /oauth/authorizationDetailTypes/{id} | Delete an authorization detail type.
[**get_authorization_detail_type_by_id**](OauthauthorizationDetailTypesApi.md#get_authorization_detail_type_by_id) | **GET** /oauth/authorizationDetailTypes/{id} | Get an authorization detail type.
[**get_authorization_detail_types**](OauthauthorizationDetailTypesApi.md#get_authorization_detail_types) | **GET** /oauth/authorizationDetailTypes | Get the list of authorization detail types.
[**update_authorization_detail_type**](OauthauthorizationDetailTypesApi.md#update_authorization_detail_type) | **PUT** /oauth/authorizationDetailTypes/{id} | Update an authorization detail type.


# **add_authorization_detail_type**
> AuthorizationDetailType add_authorization_detail_type(body)

Create a new authorization detail type.

Create an authorization detail type. If the authorization detail type is not properly configured, a 422 status code is returned along with a list of validation errors that must be corrected.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OauthauthorizationDetailTypesApi()
body = swagger_client.AuthorizationDetailType() # AuthorizationDetailType | Configuration for new authorization detail type.

try:
    # Create a new authorization detail type.
    api_response = api_instance.add_authorization_detail_type(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OauthauthorizationDetailTypesApi->add_authorization_detail_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AuthorizationDetailType**](AuthorizationDetailType.md)| Configuration for new authorization detail type. | 

### Return type

[**AuthorizationDetailType**](AuthorizationDetailType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_authorization_detail_type**
> delete_authorization_detail_type(id)

Delete an authorization detail type.

Delete an authorization detail type with the specified ID. A 404 status code is returned for nonexistent IDs. Note: If the request succeeds, the response body is empty.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OauthauthorizationDetailTypesApi()
id = 'id_example' # str | ID of the authorization detail type.

try:
    # Delete an authorization detail type.
    api_instance.delete_authorization_detail_type(id)
except ApiException as e:
    print("Exception when calling OauthauthorizationDetailTypesApi->delete_authorization_detail_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the authorization detail type. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_authorization_detail_type_by_id**
> AuthorizationDetailType get_authorization_detail_type_by_id(id)

Get an authorization detail type.

Get the configured authorization detail type with the specified ID. A 404 status code is returned for nonexistent IDs.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OauthauthorizationDetailTypesApi()
id = 'id_example' # str | ID of the authorization detail type.

try:
    # Get an authorization detail type.
    api_response = api_instance.get_authorization_detail_type_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OauthauthorizationDetailTypesApi->get_authorization_detail_type_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the authorization detail type. | 

### Return type

[**AuthorizationDetailType**](AuthorizationDetailType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_authorization_detail_types**
> AuthorizationDetailTypes get_authorization_detail_types()

Get the list of authorization detail types.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OauthauthorizationDetailTypesApi()

try:
    # Get the list of authorization detail types.
    api_response = api_instance.get_authorization_detail_types()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OauthauthorizationDetailTypesApi->get_authorization_detail_types: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AuthorizationDetailTypes**](AuthorizationDetailTypes.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_authorization_detail_type**
> AuthorizationDetailType update_authorization_detail_type(id, body)

Update an authorization detail type.

Update an authorization detail type with matching ID. If the type is not properly configured, a 422 status code is returned along with a list of validation errors that must be corrected. Note: A 404 status code is returned for nonexistent IDs.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OauthauthorizationDetailTypesApi()
id = 'id_example' # str | ID of the authorization detail type.
body = swagger_client.AuthorizationDetailType() # AuthorizationDetailType | Configuration for updated authorization detail type.

try:
    # Update an authorization detail type.
    api_response = api_instance.update_authorization_detail_type(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OauthauthorizationDetailTypesApi->update_authorization_detail_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the authorization detail type. | 
 **body** | [**AuthorizationDetailType**](AuthorizationDetailType.md)| Configuration for updated authorization detail type. | 

### Return type

[**AuthorizationDetailType**](AuthorizationDetailType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

