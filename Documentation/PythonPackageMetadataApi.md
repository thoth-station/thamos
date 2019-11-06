# thamos.swagger_client.PythonPackageMetadataApi

All URIs are relative to *https://test.thoth-station.ninja/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_package_metadata**](PythonPackageMetadataApi.md#get_package_metadata) | **GET** /python/package/metadata | Retrieve metadata relative to a Python Package from the Knowledge Graph. 

# **get_package_metadata**
> PythonPackageMetadataResponse get_package_metadata(name, version, index)

Retrieve metadata relative to a Python Package from the Knowledge Graph. 

### Example
```python
from __future__ import print_function
import time
import thamos.swagger_client
from thamos.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = thamos.swagger_client.PythonPackageMetadataApi()
name = 'name_example' # str | Name of the Python Package.
version = 'version_example' # str | Version of the Python Package.
index = 'index_example' # str | Index url of the Python Package.

try:
    # Retrieve metadata relative to a Python Package from the Knowledge Graph. 
    api_response = api_instance.get_package_metadata(name, version, index)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PythonPackageMetadataApi->get_package_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the Python Package. | 
 **version** | **str**| Version of the Python Package. | 
 **index** | **str**| Index url of the Python Package. | 

### Return type

[**PythonPackageMetadataResponse**](PythonPackageMetadataResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

