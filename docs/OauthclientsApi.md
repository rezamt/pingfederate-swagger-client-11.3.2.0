# swagger_client.OauthclientsApi

All URIs are relative to *https://localhost:9999/pf-admin-api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_client**](OauthclientsApi.md#create_client) | **POST** /oauth/clients | Create a new OAuth client.
[**delete_client**](OauthclientsApi.md#delete_client) | **DELETE** /oauth/clients/{id} | Delete an OAuth client.
[**get_client**](OauthclientsApi.md#get_client) | **GET** /oauth/clients/{id} | Find the OAuth client by ID.
[**get_client_secret**](OauthclientsApi.md#get_client_secret) | **GET** /oauth/clients/{id}/clientAuth/clientSecret | Get the client secret of an existing OAuth client.
[**get_clients**](OauthclientsApi.md#get_clients) | **GET** /oauth/clients | Get the list of OAuth clients.
[**update_client**](OauthclientsApi.md#update_client) | **PUT** /oauth/clients/{id} | Updates the OAuth client.
[**update_client_secret**](OauthclientsApi.md#update_client_secret) | **PUT** /oauth/clients/{id}/clientAuth/clientSecret | Update the client secret of an existing OAuth client.


# **create_client**
> Client create_client(body)

Create a new OAuth client.

Create a new OAuth client. If an OAuth client can't be created, a 422 status code is returned along with a list of validation errors that must be corrected.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OauthclientsApi()
body = swagger_client.Client() # Client | Configuration for new client.

try:
    # Create a new OAuth client.
    api_response = api_instance.create_client(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OauthclientsApi->create_client: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Client**](Client.md)| Configuration for new client. | 

### Return type

[**Client**](Client.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_client**
> delete_client(id)

Delete an OAuth client.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OauthclientsApi()
id = 'id_example' # str | ID of the client.

try:
    # Delete an OAuth client.
    api_instance.delete_client(id)
except ApiException as e:
    print("Exception when calling OauthclientsApi->delete_client: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the client. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_client**
> Client get_client(id)

Find the OAuth client by ID.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OauthclientsApi()
id = 'id_example' # str | ID of the client.

try:
    # Find the OAuth client by ID.
    api_response = api_instance.get_client(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OauthclientsApi->get_client: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the client. | 

### Return type

[**Client**](Client.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_client_secret**
> ClientSecret get_client_secret(id)

Get the client secret of an existing OAuth client.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OauthclientsApi()
id = 'id_example' # str | ID of the client.

try:
    # Get the client secret of an existing OAuth client.
    api_response = api_instance.get_client_secret(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OauthclientsApi->get_client_secret: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the client. | 

### Return type

[**ClientSecret**](ClientSecret.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_clients**
> Clients get_clients(page=page, number_per_page=number_per_page, filter=filter)

Get the list of OAuth clients.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OauthclientsApi()
page = 56 # int | Page number to retrieve. (optional)
number_per_page = 56 # int | Number of OAuth clients per page. (uncapped if unspecified) (optional)
filter = 'filter_example' # str | Filter criteria limits the OAuth clients that are returned to only those that match it. The filter criteria is compared to the OAuth client name and ID fields. The comparison is a case-insensitive partial match. No additional pattern based matching is supported. (optional)

try:
    # Get the list of OAuth clients.
    api_response = api_instance.get_clients(page=page, number_per_page=number_per_page, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OauthclientsApi->get_clients: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number to retrieve. | [optional] 
 **number_per_page** | **int**| Number of OAuth clients per page. (uncapped if unspecified) | [optional] 
 **filter** | **str**| Filter criteria limits the OAuth clients that are returned to only those that match it. The filter criteria is compared to the OAuth client name and ID fields. The comparison is a case-insensitive partial match. No additional pattern based matching is supported. | [optional] 

### Return type

[**Clients**](Clients.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_client**
> Client update_client(id, body)

Updates the OAuth client.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OauthclientsApi()
id = 'id_example' # str | ID of the client to be updated.
body = swagger_client.Client() # Client | Configuration for the client.

try:
    # Updates the OAuth client.
    api_response = api_instance.update_client(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OauthclientsApi->update_client: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the client to be updated. | 
 **body** | [**Client**](Client.md)| Configuration for the client. | 

### Return type

[**Client**](Client.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_client_secret**
> ClientSecret update_client_secret(id, body)

Update the client secret of an existing OAuth client.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OauthclientsApi()
id = 'id_example' # str | ID of the client to be updated.
body = swagger_client.ClientSecret() # ClientSecret | Client Secret.

try:
    # Update the client secret of an existing OAuth client.
    api_response = api_instance.update_client_secret(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OauthclientsApi->update_client_secret: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the client to be updated. | 
 **body** | [**ClientSecret**](ClientSecret.md)| Client Secret. | 

### Return type

[**ClientSecret**](ClientSecret.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

