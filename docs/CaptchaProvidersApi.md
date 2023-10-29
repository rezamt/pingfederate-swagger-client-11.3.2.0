# swagger_client.CaptchaProvidersApi

All URIs are relative to *https://localhost:9999/pf-admin-api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_captcha_provider**](CaptchaProvidersApi.md#create_captcha_provider) | **POST** /captchaProviders | Create a CAPTCHA provider plugin instance.
[**delete_captcha_provider**](CaptchaProvidersApi.md#delete_captcha_provider) | **DELETE** /captchaProviders/{id} | Delete a CAPTCHA provider plugin instance.
[**get_captcha_provider**](CaptchaProvidersApi.md#get_captcha_provider) | **GET** /captchaProviders/{id} | Get a specific CAPTCHA provider plugin instance.
[**get_captcha_provider_plugin_descriptor**](CaptchaProvidersApi.md#get_captcha_provider_plugin_descriptor) | **GET** /captchaProviders/descriptors/{id} | Get a CAPTCHA provider plugin descriptor.
[**get_captcha_provider_plugin_descriptors**](CaptchaProvidersApi.md#get_captcha_provider_plugin_descriptors) | **GET** /captchaProviders/descriptors | Get a list of available CAPTCHA provider plugin descriptors.
[**get_captcha_providers**](CaptchaProvidersApi.md#get_captcha_providers) | **GET** /captchaProviders | Get a list of CAPTCHA provider plugin instances.
[**get_settings**](CaptchaProvidersApi.md#get_settings) | **GET** /captchaProviders/settings | Get general CAPTCHA providers settings.
[**update_captcha_provider**](CaptchaProvidersApi.md#update_captcha_provider) | **PUT** /captchaProviders/{id} | Update a CAPTCHA provider plugin instance.
[**update_settings**](CaptchaProvidersApi.md#update_settings) | **PUT** /captchaProviders/settings | Update general CAPTCHA providers settings.


# **create_captcha_provider**
> CaptchaProvider create_captcha_provider(body)

Create a CAPTCHA provider plugin instance.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CaptchaProvidersApi()
body = swagger_client.CaptchaProvider() # CaptchaProvider | Configuration for a CAPTCHA provider plugin instance.

try:
    # Create a CAPTCHA provider plugin instance.
    api_response = api_instance.create_captcha_provider(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CaptchaProvidersApi->create_captcha_provider: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CaptchaProvider**](CaptchaProvider.md)| Configuration for a CAPTCHA provider plugin instance. | 

### Return type

[**CaptchaProvider**](CaptchaProvider.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_captcha_provider**
> delete_captcha_provider(id)

Delete a CAPTCHA provider plugin instance.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CaptchaProvidersApi()
id = 'id_example' # str | ID of a CAPTCHA provider plugin instance.

try:
    # Delete a CAPTCHA provider plugin instance.
    api_instance.delete_captcha_provider(id)
except ApiException as e:
    print("Exception when calling CaptchaProvidersApi->delete_captcha_provider: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of a CAPTCHA provider plugin instance. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_captcha_provider**
> CaptchaProvider get_captcha_provider(id)

Get a specific CAPTCHA provider plugin instance.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CaptchaProvidersApi()
id = 'id_example' # str | ID of a CAPTCHA provider plugin instance.

try:
    # Get a specific CAPTCHA provider plugin instance.
    api_response = api_instance.get_captcha_provider(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CaptchaProvidersApi->get_captcha_provider: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of a CAPTCHA provider plugin instance. | 

### Return type

[**CaptchaProvider**](CaptchaProvider.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_captcha_provider_plugin_descriptor**
> ACAPTCHAProviderPluginDescriptor_ get_captcha_provider_plugin_descriptor(id)

Get a CAPTCHA provider plugin descriptor.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CaptchaProvidersApi()
id = 'id_example' # str | ID of CAPTCHA provider plugin descriptor.

try:
    # Get a CAPTCHA provider plugin descriptor.
    api_response = api_instance.get_captcha_provider_plugin_descriptor(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CaptchaProvidersApi->get_captcha_provider_plugin_descriptor: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of CAPTCHA provider plugin descriptor. | 

### Return type

[**ACAPTCHAProviderPluginDescriptor_**](ACAPTCHAProviderPluginDescriptor_.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_captcha_provider_plugin_descriptors**
> ACollectionOfCAPTCHAProviderPluginDescriptors_ get_captcha_provider_plugin_descriptors()

Get a list of available CAPTCHA provider plugin descriptors.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CaptchaProvidersApi()

try:
    # Get a list of available CAPTCHA provider plugin descriptors.
    api_response = api_instance.get_captcha_provider_plugin_descriptors()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CaptchaProvidersApi->get_captcha_provider_plugin_descriptors: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ACollectionOfCAPTCHAProviderPluginDescriptors_**](ACollectionOfCAPTCHAProviderPluginDescriptors_.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_captcha_providers**
> CaptchaProviders get_captcha_providers()

Get a list of CAPTCHA provider plugin instances.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CaptchaProvidersApi()

try:
    # Get a list of CAPTCHA provider plugin instances.
    api_response = api_instance.get_captcha_providers()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CaptchaProvidersApi->get_captcha_providers: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**CaptchaProviders**](CaptchaProviders.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_settings**
> CaptchaProvidersSettings get_settings()

Get general CAPTCHA providers settings.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CaptchaProvidersApi()

try:
    # Get general CAPTCHA providers settings.
    api_response = api_instance.get_settings()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CaptchaProvidersApi->get_settings: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**CaptchaProvidersSettings**](CaptchaProvidersSettings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_captcha_provider**
> CaptchaProvider update_captcha_provider(id, body)

Update a CAPTCHA provider plugin instance.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CaptchaProvidersApi()
id = 'id_example' # str | ID of a CAPTCHA provider plugin instance.
body = swagger_client.CaptchaProvider() # CaptchaProvider | Configuration for a CAPTCHA provider plugin instance.

try:
    # Update a CAPTCHA provider plugin instance.
    api_response = api_instance.update_captcha_provider(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CaptchaProvidersApi->update_captcha_provider: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of a CAPTCHA provider plugin instance. | 
 **body** | [**CaptchaProvider**](CaptchaProvider.md)| Configuration for a CAPTCHA provider plugin instance. | 

### Return type

[**CaptchaProvider**](CaptchaProvider.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_settings**
> CaptchaProvidersSettings update_settings(body)

Update general CAPTCHA providers settings.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CaptchaProvidersApi()
body = swagger_client.CaptchaProvidersSettings() # CaptchaProvidersSettings | CAPTCHA providers settings.

try:
    # Update general CAPTCHA providers settings.
    api_response = api_instance.update_settings(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CaptchaProvidersApi->update_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CaptchaProvidersSettings**](CaptchaProvidersSettings.md)| CAPTCHA providers settings. | 

### Return type

[**CaptchaProvidersSettings**](CaptchaProvidersSettings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

