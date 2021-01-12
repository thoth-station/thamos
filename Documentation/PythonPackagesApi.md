# thamos.swagger_client.PythonPackagesApi

All URIs are relative to https://test.thoth-station.ninja/api/v1

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_package_metadata**](PythonPackagesApi.md#get_package_metadata) | **GET** /python/package/metadata | Retrieve metadata relative to a Python Package from the Knowledge Graph.
[**get_python_package_dependencies**](PythonPackagesApi.md#get_python_package_dependencies) | **GET** /python/package/dependencies | Get direct dependencies of Python libraries. If environment is provided, take into account environment markers that are evaluated during dependencies installation. If environment is not provided, any environment is considered.
[**get_python_package_versions_count**](PythonPackagesApi.md#get_python_package_versions_count) | **GET** /python/packages/count | Retrieve information from the Knowledge Graph with regards to total number of Python packages.
[**get_python_platform**](PythonPackagesApi.md#get_python_platform) | **GET** /python/platform | Get supported platforms for Python ecosystem.
[**list_python_package_indexes**](PythonPackagesApi.md#list_python_package_indexes) | **GET** /python-package-index | List registered Python package indexes.
[**list_python_package_versions**](PythonPackagesApi.md#list_python_package_versions) | **GET** /python/package/versions | List versions of the given Python package.

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
api_instance = thamos.swagger_client.PythonPackagesApi()
name = 'tensorflow' # str | Name of the Python Package. (default to tensorflow)
version = '2.0.0' # str | Version of the Python Package. (default to 2.0.0)
index = 'https://pypi.org/simple' # str | Index url of the Python Package. (default to https://pypi.org/simple)

try:
    # Retrieve metadata relative to a Python Package from the Knowledge Graph.
    api_response = api_instance.get_package_metadata(name, version, index)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PythonPackagesApi->get_package_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the Python Package. | [default to tensorflow]
 **version** | **str**| Version of the Python Package. | [default to 2.0.0]
 **index** | **str**| Index url of the Python Package. | [default to https://pypi.org/simple]

### Return type

[**PythonPackageMetadataResponse**](PythonPackageMetadataResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_python_package_dependencies**
> PythonPackageDependencies get_python_package_dependencies(name, version, index, os_name=os_name, os_version=os_version, python_version=python_version, marker_evaluation_result=marker_evaluation_result)

Get direct dependencies of Python libraries. If environment is provided, take into account environment markers that are evaluated during dependencies installation. If environment is not provided, any environment is considered.

### Example
```python
from __future__ import print_function
import time
import thamos.swagger_client
from thamos.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = thamos.swagger_client.PythonPackagesApi()
name = 'tensorflow' # str | Name of the Python Package. (default to tensorflow)
version = '2.0.0' # str | Version of the Python Package. (default to 2.0.0)
index = 'https://pypi.org/simple' # str | Index url of the Python Package. (default to https://pypi.org/simple)
os_name = 'os_name_example' # str | Name of operating system to consider as environment where package is installed in. (optional)
os_version = 'os_version_example' # str | Version of operating system to consider as environment where package is installed in. (optional)
python_version = 'python_version_example' # str | Version of Python interpreter used to install the given package. (optional)
marker_evaluation_result = true # bool | Consider marker evaluation result for the given environment. If set to None, marker evaluation result is not taken into account.  (optional)

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
 **name** | **str**| Name of the Python Package. | [default to tensorflow]
 **version** | **str**| Version of the Python Package. | [default to 2.0.0]
 **index** | **str**| Index url of the Python Package. | [default to https://pypi.org/simple]
 **os_name** | **str**| Name of operating system to consider as environment where package is installed in. | [optional]
 **os_version** | **str**| Version of operating system to consider as environment where package is installed in. | [optional]
 **python_version** | **str**| Version of Python interpreter used to install the given package. | [optional]
 **marker_evaluation_result** | **bool**| Consider marker evaluation result for the given environment. If set to None, marker evaluation result is not taken into account.  | [optional]

### Return type

[**PythonPackageDependencies**](PythonPackageDependencies.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

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

# create an instance of the API class
api_instance = thamos.swagger_client.PythonPackagesApi()
name = 'null' # str | Name of the Python Package. (optional) (default to null)
version = 'null' # str | Version of the Python Package. (optional) (default to null)
index = 'null' # str | Index url of the Python Package. (optional) (default to null)

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
 **name** | **str**| Name of the Python Package. | [optional] [default to null]
 **version** | **str**| Version of the Python Package. | [optional] [default to null]
 **index** | **str**| Index url of the Python Package. | [optional] [default to null]

### Return type

[**PythonPackagesCountInfoResponse**](PythonPackagesCountInfoResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_python_platform**
> PythonPlatforms get_python_platform()

Get supported platforms for Python ecosystem.

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
    # Get supported platforms for Python ecosystem.
    api_response = api_instance.get_python_platform()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PythonPackagesApi->get_python_platform: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**PythonPlatforms**](PythonPlatforms.md)

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
api_instance = thamos.swagger_client.PythonPackagesApi()

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

[**PythonPackageIndexes**](PythonPackageIndexes.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_python_package_versions**
> PythonPackageVersionsResponse list_python_package_versions(name, page=page)

List versions of the given Python package.

### Example
```python
from __future__ import print_function
import time
import thamos.swagger_client
from thamos.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = thamos.swagger_client.PythonPackagesApi()
name = 'tensorflow' # str | Name of the Python Package. (default to tensorflow)
page = 0 # int | Page offset in pagination. (optional) (default to 0)

try:
    # List versions of the given Python package.
    api_response = api_instance.list_python_package_versions(name, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PythonPackagesApi->list_python_package_versions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the Python Package. | [default to tensorflow]
 **page** | **int**| Page offset in pagination. | [optional] [default to 0]

### Return type

[**PythonPackageVersionsResponse**](PythonPackageVersionsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
