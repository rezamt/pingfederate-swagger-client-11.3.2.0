# swagger_client.ConfigStoreApi

All URIs are relative to *https://localhost:9999/pf-admin-api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_setting**](ConfigStoreApi.md#delete_setting) | **DELETE** /configStore/{bundle}/{id} | Delete a setting.
[**get_setting**](ConfigStoreApi.md#get_setting) | **GET** /configStore/{bundle}/{id} | Get a single setting from a bundle.
[**get_settings**](ConfigStoreApi.md#get_settings) | **GET** /configStore/{bundle} | Get all settings from a bundle.
[**update_setting**](ConfigStoreApi.md#update_setting) | **PUT** /configStore/{bundle}/{id} | Create or update a setting/bundle.


# **delete_setting**
> delete_setting(bundle, id)

Delete a setting.

Delete a setting. This is an advanced operation with minimal validation. Incorrect use of this operation can harm the integrity of your PingFederate configuration. Please ensure you have specified the correct bundle name and setting ID before invoking this operation.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConfigStoreApi()
bundle = 'bundle_example' # str | This field represents a configuration file that contains a bundle of settings.
id = 'id_example' # str | ID of setting to delete.

try:
    # Delete a setting.
    api_instance.delete_setting(bundle, id)
except ApiException as e:
    print("Exception when calling ConfigStoreApi->delete_setting: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bundle** | **str**| This field represents a configuration file that contains a bundle of settings. | 
 **id** | **str**| ID of setting to delete. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_setting**
> ConfigStoreSetting get_setting(bundle, id)

Get a single setting from a bundle.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConfigStoreApi()
bundle = 'bundle_example' # str | This field represents a configuration file that contains a bundle of settings.
id = 'id_example' # str | ID of setting to retrieve.

try:
    # Get a single setting from a bundle.
    api_response = api_instance.get_setting(bundle, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigStoreApi->get_setting: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bundle** | **str**| This field represents a configuration file that contains a bundle of settings. | 
 **id** | **str**| ID of setting to retrieve. | 

### Return type

[**ConfigStoreSetting**](ConfigStoreSetting.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_settings**
> ConfigStoreBundle get_settings(bundle)

Get all settings from a bundle.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConfigStoreApi()
bundle = 'bundle_example' # str | This field represents a configuration file that contains a bundle of settings.

try:
    # Get all settings from a bundle.
    api_response = api_instance.get_settings(bundle)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigStoreApi->get_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bundle** | **str**| This field represents a configuration file that contains a bundle of settings. | 

### Return type

[**ConfigStoreBundle**](ConfigStoreBundle.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_setting**
> ConfigStoreSetting update_setting(bundle, id, body)

Create or update a setting/bundle.

Create or update a setting/bundle. This is an advanced operation with minimal validation. Incorrect use of this operation can harm the integrity of your PingFederate configuration. Please ensure you have specified the correct bundle name, setting ID, and setting value before invoking this operation.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConfigStoreApi()
bundle = 'bundle_example' # str | This field represents a configuration file that contains a bundle of settings.
id = 'id_example' # str | ID of setting to create/update.
body = swagger_client.ConfigStoreSetting() # ConfigStoreSetting | Configuration setting.

try:
    # Create or update a setting/bundle.
    api_response = api_instance.update_setting(bundle, id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigStoreApi->update_setting: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bundle** | **str**| This field represents a configuration file that contains a bundle of settings. | 
 **id** | **str**| ID of setting to create/update. | 
 **body** | [**ConfigStoreSetting**](ConfigStoreSetting.md)| Configuration setting. | 

### Return type

[**ConfigStoreSetting**](ConfigStoreSetting.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

