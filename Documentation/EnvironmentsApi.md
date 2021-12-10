# thamos.swagger_client.EnvironmentsApi

All URIs are relative to https://test.thoth-station.ninja/api/v1

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_environments**](EnvironmentsApi.md#get_environments) | **GET** /python/environment | Get environments available for Python resolutions.

# **get_environments**
> PythonEnvironments get_environments()

Get environments available for Python resolutions.

### Example
```python
from __future__ import print_function
import time
import thamos.swagger_client
from thamos.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = thamos.swagger_client.EnvironmentsApi()

try:
    # Get environments available for Python resolutions.
    api_response = api_instance.get_environments()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnvironmentsApi->get_environments: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**PythonEnvironments**](PythonEnvironments.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

