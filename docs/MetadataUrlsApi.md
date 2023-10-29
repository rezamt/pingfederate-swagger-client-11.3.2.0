# swagger_client.MetadataUrlsApi

All URIs are relative to *https://localhost:9999/pf-admin-api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_metadata_url**](MetadataUrlsApi.md#add_metadata_url) | **POST** /metadataUrls | Add a new Metadata URL.
[**delete_metadata_url**](MetadataUrlsApi.md#delete_metadata_url) | **DELETE** /metadataUrls/{id} | Delete a Metadata URL by ID.
[**get_metadata_url**](MetadataUrlsApi.md#get_metadata_url) | **GET** /metadataUrls/{id} | Get a Metadata URL by ID.
[**get_metadata_urls**](MetadataUrlsApi.md#get_metadata_urls) | **GET** /metadataUrls | Get a list of Metadata URLs
[**update_metadata_url**](MetadataUrlsApi.md#update_metadata_url) | **PUT** /metadataUrls/{id} | Update a Metadata URL by ID.


# **add_metadata_url**
> MetadataUrl add_metadata_url(body)

Add a new Metadata URL.

Add a new Metadata URL. If the Metadata URL is not properly configured, a 422 status code is returned along with a list of validation errors that must be corrected.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MetadataUrlsApi()
body = swagger_client.MetadataUrl() # MetadataUrl | Configuration for a new Metadata URL.

try:
    # Add a new Metadata URL.
    api_response = api_instance.add_metadata_url(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetadataUrlsApi->add_metadata_url: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MetadataUrl**](MetadataUrl.md)| Configuration for a new Metadata URL. | 

### Return type

[**MetadataUrl**](MetadataUrl.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_metadata_url**
> delete_metadata_url(id)

Delete a Metadata URL by ID.

Delete Metadata URL with the specified ID. A 404 status code is returned for nonexistent IDs. Note: If the request succeeds, the response body is empty. If the request fails, an ApiResult is returned with details of the error.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MetadataUrlsApi()
id = 'id_example' # str | ID of Metadata URL to delete.

try:
    # Delete a Metadata URL by ID.
    api_instance.delete_metadata_url(id)
except ApiException as e:
    print("Exception when calling MetadataUrlsApi->delete_metadata_url: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of Metadata URL to delete. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_metadata_url**
> MetadataUrl get_metadata_url(id)

Get a Metadata URL by ID.

Get a Metadata URL with the specified ID. A 404 status code is returned for nonexistent IDs

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MetadataUrlsApi()
id = 'id_example' # str | ID of Metadata URL to fetch

try:
    # Get a Metadata URL by ID.
    api_response = api_instance.get_metadata_url(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetadataUrlsApi->get_metadata_url: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of Metadata URL to fetch | 

### Return type

[**MetadataUrl**](MetadataUrl.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_metadata_urls**
> MetadataUrls get_metadata_urls()

Get a list of Metadata URLs



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MetadataUrlsApi()

try:
    # Get a list of Metadata URLs
    api_response = api_instance.get_metadata_urls()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetadataUrlsApi->get_metadata_urls: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**MetadataUrls**](MetadataUrls.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_metadata_url**
> MetadataUrl update_metadata_url(id, body)

Update a Metadata URL by ID.

Update a Metadata URL by ID. If the Metadata URL is not properly configured, a 422 status code is returned along with a list of validation errors that must be corrected.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MetadataUrlsApi()
id = 'id_example' # str | ID of the Metadata URL to update.
body = swagger_client.MetadataUrl() # MetadataUrl | Configuration for the Metadata URL.

try:
    # Update a Metadata URL by ID.
    api_response = api_instance.update_metadata_url(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetadataUrlsApi->update_metadata_url: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the Metadata URL to update. | 
 **body** | [**MetadataUrl**](MetadataUrl.md)| Configuration for the Metadata URL. | 

### Return type

[**MetadataUrl**](MetadataUrl.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

