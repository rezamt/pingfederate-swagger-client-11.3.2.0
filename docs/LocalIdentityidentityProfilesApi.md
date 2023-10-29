# swagger_client.LocalIdentityidentityProfilesApi

All URIs are relative to *https://localhost:9999/pf-admin-api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_identity_profile**](LocalIdentityidentityProfilesApi.md#create_identity_profile) | **POST** /localIdentity/identityProfiles | Create a new local identity profile.
[**delete_identity_profile**](LocalIdentityidentityProfilesApi.md#delete_identity_profile) | **DELETE** /localIdentity/identityProfiles/{id} | Delete the local identity profile by ID.
[**get_identity_profile**](LocalIdentityidentityProfilesApi.md#get_identity_profile) | **GET** /localIdentity/identityProfiles/{id} | Get the local identity profile by ID.
[**get_identity_profiles**](LocalIdentityidentityProfilesApi.md#get_identity_profiles) | **GET** /localIdentity/identityProfiles | Get the list of configured local identity profiles.
[**update_identity_profile**](LocalIdentityidentityProfilesApi.md#update_identity_profile) | **PUT** /localIdentity/identityProfiles/{id} | Update the local identity profile by ID.


# **create_identity_profile**
> LocalIdentityProfile create_identity_profile(body, x_bypass_external_validation=x_bypass_external_validation)

Create a new local identity profile.

Create a new local identity profile. If the local identity profile is not properly configured, a 422 status code is returned along with a list of validation errors that must be corrected.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LocalIdentityidentityProfilesApi()
body = swagger_client.LocalIdentityProfile() # LocalIdentityProfile | Configuration for a new profile.
x_bypass_external_validation = false # bool | External validation will be bypassed when set to true. Default to false. (optional) (default to false)

try:
    # Create a new local identity profile.
    api_response = api_instance.create_identity_profile(body, x_bypass_external_validation=x_bypass_external_validation)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LocalIdentityidentityProfilesApi->create_identity_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LocalIdentityProfile**](LocalIdentityProfile.md)| Configuration for a new profile. | 
 **x_bypass_external_validation** | **bool**| External validation will be bypassed when set to true. Default to false. | [optional] [default to false]

### Return type

[**LocalIdentityProfile**](LocalIdentityProfile.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_identity_profile**
> delete_identity_profile(id)

Delete the local identity profile by ID.

Delete a local identity profile with the specified ID. A 404 status code is returned for nonexistent IDs. Note: If the request succeeds, the response body is empty. If the request fails, an ApiResult is returned with details of the error.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LocalIdentityidentityProfilesApi()
id = 'id_example' # str | ID of the profile to delete

try:
    # Delete the local identity profile by ID.
    api_instance.delete_identity_profile(id)
except ApiException as e:
    print("Exception when calling LocalIdentityidentityProfilesApi->delete_identity_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the profile to delete | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_identity_profile**
> LocalIdentityProfile get_identity_profile(id)

Get the local identity profile by ID.

Get a local identity profile with the specified ID. A 404 status code is returned for nonexistent IDs.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LocalIdentityidentityProfilesApi()
id = 'id_example' # str | ID of profile to fetch

try:
    # Get the local identity profile by ID.
    api_response = api_instance.get_identity_profile(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LocalIdentityidentityProfilesApi->get_identity_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of profile to fetch | 

### Return type

[**LocalIdentityProfile**](LocalIdentityProfile.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_identity_profiles**
> LocalIdentityProfiles get_identity_profiles(page=page, number_per_page=number_per_page, filter=filter, apc_id=apc_id)

Get the list of configured local identity profiles.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LocalIdentityidentityProfilesApi()
page = 56 # int | Page number to retrieve. (optional)
number_per_page = 56 # int | Number of local identity profiles per page. (optional)
filter = 'filter_example' # str | Filter criteria limits the local identity profiles that are returned to only those that match it. The filter criteria is compared to the local identity profile name and ID fields. The comparison is a case-insensitive partial match. No additional pattern based matching is supported. (optional)
apc_id = 'apc_id_example' # str | Filter the local identity profiles by matching policy contract ID. (optional)

try:
    # Get the list of configured local identity profiles.
    api_response = api_instance.get_identity_profiles(page=page, number_per_page=number_per_page, filter=filter, apc_id=apc_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LocalIdentityidentityProfilesApi->get_identity_profiles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number to retrieve. | [optional] 
 **number_per_page** | **int**| Number of local identity profiles per page. | [optional] 
 **filter** | **str**| Filter criteria limits the local identity profiles that are returned to only those that match it. The filter criteria is compared to the local identity profile name and ID fields. The comparison is a case-insensitive partial match. No additional pattern based matching is supported. | [optional] 
 **apc_id** | **str**| Filter the local identity profiles by matching policy contract ID. | [optional] 

### Return type

[**LocalIdentityProfiles**](LocalIdentityProfiles.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_identity_profile**
> LocalIdentityProfile update_identity_profile(id, body, x_bypass_external_validation=x_bypass_external_validation)

Update the local identity profile by ID.

Update a local identity profile with the specified ID. A 404 status code is returned for nonexistent IDs.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LocalIdentityidentityProfilesApi()
id = 'id_example' # str | ID of the profile to update
body = swagger_client.LocalIdentityProfile() # LocalIdentityProfile | Configuration for updated local identity profile.
x_bypass_external_validation = false # bool | External validation will be bypassed when set to true. Default to false. (optional) (default to false)

try:
    # Update the local identity profile by ID.
    api_response = api_instance.update_identity_profile(id, body, x_bypass_external_validation=x_bypass_external_validation)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LocalIdentityidentityProfilesApi->update_identity_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the profile to update | 
 **body** | [**LocalIdentityProfile**](LocalIdentityProfile.md)| Configuration for updated local identity profile. | 
 **x_bypass_external_validation** | **bool**| External validation will be bypassed when set to true. Default to false. | [optional] [default to false]

### Return type

[**LocalIdentityProfile**](LocalIdentityProfile.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

