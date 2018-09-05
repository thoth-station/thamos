# thamos.swagger_client.AdminApi

All URIs are relative to *https://localhost/api/v1/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**erase_graph**](AdminApi.md#erase_graph) | **POST** /erase-graph | Clean graph database.
[**sync**](AdminApi.md#sync) | **POST** /sync | Force run sync to graph database.


# **erase_graph**
> erase_graph(secret)

Clean graph database.

### Example
```python
from __future__ import print_function
import time
import thamos.swagger_client
from thamos.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = thamos.swagger_client.AdminApi()
secret = 'false' # str | A secret to clean graph database. (default to false)

try:
    # Clean graph database.
    api_instance.erase_graph(secret)
except ApiException as e:
    print("Exception when calling AdminApi->erase_graph: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **secret** | **str**| A secret to clean graph database. | [default to false]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sync**
> sync(secret, force_analysis_results_sync=force_analysis_results_sync, force_solver_results_sync=force_solver_results_sync)

Force run sync to graph database.

### Example
```python
from __future__ import print_function
import time
import thamos.swagger_client
from thamos.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = thamos.swagger_client.AdminApi()
secret = 'secret_example' # str | A secret to sync graph database.
force_analysis_results_sync = false # bool | Force resync all analysis results. (optional) (default to false)
force_solver_results_sync = false # bool | Force resync all solver results. (optional) (default to false)

try:
    # Force run sync to graph database.
    api_instance.sync(secret, force_analysis_results_sync=force_analysis_results_sync, force_solver_results_sync=force_solver_results_sync)
except ApiException as e:
    print("Exception when calling AdminApi->sync: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **secret** | **str**| A secret to sync graph database. | 
 **force_analysis_results_sync** | **bool**| Force resync all analysis results. | [optional] [default to false]
 **force_solver_results_sync** | **bool**| Force resync all solver results. | [optional] [default to false]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

