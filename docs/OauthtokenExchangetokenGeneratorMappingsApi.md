# swagger_client.OauthtokenExchangetokenGeneratorMappingsApi

All URIs are relative to *https://localhost:9999/pf-admin-api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_token_generator_mapping**](OauthtokenExchangetokenGeneratorMappingsApi.md#create_token_generator_mapping) | **POST** /oauth/tokenExchange/tokenGeneratorMappings | Create a new Token Exchange Processor policy to Token Generator Mapping.
[**delete_token_generator_mapping_by_id**](OauthtokenExchangetokenGeneratorMappingsApi.md#delete_token_generator_mapping_by_id) | **DELETE** /oauth/tokenExchange/tokenGeneratorMappings/{id} | Delete a Token Exchange Processor policy to Token Generator Mapping.
[**get_token_generator_mapping_by_id**](OauthtokenExchangetokenGeneratorMappingsApi.md#get_token_generator_mapping_by_id) | **GET** /oauth/tokenExchange/tokenGeneratorMappings/{id} | Get a Token Exchange Processor policy to Token Generator Mapping.
[**get_token_generator_mappings**](OauthtokenExchangetokenGeneratorMappingsApi.md#get_token_generator_mappings) | **GET** /oauth/tokenExchange/tokenGeneratorMappings | Get the list of Token Exchange Processor policy to Token Generator Mappings.
[**update_token_generator_mapping_by_id**](OauthtokenExchangetokenGeneratorMappingsApi.md#update_token_generator_mapping_by_id) | **PUT** /oauth/tokenExchange/tokenGeneratorMappings/{id} | Update a Token Exchange Processor policy to Token Generator Mapping.


# **create_token_generator_mapping**
> ProcessorPolicyToGeneratorMapping create_token_generator_mapping(body, x_bypass_external_validation=x_bypass_external_validation)

Create a new Token Exchange Processor policy to Token Generator Mapping.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OauthtokenExchangetokenGeneratorMappingsApi()
body = swagger_client.ProcessorPolicyToGeneratorMapping() # ProcessorPolicyToGeneratorMapping | Configuration for a new Token Exchange Processor policy to Token Generator Mapping.
x_bypass_external_validation = false # bool | External validation will be bypassed when set to true. Default to false. (optional) (default to false)

try:
    # Create a new Token Exchange Processor policy to Token Generator Mapping.
    api_response = api_instance.create_token_generator_mapping(body, x_bypass_external_validation=x_bypass_external_validation)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OauthtokenExchangetokenGeneratorMappingsApi->create_token_generator_mapping: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProcessorPolicyToGeneratorMapping**](ProcessorPolicyToGeneratorMapping.md)| Configuration for a new Token Exchange Processor policy to Token Generator Mapping. | 
 **x_bypass_external_validation** | **bool**| External validation will be bypassed when set to true. Default to false. | [optional] [default to false]

### Return type

[**ProcessorPolicyToGeneratorMapping**](ProcessorPolicyToGeneratorMapping.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_token_generator_mapping_by_id**
> delete_token_generator_mapping_by_id(id)

Delete a Token Exchange Processor policy to Token Generator Mapping.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OauthtokenExchangetokenGeneratorMappingsApi()
id = 'id_example' # str | ID of Token Exchange Processor policy to Token Generator Mapping to delete.

try:
    # Delete a Token Exchange Processor policy to Token Generator Mapping.
    api_instance.delete_token_generator_mapping_by_id(id)
except ApiException as e:
    print("Exception when calling OauthtokenExchangetokenGeneratorMappingsApi->delete_token_generator_mapping_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of Token Exchange Processor policy to Token Generator Mapping to delete. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_token_generator_mapping_by_id**
> ProcessorPolicyToGeneratorMapping get_token_generator_mapping_by_id(id)

Get a Token Exchange Processor policy to Token Generator Mapping.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OauthtokenExchangetokenGeneratorMappingsApi()
id = 'id_example' # str | ID of Token Exchange Processor policy to Token Generator Mapping to fetch.

try:
    # Get a Token Exchange Processor policy to Token Generator Mapping.
    api_response = api_instance.get_token_generator_mapping_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OauthtokenExchangetokenGeneratorMappingsApi->get_token_generator_mapping_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of Token Exchange Processor policy to Token Generator Mapping to fetch. | 

### Return type

[**ProcessorPolicyToGeneratorMapping**](ProcessorPolicyToGeneratorMapping.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_token_generator_mappings**
> ProcessorPolicyToGeneratorMappings get_token_generator_mappings()

Get the list of Token Exchange Processor policy to Token Generator Mappings.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OauthtokenExchangetokenGeneratorMappingsApi()

try:
    # Get the list of Token Exchange Processor policy to Token Generator Mappings.
    api_response = api_instance.get_token_generator_mappings()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OauthtokenExchangetokenGeneratorMappingsApi->get_token_generator_mappings: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ProcessorPolicyToGeneratorMappings**](ProcessorPolicyToGeneratorMappings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_token_generator_mapping_by_id**
> ProcessorPolicyToGeneratorMapping update_token_generator_mapping_by_id(id, body, x_bypass_external_validation=x_bypass_external_validation)

Update a Token Exchange Processor policy to Token Generator Mapping.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OauthtokenExchangetokenGeneratorMappingsApi()
id = 'id_example' # str | ID of Token Exchange Processor policy to Token Generator Mapping to update.
body = swagger_client.ProcessorPolicyToGeneratorMapping() # ProcessorPolicyToGeneratorMapping | Configuration for updated Token Exchange Processor policy to Token Generator Mapping.
x_bypass_external_validation = false # bool | External validation will be bypassed when set to true. Default to false. (optional) (default to false)

try:
    # Update a Token Exchange Processor policy to Token Generator Mapping.
    api_response = api_instance.update_token_generator_mapping_by_id(id, body, x_bypass_external_validation=x_bypass_external_validation)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OauthtokenExchangetokenGeneratorMappingsApi->update_token_generator_mapping_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of Token Exchange Processor policy to Token Generator Mapping to update. | 
 **body** | [**ProcessorPolicyToGeneratorMapping**](ProcessorPolicyToGeneratorMapping.md)| Configuration for updated Token Exchange Processor policy to Token Generator Mapping. | 
 **x_bypass_external_validation** | **bool**| External validation will be bypassed when set to true. Default to false. | [optional] [default to false]

### Return type

[**ProcessorPolicyToGeneratorMapping**](ProcessorPolicyToGeneratorMapping.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

