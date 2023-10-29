# swagger_client.ConfigurationEncryptionKeysApi

All URIs are relative to *https://localhost:9999/pf-admin-api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_configuration_encryption_keys**](ConfigurationEncryptionKeysApi.md#get_configuration_encryption_keys) | **GET** /configurationEncryptionKeys | Get the list of Configuration Encryption Keys.
[**rotate_configuration_encryption_key**](ConfigurationEncryptionKeysApi.md#rotate_configuration_encryption_key) | **POST** /configurationEncryptionKeys/rotate | Rotate the current Configuration Encryption Key.


# **get_configuration_encryption_keys**
> ConfigurationEncryptionKeys get_configuration_encryption_keys()

Get the list of Configuration Encryption Keys.

The first key in the list is the current key used for encryption and decryption. Other keys are used for decryption.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConfigurationEncryptionKeysApi()

try:
    # Get the list of Configuration Encryption Keys.
    api_response = api_instance.get_configuration_encryption_keys()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurationEncryptionKeysApi->get_configuration_encryption_keys: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ConfigurationEncryptionKeys**](ConfigurationEncryptionKeys.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rotate_configuration_encryption_key**
> ConfigurationEncryptionKeys rotate_configuration_encryption_key()

Rotate the current Configuration Encryption Key.

A new key will be generated and will be used for encryption and decryption. The previous encryption key will continue to be used for decryption.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConfigurationEncryptionKeysApi()

try:
    # Rotate the current Configuration Encryption Key.
    api_response = api_instance.rotate_configuration_encryption_key()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurationEncryptionKeysApi->rotate_configuration_encryption_key: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ConfigurationEncryptionKeys**](ConfigurationEncryptionKeys.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

