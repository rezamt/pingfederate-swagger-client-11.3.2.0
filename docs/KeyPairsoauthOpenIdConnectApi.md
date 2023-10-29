# swagger_client.KeyPairsoauthOpenIdConnectApi

All URIs are relative to *https://localhost:9999/pf-admin-api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_key_set**](KeyPairsoauthOpenIdConnectApi.md#create_key_set) | **POST** /keyPairs/oauthOpenIdConnect/additionalKeySets | Create a new OAuth/OpenID Connect additional signing key set.
[**delete_key_set**](KeyPairsoauthOpenIdConnectApi.md#delete_key_set) | **DELETE** /keyPairs/oauthOpenIdConnect/additionalKeySets/{id} | Delete an existing OAuth/OpenID Connect additional signing key set.
[**get_key_set**](KeyPairsoauthOpenIdConnectApi.md#get_key_set) | **GET** /keyPairs/oauthOpenIdConnect/additionalKeySets/{id} | Retrieve an OAuth/OpenID Connect additional signing key set.
[**get_key_sets**](KeyPairsoauthOpenIdConnectApi.md#get_key_sets) | **GET** /keyPairs/oauthOpenIdConnect/additionalKeySets | Retrieve OAuth/OpenID Connect additional signing key sets.
[**get_oauth_oidc_keys_settings**](KeyPairsoauthOpenIdConnectApi.md#get_oauth_oidc_keys_settings) | **GET** /keyPairs/oauthOpenIdConnect | Retrieve OAuth/OpenID Connect key settings.
[**update_key_set**](KeyPairsoauthOpenIdConnectApi.md#update_key_set) | **PUT** /keyPairs/oauthOpenIdConnect/additionalKeySets/{id} | Update an existing OAuth/OpenID Connect additional signing key set.
[**update_o_auth_oidc_keys_settings**](KeyPairsoauthOpenIdConnectApi.md#update_o_auth_oidc_keys_settings) | **PUT** /keyPairs/oauthOpenIdConnect | Update OAuth/OpenID Connect key settings.


# **create_key_set**
> AdditionalKeySet create_key_set(body)

Create a new OAuth/OpenID Connect additional signing key set.

Create a new OAuth/OpenID Connect additional signing key set.  If not properly configured, a 422 status code is returned along with a list of validation errors that must be corrected.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.KeyPairsoauthOpenIdConnectApi()
body = swagger_client.AdditionalKeySet() # AdditionalKeySet | Configuration for a new signing key set.

try:
    # Create a new OAuth/OpenID Connect additional signing key set.
    api_response = api_instance.create_key_set(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KeyPairsoauthOpenIdConnectApi->create_key_set: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AdditionalKeySet**](AdditionalKeySet.md)| Configuration for a new signing key set. | 

### Return type

[**AdditionalKeySet**](AdditionalKeySet.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_key_set**
> delete_key_set(id)

Delete an existing OAuth/OpenID Connect additional signing key set.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.KeyPairsoauthOpenIdConnectApi()
id = 'id_example' # str | ID of an additional key set to be deleted.

try:
    # Delete an existing OAuth/OpenID Connect additional signing key set.
    api_instance.delete_key_set(id)
except ApiException as e:
    print("Exception when calling KeyPairsoauthOpenIdConnectApi->delete_key_set: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of an additional key set to be deleted. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_key_set**
> AdditionalKeySet get_key_set(id)

Retrieve an OAuth/OpenID Connect additional signing key set.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.KeyPairsoauthOpenIdConnectApi()
id = 'id_example' # str | ID of an OAuth/OpenID Connect additional signing key set to update.

try:
    # Retrieve an OAuth/OpenID Connect additional signing key set.
    api_response = api_instance.get_key_set(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KeyPairsoauthOpenIdConnectApi->get_key_set: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of an OAuth/OpenID Connect additional signing key set to update. | 

### Return type

[**AdditionalKeySet**](AdditionalKeySet.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_key_sets**
> AdditionalKeySets get_key_sets()

Retrieve OAuth/OpenID Connect additional signing key sets.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.KeyPairsoauthOpenIdConnectApi()

try:
    # Retrieve OAuth/OpenID Connect additional signing key sets.
    api_response = api_instance.get_key_sets()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KeyPairsoauthOpenIdConnectApi->get_key_sets: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AdditionalKeySets**](AdditionalKeySets.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_oauth_oidc_keys_settings**
> OAuthOidcKeysSettings get_oauth_oidc_keys_settings()

Retrieve OAuth/OpenID Connect key settings.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.KeyPairsoauthOpenIdConnectApi()

try:
    # Retrieve OAuth/OpenID Connect key settings.
    api_response = api_instance.get_oauth_oidc_keys_settings()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KeyPairsoauthOpenIdConnectApi->get_oauth_oidc_keys_settings: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**OAuthOidcKeysSettings**](OAuthOidcKeysSettings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_key_set**
> AdditionalKeySet update_key_set(id, body)

Update an existing OAuth/OpenID Connect additional signing key set.

Update an existing OAuth/OpenID Connect additional signing key set.  If not properly configured, a 422 status code is returned along with a list of validation errors that must be corrected.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.KeyPairsoauthOpenIdConnectApi()
id = 'id_example' # str | ID of an OAuth/OpenID Connect additional signing key set to update.
body = swagger_client.AdditionalKeySet() # AdditionalKeySet | Configuration for updated OAuth/OpenID Connect additional signing key set.

try:
    # Update an existing OAuth/OpenID Connect additional signing key set.
    api_response = api_instance.update_key_set(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KeyPairsoauthOpenIdConnectApi->update_key_set: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of an OAuth/OpenID Connect additional signing key set to update. | 
 **body** | [**AdditionalKeySet**](AdditionalKeySet.md)| Configuration for updated OAuth/OpenID Connect additional signing key set. | 

### Return type

[**AdditionalKeySet**](AdditionalKeySet.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_o_auth_oidc_keys_settings**
> OAuthOidcKeysSettings update_o_auth_oidc_keys_settings(body)

Update OAuth/OpenID Connect key settings.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.KeyPairsoauthOpenIdConnectApi()
body = swagger_client.OAuthOidcKeysSettings() # OAuthOidcKeysSettings | OAuth and OpenID Connect static key settings

try:
    # Update OAuth/OpenID Connect key settings.
    api_response = api_instance.update_o_auth_oidc_keys_settings(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KeyPairsoauthOpenIdConnectApi->update_o_auth_oidc_keys_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OAuthOidcKeysSettings**](OAuthOidcKeysSettings.md)| OAuth and OpenID Connect static key settings | 

### Return type

[**OAuthOidcKeysSettings**](OAuthOidcKeysSettings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

