# swagger_client.ProtocolMetadataApi

All URIs are relative to *https://localhost:9999/pf-admin-api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_lifetime_settings**](ProtocolMetadataApi.md#get_lifetime_settings) | **GET** /protocolMetadata/lifetimeSettings | Get metadata cache duration and reload delay for automated reloading.
[**get_signing_settings**](ProtocolMetadataApi.md#get_signing_settings) | **GET** /protocolMetadata/signingSettings | Get the certificate ID and algorithm used for metadata signing.
[**update_lifetime_settings**](ProtocolMetadataApi.md#update_lifetime_settings) | **PUT** /protocolMetadata/lifetimeSettings | Update metadata cache duration and reload delay for automated reloading.
[**update_signing_settings**](ProtocolMetadataApi.md#update_signing_settings) | **PUT** /protocolMetadata/signingSettings | Update the certificate and algorithm for metadata signing.


# **get_lifetime_settings**
> MetadataLifetimeSettings get_lifetime_settings()

Get metadata cache duration and reload delay for automated reloading.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProtocolMetadataApi()

try:
    # Get metadata cache duration and reload delay for automated reloading.
    api_response = api_instance.get_lifetime_settings()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProtocolMetadataApi->get_lifetime_settings: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**MetadataLifetimeSettings**](MetadataLifetimeSettings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_signing_settings**
> MetadataSigningSettings get_signing_settings()

Get the certificate ID and algorithm used for metadata signing.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProtocolMetadataApi()

try:
    # Get the certificate ID and algorithm used for metadata signing.
    api_response = api_instance.get_signing_settings()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProtocolMetadataApi->get_signing_settings: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**MetadataSigningSettings**](MetadataSigningSettings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_lifetime_settings**
> MetadataLifetimeSettings update_lifetime_settings(body)

Update metadata cache duration and reload delay for automated reloading.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProtocolMetadataApi()
body = swagger_client.MetadataLifetimeSettings() # MetadataLifetimeSettings | Metadata lifetime settings.

try:
    # Update metadata cache duration and reload delay for automated reloading.
    api_response = api_instance.update_lifetime_settings(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProtocolMetadataApi->update_lifetime_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MetadataLifetimeSettings**](MetadataLifetimeSettings.md)| Metadata lifetime settings. | 

### Return type

[**MetadataLifetimeSettings**](MetadataLifetimeSettings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_signing_settings**
> MetadataSigningSettings update_signing_settings(body=body)

Update the certificate and algorithm for metadata signing.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProtocolMetadataApi()
body = swagger_client.MetadataSigningSettings() # MetadataSigningSettings |  (optional)

try:
    # Update the certificate and algorithm for metadata signing.
    api_response = api_instance.update_signing_settings(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProtocolMetadataApi->update_signing_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MetadataSigningSettings**](MetadataSigningSettings.md)|  | [optional] 

### Return type

[**MetadataSigningSettings**](MetadataSigningSettings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

