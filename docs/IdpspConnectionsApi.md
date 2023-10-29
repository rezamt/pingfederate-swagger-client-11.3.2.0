# swagger_client.IdpspConnectionsApi

All URIs are relative to *https://localhost:9999/pf-admin-api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_connection_cert**](IdpspConnectionsApi.md#add_connection_cert) | **POST** /idp/spConnections/{id}/credentials/certs | Add a new SP connection certificate.
[**create_connection**](IdpspConnectionsApi.md#create_connection) | **POST** /idp/spConnections | Create a new SP connection.
[**delete_connection**](IdpspConnectionsApi.md#delete_connection) | **DELETE** /idp/spConnections/{id} | Delete an SP connection.
[**get_connection**](IdpspConnectionsApi.md#get_connection) | **GET** /idp/spConnections/{id} | Find SP connection by ID.
[**get_connection_certs**](IdpspConnectionsApi.md#get_connection_certs) | **GET** /idp/spConnections/{id}/credentials/certs | Get the SP connection&#39;s certificates.
[**get_connections**](IdpspConnectionsApi.md#get_connections) | **GET** /idp/spConnections | Get list of SP connections.
[**get_decryption_keys**](IdpspConnectionsApi.md#get_decryption_keys) | **GET** /idp/spConnections/{id}/credentials/decryptionKeys | Get the decryption keys of an SP connection.
[**get_signing_settings**](IdpspConnectionsApi.md#get_signing_settings) | **GET** /idp/spConnections/{id}/credentials/signingSettings | Get the SP connection&#39;s signature settings.
[**update_connection**](IdpspConnectionsApi.md#update_connection) | **PUT** /idp/spConnections/{id} | Update an SP connection.
[**update_connection_certs**](IdpspConnectionsApi.md#update_connection_certs) | **PUT** /idp/spConnections/{id}/credentials/certs | Update the SP connection&#39;s certificates.
[**update_decryption_keys**](IdpspConnectionsApi.md#update_decryption_keys) | **PUT** /idp/spConnections/{id}/credentials/decryptionKeys | Updating the SP connection&#39;s decryption keys.
[**update_signing_settings**](IdpspConnectionsApi.md#update_signing_settings) | **PUT** /idp/spConnections/{id}/credentials/signingSettings | Update the SP connection&#39;s signature settings.


# **add_connection_cert**
> ConnectionCert add_connection_cert(id, body)

Add a new SP connection certificate.

If the certificate's activeVerificationCert flag is set to true, it will become the connection's primary verification certificate.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IdpspConnectionsApi()
id = 'id_example' # str | ID of the SP Connection to update.
body = swagger_client.ConnectionCert() # ConnectionCert | Configuration for a verification certificate.

try:
    # Add a new SP connection certificate.
    api_response = api_instance.add_connection_cert(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IdpspConnectionsApi->add_connection_cert: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the SP Connection to update. | 
 **body** | [**ConnectionCert**](ConnectionCert.md)| Configuration for a verification certificate. | 

### Return type

[**ConnectionCert**](ConnectionCert.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_connection**
> SpConnection create_connection(body, x_bypass_external_validation=x_bypass_external_validation)

Create a new SP connection.

Create a new SP connection. If the SP connection is not properly configured, a 422 status code is returned along with a list of validation errors that must be corrected.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IdpspConnectionsApi()
body = swagger_client.SpConnection() # SpConnection | Configuration for new connection.
x_bypass_external_validation = false # bool | External validation will be bypassed when set to true. Default to false. (optional) (default to false)

try:
    # Create a new SP connection.
    api_response = api_instance.create_connection(body, x_bypass_external_validation=x_bypass_external_validation)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IdpspConnectionsApi->create_connection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SpConnection**](SpConnection.md)| Configuration for new connection. | 
 **x_bypass_external_validation** | **bool**| External validation will be bypassed when set to true. Default to false. | [optional] [default to false]

### Return type

[**SpConnection**](SpConnection.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_connection**
> delete_connection(id)

Delete an SP connection.

Delete an SP connection with the specified ID. A 404 status code is returned for nonexistent IDs. Note: Only inactive connections can be deleted. If the request succeeds, the response body is empty. If the request fails, an ApiResult is returned with details of the error.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IdpspConnectionsApi()
id = 'id_example' # str | ID of SP Connection to delete.

try:
    # Delete an SP connection.
    api_instance.delete_connection(id)
except ApiException as e:
    print("Exception when calling IdpspConnectionsApi->delete_connection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of SP Connection to delete. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_connection**
> SpConnection get_connection(id)

Find SP connection by ID.

Get an SP connection with the specified ID. A 404 status code is returned for nonexistent IDs.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IdpspConnectionsApi()
id = 'id_example' # str | ID of the SP Connection to fetch.

try:
    # Find SP connection by ID.
    api_response = api_instance.get_connection(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IdpspConnectionsApi->get_connection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the SP Connection to fetch. | 

### Return type

[**SpConnection**](SpConnection.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_connection_certs**
> ConnectionCerts get_connection_certs(id)

Get the SP connection's certificates.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IdpspConnectionsApi()
id = 'id_example' # str | ID of the SP Connection.

try:
    # Get the SP connection's certificates.
    api_response = api_instance.get_connection_certs(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IdpspConnectionsApi->get_connection_certs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the SP Connection. | 

### Return type

[**ConnectionCerts**](ConnectionCerts.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_connections**
> SpConnections get_connections(entity_id=entity_id, page=page, number_per_page=number_per_page, filter=filter)

Get list of SP connections.

Get a list of all the WS-Fed, WS-Trust, SAML1.0, SAML1.1 and SAML 2.0 SP connections.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IdpspConnectionsApi()
entity_id = 'entity_id_example' # str | Entity ID of the connection to fetch. (case-sensitive) (optional)
page = 56 # int | Page number to retrieve. (optional)
number_per_page = 56 # int | Number of connections per page. (optional)
filter = 'filter_example' # str | Filter criteria limits the SP connections that are returned to only those that match it. The filter criteria is compared to the SP connection name and partner entity ID fields. The comparison is a case-insensitive partial match. No additional pattern based matching is supported. (optional)

try:
    # Get list of SP connections.
    api_response = api_instance.get_connections(entity_id=entity_id, page=page, number_per_page=number_per_page, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IdpspConnectionsApi->get_connections: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_id** | **str**| Entity ID of the connection to fetch. (case-sensitive) | [optional] 
 **page** | **int**| Page number to retrieve. | [optional] 
 **number_per_page** | **int**| Number of connections per page. | [optional] 
 **filter** | **str**| Filter criteria limits the SP connections that are returned to only those that match it. The filter criteria is compared to the SP connection name and partner entity ID fields. The comparison is a case-insensitive partial match. No additional pattern based matching is supported. | [optional] 

### Return type

[**SpConnections**](SpConnections.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_decryption_keys**
> DecryptionKeys get_decryption_keys(id)

Get the decryption keys of an SP connection.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IdpspConnectionsApi()
id = 'id_example' # str | ID of the SP Connection to update.

try:
    # Get the decryption keys of an SP connection.
    api_response = api_instance.get_decryption_keys(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IdpspConnectionsApi->get_decryption_keys: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the SP Connection to update. | 

### Return type

[**DecryptionKeys**](DecryptionKeys.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_signing_settings**
> SigningSettings get_signing_settings(id)

Get the SP connection's signature settings.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IdpspConnectionsApi()
id = 'id_example' # str | ID of the SP Connection.

try:
    # Get the SP connection's signature settings.
    api_response = api_instance.get_signing_settings(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IdpspConnectionsApi->get_signing_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the SP Connection. | 

### Return type

[**SigningSettings**](SigningSettings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_connection**
> SpConnection update_connection(id, body, x_bypass_external_validation=x_bypass_external_validation)

Update an SP connection.

Update an SP connection with the matching ID. If the SP connection is not properly configured, a 422 status code is returned along with a list of validation errors that must be corrected. Note: A 404 status code is returned for nonexistent IDs.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IdpspConnectionsApi()
id = 'id_example' # str | ID of SP Connection to update.
body = swagger_client.SpConnection() # SpConnection | Configuration for updated connection.
x_bypass_external_validation = false # bool | External validation will be bypassed when set to true. Default to false. (optional) (default to false)

try:
    # Update an SP connection.
    api_response = api_instance.update_connection(id, body, x_bypass_external_validation=x_bypass_external_validation)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IdpspConnectionsApi->update_connection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of SP Connection to update. | 
 **body** | [**SpConnection**](SpConnection.md)| Configuration for updated connection. | 
 **x_bypass_external_validation** | **bool**| External validation will be bypassed when set to true. Default to false. | [optional] [default to false]

### Return type

[**SpConnection**](SpConnection.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_connection_certs**
> ConnectionCerts update_connection_certs(id, body)

Update the SP connection's certificates.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IdpspConnectionsApi()
id = 'id_example' # str | ID of the SP Connection to update.
body = swagger_client.ConnectionCerts() # ConnectionCerts | Configuration for a verification certificates.

try:
    # Update the SP connection's certificates.
    api_response = api_instance.update_connection_certs(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IdpspConnectionsApi->update_connection_certs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the SP Connection to update. | 
 **body** | [**ConnectionCerts**](ConnectionCerts.md)| Configuration for a verification certificates. | 

### Return type

[**ConnectionCerts**](ConnectionCerts.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_decryption_keys**
> DecryptionKeys update_decryption_keys(id, body)

Updating the SP connection's decryption keys.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IdpspConnectionsApi()
id = 'id_example' # str | ID of the SP Connection to update.
body = swagger_client.DecryptionKeys() # DecryptionKeys | Configuration for decryption keys.

try:
    # Updating the SP connection's decryption keys.
    api_response = api_instance.update_decryption_keys(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IdpspConnectionsApi->update_decryption_keys: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the SP Connection to update. | 
 **body** | [**DecryptionKeys**](DecryptionKeys.md)| Configuration for decryption keys. | 

### Return type

[**DecryptionKeys**](DecryptionKeys.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_signing_settings**
> SigningSettings update_signing_settings(id, body)

Update the SP connection's signature settings.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IdpspConnectionsApi()
id = 'id_example' # str | ID of the SP Connection to update.
body = swagger_client.SigningSettings() # SigningSettings | Signature settings.

try:
    # Update the SP connection's signature settings.
    api_response = api_instance.update_signing_settings(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IdpspConnectionsApi->update_signing_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the SP Connection to update. | 
 **body** | [**SigningSettings**](SigningSettings.md)| Signature settings. | 

### Return type

[**SigningSettings**](SigningSettings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

