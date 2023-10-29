# swagger_client.SpdefaultUrlsApi

All URIs are relative to *https://localhost:9999/pf-admin-api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_default_urls**](SpdefaultUrlsApi.md#get_default_urls) | **GET** /sp/defaultUrls | Gets the SP Default URLs. These are Values that affect the user&#39;s experience when executing SP-initiated SSO operations.
[**update_default_urls**](SpdefaultUrlsApi.md#update_default_urls) | **PUT** /sp/defaultUrls | Update the SP Default URLs. Enter values that affect the user&#39;s experience when executing SP-initiated SSO operations.


# **get_default_urls**
> SpDefaultUrls get_default_urls()

Gets the SP Default URLs. These are Values that affect the user's experience when executing SP-initiated SSO operations.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SpdefaultUrlsApi()

try:
    # Gets the SP Default URLs. These are Values that affect the user's experience when executing SP-initiated SSO operations.
    api_response = api_instance.get_default_urls()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpdefaultUrlsApi->get_default_urls: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SpDefaultUrls**](SpDefaultUrls.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_default_urls**
> SpDefaultUrls update_default_urls(body)

Update the SP Default URLs. Enter values that affect the user's experience when executing SP-initiated SSO operations.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SpdefaultUrlsApi()
body = swagger_client.SpDefaultUrls() # SpDefaultUrls | Configuration for the IDP Default URL settings.

try:
    # Update the SP Default URLs. Enter values that affect the user's experience when executing SP-initiated SSO operations.
    api_response = api_instance.update_default_urls(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpdefaultUrlsApi->update_default_urls: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SpDefaultUrls**](SpDefaultUrls.md)| Configuration for the IDP Default URL settings. | 

### Return type

[**SpDefaultUrls**](SpDefaultUrls.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

