# swagger_client.ClusterApi

All URIs are relative to *https://localhost:9999/pf-admin-api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_cluster_status**](ClusterApi.md#get_cluster_status) | **GET** /cluster/status | Get information on the current status of the cluster.
[**start_replication**](ClusterApi.md#start_replication) | **POST** /cluster/replicate | Replicate configuration updates to all nodes in the cluster.


# **get_cluster_status**
> ClusterStatus get_cluster_status()

Get information on the current status of the cluster.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ClusterApi()

try:
    # Get information on the current status of the cluster.
    api_response = api_instance.get_cluster_status()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterApi->get_cluster_status: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ClusterStatus**](ClusterStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_replication**
> ApiResult start_replication()

Replicate configuration updates to all nodes in the cluster.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ClusterApi()

try:
    # Replicate configuration updates to all nodes in the cluster.
    api_response = api_instance.start_replication()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterApi->start_replication: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ApiResult**](ApiResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

