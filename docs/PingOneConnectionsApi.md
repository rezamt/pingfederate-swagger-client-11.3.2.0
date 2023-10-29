# swagger_client.PingOneConnectionsApi

All URIs are relative to *https://localhost:9999/pf-admin-api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_ping_one_connection**](PingOneConnectionsApi.md#create_ping_one_connection) | **POST** /pingOneConnections | Create a new PingOne connection.
[**delete_ping_one_connection**](PingOneConnectionsApi.md#delete_ping_one_connection) | **DELETE** /pingOneConnections/{id} | Delete a PingOne connection.
[**get_credential_status**](PingOneConnectionsApi.md#get_credential_status) | **GET** /pingOneConnections/{id}/credentialStatus | Get the status of the credential associated with the PingOne connection
[**get_ping_one_connection**](PingOneConnectionsApi.md#get_ping_one_connection) | **GET** /pingOneConnections/{id} | Get a PingOne connection with the specified ID.
[**get_ping_one_connection_associations**](PingOneConnectionsApi.md#get_ping_one_connection_associations) | **GET** /pingOneConnections/{id}/serviceAssociations | Get information about components using this connection to access PingOne services.
[**get_ping_one_connection_environments**](PingOneConnectionsApi.md#get_ping_one_connection_environments) | **GET** /pingOneConnections/{id}/environments | Get the list of environments that the PingOne connection has access to.
[**get_ping_one_connection_usages**](PingOneConnectionsApi.md#get_ping_one_connection_usages) | **GET** /pingOneConnections/{id}/usage | Get the list of resources that reference this PingOne connection.
[**get_ping_one_connections**](PingOneConnectionsApi.md#get_ping_one_connections) | **GET** /pingOneConnections | Get the list of all PingOne connections.
[**update_ping_one_connection**](PingOneConnectionsApi.md#update_ping_one_connection) | **PUT** /pingOneConnections/{id} | Update a PingOne connection.


# **create_ping_one_connection**
> PingOneConnection create_ping_one_connection(body, x_bypass_external_validation=x_bypass_external_validation)

Create a new PingOne connection.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PingOneConnectionsApi()
body = swagger_client.PingOneConnection() # PingOneConnection | Configuration for the new PingOne connection.
x_bypass_external_validation = false # bool | External validation will be bypassed when set to true. Default to false. (optional) (default to false)

try:
    # Create a new PingOne connection.
    api_response = api_instance.create_ping_one_connection(body, x_bypass_external_validation=x_bypass_external_validation)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PingOneConnectionsApi->create_ping_one_connection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PingOneConnection**](PingOneConnection.md)| Configuration for the new PingOne connection. | 
 **x_bypass_external_validation** | **bool**| External validation will be bypassed when set to true. Default to false. | [optional] [default to false]

### Return type

[**PingOneConnection**](PingOneConnection.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_ping_one_connection**
> delete_ping_one_connection(id)

Delete a PingOne connection.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PingOneConnectionsApi()
id = 'id_example' # str | ID of the PingOne connection to delete.

try:
    # Delete a PingOne connection.
    api_instance.delete_ping_one_connection(id)
except ApiException as e:
    print("Exception when calling PingOneConnectionsApi->delete_ping_one_connection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the PingOne connection to delete. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_credential_status**
> PingOneCredentialStatus get_credential_status(id)

Get the status of the credential associated with the PingOne connection



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PingOneConnectionsApi()
id = 'id_example' # str | ID of the PingOne connection.

try:
    # Get the status of the credential associated with the PingOne connection
    api_response = api_instance.get_credential_status(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PingOneConnectionsApi->get_credential_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the PingOne connection. | 

### Return type

[**PingOneCredentialStatus**](PingOneCredentialStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ping_one_connection**
> PingOneConnection get_ping_one_connection(id)

Get a PingOne connection with the specified ID.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PingOneConnectionsApi()
id = 'id_example' # str | ID of the connection to fetch.

try:
    # Get a PingOne connection with the specified ID.
    api_response = api_instance.get_ping_one_connection(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PingOneConnectionsApi->get_ping_one_connection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the connection to fetch. | 

### Return type

[**PingOneConnection**](PingOneConnection.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ping_one_connection_associations**
> ServiceAssociations get_ping_one_connection_associations(id)

Get information about components using this connection to access PingOne services.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PingOneConnectionsApi()
id = 'id_example' # str | ID of the PingOne connection.

try:
    # Get information about components using this connection to access PingOne services.
    api_response = api_instance.get_ping_one_connection_associations(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PingOneConnectionsApi->get_ping_one_connection_associations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the PingOne connection. | 

### Return type

[**ServiceAssociations**](ServiceAssociations.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ping_one_connection_environments**
> PingOneEnvironments get_ping_one_connection_environments(id, page=page, number_per_page=number_per_page, filter=filter)

Get the list of environments that the PingOne connection has access to.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PingOneConnectionsApi()
id = 'id_example' # str | ID of the PingOne connection.
page = 56 # int | Page number to retrieve. (optional)
number_per_page = 56 # int | Number of environments per page. (optional)
filter = 'filter_example' # str | Filter criteria limits the environments that are returned to only those that match it. The filter criteria is compared to the environment name and ID fields. The comparison is a case-insensitive partial match. No additional pattern based matching is supported. (optional)

try:
    # Get the list of environments that the PingOne connection has access to.
    api_response = api_instance.get_ping_one_connection_environments(id, page=page, number_per_page=number_per_page, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PingOneConnectionsApi->get_ping_one_connection_environments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the PingOne connection. | 
 **page** | **int**| Page number to retrieve. | [optional] 
 **number_per_page** | **int**| Number of environments per page. | [optional] 
 **filter** | **str**| Filter criteria limits the environments that are returned to only those that match it. The filter criteria is compared to the environment name and ID fields. The comparison is a case-insensitive partial match. No additional pattern based matching is supported. | [optional] 

### Return type

[**PingOneEnvironments**](PingOneEnvironments.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ping_one_connection_usages**
> ResourceUsages get_ping_one_connection_usages(id)

Get the list of resources that reference this PingOne connection.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PingOneConnectionsApi()
id = 'id_example' # str | ID of the PingOne connection.

try:
    # Get the list of resources that reference this PingOne connection.
    api_response = api_instance.get_ping_one_connection_usages(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PingOneConnectionsApi->get_ping_one_connection_usages: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the PingOne connection. | 

### Return type

[**ResourceUsages**](ResourceUsages.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ping_one_connections**
> PingOneConnections get_ping_one_connections()

Get the list of all PingOne connections.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PingOneConnectionsApi()

try:
    # Get the list of all PingOne connections.
    api_response = api_instance.get_ping_one_connections()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PingOneConnectionsApi->get_ping_one_connections: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**PingOneConnections**](PingOneConnections.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_ping_one_connection**
> PingOneConnection update_ping_one_connection(id, body, x_bypass_external_validation=x_bypass_external_validation)

Update a PingOne connection.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PingOneConnectionsApi()
id = 'id_example' # str | ID of the PingOne connection to update.
body = swagger_client.PingOneConnection() # PingOneConnection | Configuration for the updated connection.
x_bypass_external_validation = false # bool | External validation will be bypassed when set to true. Default to false. (optional) (default to false)

try:
    # Update a PingOne connection.
    api_response = api_instance.update_ping_one_connection(id, body, x_bypass_external_validation=x_bypass_external_validation)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PingOneConnectionsApi->update_ping_one_connection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the PingOne connection to update. | 
 **body** | [**PingOneConnection**](PingOneConnection.md)| Configuration for the updated connection. | 
 **x_bypass_external_validation** | **bool**| External validation will be bypassed when set to true. Default to false. | [optional] [default to false]

### Return type

[**PingOneConnection**](PingOneConnection.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

