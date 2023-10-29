# swagger_client.AuthenticationPolicyContractsApi

All URIs are relative to *https://localhost:9999/pf-admin-api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_authentication_policy_contract**](AuthenticationPolicyContractsApi.md#create_authentication_policy_contract) | **POST** /authenticationPolicyContracts | Create a new Authentication Policy Contract.
[**delete_authentication_policy_contract**](AuthenticationPolicyContractsApi.md#delete_authentication_policy_contract) | **DELETE** /authenticationPolicyContracts/{id} | Delete an Authentication Policy Contract.
[**get_authentication_policy_contract**](AuthenticationPolicyContractsApi.md#get_authentication_policy_contract) | **GET** /authenticationPolicyContracts/{id} | Gets the Authentication Policy Contract by ID.
[**get_authentication_policy_contracts**](AuthenticationPolicyContractsApi.md#get_authentication_policy_contracts) | **GET** /authenticationPolicyContracts | Gets the Authentication Policy Contracts.
[**update_authentication_policy_contract**](AuthenticationPolicyContractsApi.md#update_authentication_policy_contract) | **PUT** /authenticationPolicyContracts/{id} | Update an Authentication Policy Contract by ID.


# **create_authentication_policy_contract**
> AuthenticationPolicyContract create_authentication_policy_contract(body)

Create a new Authentication Policy Contract.

Create a new Authentication Policy Contract. If the Authentication Policy Contract is not properly configured, a 422 status code is returned along with a list of validation errors that must be corrected.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AuthenticationPolicyContractsApi()
body = swagger_client.AuthenticationPolicyContract() # AuthenticationPolicyContract | Configuration for a new contract.

try:
    # Create a new Authentication Policy Contract.
    api_response = api_instance.create_authentication_policy_contract(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationPolicyContractsApi->create_authentication_policy_contract: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AuthenticationPolicyContract**](AuthenticationPolicyContract.md)| Configuration for a new contract. | 

### Return type

[**AuthenticationPolicyContract**](AuthenticationPolicyContract.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_authentication_policy_contract**
> delete_authentication_policy_contract(id)

Delete an Authentication Policy Contract.

Delete an Authentication Policy Contract with the specified ID. A 404 status code is returned for nonexistent IDs. Note: If the request succeeds, the response body is empty. If the request fails, an ApiResult is returned with details of the error.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AuthenticationPolicyContractsApi()
id = 'id_example' # str | ID of Authentication Policy Contract to delete.

try:
    # Delete an Authentication Policy Contract.
    api_instance.delete_authentication_policy_contract(id)
except ApiException as e:
    print("Exception when calling AuthenticationPolicyContractsApi->delete_authentication_policy_contract: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of Authentication Policy Contract to delete. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_authentication_policy_contract**
> AuthenticationPolicyContract get_authentication_policy_contract(id)

Gets the Authentication Policy Contract by ID.

Get an Authentication Policy Contract with the specified ID. A 404 status code is returned for nonexistent IDs

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AuthenticationPolicyContractsApi()
id = 'id_example' # str | ID of contract to fetch

try:
    # Gets the Authentication Policy Contract by ID.
    api_response = api_instance.get_authentication_policy_contract(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationPolicyContractsApi->get_authentication_policy_contract: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of contract to fetch | 

### Return type

[**AuthenticationPolicyContract**](AuthenticationPolicyContract.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_authentication_policy_contracts**
> AuthenticationPolicyContracts get_authentication_policy_contracts(page=page, number_per_page=number_per_page, filter=filter)

Gets the Authentication Policy Contracts.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AuthenticationPolicyContractsApi()
page = 56 # int | Page number to retrieve. (optional)
number_per_page = 56 # int | Number of contracts per page. (optional)
filter = 'filter_example' # str | Filter criteria limits the authentication policy contracts that are returned to only those that match it. The filter criteria is compared to the authentication policy contract name and ID fields. The comparison is a case-insensitive partial match. No additional pattern based matching is supported. (optional)

try:
    # Gets the Authentication Policy Contracts.
    api_response = api_instance.get_authentication_policy_contracts(page=page, number_per_page=number_per_page, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationPolicyContractsApi->get_authentication_policy_contracts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number to retrieve. | [optional] 
 **number_per_page** | **int**| Number of contracts per page. | [optional] 
 **filter** | **str**| Filter criteria limits the authentication policy contracts that are returned to only those that match it. The filter criteria is compared to the authentication policy contract name and ID fields. The comparison is a case-insensitive partial match. No additional pattern based matching is supported. | [optional] 

### Return type

[**AuthenticationPolicyContracts**](AuthenticationPolicyContracts.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_authentication_policy_contract**
> AuthenticationPolicyContract update_authentication_policy_contract(id, body)

Update an Authentication Policy Contract by ID.

Update an Authentication Policy Contract with the specified ID. A 404 status code is returned for nonexistent IDs.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AuthenticationPolicyContractsApi()
id = 'id_example' # str | ID of the Authentication Policy Contract to update.
body = swagger_client.AuthenticationPolicyContract() # AuthenticationPolicyContract | Configuration for updated Authentication Policy Contract.

try:
    # Update an Authentication Policy Contract by ID.
    api_response = api_instance.update_authentication_policy_contract(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationPolicyContractsApi->update_authentication_policy_contract: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the Authentication Policy Contract to update. | 
 **body** | [**AuthenticationPolicyContract**](AuthenticationPolicyContract.md)| Configuration for updated Authentication Policy Contract. | 

### Return type

[**AuthenticationPolicyContract**](AuthenticationPolicyContract.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

