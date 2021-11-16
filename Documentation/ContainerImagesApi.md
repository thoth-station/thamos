# thamos.swagger_client.ContainerImagesApi

All URIs are relative to https://test.thoth-station.ninja/api/v1

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_thoth_container_images**](ContainerImagesApi.md#list_thoth_container_images) | **GET** /container-images | List available Thoth container images.

# **list_thoth_container_images**
> ContainerImagesResponse list_thoth_container_images()

List available Thoth container images.

### Example
```python
from __future__ import print_function
import time
import thamos.swagger_client
from thamos.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = thamos.swagger_client.ContainerImagesApi()

try:
    # List available Thoth container images.
    api_response = api_instance.list_thoth_container_images()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContainerImagesApi->list_thoth_container_images: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ContainerImagesResponse**](ContainerImagesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

