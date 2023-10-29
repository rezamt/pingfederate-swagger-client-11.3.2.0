# swagger_client.IdentityStoreProvisionersApi

All URIs are relative to *https://localhost:9999/pf-admin-api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_identity_store_provisioner**](IdentityStoreProvisionersApi.md#create_identity_store_provisioner) | **POST** /identityStoreProvisioners | Create a new identity store provisioner instance.
[**delete_identity_store_provisioner**](IdentityStoreProvisionersApi.md#delete_identity_store_provisioner) | **DELETE** /identityStoreProvisioners/{id} | Delete an identity store provisioner instance
[**get_identity_store_provisioner**](IdentityStoreProvisionersApi.md#get_identity_store_provisioner) | **GET** /identityStoreProvisioners/{id} | Get an identity store provisioner by ID.
[**get_identity_store_provisioner_descriptor_by_id**](IdentityStoreProvisionersApi.md#get_identity_store_provisioner_descriptor_by_id) | **GET** /identityStoreProvisioners/descriptors/{id} | Get the descriptor of an identity store provisioner by ID.
[**get_identity_store_provisioner_descriptors**](IdentityStoreProvisionersApi.md#get_identity_store_provisioner_descriptors) | **GET** /identityStoreProvisioners/descriptors | Get the list of available identity store provisioner descriptors.
[**get_identity_store_provisioners**](IdentityStoreProvisionersApi.md#get_identity_store_provisioners) | **GET** /identityStoreProvisioners | Get the list of configured identity store provisioner instances.
[**update_identity_store_provisioner**](IdentityStoreProvisionersApi.md#update_identity_store_provisioner) | **PUT** /identityStoreProvisioners/{id} | Update an identity store provisioner instance


# **create_identity_store_provisioner**
> IdentityStoreProvisioner create_identity_store_provisioner(body)

Create a new identity store provisioner instance.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IdentityStoreProvisionersApi()
body = swagger_client.IdentityStoreProvisioner() # IdentityStoreProvisioner | Configuration for the identity store provisioner instance.

try:
    # Create a new identity store provisioner instance.
    api_response = api_instance.create_identity_store_provisioner(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IdentityStoreProvisionersApi->create_identity_store_provisioner: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**IdentityStoreProvisioner**](IdentityStoreProvisioner.md)| Configuration for the identity store provisioner instance. | 

### Return type

[**IdentityStoreProvisioner**](IdentityStoreProvisioner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_identity_store_provisioner**
> delete_identity_store_provisioner(id)

Delete an identity store provisioner instance



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IdentityStoreProvisionersApi()
id = 'id_example' # str | ID of identity store provisioner instance

try:
    # Delete an identity store provisioner instance
    api_instance.delete_identity_store_provisioner(id)
except ApiException as e:
    print("Exception when calling IdentityStoreProvisionersApi->delete_identity_store_provisioner: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of identity store provisioner instance | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_identity_store_provisioner**
> IdentityStoreProvisioner get_identity_store_provisioner(id)

Get an identity store provisioner by ID.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IdentityStoreProvisionersApi()
id = 'id_example' # str | ID of identity store provisioner instance

try:
    # Get an identity store provisioner by ID.
    api_response = api_instance.get_identity_store_provisioner(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IdentityStoreProvisionersApi->get_identity_store_provisioner: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of identity store provisioner instance | 

### Return type

[**IdentityStoreProvisioner**](IdentityStoreProvisioner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_identity_store_provisioner_descriptor_by_id**
> IdentityStoreProvisionerDescriptor get_identity_store_provisioner_descriptor_by_id(id)

Get the descriptor of an identity store provisioner by ID.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IdentityStoreProvisionersApi()
id = 'id_example' # str | ID of identity store provisioner descriptor

try:
    # Get the descriptor of an identity store provisioner by ID.
    api_response = api_instance.get_identity_store_provisioner_descriptor_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IdentityStoreProvisionersApi->get_identity_store_provisioner_descriptor_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of identity store provisioner descriptor | 

### Return type

[**IdentityStoreProvisionerDescriptor**](IdentityStoreProvisionerDescriptor.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_identity_store_provisioner_descriptors**
> IdentityStoreProvisionerDescriptors get_identity_store_provisioner_descriptors()

Get the list of available identity store provisioner descriptors.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IdentityStoreProvisionersApi()

try:
    # Get the list of available identity store provisioner descriptors.
    api_response = api_instance.get_identity_store_provisioner_descriptors()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IdentityStoreProvisionersApi->get_identity_store_provisioner_descriptors: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**IdentityStoreProvisionerDescriptors**](IdentityStoreProvisionerDescriptors.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_identity_store_provisioners**
> IdentityStoreProvisioners get_identity_store_provisioners()

Get the list of configured identity store provisioner instances.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IdentityStoreProvisionersApi()

try:
    # Get the list of configured identity store provisioner instances.
    api_response = api_instance.get_identity_store_provisioners()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IdentityStoreProvisionersApi->get_identity_store_provisioners: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**IdentityStoreProvisioners**](IdentityStoreProvisioners.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_identity_store_provisioner**
> IdentityStoreProvisioner update_identity_store_provisioner(id, body)

Update an identity store provisioner instance



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IdentityStoreProvisionersApi()
id = 'id_example' # str | ID of identity store provisioner instance
body = swagger_client.IdentityStoreProvisioner() # IdentityStoreProvisioner | Configuration for the identity store provisioner instance

try:
    # Update an identity store provisioner instance
    api_response = api_instance.update_identity_store_provisioner(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IdentityStoreProvisionersApi->update_identity_store_provisioner: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of identity store provisioner instance | 
 **body** | [**IdentityStoreProvisioner**](IdentityStoreProvisioner.md)| Configuration for the identity store provisioner instance | 

### Return type

[**IdentityStoreProvisioner**](IdentityStoreProvisioner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

