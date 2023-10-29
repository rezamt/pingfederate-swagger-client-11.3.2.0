# swagger_client.AdministrativeAccountsApi

All URIs are relative to *https://localhost:9999/pf-admin-api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_account**](AdministrativeAccountsApi.md#add_account) | **POST** /administrativeAccounts | Add a new PingFederate native Administrative Account.
[**change_password**](AdministrativeAccountsApi.md#change_password) | **POST** /administrativeAccounts/changePassword | Change the Password of current PingFederate native Account.
[**delete_account**](AdministrativeAccountsApi.md#delete_account) | **DELETE** /administrativeAccounts/{username} | Delete a PingFederate native Administrative Account information.
[**get_account**](AdministrativeAccountsApi.md#get_account) | **GET** /administrativeAccounts/{username} | Get a PingFederate native Administrative Account.
[**get_accounts**](AdministrativeAccountsApi.md#get_accounts) | **GET** /administrativeAccounts | Get all the PingFederate native Administrative Accounts.
[**reset_password**](AdministrativeAccountsApi.md#reset_password) | **POST** /administrativeAccounts/{username}/resetPassword | Reset the Password of an existing PingFederate native Administrative Account.
[**update_account**](AdministrativeAccountsApi.md#update_account) | **PUT** /administrativeAccounts/{username} | Update the information for a native Administrative Account.


# **add_account**
> AdministrativeAccount add_account(body)

Add a new PingFederate native Administrative Account.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AdministrativeAccountsApi()
body = swagger_client.AdministrativeAccount() # AdministrativeAccount | Administrative account information.

try:
    # Add a new PingFederate native Administrative Account.
    api_response = api_instance.add_account(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdministrativeAccountsApi->add_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AdministrativeAccount**](AdministrativeAccount.md)| Administrative account information. | 

### Return type

[**AdministrativeAccount**](AdministrativeAccount.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_password**
> UserCredentials change_password(body)

Change the Password of current PingFederate native Account.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AdministrativeAccountsApi()
body = swagger_client.UserCredentials() # UserCredentials | User Account credential.

try:
    # Change the Password of current PingFederate native Account.
    api_response = api_instance.change_password(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdministrativeAccountsApi->change_password: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UserCredentials**](UserCredentials.md)| User Account credential. | 

### Return type

[**UserCredentials**](UserCredentials.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_account**
> delete_account(username)

Delete a PingFederate native Administrative Account information.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AdministrativeAccountsApi()
username = 'username_example' # str | Username of the account to be deleted.

try:
    # Delete a PingFederate native Administrative Account information.
    api_instance.delete_account(username)
except ApiException as e:
    print("Exception when calling AdministrativeAccountsApi->delete_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| Username of the account to be deleted. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_account**
> AdministrativeAccount get_account(username)

Get a PingFederate native Administrative Account.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AdministrativeAccountsApi()
username = 'username_example' # str | Username of the administrative account.

try:
    # Get a PingFederate native Administrative Account.
    api_response = api_instance.get_account(username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdministrativeAccountsApi->get_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| Username of the administrative account. | 

### Return type

[**AdministrativeAccount**](AdministrativeAccount.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_accounts**
> AdministrativeAccounts get_accounts()

Get all the PingFederate native Administrative Accounts.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AdministrativeAccountsApi()

try:
    # Get all the PingFederate native Administrative Accounts.
    api_response = api_instance.get_accounts()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdministrativeAccountsApi->get_accounts: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AdministrativeAccounts**](AdministrativeAccounts.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reset_password**
> UserCredentials reset_password(username, body)

Reset the Password of an existing PingFederate native Administrative Account.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AdministrativeAccountsApi()
username = 'username_example' # str | Username of the administrative account.
body = swagger_client.UserCredentials() # UserCredentials | New password.

try:
    # Reset the Password of an existing PingFederate native Administrative Account.
    api_response = api_instance.reset_password(username, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdministrativeAccountsApi->reset_password: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| Username of the administrative account. | 
 **body** | [**UserCredentials**](UserCredentials.md)| New password. | 

### Return type

[**UserCredentials**](UserCredentials.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_account**
> AdministrativeAccount update_account(username, body)

Update the information for a native Administrative Account.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AdministrativeAccountsApi()
username = 'username_example' # str | Username of the account to be updated.
body = swagger_client.AdministrativeAccount() # AdministrativeAccount | Administrative account information.

try:
    # Update the information for a native Administrative Account.
    api_response = api_instance.update_account(username, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdministrativeAccountsApi->update_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| Username of the account to be updated. | 
 **body** | [**AdministrativeAccount**](AdministrativeAccount.md)| Administrative account information. | 

### Return type

[**AdministrativeAccount**](AdministrativeAccount.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

