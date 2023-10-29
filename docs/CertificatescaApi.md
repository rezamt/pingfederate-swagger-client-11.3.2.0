# swagger_client.CertificatescaApi

All URIs are relative to *https://localhost:9999/pf-admin-api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_trusted_ca**](CertificatescaApi.md#delete_trusted_ca) | **DELETE** /certificates/ca/{id} | Delete a trusted certificate authority.
[**export_certificate_file**](CertificatescaApi.md#export_certificate_file) | **GET** /certificates/ca/{id}/file | Download the certificate from a given trusted certificate authority.
[**get_trusted_cas**](CertificatescaApi.md#get_trusted_cas) | **GET** /certificates/ca | Get list of trusted certificate authorities.
[**get_trusted_cert**](CertificatescaApi.md#get_trusted_cert) | **GET** /certificates/ca/{id} | Retrieve details of a trusted certificate authority.
[**import_trusted_ca**](CertificatescaApi.md#import_trusted_ca) | **POST** /certificates/ca/import | Import a new trusted certificate authority.


# **delete_trusted_ca**
> delete_trusted_ca(id)

Delete a trusted certificate authority.

If the request is successful, the response body is empty. If the request fails, an ApiResult is returned with details of the error.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CertificatescaApi()
id = 'id_example' # str | ID of the trusted certificate authority to delete.

try:
    # Delete a trusted certificate authority.
    api_instance.delete_trusted_ca(id)
except ApiException as e:
    print("Exception when calling CertificatescaApi->delete_trusted_ca: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the trusted certificate authority to delete. | 

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

Download the certificate from a given trusted certificate authority.

For a successful request, the PEM-encoded certificate file is directly returned as text and the response content type is application/x-x509-ca-cert. If an error occurs, an ApiResult is returned in JSON format and the content type is application/json.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CertificatescaApi()
id = 'id_example' # str | ID of the trusted certificate authority.

try:
    # Download the certificate from a given trusted certificate authority.
    api_response = api_instance.export_certificate_file(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CertificatescaApi->export_certificate_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the trusted certificate authority. | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_trusted_cas**
> CertViews get_trusted_cas()

Get list of trusted certificate authorities.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CertificatescaApi()

try:
    # Get list of trusted certificate authorities.
    api_response = api_instance.get_trusted_cas()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CertificatescaApi->get_trusted_cas: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**CertViews**](CertViews.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_trusted_cert**
> CertView get_trusted_cert(id)

Retrieve details of a trusted certificate authority.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CertificatescaApi()
id = 'id_example' # str | ID of the trusted certificate authority to retrieve.

try:
    # Retrieve details of a trusted certificate authority.
    api_response = api_instance.get_trusted_cert(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CertificatescaApi->get_trusted_cert: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the trusted certificate authority to retrieve. | 

### Return type

[**CertView**](CertView.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_trusted_ca**
> CertView import_trusted_ca(body)

Import a new trusted certificate authority.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CertificatescaApi()
body = swagger_client.X509File() # X509File | File data to import.

try:
    # Import a new trusted certificate authority.
    api_response = api_instance.import_trusted_ca(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CertificatescaApi->import_trusted_ca: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**X509File**](X509File.md)| File data to import. | 

### Return type

[**CertView**](CertView.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

