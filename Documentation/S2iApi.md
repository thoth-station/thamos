# thamos.swagger_client.S2iApi

All URIs are relative to https://test.thoth-station.ninja/api/v1

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_s2i_python**](S2iApi.md#list_s2i_python) | **GET** /s2i/python | Get available S2I base container images for Python applications.

# **list_s2i_python**
> S2IPythonResponse list_s2i_python()

Get available S2I base container images for Python applications.

### Example
```python
from __future__ import print_function
import time
import thamos.swagger_client
from thamos.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = thamos.swagger_client.S2iApi()

try:
    # Get available S2I base container images for Python applications.
    api_response = api_instance.list_s2i_python()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling S2iApi->list_s2i_python: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**S2IPythonResponse**](S2IPythonResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
