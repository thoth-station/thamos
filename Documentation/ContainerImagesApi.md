# thamos.swagger_client.ContainerImagesApi

All URIs are relative to https://test.thoth-station.ninja/api/v1

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_thoth_container_images**](ContainerImagesApi.md#list_thoth_container_images) | **GET** /container-images | List available Thoth container images

# **list_thoth_container_images**
> ContainerImagesResponse list_thoth_container_images(page=page, per_page=per_page, os_name=os_name, os_version=os_version, python_version=python_version, cuda_version=cuda_version, image_name=image_name, library_name=library_name, symbol=symbol, package_name=package_name, rpm_package_name=rpm_package_name)

List available Thoth container images

### Example
```python
from __future__ import print_function
import time
import thamos.swagger_client
from thamos.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = thamos.swagger_client.ContainerImagesApi()
page = 0 # int | Page offset in pagination (optional) (default to 0)
per_page = 25 # int | Number of items returned per page (optional) (default to 25)
os_name = 'os_name_example' # str | Name of the operating system to consider (optional)
os_version = 'os_version_example' # str | Version of the operating system to consider (optional)
python_version = 'python_version_example' # str | Version of Python interpreter provided (optional)
cuda_version = 'cuda_version_example' # str | Filter based on CUDA version available (optional)
image_name = 'image_name_example' # str | Filter based on the image name (optional)
library_name = 'library_name_example' # str | Filter based on library name (optional)
symbol = 'symbol_example' # str | Filter based on symbol (optional)
package_name = 'package_name_example' # str | Filter based on Python package name (optional)
rpm_package_name = 'rpm_package_name_example' # str | Filter based on RPM package name (optional)

try:
    # List available Thoth container images
    api_response = api_instance.list_thoth_container_images(page=page, per_page=per_page, os_name=os_name, os_version=os_version, python_version=python_version, cuda_version=cuda_version, image_name=image_name, library_name=library_name, symbol=symbol, package_name=package_name, rpm_package_name=rpm_package_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContainerImagesApi->list_thoth_container_images: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page offset in pagination | [optional] [default to 0]
 **per_page** | **int**| Number of items returned per page | [optional] [default to 25]
 **os_name** | **str**| Name of the operating system to consider | [optional]
 **os_version** | **str**| Version of the operating system to consider | [optional]
 **python_version** | **str**| Version of Python interpreter provided | [optional]
 **cuda_version** | **str**| Filter based on CUDA version available | [optional]
 **image_name** | **str**| Filter based on the image name | [optional]
 **library_name** | **str**| Filter based on library name | [optional]
 **symbol** | **str**| Filter based on symbol | [optional]
 **package_name** | **str**| Filter based on Python package name | [optional]
 **rpm_package_name** | **str**| Filter based on RPM package name | [optional]

### Return type

[**ContainerImagesResponse**](ContainerImagesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

