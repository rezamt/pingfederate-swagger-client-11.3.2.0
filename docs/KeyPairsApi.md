# swagger_client.KeyPairsApi

All URIs are relative to *https://localhost:9999/pf-admin-api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_key_algorithms**](KeyPairsApi.md#get_key_algorithms) | **GET** /keyPairs/keyAlgorithms | Get list of the key algorithms supported for key pair generation.


# **get_key_algorithms**
> KeyAlgorithms get_key_algorithms()

Get list of the key algorithms supported for key pair generation.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.KeyPairsApi()

try:
    # Get list of the key algorithms supported for key pair generation.
    api_response = api_instance.get_key_algorithms()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KeyPairsApi->get_key_algorithms: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**KeyAlgorithms**](KeyAlgorithms.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

