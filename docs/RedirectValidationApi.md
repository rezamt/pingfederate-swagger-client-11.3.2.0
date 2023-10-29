# swagger_client.RedirectValidationApi

All URIs are relative to *https://localhost:9999/pf-admin-api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_redirect_validation_settings**](RedirectValidationApi.md#get_redirect_validation_settings) | **GET** /redirectValidation | Retrieve redirect validation settings.
[**update_redirect_validation_settings**](RedirectValidationApi.md#update_redirect_validation_settings) | **PUT** /redirectValidation | Update redirect validation settings.


# **get_redirect_validation_settings**
> RedirectValidationSettings get_redirect_validation_settings()

Retrieve redirect validation settings.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RedirectValidationApi()

try:
    # Retrieve redirect validation settings.
    api_response = api_instance.get_redirect_validation_settings()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RedirectValidationApi->get_redirect_validation_settings: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**RedirectValidationSettings**](RedirectValidationSettings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_redirect_validation_settings**
> RedirectValidationSettings update_redirect_validation_settings(body)

Update redirect validation settings.

<b>Note: </b>Ensure IdP Discovery and/or WS-Federation is enabled for redirect validation to function for IdP Discovery and/or wreply for SLO respectively.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RedirectValidationApi()
body = swagger_client.RedirectValidationSettings() # RedirectValidationSettings | Redirect validation settings.

try:
    # Update redirect validation settings.
    api_response = api_instance.update_redirect_validation_settings(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RedirectValidationApi->update_redirect_validation_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RedirectValidationSettings**](RedirectValidationSettings.md)| Redirect validation settings. | 

### Return type

[**RedirectValidationSettings**](RedirectValidationSettings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

