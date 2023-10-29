# swagger_client.PingOneForEnterpriseApi

All URIs are relative to *https://localhost:9999/pf-admin-api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**disconnect**](PingOneForEnterpriseApi.md#disconnect) | **POST** /pingOneForEnterprise/disconnect | Disconnect from PingOne for Enterprise
[**get_key_pairs**](PingOneForEnterpriseApi.md#get_key_pairs) | **GET** /pingOneForEnterprise/keyPairs | Get the PingOne for Enterprise key pair settings
[**get_ping_one_for_enterprise_settings**](PingOneForEnterpriseApi.md#get_ping_one_for_enterprise_settings) | **GET** /pingOneForEnterprise | Get the PingOne for Enterprise settings
[**rotate_keys**](PingOneForEnterpriseApi.md#rotate_keys) | **POST** /pingOneForEnterprise/keyPairs/rotate | Rotate the authentication key
[**update_ping_one_for_enterprise_identity_repository**](PingOneForEnterpriseApi.md#update_ping_one_for_enterprise_identity_repository) | **POST** /pingOneForEnterprise/updateIdentityRepository | Update the PingOne Identity Repository
[**update_ping_one_settings**](PingOneForEnterpriseApi.md#update_ping_one_settings) | **PUT** /pingOneForEnterprise | Update the PingOne for Enterprise settings.


# **disconnect**
> PingOneForEnterpriseSettings disconnect()

Disconnect from PingOne for Enterprise



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PingOneForEnterpriseApi()

try:
    # Disconnect from PingOne for Enterprise
    api_response = api_instance.disconnect()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PingOneForEnterpriseApi->disconnect: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**PingOneForEnterpriseSettings**](PingOneForEnterpriseSettings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_key_pairs**
> P14EKeysView get_key_pairs()

Get the PingOne for Enterprise key pair settings



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PingOneForEnterpriseApi()

try:
    # Get the PingOne for Enterprise key pair settings
    api_response = api_instance.get_key_pairs()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PingOneForEnterpriseApi->get_key_pairs: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**P14EKeysView**](P14EKeysView.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ping_one_for_enterprise_settings**
> PingOneForEnterpriseSettings get_ping_one_for_enterprise_settings()

Get the PingOne for Enterprise settings



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PingOneForEnterpriseApi()

try:
    # Get the PingOne for Enterprise settings
    api_response = api_instance.get_ping_one_for_enterprise_settings()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PingOneForEnterpriseApi->get_ping_one_for_enterprise_settings: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**PingOneForEnterpriseSettings**](PingOneForEnterpriseSettings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rotate_keys**
> P14EKeysView rotate_keys()

Rotate the authentication key



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PingOneForEnterpriseApi()

try:
    # Rotate the authentication key
    api_response = api_instance.rotate_keys()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PingOneForEnterpriseApi->rotate_keys: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**P14EKeysView**](P14EKeysView.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_ping_one_for_enterprise_identity_repository**
> PingOneForEnterpriseSettings update_ping_one_for_enterprise_identity_repository()

Update the PingOne Identity Repository

Update the identity repository to keep your PingFederate and PingOne for Enterprise settings synchronized.<br>CAUTION: Updating the identity repository overwrites the existing PingOne for Enterprise identity repository, causing users to be directed to the current PingFederate instance for SSO.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PingOneForEnterpriseApi()

try:
    # Update the PingOne Identity Repository
    api_response = api_instance.update_ping_one_for_enterprise_identity_repository()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PingOneForEnterpriseApi->update_ping_one_for_enterprise_identity_repository: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**PingOneForEnterpriseSettings**](PingOneForEnterpriseSettings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_ping_one_settings**
> PingOneForEnterpriseSettings update_ping_one_settings(body)

Update the PingOne for Enterprise settings.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PingOneForEnterpriseApi()
body = swagger_client.PingOneForEnterpriseSettings() # PingOneForEnterpriseSettings | PingOne for Enterprise connection settings

try:
    # Update the PingOne for Enterprise settings.
    api_response = api_instance.update_ping_one_settings(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PingOneForEnterpriseApi->update_ping_one_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PingOneForEnterpriseSettings**](PingOneForEnterpriseSettings.md)| PingOne for Enterprise connection settings | 

### Return type

[**PingOneForEnterpriseSettings**](PingOneForEnterpriseSettings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

