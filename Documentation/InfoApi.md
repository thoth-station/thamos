# thamos.swagger_client.InfoApi

All URIs are relative to *https://localhost/api/v1/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_python_package_indexes**](InfoApi.md#list_python_package_indexes) | **GET** /python-package-index | List registered Python package indexes.


# **list_python_package_indexes**
> PythonPackageIndexes list_python_package_indexes()

List registered Python package indexes.

### Example
```python
from __future__ import print_function
import time
import thamos.swagger_client
from thamos.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = thamos.swagger_client.InfoApi()

try:
    # List registered Python package indexes.
    api_response = api_instance.list_python_package_indexes()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InfoApi->list_python_package_indexes: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**PythonPackageIndexes**](PythonPackageIndexes.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

