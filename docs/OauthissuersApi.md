# swagger_client.OauthissuersApi

All URIs are relative to *https://localhost:9999/pf-admin-api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_issuer**](OauthissuersApi.md#add_issuer) | **POST** /oauth/issuers | Create a new virtual issuer.
[**delete_issuer**](OauthissuersApi.md#delete_issuer) | **DELETE** /oauth/issuers/{id} | Delete a virtual issuer.
[**get_issuer_by_id**](OauthissuersApi.md#get_issuer_by_id) | **GET** /oauth/issuers/{id} | Find a virtual issuer by ID.
[**get_issuers**](OauthissuersApi.md#get_issuers) | **GET** /oauth/issuers | Get the list of virtual issuers.
[**update_issuer**](OauthissuersApi.md#update_issuer) | **PUT** /oauth/issuers/{id} | Update a virtual issuer.


# **add_issuer**
> Issuer add_issuer(body)

Create a new virtual issuer.

Create a new virtual issuer. If the virtual issuer is not properly configured, a 422 status code is returned along with a list of validation errors that must be corrected.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OauthissuersApi()
body = swagger_client.Issuer() # Issuer | Configuration for new virtual issuer.

try:
    # Create a new virtual issuer.
    api_response = api_instance.add_issuer(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OauthissuersApi->add_issuer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Issuer**](Issuer.md)| Configuration for new virtual issuer. | 

### Return type

[**Issuer**](Issuer.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_issuer**
> delete_issuer(id)

Delete a virtual issuer.

Delete a virtual issuer with the specified ID. A 404 status code is returned for nonexistent IDs. Note: If the request succeeds, the response body is empty. If the request fails, an ApiResult is returned with details of the error.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OauthissuersApi()
id = 'id_example' # str | ID of the virtual issuer to delete.

try:
    # Delete a virtual issuer.
    api_instance.delete_issuer(id)
except ApiException as e:
    print("Exception when calling OauthissuersApi->delete_issuer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the virtual issuer to delete. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_issuer_by_id**
> Issuer get_issuer_by_id(id)

Find a virtual issuer by ID.

Get a virtual issuer with the specified ID. A 404 status code is returned for nonexistent IDs.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OauthissuersApi()
id = 'id_example' # str | ID of the virtual issuer to fetch.

try:
    # Find a virtual issuer by ID.
    api_response = api_instance.get_issuer_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OauthissuersApi->get_issuer_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the virtual issuer to fetch. | 

### Return type

[**Issuer**](Issuer.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_issuers**
> Issuers get_issuers()

Get the list of virtual issuers.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OauthissuersApi()

try:
    # Get the list of virtual issuers.
    api_response = api_instance.get_issuers()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OauthissuersApi->get_issuers: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Issuers**](Issuers.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_issuer**
> Issuer update_issuer(id, body)

Update a virtual issuer.

Update a virtual issuer with the matching ID. If the policy is not properly configured, a 422 status code is returned along with a list of validation errors that must be corrected. Note: A 404 status code is returned for nonexistent IDs.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OauthissuersApi()
id = 'id_example' # str | ID of the virtual issuer to update.
body = swagger_client.Issuer() # Issuer | Configuration for updated virtual issuer.

try:
    # Update a virtual issuer.
    api_response = api_instance.update_issuer(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OauthissuersApi->update_issuer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the virtual issuer to update. | 
 **body** | [**Issuer**](Issuer.md)| Configuration for updated virtual issuer. | 

### Return type

[**Issuer**](Issuer.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

