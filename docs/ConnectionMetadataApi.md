# swagger_client.ConnectionMetadataApi

All URIs are relative to *https://localhost:9999/pf-admin-api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**convert**](ConnectionMetadataApi.md#convert) | **POST** /connectionMetadata/convert | Convert a partner&#39;s SAML metadata into a JSON representation.
[**export**](ConnectionMetadataApi.md#export) | **POST** /connectionMetadata/export | Export a connection&#39;s SAML metadata that can be given to a partner.


# **convert**
> ConvertMetadataResponse convert(body)

Convert a partner's SAML metadata into a JSON representation.

Convert a partner's SAML metadata into an API JSON representation that can be later saved using one of the connection creation endpoints. The metadata can also be overlaid on top of a specified template connection. The convert operation also returns the authenticity of the metadata based on its certificate. If a certificate isn't embedded in the metadata, one can be provided. Bindings and profiles are only enabled in the resulting connection if the partner metadata provides related endpoints. In several scenarios, additional connection configuration details (such as backchannel authentication) may be required in the connection.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConnectionMetadataApi()
body = swagger_client.ConvertMetadataRequest() # ConvertMetadataRequest | Convert metadata request.

try:
    # Convert a partner's SAML metadata into a JSON representation.
    api_response = api_instance.convert(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConnectionMetadataApi->convert: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ConvertMetadataRequest**](ConvertMetadataRequest.md)| Convert metadata request. | 

### Return type

[**ConvertMetadataResponse**](ConvertMetadataResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export**
> str export(body)

Export a connection's SAML metadata that can be given to a partner.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConnectionMetadataApi()
body = swagger_client.ExportMetadataRequest() # ExportMetadataRequest | Export metadata request.

try:
    # Export a connection's SAML metadata that can be given to a partner.
    api_response = api_instance.export(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConnectionMetadataApi->export: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ExportMetadataRequest**](ExportMetadataRequest.md)| Export metadata request. | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

