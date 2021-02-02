# thamos.swagger_client.HardwareApi

All URIs are relative to https://test.thoth-station.ninja/api/v1

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_hardware_environments**](HardwareApi.md#list_hardware_environments) | **GET** /hardware | Retrieve a list of supported hardware environments

# **list_hardware_environments**
> InlineResponse200 list_hardware_environments(page=page)

Retrieve a list of supported hardware environments

### Example
```python
from __future__ import print_function
import time
import thamos.swagger_client
from thamos.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = thamos.swagger_client.HardwareApi()
page = 0 # int | Page offset in pagination. (optional) (default to 0)

try:
    # Retrieve a list of supported hardware environments
    api_response = api_instance.list_hardware_environments(page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HardwareApi->list_hardware_environments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page offset in pagination. | [optional] [default to 0]

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
