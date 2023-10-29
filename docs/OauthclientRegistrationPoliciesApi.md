# swagger_client.OauthclientRegistrationPoliciesApi

All URIs are relative to *https://localhost:9999/pf-admin-api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_dynamic_client_registration_policy**](OauthclientRegistrationPoliciesApi.md#create_dynamic_client_registration_policy) | **POST** /oauth/clientRegistrationPolicies | Create a client registration policy plugin instance.
[**delete_dynamic_client_registration_policy**](OauthclientRegistrationPoliciesApi.md#delete_dynamic_client_registration_policy) | **DELETE** /oauth/clientRegistrationPolicies/{id} | Delete a client registration policy plugin instance.
[**get_dynamic_client_registration_descriptor**](OauthclientRegistrationPoliciesApi.md#get_dynamic_client_registration_descriptor) | **GET** /oauth/clientRegistrationPolicies/descriptors/{id} | Get the description of a client registration policy plugin descriptor.
[**get_dynamic_client_registration_descriptors**](OauthclientRegistrationPoliciesApi.md#get_dynamic_client_registration_descriptors) | **GET** /oauth/clientRegistrationPolicies/descriptors | Get the list of available client registration policy plugin descriptors.
[**get_dynamic_client_registration_policies**](OauthclientRegistrationPoliciesApi.md#get_dynamic_client_registration_policies) | **GET** /oauth/clientRegistrationPolicies | Get a list of client registration policy plugin instances.
[**get_dynamic_client_registration_policy**](OauthclientRegistrationPoliciesApi.md#get_dynamic_client_registration_policy) | **GET** /oauth/clientRegistrationPolicies/{id} | Get a specific client registration policy plugin instance.
[**update_dynamic_client_registration_policy**](OauthclientRegistrationPoliciesApi.md#update_dynamic_client_registration_policy) | **PUT** /oauth/clientRegistrationPolicies/{id} | Update a client registration policy plugin instance.


# **create_dynamic_client_registration_policy**
> ClientRegistrationPolicy create_dynamic_client_registration_policy(body)

Create a client registration policy plugin instance.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OauthclientRegistrationPoliciesApi()
body = swagger_client.ClientRegistrationPolicy() # ClientRegistrationPolicy | Configuration for a client registration policy plugin instance.

try:
    # Create a client registration policy plugin instance.
    api_response = api_instance.create_dynamic_client_registration_policy(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OauthclientRegistrationPoliciesApi->create_dynamic_client_registration_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ClientRegistrationPolicy**](ClientRegistrationPolicy.md)| Configuration for a client registration policy plugin instance. | 

### Return type

[**ClientRegistrationPolicy**](ClientRegistrationPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_dynamic_client_registration_policy**
> delete_dynamic_client_registration_policy(id)

Delete a client registration policy plugin instance.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OauthclientRegistrationPoliciesApi()
id = 'id_example' # str | ID of a client registration policy plugin instance.

try:
    # Delete a client registration policy plugin instance.
    api_instance.delete_dynamic_client_registration_policy(id)
except ApiException as e:
    print("Exception when calling OauthclientRegistrationPoliciesApi->delete_dynamic_client_registration_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of a client registration policy plugin instance. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dynamic_client_registration_descriptor**
> ClientRegistrationPolicyDescriptor get_dynamic_client_registration_descriptor(id)

Get the description of a client registration policy plugin descriptor.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OauthclientRegistrationPoliciesApi()
id = 'id_example' # str | ID of client registration policy plugin descriptor.

try:
    # Get the description of a client registration policy plugin descriptor.
    api_response = api_instance.get_dynamic_client_registration_descriptor(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OauthclientRegistrationPoliciesApi->get_dynamic_client_registration_descriptor: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of client registration policy plugin descriptor. | 

### Return type

[**ClientRegistrationPolicyDescriptor**](ClientRegistrationPolicyDescriptor.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dynamic_client_registration_descriptors**
> ClientRegistrationPolicyDescriptors get_dynamic_client_registration_descriptors()

Get the list of available client registration policy plugin descriptors.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OauthclientRegistrationPoliciesApi()

try:
    # Get the list of available client registration policy plugin descriptors.
    api_response = api_instance.get_dynamic_client_registration_descriptors()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OauthclientRegistrationPoliciesApi->get_dynamic_client_registration_descriptors: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ClientRegistrationPolicyDescriptors**](ClientRegistrationPolicyDescriptors.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dynamic_client_registration_policies**
> ClientRegistrationPolicies get_dynamic_client_registration_policies()

Get a list of client registration policy plugin instances.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OauthclientRegistrationPoliciesApi()

try:
    # Get a list of client registration policy plugin instances.
    api_response = api_instance.get_dynamic_client_registration_policies()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OauthclientRegistrationPoliciesApi->get_dynamic_client_registration_policies: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ClientRegistrationPolicies**](ClientRegistrationPolicies.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dynamic_client_registration_policy**
> ClientRegistrationPolicy get_dynamic_client_registration_policy(id)

Get a specific client registration policy plugin instance.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OauthclientRegistrationPoliciesApi()
id = 'id_example' # str | ID of client registration policy plugin instance.

try:
    # Get a specific client registration policy plugin instance.
    api_response = api_instance.get_dynamic_client_registration_policy(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OauthclientRegistrationPoliciesApi->get_dynamic_client_registration_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of client registration policy plugin instance. | 

### Return type

[**ClientRegistrationPolicy**](ClientRegistrationPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_dynamic_client_registration_policy**
> ClientRegistrationPolicy update_dynamic_client_registration_policy(id, body)

Update a client registration policy plugin instance.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OauthclientRegistrationPoliciesApi()
id = 'id_example' # str | ID of a client registration policy plugin instance.
body = swagger_client.ClientRegistrationPolicy() # ClientRegistrationPolicy | Configuration for a client registration policy plugin instance.

try:
    # Update a client registration policy plugin instance.
    api_response = api_instance.update_dynamic_client_registration_policy(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OauthclientRegistrationPoliciesApi->update_dynamic_client_registration_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of a client registration policy plugin instance. | 
 **body** | [**ClientRegistrationPolicy**](ClientRegistrationPolicy.md)| Configuration for a client registration policy plugin instance. | 

### Return type

[**ClientRegistrationPolicy**](ClientRegistrationPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

