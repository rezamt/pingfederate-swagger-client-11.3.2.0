# swagger_client.PasswordCredentialValidatorsApi

All URIs are relative to *https://localhost:9999/pf-admin-api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_password_credential_validator**](PasswordCredentialValidatorsApi.md#create_password_credential_validator) | **POST** /passwordCredentialValidators | Create a new password credential validator instance
[**delete_password_credential_validator**](PasswordCredentialValidatorsApi.md#delete_password_credential_validator) | **DELETE** /passwordCredentialValidators/{id} | Delete a password credential validator instance.
[**get_password_credential_validator**](PasswordCredentialValidatorsApi.md#get_password_credential_validator) | **GET** /passwordCredentialValidators/{id} | Find a password credential validator by ID.
[**get_password_credential_validator_descriptor**](PasswordCredentialValidatorsApi.md#get_password_credential_validator_descriptor) | **GET** /passwordCredentialValidators/descriptors/{id} | Get the description of a password credential validator by ID.
[**get_password_credential_validator_descriptors**](PasswordCredentialValidatorsApi.md#get_password_credential_validator_descriptors) | **GET** /passwordCredentialValidators/descriptors | Get a list of available password credential validator descriptors.
[**get_password_credential_validators**](PasswordCredentialValidatorsApi.md#get_password_credential_validators) | **GET** /passwordCredentialValidators | Get the list of available password credential validators
[**update_password_credential_validator**](PasswordCredentialValidatorsApi.md#update_password_credential_validator) | **PUT** /passwordCredentialValidators/{id} | Update a password credential validator instance.


# **create_password_credential_validator**
> PasswordCredentialValidator create_password_credential_validator(body)

Create a new password credential validator instance

Create a new password credential validator instance. If the password credential validator is not properly configured, a 422 status code is returned along with a list of validation errors that must be corrected.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PasswordCredentialValidatorsApi()
body = swagger_client.PasswordCredentialValidator() # PasswordCredentialValidator | Configuration for the new password credential validator instance.

try:
    # Create a new password credential validator instance
    api_response = api_instance.create_password_credential_validator(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PasswordCredentialValidatorsApi->create_password_credential_validator: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PasswordCredentialValidator**](PasswordCredentialValidator.md)| Configuration for the new password credential validator instance. | 

### Return type

[**PasswordCredentialValidator**](PasswordCredentialValidator.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_password_credential_validator**
> delete_password_credential_validator(id)

Delete a password credential validator instance.

Delete a password credential validator instance with the specified ID. A 404 status code is returned for nonexistent IDs. Note: Only validators not in use can be deleted. If the request succeeds, the response body is empty. If the request fails, an ApiResult is returned with details of the errors.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PasswordCredentialValidatorsApi()
id = 'id_example' # str | ID of the password credential validator to delete.

try:
    # Delete a password credential validator instance.
    api_instance.delete_password_credential_validator(id)
except ApiException as e:
    print("Exception when calling PasswordCredentialValidatorsApi->delete_password_credential_validator: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the password credential validator to delete. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_password_credential_validator**
> PasswordCredentialValidator get_password_credential_validator(id)

Find a password credential validator by ID.

Get the configured password credential validator instance with the specified ID. A 404 status code is returned for a nonexistent ID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PasswordCredentialValidatorsApi()
id = 'id_example' # str | ID of password credential validator instance to fetch.

try:
    # Find a password credential validator by ID.
    api_response = api_instance.get_password_credential_validator(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PasswordCredentialValidatorsApi->get_password_credential_validator: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of password credential validator instance to fetch. | 

### Return type

[**PasswordCredentialValidator**](PasswordCredentialValidator.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_password_credential_validator_descriptor**
> PasswordCredentialValidatorDescriptor get_password_credential_validator_descriptor(id)

Get the description of a password credential validator by ID.

Get the description of a password credential validator by ID. A 404 status code is returned for a nonexistent ID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PasswordCredentialValidatorsApi()
id = 'id_example' # str | ID of the password credential validator descriptor to fetch.

try:
    # Get the description of a password credential validator by ID.
    api_response = api_instance.get_password_credential_validator_descriptor(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PasswordCredentialValidatorsApi->get_password_credential_validator_descriptor: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the password credential validator descriptor to fetch. | 

### Return type

[**PasswordCredentialValidatorDescriptor**](PasswordCredentialValidatorDescriptor.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_password_credential_validator_descriptors**
> PasswordCredentialValidatorDescriptors get_password_credential_validator_descriptors()

Get a list of available password credential validator descriptors.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PasswordCredentialValidatorsApi()

try:
    # Get a list of available password credential validator descriptors.
    api_response = api_instance.get_password_credential_validator_descriptors()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PasswordCredentialValidatorsApi->get_password_credential_validator_descriptors: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**PasswordCredentialValidatorDescriptors**](PasswordCredentialValidatorDescriptors.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_password_credential_validators**
> PasswordCredentialValidators get_password_credential_validators()

Get the list of available password credential validators



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PasswordCredentialValidatorsApi()

try:
    # Get the list of available password credential validators
    api_response = api_instance.get_password_credential_validators()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PasswordCredentialValidatorsApi->get_password_credential_validators: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**PasswordCredentialValidators**](PasswordCredentialValidators.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_password_credential_validator**
> PasswordCredentialValidator update_password_credential_validator(id, body)

Update a password credential validator instance.

Update a password credential validator instance. If the password credential validator is not properly configured, a 422 status code is returned along with a list of validation errors that need to be corrected.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PasswordCredentialValidatorsApi()
id = 'id_example' # str | ID of the password credential validator instance
body = swagger_client.PasswordCredentialValidator() # PasswordCredentialValidator | Configuration for the updated password credential validator instance.

try:
    # Update a password credential validator instance.
    api_response = api_instance.update_password_credential_validator(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PasswordCredentialValidatorsApi->update_password_credential_validator: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the password credential validator instance | 
 **body** | [**PasswordCredentialValidator**](PasswordCredentialValidator.md)| Configuration for the updated password credential validator instance. | 

### Return type

[**PasswordCredentialValidator**](PasswordCredentialValidator.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

