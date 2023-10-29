# swagger_client.CertificatesrevocationApi

All URIs are relative to *https://localhost:9999/pf-admin-api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_ocsp_certificate_by_id**](CertificatesrevocationApi.md#delete_ocsp_certificate_by_id) | **DELETE** /certificates/revocation/ocspCertificates/{id} | Delete an OCSP responder signature verification certificate by ID.
[**get_ocsp_certificate_by_id**](CertificatesrevocationApi.md#get_ocsp_certificate_by_id) | **GET** /certificates/revocation/ocspCertificates/{id} | Get an OCSP responder signature verification certificate by ID.
[**get_ocsp_certificates**](CertificatesrevocationApi.md#get_ocsp_certificates) | **GET** /certificates/revocation/ocspCertificates | Get the list of available OCSP responder signature verification certificates.
[**get_revocation_settings**](CertificatesrevocationApi.md#get_revocation_settings) | **GET** /certificates/revocation/settings | Get certificate revocation settings.
[**import_ocsp_certificate**](CertificatesrevocationApi.md#import_ocsp_certificate) | **POST** /certificates/revocation/ocspCertificates | Import an OCSP responder signature verification certificate.
[**update_revocation_settings**](CertificatesrevocationApi.md#update_revocation_settings) | **PUT** /certificates/revocation/settings | Update certificate revocation settings.


# **delete_ocsp_certificate_by_id**
> delete_ocsp_certificate_by_id(id)

Delete an OCSP responder signature verification certificate by ID.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CertificatesrevocationApi()
id = 'id_example' # str | Certificate ID.

try:
    # Delete an OCSP responder signature verification certificate by ID.
    api_instance.delete_ocsp_certificate_by_id(id)
except ApiException as e:
    print("Exception when calling CertificatesrevocationApi->delete_ocsp_certificate_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Certificate ID. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ocsp_certificate_by_id**
> CertView get_ocsp_certificate_by_id(id)

Get an OCSP responder signature verification certificate by ID.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CertificatesrevocationApi()
id = 'id_example' # str | Certificate ID.

try:
    # Get an OCSP responder signature verification certificate by ID.
    api_response = api_instance.get_ocsp_certificate_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CertificatesrevocationApi->get_ocsp_certificate_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Certificate ID. | 

### Return type

[**CertView**](CertView.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ocsp_certificates**
> CertViews get_ocsp_certificates()

Get the list of available OCSP responder signature verification certificates.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CertificatesrevocationApi()

try:
    # Get the list of available OCSP responder signature verification certificates.
    api_response = api_instance.get_ocsp_certificates()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CertificatesrevocationApi->get_ocsp_certificates: %s\n" % e)
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

# **get_revocation_settings**
> CertificateRevocationSettings get_revocation_settings()

Get certificate revocation settings.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CertificatesrevocationApi()

try:
    # Get certificate revocation settings.
    api_response = api_instance.get_revocation_settings()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CertificatesrevocationApi->get_revocation_settings: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**CertificateRevocationSettings**](CertificateRevocationSettings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_ocsp_certificate**
> CertView import_ocsp_certificate(body)

Import an OCSP responder signature verification certificate.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CertificatesrevocationApi()
body = swagger_client.X509File() # X509File | File to import.

try:
    # Import an OCSP responder signature verification certificate.
    api_response = api_instance.import_ocsp_certificate(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CertificatesrevocationApi->import_ocsp_certificate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**X509File**](X509File.md)| File to import. | 

### Return type

[**CertView**](CertView.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_revocation_settings**
> CertificateRevocationSettings update_revocation_settings(body)

Update certificate revocation settings.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CertificatesrevocationApi()
body = swagger_client.CertificateRevocationSettings() # CertificateRevocationSettings | Certificate revocation settings.

try:
    # Update certificate revocation settings.
    api_response = api_instance.update_revocation_settings(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CertificatesrevocationApi->update_revocation_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CertificateRevocationSettings**](CertificateRevocationSettings.md)| Certificate revocation settings. | 

### Return type

[**CertificateRevocationSettings**](CertificateRevocationSettings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

