# swagger_client.LicenseApi

All URIs are relative to *https://localhost:9999/pf-admin-api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_license**](LicenseApi.md#get_license) | **GET** /license | Get a license summary.
[**get_license_agreement**](LicenseApi.md#get_license_agreement) | **GET** /license/agreement | Get license agreement link.
[**update_license**](LicenseApi.md#update_license) | **PUT** /license | Import a license.
[**update_license_agreement**](LicenseApi.md#update_license_agreement) | **PUT** /license/agreement | Accept license agreement.


# **get_license**
> LicenseView get_license()

Get a license summary.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LicenseApi()

try:
    # Get a license summary.
    api_response = api_instance.get_license()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LicenseApi->get_license: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**LicenseView**](LicenseView.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_license_agreement**
> LicenseAgreementInfo get_license_agreement()

Get license agreement link.

The license agreement has to be accepted before performing any other API calls.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LicenseApi()

try:
    # Get license agreement link.
    api_response = api_instance.get_license_agreement()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LicenseApi->get_license_agreement: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**LicenseAgreementInfo**](LicenseAgreementInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_license**
> LicenseView update_license(body)

Import a license.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LicenseApi()
body = swagger_client.LicenseFile() # LicenseFile | Base64 encoded value of a license.

try:
    # Import a license.
    api_response = api_instance.update_license(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LicenseApi->update_license: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LicenseFile**](LicenseFile.md)| Base64 encoded value of a license. | 

### Return type

[**LicenseView**](LicenseView.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_license_agreement**
> LicenseAgreementInfo update_license_agreement(body)

Accept license agreement.

The license agreement has to be accepted before performing any other API calls.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LicenseApi()
body = swagger_client.LicenseAgreementInfo() # LicenseAgreementInfo | License Agreement reference.

try:
    # Accept license agreement.
    api_response = api_instance.update_license_agreement(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LicenseApi->update_license_agreement: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LicenseAgreementInfo**](LicenseAgreementInfo.md)| License Agreement reference. | 

### Return type

[**LicenseAgreementInfo**](LicenseAgreementInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

