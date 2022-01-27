# thamos.swagger_client.PythonPackagesApi

All URIs are relative to https://test.thoth-station.ninja/api/v1

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_package_from_imported_packages**](PythonPackagesApi.md#get_package_from_imported_packages) | **GET** /python/imports | List imported packages&#x27; (name, version, index)
[**get_python_package_dependencies**](PythonPackagesApi.md#get_python_package_dependencies) | **GET** /python/package/dependencies | Get direct dependencies of Python libraries. If environment is provided, take into account environment markers that are evaluated during dependencies installation. If environment is not provided, any environment is considered
[**get_python_package_version_metadata**](PythonPackagesApi.md#get_python_package_version_metadata) | **GET** /python/package/version/metadata | Get metadata for the given package
[**get_python_platform**](PythonPackagesApi.md#get_python_platform) | **GET** /python/platform | Get supported platforms for the Python ecosystem
[**list_python_package_indexes**](PythonPackagesApi.md#list_python_package_indexes) | **GET** /python-package-index | List registered Python package indexes
[**list_python_package_version_environments**](PythonPackagesApi.md#list_python_package_version_environments) | **GET** /python/package/version/environments | List environments used to solve the given Python package
[**list_python_package_versions**](PythonPackagesApi.md#list_python_package_versions) | **GET** /python/package/versions | List versions of the given Python package
[**list_python_packages**](PythonPackagesApi.md#list_python_packages) | **GET** /python/package | List Python packages

# **get_package_from_imported_packages**
> PythonPackageNameImportResponse get_package_from_imported_packages(import_name)

List imported packages' (name, version, index)

### Example
```python
from __future__ import print_function
import time
import thamos.swagger_client
from thamos.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = thamos.swagger_client.PythonPackagesApi()
import_name = 'import_name_example' # str | Names of the Python Packages (name, version, index) for the given import package name

try:
    # List imported packages' (name, version, index)
    api_response = api_instance.get_package_from_imported_packages(import_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PythonPackagesApi->get_package_from_imported_packages: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **import_name** | **str**| Names of the Python Packages (name, version, index) for the given import package name  |

### Return type

[**PythonPackageNameImportResponse**](PythonPackageNameImportResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_python_package_dependencies**
> PythonPackageDependencies get_python_package_dependencies(name, version, index, os_name=os_name, os_version=os_version, python_version=python_version, marker_evaluation_result=marker_evaluation_result)

Get direct dependencies of Python libraries. If environment is provided, take into account environment markers that are evaluated during dependencies installation. If environment is not provided, any environment is considered

### Example
```python
from __future__ import print_function
import time
import thamos.swagger_client
from thamos.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = thamos.swagger_client.PythonPackagesApi()
name = 'name_example' # str | Name of the Python Package
version = 'version_example' # str | Version of the Python Package
index = 'https://pypi.org/simple' # str | Index url of the Python Package (default to https://pypi.org/simple)
os_name = 'os_name_example' # str | Name of the operating system to consider (optional)
os_version = 'os_version_example' # str | Version of the operating system to consider (optional)
python_version = 'python_version_example' # str | Version of Python interpreter provided (optional)
marker_evaluation_result = true # bool | Consider marker evaluation result for the given environment. If set to None, marker evaluation result is not taken into account  (optional)

try:
    # Get direct dependencies of Python libraries. If environment is provided, take into account environment markers that are evaluated during dependencies installation. If environment is not provided, any environment is considered
    api_response = api_instance.get_python_package_dependencies(name, version, index, os_name=os_name, os_version=os_version, python_version=python_version, marker_evaluation_result=marker_evaluation_result)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PythonPackagesApi->get_python_package_dependencies: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the Python Package |
 **version** | **str**| Version of the Python Package |
 **index** | **str**| Index url of the Python Package | [default to https://pypi.org/simple]
 **os_name** | **str**| Name of the operating system to consider | [optional]
 **os_version** | **str**| Version of the operating system to consider | [optional]
 **python_version** | **str**| Version of Python interpreter provided | [optional]
 **marker_evaluation_result** | **bool**| Consider marker evaluation result for the given environment. If set to None, marker evaluation result is not taken into account  | [optional]

### Return type

[**PythonPackageDependencies**](PythonPackageDependencies.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_python_package_version_metadata**
> PythonPackageVersionMetadataResponse get_python_package_version_metadata(name, version, index, os_name, os_version, python_version)

Get metadata for the given package

### Example
```python
from __future__ import print_function
import time
import thamos.swagger_client
from thamos.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = thamos.swagger_client.PythonPackagesApi()
name = 'name_example' # str | Name of the Python Package
version = 'version_example' # str | Version of the Python Package
index = 'https://pypi.org/simple' # str | Index url of the Python Package (default to https://pypi.org/simple)
os_name = 'os_name_example' # str | Name of operating system to consider as environment where package is installed in
os_version = 'os_version_example' # str | Version of operating system to consider as environment where package is installed in
python_version = 'python_version_example' # str | Version of Python interpreter used to install the given package

try:
    # Get metadata for the given package
    api_response = api_instance.get_python_package_version_metadata(name, version, index, os_name, os_version, python_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PythonPackagesApi->get_python_package_version_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the Python Package |
 **version** | **str**| Version of the Python Package |
 **index** | **str**| Index url of the Python Package | [default to https://pypi.org/simple]
 **os_name** | **str**| Name of operating system to consider as environment where package is installed in |
 **os_version** | **str**| Version of operating system to consider as environment where package is installed in |
 **python_version** | **str**| Version of Python interpreter used to install the given package |

### Return type

[**PythonPackageVersionMetadataResponse**](PythonPackageVersionMetadataResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_python_platform**
> PythonPlatforms get_python_platform()

Get supported platforms for the Python ecosystem

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
    # Get supported platforms for the Python ecosystem
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

List registered Python package indexes

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
    # List registered Python package indexes
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

# **list_python_package_version_environments**
> PythonPackageVersionEnvironmentsResponse list_python_package_version_environments(name, version, index)

List environments used to solve the given Python package

### Example
```python
from __future__ import print_function
import time
import thamos.swagger_client
from thamos.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = thamos.swagger_client.PythonPackagesApi()
name = 'name_example' # str | Name of the Python Package
version = 'version_example' # str | Version of the Python Package
index = 'https://pypi.org/simple' # str | Index url of the Python Package (default to https://pypi.org/simple)

try:
    # List environments used to solve the given Python package
    api_response = api_instance.list_python_package_version_environments(name, version, index)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PythonPackagesApi->list_python_package_version_environments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the Python Package |
 **version** | **str**| Version of the Python Package |
 **index** | **str**| Index url of the Python Package | [default to https://pypi.org/simple]

### Return type

[**PythonPackageVersionEnvironmentsResponse**](PythonPackageVersionEnvironmentsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_python_package_versions**
> PythonPackageVersionsResponse list_python_package_versions(name, page=page, per_page=per_page, os_name=os_name, os_version=os_version, python_version=python_version)

List versions of the given Python package

### Example
```python
from __future__ import print_function
import time
import thamos.swagger_client
from thamos.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = thamos.swagger_client.PythonPackagesApi()
name = 'name_example' # str | Name of the Python Package
page = 0 # int | Page offset in pagination (optional) (default to 0)
per_page = 25 # int | Number of items returned per page (optional) (default to 25)
os_name = 'os_name_example' # str | Name of the operating system to consider (optional)
os_version = 'os_version_example' # str | Version of the operating system to consider (optional)
python_version = 'python_version_example' # str | Version of Python interpreter provided (optional)

try:
    # List versions of the given Python package
    api_response = api_instance.list_python_package_versions(name, page=page, per_page=per_page, os_name=os_name, os_version=os_version, python_version=python_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PythonPackagesApi->list_python_package_versions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the Python Package |
 **page** | **int**| Page offset in pagination | [optional] [default to 0]
 **per_page** | **int**| Number of items returned per page | [optional] [default to 25]
 **os_name** | **str**| Name of the operating system to consider | [optional]
 **os_version** | **str**| Version of the operating system to consider | [optional]
 **python_version** | **str**| Version of Python interpreter provided | [optional]

### Return type

[**PythonPackageVersionsResponse**](PythonPackageVersionsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_python_packages**
> PythonPackagesResponse list_python_packages(page=page, per_page=per_page, os_name=os_name, os_version=os_version, python_version=python_version)

List Python packages

### Example
```python
from __future__ import print_function
import time
import thamos.swagger_client
from thamos.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = thamos.swagger_client.PythonPackagesApi()
page = 0 # int | Page offset in pagination (optional) (default to 0)
per_page = 25 # int | Number of items returned per page (optional) (default to 25)
os_name = 'os_name_example' # str | Name of the operating system to consider (optional)
os_version = 'os_version_example' # str | Version of the operating system to consider (optional)
python_version = 'python_version_example' # str | Version of Python interpreter provided (optional)

try:
    # List Python packages
    api_response = api_instance.list_python_packages(page=page, per_page=per_page, os_name=os_name, os_version=os_version, python_version=python_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PythonPackagesApi->list_python_packages: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page offset in pagination | [optional] [default to 0]
 **per_page** | **int**| Number of items returned per page | [optional] [default to 25]
 **os_name** | **str**| Name of the operating system to consider | [optional]
 **os_version** | **str**| Version of the operating system to consider | [optional]
 **python_version** | **str**| Version of Python interpreter provided | [optional]

### Return type

[**PythonPackagesResponse**](PythonPackagesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

