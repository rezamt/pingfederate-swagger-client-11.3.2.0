# swagger_client.BulkApi

All URIs are relative to *https://localhost:9999/pf-admin-api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**export_configuration**](BulkApi.md#export_configuration) | **GET** /bulk/export | Export all API resources to a JSON file.
[**import_configuration**](BulkApi.md#import_configuration) | **POST** /bulk/import | Import configuration for a PingFederate deployment from a JSON file.


# **export_configuration**
> BulkConfig export_configuration(include_external_resources=include_external_resources)

Export all API resources to a JSON file.

For the /configStore resource type, only the settings that are different from the defaults for this version of PingFederate are included in the export.<br><br>Only resource types currently supported by the Administrative API are included in the exported data. Resources not yet supported include:<br><br>- SMS Provider Settings<br>

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BulkApi()
include_external_resources = false # bool | Include external resources like OAuth clients stored outside of PingFederate. (optional) (default to false)

try:
    # Export all API resources to a JSON file.
    api_response = api_instance.export_configuration(include_external_resources=include_external_resources)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BulkApi->export_configuration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **include_external_resources** | **bool**| Include external resources like OAuth clients stored outside of PingFederate. | [optional] [default to false]

### Return type

[**BulkConfig**](BulkConfig.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_configuration**
> import_configuration(body, fail_fast=fail_fast, x_bypass_external_validation=x_bypass_external_validation)

Import configuration for a PingFederate deployment from a JSON file.

All existing configuration will be wiped before the import begins. If any validation errors are found, PingFederate will roll back to the previous configuration. The master key set in pf.jwk must include the key in use when the JSON configuration was originally exported.  JSON configurations exported from earlier versions of PingFederate can be imported. However, this is not a supported way of upgrading from an earlier version. Instead, you should run the upgrade utility and then reexport to get an updated configuration JSON.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BulkApi()
body = swagger_client.BulkConfig() # BulkConfig | Configuration to import.
fail_fast = true # bool | When set to true, stops the import as soon as any validation errors are encountered. When false, import will continue to validate configuration after the first failure to identify all validation errors. If any validation errors are present PingFederate will roll back to the state prior to the import attempt. (optional) (default to true)
x_bypass_external_validation = false # bool | External validation will be bypassed when set to true. Default to false. (optional) (default to false)

try:
    # Import configuration for a PingFederate deployment from a JSON file.
    api_instance.import_configuration(body, fail_fast=fail_fast, x_bypass_external_validation=x_bypass_external_validation)
except ApiException as e:
    print("Exception when calling BulkApi->import_configuration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BulkConfig**](BulkConfig.md)| Configuration to import. | 
 **fail_fast** | **bool**| When set to true, stops the import as soon as any validation errors are encountered. When false, import will continue to validate configuration after the first failure to identify all validation errors. If any validation errors are present PingFederate will roll back to the state prior to the import attempt. | [optional] [default to true]
 **x_bypass_external_validation** | **bool**| External validation will be bypassed when set to true. Default to false. | [optional] [default to false]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

