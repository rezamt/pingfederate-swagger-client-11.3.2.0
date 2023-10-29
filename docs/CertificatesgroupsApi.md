# swagger_client.CertificatesgroupsApi

All URIs are relative to *https://localhost:9999/pf-admin-api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_certificate_from_group**](CertificatesgroupsApi.md#delete_certificate_from_group) | **DELETE** /certificates/groups/{groupName}/{id} | Delete a certificate from a group.
[**get_certificate_from_group**](CertificatesgroupsApi.md#get_certificate_from_group) | **GET** /certificates/groups/{groupName}/{id} | Retrieve details of a certificate.
[**get_certificates_for_group**](CertificatesgroupsApi.md#get_certificates_for_group) | **GET** /certificates/groups/{groupName} | Get list of all certificates for a group.
[**import_feature_cert**](CertificatesgroupsApi.md#import_feature_cert) | **POST** /certificates/groups/{groupName}/import | Import a new certificate to a group.


# **delete_certificate_from_group**
> delete_certificate_from_group(group_name, id)

Delete a certificate from a group.

If the request is successful, the response body is empty. If the request fails, an ApiResult is returned with details of the error.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CertificatesgroupsApi()
group_name = 'group_name_example' # str | Name of the group to retrieve certificates for.
id = 'id_example' # str | ID of the certificate to retrieve.

try:
    # Delete a certificate from a group.
    api_instance.delete_certificate_from_group(group_name, id)
except ApiException as e:
    print("Exception when calling CertificatesgroupsApi->delete_certificate_from_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_name** | **str**| Name of the group to retrieve certificates for. | 
 **id** | **str**| ID of the certificate to retrieve. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_certificate_from_group**
> CertView get_certificate_from_group(group_name, id)

Retrieve details of a certificate.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CertificatesgroupsApi()
group_name = 'group_name_example' # str | Name of the group to retrieve certificates for.
id = 'id_example' # str | ID of the certificate to retrieve.

try:
    # Retrieve details of a certificate.
    api_response = api_instance.get_certificate_from_group(group_name, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CertificatesgroupsApi->get_certificate_from_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_name** | **str**| Name of the group to retrieve certificates for. | 
 **id** | **str**| ID of the certificate to retrieve. | 

### Return type

[**CertView**](CertView.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_certificates_for_group**
> CertViews get_certificates_for_group(group_name)

Get list of all certificates for a group.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CertificatesgroupsApi()
group_name = 'group_name_example' # str | Name of the group to retrieve certificates for.

try:
    # Get list of all certificates for a group.
    api_response = api_instance.get_certificates_for_group(group_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CertificatesgroupsApi->get_certificates_for_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_name** | **str**| Name of the group to retrieve certificates for. | 

### Return type

[**CertViews**](CertViews.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_feature_cert**
> CertView import_feature_cert(group_name, body)

Import a new certificate to a group.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CertificatesgroupsApi()
group_name = 'group_name_example' # str | Name of the group to retrieve certificates for.
body = swagger_client.X509File() # X509File | File data to import.

try:
    # Import a new certificate to a group.
    api_response = api_instance.import_feature_cert(group_name, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CertificatesgroupsApi->import_feature_cert: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_name** | **str**| Name of the group to retrieve certificates for. | 
 **body** | [**X509File**](X509File.md)| File data to import. | 

### Return type

[**CertView**](CertView.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

