# swagger_client.IdpdefaultUrlsApi

All URIs are relative to *https://localhost:9999/pf-admin-api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_default_url**](IdpdefaultUrlsApi.md#get_default_url) | **GET** /idp/defaultUrls | Gets the IDP Default URL settings.
[**update_default_url_settings**](IdpdefaultUrlsApi.md#update_default_url_settings) | **PUT** /idp/defaultUrls | Update the IDP Default URL settings.


# **get_default_url**
> IdpDefaultUrl get_default_url()

Gets the IDP Default URL settings.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IdpdefaultUrlsApi()

try:
    # Gets the IDP Default URL settings.
    api_response = api_instance.get_default_url()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IdpdefaultUrlsApi->get_default_url: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**IdpDefaultUrl**](IdpDefaultUrl.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_default_url_settings**
> IdpDefaultUrl update_default_url_settings(body)

Update the IDP Default URL settings.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IdpdefaultUrlsApi()
body = swagger_client.IdpDefaultUrl() # IdpDefaultUrl | Configuration for the IdP Default URL settings.

try:
    # Update the IDP Default URL settings.
    api_response = api_instance.update_default_url_settings(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IdpdefaultUrlsApi->update_default_url_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**IdpDefaultUrl**](IdpDefaultUrl.md)| Configuration for the IdP Default URL settings. | 

### Return type

[**IdpDefaultUrl**](IdpDefaultUrl.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

