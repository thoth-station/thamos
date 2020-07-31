# thamos.swagger_client.PythonPackagesApi

All URIs are relative to *https://test.thoth-station.ninja/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_python_package_dependencies**](PythonPackagesApi.md#get_python_package_dependencies) | **GET** /python/dependencies | Get direct dependencies of Python libraries. If environment is provided, take into account environment markers that are evaluated during dependencies installation. If environment is not provided, any environment is considered.
[**get_python_package_versions_count**](PythonPackagesApi.md#get_python_package_versions_count) | **GET** /python/packages/count | Retrieve information from the Knowledge Graph with regards to total number of Python packages.
[**list_python_package_indexes**](PythonPackagesApi.md#list_python_package_indexes) | **GET** /python-package-index | List registered Python package indexes.


# **get_python_package_dependencies**
> list[object] get_python_package_dependencies(name, version, index, os_name=os_name, os_version=os_version, python_version=python_version, marker_evaluation_result=marker_evaluation_result)

Get direct dependencies of Python libraries. If environment is provided, take into account environment markers that are evaluated during dependencies installation. If environment is not provided, any environment is considered.

### Example

```python
from __future__ import print_function
import time
import thamos.swagger_client
from thamos.swagger_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://test.thoth-station.ninja/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = thamos.swagger_client.Configuration(
    host = "https://test.thoth-station.ninja/api/v1"
)


# Enter a context with an instance of the API client
with thamos.swagger_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = thamos.swagger_client.PythonPackagesApi(api_client)
    name = 'tensorflow' # str | Name of the Python Package. (default to 'tensorflow')
version = '2.0.0' # str | Version of the Python Package. (default to '2.0.0')
index = 'https://pypi.org/simple' # str | Index url of the Python Package. (default to 'https://pypi.org/simple')
os_name = 'os_name_example' # str | Name of operating system to consider as environment where package is installed in. (optional)
os_version = 'os_version_example' # str | Version of operating system to consider as environment where package is installed in. (optional)
python_version = 'python_version_example' # str | Version of Python interpreter used to install the given package. (optional)
marker_evaluation_result = True # bool | Consider marker evaluation result for the given environment. If set to None, marker evaluation result is not taken into account.  (optional)

    try:
        # Get direct dependencies of Python libraries. If environment is provided, take into account environment markers that are evaluated during dependencies installation. If environment is not provided, any environment is considered.
        api_response = api_instance.get_python_package_dependencies(name, version, index, os_name=os_name, os_version=os_version, python_version=python_version, marker_evaluation_result=marker_evaluation_result)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PythonPackagesApi->get_python_package_dependencies: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the Python Package. | [default to &#39;tensorflow&#39;]
 **version** | **str**| Version of the Python Package. | [default to &#39;2.0.0&#39;]
 **index** | **str**| Index url of the Python Package. | [default to &#39;https://pypi.org/simple&#39;]
 **os_name** | **str**| Name of operating system to consider as environment where package is installed in. | [optional]
 **os_version** | **str**| Version of operating system to consider as environment where package is installed in. | [optional]
 **python_version** | **str**| Version of Python interpreter used to install the given package. | [optional]
 **marker_evaluation_result** | **bool**| Consider marker evaluation result for the given environment. If set to None, marker evaluation result is not taken into account.  | [optional]

### Return type

**list[object]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The number of Python packages in Thoth Knowledge Graph. |  -  |
**404** | The given record does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_python_package_versions_count**
> PythonPackagesCountInfoResponse get_python_package_versions_count(name=name, version=version, index=index)

Retrieve information from the Knowledge Graph with regards to total number of Python packages.

### Example

```python
from __future__ import print_function
import time
import thamos.swagger_client
from thamos.swagger_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://test.thoth-station.ninja/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = thamos.swagger_client.Configuration(
    host = "https://test.thoth-station.ninja/api/v1"
)


# Enter a context with an instance of the API client
with thamos.swagger_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = thamos.swagger_client.PythonPackagesApi(api_client)
    name = 'null' # str | Name of the Python Package. (optional) (default to 'null')
version = 'null' # str | Version of the Python Package. (optional) (default to 'null')
index = 'null' # str | Index url of the Python Package. (optional) (default to 'null')

    try:
        # Retrieve information from the Knowledge Graph with regards to total number of Python packages.
        api_response = api_instance.get_python_package_versions_count(name=name, version=version, index=index)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PythonPackagesApi->get_python_package_versions_count: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the Python Package. | [optional] [default to &#39;null&#39;]
 **version** | **str**| Version of the Python Package. | [optional] [default to &#39;null&#39;]
 **index** | **str**| Index url of the Python Package. | [optional] [default to &#39;null&#39;]

### Return type

[**PythonPackagesCountInfoResponse**](PythonPackagesCountInfoResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The number of Python packages in Thoth Knowledge Graph. |  -  |
**400** | On invalid request. |  -  |
**404** | The given record does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_python_package_indexes**
> list[object] list_python_package_indexes()

List registered Python package indexes.

### Example

```python
from __future__ import print_function
import time
import thamos.swagger_client
from thamos.swagger_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://test.thoth-station.ninja/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = thamos.swagger_client.Configuration(
    host = "https://test.thoth-station.ninja/api/v1"
)


# Enter a context with an instance of the API client
with thamos.swagger_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = thamos.swagger_client.PythonPackagesApi(api_client)

    try:
        # List registered Python package indexes.
        api_response = api_instance.list_python_package_indexes()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PythonPackagesApi->list_python_package_indexes: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**list[object]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Listing of available Python package indexes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
