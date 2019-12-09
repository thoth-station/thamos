# thamos.swagger_client.PythonPackagesApi

All URIs are relative to *https://test.thoth-station.ninja/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_python_package_versions_count**](PythonPackagesApi.md#get_python_package_versions_count) | **GET** /python/packages/count | Retrieve information from the Knowledge Graph with regards to total number of Python packages. 

# **get_python_package_versions_count**
> PythonPackagesCountInfoResponse get_python_package_versions_count()

Retrieve information from the Knowledge Graph with regards to total number of Python packages. 

### Example
```python
from __future__ import print_function
import time
import thamos.swagger_client
from thamos.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = thamos.swagger_client.PythonPackagesApi()

try:
    # Retrieve information from the Knowledge Graph with regards to total number of Python packages. 
    api_response = api_instance.get_python_package_versions_count()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PythonPackagesApi->get_python_package_versions_count: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**PythonPackagesCountInfoResponse**](PythonPackagesCountInfoResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

