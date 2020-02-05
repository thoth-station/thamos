# thamos.swagger_client.InfoApi

All URIs are relative to *https://test.thoth-station.ninja/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_hardware_environments**](InfoApi.md#list_hardware_environments) | **GET** /hardware-environment | Retrieve a list of supported hardware environments
[**list_python_package_indexes**](InfoApi.md#list_python_package_indexes) | **GET** /python-package-index | List registered Python package indexes.
[**list_runtime_environments**](InfoApi.md#list_runtime_environments) | **GET** /runtime-environment | Retrieve a list of supported runtime environments
[**list_software_environments**](InfoApi.md#list_software_environments) | **GET** /software-environment | Retrieve a list of supported software environments

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
api_instance = thamos.swagger_client.InfoApi()
page = 0 # int | Page offset in pagination. (optional) (default to 0)

try:
    # Retrieve a list of supported hardware environments
    api_response = api_instance.list_hardware_environments(page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InfoApi->list_hardware_environments: %s\n" % e)
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

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_runtime_environments**
> InlineResponse2001 list_runtime_environments()

Retrieve a list of supported runtime environments

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
    # Retrieve a list of supported runtime environments
    api_response = api_instance.list_runtime_environments()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InfoApi->list_runtime_environments: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_software_environments**
> InlineResponse2002 list_software_environments(page=page)

Retrieve a list of supported software environments

### Example
```python
from __future__ import print_function
import time
import thamos.swagger_client
from thamos.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = thamos.swagger_client.InfoApi()
page = 0 # int | Page offset in pagination. (optional) (default to 0)

try:
    # Retrieve a list of supported software environments
    api_response = api_instance.list_software_environments(page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InfoApi->list_software_environments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page offset in pagination. | [optional] [default to 0]

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

