# swagger_client.IdpstsRequestParametersContractsApi

All URIs are relative to *https://localhost:9999/pf-admin-api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_sts_request_param_contract**](IdpstsRequestParametersContractsApi.md#create_sts_request_param_contract) | **POST** /idp/stsRequestParametersContracts | Create a new STS Request Parameters Contract.
[**delete_sts_request_param_contract_by_id**](IdpstsRequestParametersContractsApi.md#delete_sts_request_param_contract_by_id) | **DELETE** /idp/stsRequestParametersContracts/{id} | Delete a STS Request Parameters Contract.
[**get_sts_request_param_contract_by_id**](IdpstsRequestParametersContractsApi.md#get_sts_request_param_contract_by_id) | **GET** /idp/stsRequestParametersContracts/{id} | Get a STS Request Parameters Contract.
[**get_sts_request_param_contracts**](IdpstsRequestParametersContractsApi.md#get_sts_request_param_contracts) | **GET** /idp/stsRequestParametersContracts | Get the list of STS Request Parameters Contracts.
[**update_sts_request_param_contract_by_id**](IdpstsRequestParametersContractsApi.md#update_sts_request_param_contract_by_id) | **PUT** /idp/stsRequestParametersContracts/{id} | Update a STS Request Parameters Contract.


# **create_sts_request_param_contract**
> StsRequestParametersContract create_sts_request_param_contract(body)

Create a new STS Request Parameters Contract.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IdpstsRequestParametersContractsApi()
body = swagger_client.StsRequestParametersContract() # StsRequestParametersContract | Details for the STS Request Parameters Contract.

try:
    # Create a new STS Request Parameters Contract.
    api_response = api_instance.create_sts_request_param_contract(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IdpstsRequestParametersContractsApi->create_sts_request_param_contract: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**StsRequestParametersContract**](StsRequestParametersContract.md)| Details for the STS Request Parameters Contract. | 

### Return type

[**StsRequestParametersContract**](StsRequestParametersContract.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_sts_request_param_contract_by_id**
> delete_sts_request_param_contract_by_id(id)

Delete a STS Request Parameters Contract.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IdpstsRequestParametersContractsApi()
id = 'id_example' # str | ID of STS Request Parameters Contract to delete.

try:
    # Delete a STS Request Parameters Contract.
    api_instance.delete_sts_request_param_contract_by_id(id)
except ApiException as e:
    print("Exception when calling IdpstsRequestParametersContractsApi->delete_sts_request_param_contract_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of STS Request Parameters Contract to delete. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sts_request_param_contract_by_id**
> StsRequestParametersContract get_sts_request_param_contract_by_id(id)

Get a STS Request Parameters Contract.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IdpstsRequestParametersContractsApi()
id = 'id_example' # str | ID of STS Request Parameters Contract to fetch.

try:
    # Get a STS Request Parameters Contract.
    api_response = api_instance.get_sts_request_param_contract_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IdpstsRequestParametersContractsApi->get_sts_request_param_contract_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of STS Request Parameters Contract to fetch. | 

### Return type

[**StsRequestParametersContract**](StsRequestParametersContract.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sts_request_param_contracts**
> StsRequestParametersContracts get_sts_request_param_contracts()

Get the list of STS Request Parameters Contracts.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IdpstsRequestParametersContractsApi()

try:
    # Get the list of STS Request Parameters Contracts.
    api_response = api_instance.get_sts_request_param_contracts()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IdpstsRequestParametersContractsApi->get_sts_request_param_contracts: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**StsRequestParametersContracts**](StsRequestParametersContracts.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_sts_request_param_contract_by_id**
> StsRequestParametersContract update_sts_request_param_contract_by_id(id, body)

Update a STS Request Parameters Contract.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IdpstsRequestParametersContractsApi()
id = 'id_example' # str | ID of STS Request Parameters Contract to update.
body = swagger_client.StsRequestParametersContract() # StsRequestParametersContract | Details for updated STS Request Parameters Contract.

try:
    # Update a STS Request Parameters Contract.
    api_response = api_instance.update_sts_request_param_contract_by_id(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IdpstsRequestParametersContractsApi->update_sts_request_param_contract_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of STS Request Parameters Contract to update. | 
 **body** | [**StsRequestParametersContract**](StsRequestParametersContract.md)| Details for updated STS Request Parameters Contract. | 

### Return type

[**StsRequestParametersContract**](StsRequestParametersContract.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

