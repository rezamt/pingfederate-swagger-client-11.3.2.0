# swagger_client.KeyPairssslServerApi

All URIs are relative to *https://localhost:9999/pf-admin-api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_key_pair**](KeyPairssslServerApi.md#create_key_pair) | **POST** /keyPairs/sslServer/generate | Generate a new key pair.
[**delete_key_pair**](KeyPairssslServerApi.md#delete_key_pair) | **DELETE** /keyPairs/sslServer/{id} | Delete a key pair.
[**export_certificate_file**](KeyPairssslServerApi.md#export_certificate_file) | **GET** /keyPairs/sslServer/{id}/certificate | Download the certificate from a given key pair.
[**export_csr**](KeyPairssslServerApi.md#export_csr) | **GET** /keyPairs/sslServer/{id}/csr | Generate a new certificate signing request (CSR) for this key pair.
[**export_pem_file**](KeyPairssslServerApi.md#export_pem_file) | **POST** /keyPairs/sslServer/{id}/pem | Download the key pair in PEM format.
[**export_pkcs12_file**](KeyPairssslServerApi.md#export_pkcs12_file) | **POST** /keyPairs/sslServer/{id}/pkcs12 | Download the key pair in PKCS12 format.
[**get_key_pair**](KeyPairssslServerApi.md#get_key_pair) | **GET** /keyPairs/sslServer/{id} | Retrieve details of a key pair.
[**get_key_pairs**](KeyPairssslServerApi.md#get_key_pairs) | **GET** /keyPairs/sslServer | Get list of key pairs.
[**get_settings**](KeyPairssslServerApi.md#get_settings) | **GET** /keyPairs/sslServer/settings | Get the SSL Server Certificate Settings.
[**import_csr_response**](KeyPairssslServerApi.md#import_csr_response) | **POST** /keyPairs/sslServer/{id}/csr | Import a CSR response for this key pair.
[**import_key_pair**](KeyPairssslServerApi.md#import_key_pair) | **POST** /keyPairs/sslServer/import | Import a new key pair.
[**update_settings**](KeyPairssslServerApi.md#update_settings) | **PUT** /keyPairs/sslServer/settings | Update the SSL Server Certificate Settings.


# **create_key_pair**
> KeyPairView create_key_pair(body)

Generate a new key pair.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.KeyPairssslServerApi()
body = swagger_client.NewKeyPairSettings() # NewKeyPairSettings | Settings for the new key pair.

try:
    # Generate a new key pair.
    api_response = api_instance.create_key_pair(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KeyPairssslServerApi->create_key_pair: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NewKeyPairSettings**](NewKeyPairSettings.md)| Settings for the new key pair. | 

### Return type

[**KeyPairView**](KeyPairView.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_key_pair**
> delete_key_pair(id)

Delete a key pair.

If the request is successful, the response body is empty. If the request fails, an ApiResult is returned with details of the error.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.KeyPairssslServerApi()
id = 'id_example' # str | ID of the key pair to delete.

try:
    # Delete a key pair.
    api_instance.delete_key_pair(id)
except ApiException as e:
    print("Exception when calling KeyPairssslServerApi->delete_key_pair: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the key pair to delete. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_certificate_file**
> str export_certificate_file(id)

Download the certificate from a given key pair.

For a successful request, the PEM-encoded certificate file is directly returned as text and the response content type is application/x-x509-ca-cert. If an error occurs, an ApiResult is returned in JSON format and the content type is application/json.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.KeyPairssslServerApi()
id = 'id_example' # str | ID of the key pair.

try:
    # Download the certificate from a given key pair.
    api_response = api_instance.export_certificate_file(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KeyPairssslServerApi->export_certificate_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the key pair. | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_csr**
> str export_csr(id)

Generate a new certificate signing request (CSR) for this key pair.

For a successful request, the PEM-encoded CSR file is directly returned as text and the response content type is application/pkcs10. If an error occurs, an ApiResult is returned in JSON format, and the content type is application/json.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.KeyPairssslServerApi()
id = 'id_example' # str | ID of the key pair.

try:
    # Generate a new certificate signing request (CSR) for this key pair.
    api_response = api_instance.export_csr(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KeyPairssslServerApi->export_csr: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the key pair. | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_pem_file**
> str export_pem_file(id, body)

Download the key pair in PEM format.

For a successful request, the PEM file is directly returned in PEM format and the response content type is application/x-pem-file. In the exported PEM file, the private key is protected with PBES2 encryption and AES. If an error occurs, an ApiResult is returned in JSON format and the content type is application/json. Due to the sensitivity of the password parameter, the method for this operation is POST rather than GET.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.KeyPairssslServerApi()
id = 'id_example' # str | ID of the key pair.
body = swagger_client.KeyPairExportSettings() # KeyPairExportSettings | Parameters for the export request

try:
    # Download the key pair in PEM format.
    api_response = api_instance.export_pem_file(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KeyPairssslServerApi->export_pem_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the key pair. | 
 **body** | [**KeyPairExportSettings**](KeyPairExportSettings.md)| Parameters for the export request | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_pkcs12_file**
> str export_pkcs12_file(id, body)

Download the key pair in PKCS12 format.

For a successful request, the PKCS12 file is directly returned in binary format and the response content type is application/x-pkcs12. If an error occurs, an ApiResult is returned in JSON format and the content type is application/json. Due to the sensitivity of the password parameter, the method for this operation is POST rather than GET.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.KeyPairssslServerApi()
id = 'id_example' # str | ID of the key pair.
body = swagger_client.KeyPairExportSettings() # KeyPairExportSettings | Parameters for the export request

try:
    # Download the key pair in PKCS12 format.
    api_response = api_instance.export_pkcs12_file(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KeyPairssslServerApi->export_pkcs12_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the key pair. | 
 **body** | [**KeyPairExportSettings**](KeyPairExportSettings.md)| Parameters for the export request | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_key_pair**
> KeyPairView get_key_pair(id)

Retrieve details of a key pair.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.KeyPairssslServerApi()
id = 'id_example' # str | ID of the key pair to retrieve.

try:
    # Retrieve details of a key pair.
    api_response = api_instance.get_key_pair(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KeyPairssslServerApi->get_key_pair: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the key pair to retrieve. | 

### Return type

[**KeyPairView**](KeyPairView.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_key_pairs**
> KeyPairViews get_key_pairs()

Get list of key pairs.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.KeyPairssslServerApi()

try:
    # Get list of key pairs.
    api_response = api_instance.get_key_pairs()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KeyPairssslServerApi->get_key_pairs: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**KeyPairViews**](KeyPairViews.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_settings**
> SslServerSettings get_settings()

Get the SSL Server Certificate Settings.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.KeyPairssslServerApi()

try:
    # Get the SSL Server Certificate Settings.
    api_response = api_instance.get_settings()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KeyPairssslServerApi->get_settings: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SslServerSettings**](SslServerSettings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_csr_response**
> KeyPairView import_csr_response(id, body)

Import a CSR response for this key pair.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.KeyPairssslServerApi()
id = 'id_example' # str | ID of the key pair.
body = swagger_client.CSRResponse() # CSRResponse | The CSR response.

try:
    # Import a CSR response for this key pair.
    api_response = api_instance.import_csr_response(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KeyPairssslServerApi->import_csr_response: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the key pair. | 
 **body** | [**CSRResponse**](CSRResponse.md)| The CSR response. | 

### Return type

[**KeyPairView**](KeyPairView.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_key_pair**
> KeyPairView import_key_pair(body)

Import a new key pair.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.KeyPairssslServerApi()
body = swagger_client.KeyPairFile() # KeyPairFile | File to import.

try:
    # Import a new key pair.
    api_response = api_instance.import_key_pair(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KeyPairssslServerApi->import_key_pair: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**KeyPairFile**](KeyPairFile.md)| File to import. | 

### Return type

[**KeyPairView**](KeyPairView.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_settings**
> SslServerSettings update_settings(body)

Update the SSL Server Certificate Settings.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.KeyPairssslServerApi()
body = swagger_client.SslServerSettings() # SslServerSettings | Configuration for activation of SSL server certificates.

try:
    # Update the SSL Server Certificate Settings.
    api_response = api_instance.update_settings(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KeyPairssslServerApi->update_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SslServerSettings**](SslServerSettings.md)| Configuration for activation of SSL server certificates. | 

### Return type

[**SslServerSettings**](SslServerSettings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

