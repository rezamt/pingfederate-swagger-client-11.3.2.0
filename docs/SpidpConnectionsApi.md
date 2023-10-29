# swagger_client.SpidpConnectionsApi

All URIs are relative to *https://localhost:9999/pf-admin-api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_connection_cert**](SpidpConnectionsApi.md#add_connection_cert) | **POST** /sp/idpConnections/{id}/credentials/certs | Add a new IdP connection certificate.
[**create_connection**](SpidpConnectionsApi.md#create_connection) | **POST** /sp/idpConnections | Create a new IdP connection.
[**delete_connection**](SpidpConnectionsApi.md#delete_connection) | **DELETE** /sp/idpConnections/{id} | Delete an IdP connection.
[**get_connection**](SpidpConnectionsApi.md#get_connection) | **GET** /sp/idpConnections/{id} | Find IdP connection by ID.
[**get_connection_certs**](SpidpConnectionsApi.md#get_connection_certs) | **GET** /sp/idpConnections/{id}/credentials/certs | Get the IdP connection&#39;s certificates.
[**get_connections**](SpidpConnectionsApi.md#get_connections) | **GET** /sp/idpConnections | Get list of IdP connections.
[**get_decryption_keys**](SpidpConnectionsApi.md#get_decryption_keys) | **GET** /sp/idpConnections/{id}/credentials/decryptionKeys | Get the decryption keys of an IdP connection.
[**get_signing_settings**](SpidpConnectionsApi.md#get_signing_settings) | **GET** /sp/idpConnections/{id}/credentials/signingSettings | Get the IdP connection&#39;s signature settings.
[**update_connection**](SpidpConnectionsApi.md#update_connection) | **PUT** /sp/idpConnections/{id} | Update an IdP connection.
[**update_connection_certs**](SpidpConnectionsApi.md#update_connection_certs) | **PUT** /sp/idpConnections/{id}/credentials/certs | Update the IdP connection&#39;s certificates.
[**update_decryption_keys**](SpidpConnectionsApi.md#update_decryption_keys) | **PUT** /sp/idpConnections/{id}/credentials/decryptionKeys | Updating the IdP connection&#39;s decryption keys.
[**update_signing_settings**](SpidpConnectionsApi.md#update_signing_settings) | **PUT** /sp/idpConnections/{id}/credentials/signingSettings | Update the IdP connection&#39;s signature settings.


# **add_connection_cert**
> ConnectionCert add_connection_cert(id, body)

Add a new IdP connection certificate.

If the certificate's activeVerificationCert flag is set to true, it will become the connection's primary verification certificate.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SpidpConnectionsApi()
id = 'id_example' # str | ID of the IdP Connection to update.
body = swagger_client.ConnectionCert() # ConnectionCert | Configuration for a verification certificate.

try:
    # Add a new IdP connection certificate.
    api_response = api_instance.add_connection_cert(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpidpConnectionsApi->add_connection_cert: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the IdP Connection to update. | 
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
> IdpConnection create_connection(body, x_bypass_external_validation=x_bypass_external_validation)

Create a new IdP connection.

Create a new IdP connection. If the IdP connection is not properly configured, a 422 status code is returned along with a list of validation errors that must be corrected.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SpidpConnectionsApi()
body = swagger_client.IdpConnection() # IdpConnection | Configuration for new connection.
x_bypass_external_validation = false # bool | External validation will be bypassed when set to true. Default to false. (optional) (default to false)

try:
    # Create a new IdP connection.
    api_response = api_instance.create_connection(body, x_bypass_external_validation=x_bypass_external_validation)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpidpConnectionsApi->create_connection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**IdpConnection**](IdpConnection.md)| Configuration for new connection. | 
 **x_bypass_external_validation** | **bool**| External validation will be bypassed when set to true. Default to false. | [optional] [default to false]

### Return type

[**IdpConnection**](IdpConnection.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_connection**
> delete_connection(id)

Delete an IdP connection.

Delete an IdP connection with the specified ID. A 404 status code is returned for nonexistent IDs. Note: Only inactive connections can be deleted. If the request succeeds, the response body is empty. If the request fails, an ApiResult is returned with details of the error.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SpidpConnectionsApi()
id = 'id_example' # str | ID of IdP Connection to delete.

try:
    # Delete an IdP connection.
    api_instance.delete_connection(id)
except ApiException as e:
    print("Exception when calling SpidpConnectionsApi->delete_connection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of IdP Connection to delete. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_connection**
> IdpConnection get_connection(id)

Find IdP connection by ID.

Get a SAML 2.0 IdP connection with the specified ID. A 404 status code is returned for nonexistent IDs.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SpidpConnectionsApi()
id = 'id_example' # str | ID of IdP Connection to fetch.

try:
    # Find IdP connection by ID.
    api_response = api_instance.get_connection(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpidpConnectionsApi->get_connection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of IdP Connection to fetch. | 

### Return type

[**IdpConnection**](IdpConnection.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_connection_certs**
> ConnectionCerts get_connection_certs(id)

Get the IdP connection's certificates.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SpidpConnectionsApi()
id = 'id_example' # str | ID of the IdP Connection.

try:
    # Get the IdP connection's certificates.
    api_response = api_instance.get_connection_certs(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpidpConnectionsApi->get_connection_certs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the IdP Connection. | 

### Return type

[**ConnectionCerts**](ConnectionCerts.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_connections**
> IdpConnections get_connections(entity_id=entity_id, page=page, number_per_page=number_per_page, filter=filter)

Get list of IdP connections.

Get a list of all the OIDC, WS-Trust, WS-Fed, SAML1.0, SAML1.1 and SAML 2.0 IdP connections.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SpidpConnectionsApi()
entity_id = 'entity_id_example' # str | Entity ID of the connection to fetch. (case-sensitive) (optional)
page = 56 # int | Page number to retrieve. (optional)
number_per_page = 56 # int | Number of connections per page. (optional)
filter = 'filter_example' # str | Filter criteria limits the IdP connections that are returned to only those that match it. The filter criteria is compared to the IdP connection name and partner entity ID fields. The comparison is a case-insensitive partial match. No additional pattern based matching is supported. (optional)

try:
    # Get list of IdP connections.
    api_response = api_instance.get_connections(entity_id=entity_id, page=page, number_per_page=number_per_page, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpidpConnectionsApi->get_connections: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_id** | **str**| Entity ID of the connection to fetch. (case-sensitive) | [optional] 
 **page** | **int**| Page number to retrieve. | [optional] 
 **number_per_page** | **int**| Number of connections per page. | [optional] 
 **filter** | **str**| Filter criteria limits the IdP connections that are returned to only those that match it. The filter criteria is compared to the IdP connection name and partner entity ID fields. The comparison is a case-insensitive partial match. No additional pattern based matching is supported. | [optional] 

### Return type

[**IdpConnections**](IdpConnections.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_decryption_keys**
> DecryptionKeys get_decryption_keys(id)

Get the decryption keys of an IdP connection.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SpidpConnectionsApi()
id = 'id_example' # str | ID of the IdP Connection to update.

try:
    # Get the decryption keys of an IdP connection.
    api_response = api_instance.get_decryption_keys(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpidpConnectionsApi->get_decryption_keys: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the IdP Connection to update. | 

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

Get the IdP connection's signature settings.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SpidpConnectionsApi()
id = 'id_example' # str | ID of the IdP Connection.

try:
    # Get the IdP connection's signature settings.
    api_response = api_instance.get_signing_settings(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpidpConnectionsApi->get_signing_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the IdP Connection. | 

### Return type

[**SigningSettings**](SigningSettings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_connection**
> IdpConnection update_connection(id, body, x_bypass_external_validation=x_bypass_external_validation)

Update an IdP connection.

Update an IdP connection with the matching ID. If the IdP connection is not properly configured, a 422 status code is returned along with a list of validation errors that must be corrected. Note: A 404 status code is returned for nonexistent IDs.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SpidpConnectionsApi()
id = 'id_example' # str | ID of IdP Connection to update.
body = swagger_client.IdpConnection() # IdpConnection | Configuration for updated connection.
x_bypass_external_validation = false # bool | External validation will be bypassed when set to true. Default to false. (optional) (default to false)

try:
    # Update an IdP connection.
    api_response = api_instance.update_connection(id, body, x_bypass_external_validation=x_bypass_external_validation)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpidpConnectionsApi->update_connection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of IdP Connection to update. | 
 **body** | [**IdpConnection**](IdpConnection.md)| Configuration for updated connection. | 
 **x_bypass_external_validation** | **bool**| External validation will be bypassed when set to true. Default to false. | [optional] [default to false]

### Return type

[**IdpConnection**](IdpConnection.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_connection_certs**
> ConnectionCerts update_connection_certs(id, body)

Update the IdP connection's certificates.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SpidpConnectionsApi()
id = 'id_example' # str | ID of the IdP Connection to update.
body = swagger_client.ConnectionCerts() # ConnectionCerts | Configuration for a verification certificates.

try:
    # Update the IdP connection's certificates.
    api_response = api_instance.update_connection_certs(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpidpConnectionsApi->update_connection_certs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the IdP Connection to update. | 
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

Updating the IdP connection's decryption keys.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SpidpConnectionsApi()
id = 'id_example' # str | ID of the IdP Connection to update.
body = swagger_client.DecryptionKeys() # DecryptionKeys | Configuration for decryption keys.

try:
    # Updating the IdP connection's decryption keys.
    api_response = api_instance.update_decryption_keys(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpidpConnectionsApi->update_decryption_keys: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the IdP Connection to update. | 
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

Update the IdP connection's signature settings.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SpidpConnectionsApi()
id = 'id_example' # str | ID of the IdP Connection to update.
body = swagger_client.SigningSettings() # SigningSettings | Signature settings.

try:
    # Update the IdP connection's signature settings.
    api_response = api_instance.update_signing_settings(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpidpConnectionsApi->update_signing_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the IdP Connection to update. | 
 **body** | [**SigningSettings**](SigningSettings.md)| Signature settings. | 

### Return type

[**SigningSettings**](SigningSettings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

