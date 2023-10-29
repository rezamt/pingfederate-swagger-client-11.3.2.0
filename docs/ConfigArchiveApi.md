# swagger_client.ConfigArchiveApi

All URIs are relative to *https://localhost:9999/pf-admin-api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**export_config_archive**](ConfigArchiveApi.md#export_config_archive) | **GET** /configArchive/export | Export a configuration archive.
[**import_config_archive**](ConfigArchiveApi.md#import_config_archive) | **POST** /configArchive/import | Import a configuration archive.


# **export_config_archive**
> export_config_archive()

Export a configuration archive.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConfigArchiveApi()

try:
    # Export a configuration archive.
    api_instance.export_config_archive()
except ApiException as e:
    print("Exception when calling ConfigArchiveApi->export_config_archive: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/zip

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_config_archive**
> ApiResult import_config_archive(file=file, force_import=force_import, force_unsupported_import=force_unsupported_import, reencrypt_data=reencrypt_data)

Import a configuration archive.

If there are missing components or license inconsistencies, the import is halted by default to allow you to install the necessary components or license. However, you can choose to force the deployment by setting 'forceImport' to true and then install the necessary files later.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConfigArchiveApi()
file = '/path/to/file.txt' # file |  (optional)
force_import = true # bool |  (optional)
force_unsupported_import = false # bool | Force import of unsupported versions. (optional) (default to false)
reencrypt_data = false # bool | Reencrypt configuration archive data with the current deployment's encryption key. (optional) (default to false)

try:
    # Import a configuration archive.
    api_response = api_instance.import_config_archive(file=file, force_import=force_import, force_unsupported_import=force_unsupported_import, reencrypt_data=reencrypt_data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigArchiveApi->import_config_archive: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **file**|  | [optional] 
 **force_import** | **bool**|  | [optional] 
 **force_unsupported_import** | **bool**| Force import of unsupported versions. | [optional] [default to false]
 **reencrypt_data** | **bool**| Reencrypt configuration archive data with the current deployment&#39;s encryption key. | [optional] [default to false]

### Return type

[**ApiResult**](ApiResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

