# swagger_client.KerberosrealmsApi

All URIs are relative to *https://localhost:9999/pf-admin-api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_kerberos_realm**](KerberosrealmsApi.md#create_kerberos_realm) | **POST** /kerberos/realms | Create a new Kerberos Realm.
[**delete_kerberos_realm**](KerberosrealmsApi.md#delete_kerberos_realm) | **DELETE** /kerberos/realms/{id} | Delete a Kerberos Realm.
[**get_kerberos_realm**](KerberosrealmsApi.md#get_kerberos_realm) | **GET** /kerberos/realms/{id} | Find a Kerberos Realm by ID.
[**get_kerberos_realm_settings**](KerberosrealmsApi.md#get_kerberos_realm_settings) | **GET** /kerberos/realms/settings | Gets the Kerberos Realms Settings.
[**get_kerberos_realms**](KerberosrealmsApi.md#get_kerberos_realms) | **GET** /kerberos/realms | Gets the Kerberos Realms.
[**update_kerberos_realm**](KerberosrealmsApi.md#update_kerberos_realm) | **PUT** /kerberos/realms/{id} | Update a Kerberos Realm by ID.
[**update_settings**](KerberosrealmsApi.md#update_settings) | **PUT** /kerberos/realms/settings | Set/Update the Kerberos Realms Settings.


# **create_kerberos_realm**
> KerberosRealm create_kerberos_realm(body, x_bypass_external_validation=x_bypass_external_validation)

Create a new Kerberos Realm.

Create a new Kerberos Realm. If the Kerberos Realm is not properly configured, a 422 status code is returned along with a list of validation errors that must be corrected.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.KerberosrealmsApi()
body = swagger_client.KerberosRealm() # KerberosRealm | Configuration for new policy.
x_bypass_external_validation = false # bool | External validation will be bypassed when set to true. Defaults to false. (optional) (default to false)

try:
    # Create a new Kerberos Realm.
    api_response = api_instance.create_kerberos_realm(body, x_bypass_external_validation=x_bypass_external_validation)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KerberosrealmsApi->create_kerberos_realm: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**KerberosRealm**](KerberosRealm.md)| Configuration for new policy. | 
 **x_bypass_external_validation** | **bool**| External validation will be bypassed when set to true. Defaults to false. | [optional] [default to false]

### Return type

[**KerberosRealm**](KerberosRealm.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_kerberos_realm**
> delete_kerberos_realm(id)

Delete a Kerberos Realm.

Delete a Kerberos Realm with the specified ID. A 404 status code is returned for nonexistent IDs. Note: If the request succeeds, the response body is empty. If the request fails, an ApiResult is returned with details of the error.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.KerberosrealmsApi()
id = 'id_example' # str | ID of Kerberos Realm to delete.

try:
    # Delete a Kerberos Realm.
    api_instance.delete_kerberos_realm(id)
except ApiException as e:
    print("Exception when calling KerberosrealmsApi->delete_kerberos_realm: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of Kerberos Realm to delete. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_kerberos_realm**
> KerberosRealm get_kerberos_realm(id)

Find a Kerberos Realm by ID.

Get a Kerberos Realm with the specified ID. A 404 status code is returned for nonexistent IDs.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.KerberosrealmsApi()
id = 'id_example' # str | ID of the Kerberos Realm to fetch.

try:
    # Find a Kerberos Realm by ID.
    api_response = api_instance.get_kerberos_realm(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KerberosrealmsApi->get_kerberos_realm: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the Kerberos Realm to fetch. | 

### Return type

[**KerberosRealm**](KerberosRealm.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_kerberos_realm_settings**
> KerberosRealmsSettings get_kerberos_realm_settings()

Gets the Kerberos Realms Settings.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.KerberosrealmsApi()

try:
    # Gets the Kerberos Realms Settings.
    api_response = api_instance.get_kerberos_realm_settings()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KerberosrealmsApi->get_kerberos_realm_settings: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**KerberosRealmsSettings**](KerberosRealmsSettings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_kerberos_realms**
> KerberosRealms get_kerberos_realms()

Gets the Kerberos Realms.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.KerberosrealmsApi()

try:
    # Gets the Kerberos Realms.
    api_response = api_instance.get_kerberos_realms()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KerberosrealmsApi->get_kerberos_realms: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**KerberosRealms**](KerberosRealms.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_kerberos_realm**
> KerberosRealm update_kerberos_realm(id, body, x_bypass_external_validation=x_bypass_external_validation)

Update a Kerberos Realm by ID.

Update a Kerberos Realm with the specified ID. A 404 status code is returned for nonexistent IDs.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.KerberosrealmsApi()
id = 'id_example' # str | ID of the Kerberos Realm to update.
body = swagger_client.KerberosRealm() # KerberosRealm | Configuration for updated Domain/Realm.
x_bypass_external_validation = false # bool | External validation will be bypassed when set to true. Defaults to false. (optional) (default to false)

try:
    # Update a Kerberos Realm by ID.
    api_response = api_instance.update_kerberos_realm(id, body, x_bypass_external_validation=x_bypass_external_validation)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KerberosrealmsApi->update_kerberos_realm: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the Kerberos Realm to update. | 
 **body** | [**KerberosRealm**](KerberosRealm.md)| Configuration for updated Domain/Realm. | 
 **x_bypass_external_validation** | **bool**| External validation will be bypassed when set to true. Defaults to false. | [optional] [default to false]

### Return type

[**KerberosRealm**](KerberosRealm.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_settings**
> KerberosRealmsSettings update_settings(body)

Set/Update the Kerberos Realms Settings.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.KerberosrealmsApi()
body = swagger_client.KerberosRealmsSettings() # KerberosRealmsSettings | Kerberos Realms Settings.

try:
    # Set/Update the Kerberos Realms Settings.
    api_response = api_instance.update_settings(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KerberosrealmsApi->update_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**KerberosRealmsSettings**](KerberosRealmsSettings.md)| Kerberos Realms Settings. | 

### Return type

[**KerberosRealmsSettings**](KerberosRealmsSettings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

