# thamos.swagger_client.EnvironmentsApi

All URIs are relative to *https://localhost/api/v1/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_runtime_environment**](EnvironmentsApi.md#get_runtime_environment) | **GET** /runtime-environment/{runtime_environment_name} | Retrieve runtime environment information.
[**list_runtime_environment_analyses**](EnvironmentsApi.md#list_runtime_environment_analyses) | **GET** /runtime-environment/{runtime_environment_name}/analyses | List analyses for the given runtime environment.
[**list_runtime_environments**](EnvironmentsApi.md#list_runtime_environments) | **GET** /runtime-environment | Retrieve a list of runtime environments analyzed.


# **get_runtime_environment**
> dict(str, ERRORUNKNOWN) get_runtime_environment(runtime_environment_name, analysis_id=analysis_id)

Retrieve runtime environment information.

### Example
```python
from __future__ import print_function
import time
import thamos.swagger_client
from thamos.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = thamos.swagger_client.EnvironmentsApi()
runtime_environment_name = 'runtime_environment_name_example' # str | Runtime environment name to be retrieved.
analysis_id = 'analysis_id_example' # str | Specify analysis id for which results should be retrieved. If omitted, the latest will be used.  (optional)

try:
    # Retrieve runtime environment information.
    api_response = api_instance.get_runtime_environment(runtime_environment_name, analysis_id=analysis_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnvironmentsApi->get_runtime_environment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **runtime_environment_name** | **str**| Runtime environment name to be retrieved. | 
 **analysis_id** | **str**| Specify analysis id for which results should be retrieved. If omitted, the latest will be used.  | [optional] 

### Return type

[**dict(str, ERRORUNKNOWN)**](ERRORUNKNOWN.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_runtime_environment_analyses**
> dict(str, ERRORUNKNOWN) list_runtime_environment_analyses(runtime_environment_name, page=page)

List analyses for the given runtime environment.

### Example
```python
from __future__ import print_function
import time
import thamos.swagger_client
from thamos.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = thamos.swagger_client.EnvironmentsApi()
runtime_environment_name = 'runtime_environment_name_example' # str | Runtime environment name for which analyses should be retrieved. 
page = 0 # int | Page offset in pagination. (optional) (default to 0)

try:
    # List analyses for the given runtime environment.
    api_response = api_instance.list_runtime_environment_analyses(runtime_environment_name, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnvironmentsApi->list_runtime_environment_analyses: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **runtime_environment_name** | **str**| Runtime environment name for which analyses should be retrieved.  | 
 **page** | **int**| Page offset in pagination. | [optional] [default to 0]

### Return type

[**dict(str, ERRORUNKNOWN)**](ERRORUNKNOWN.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_runtime_environments**
> dict(str, ERRORUNKNOWN) list_runtime_environments(page=page)

Retrieve a list of runtime environments analyzed.

### Example
```python
from __future__ import print_function
import time
import thamos.swagger_client
from thamos.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = thamos.swagger_client.EnvironmentsApi()
page = 0 # int | Page offset in pagination. (optional) (default to 0)

try:
    # Retrieve a list of runtime environments analyzed.
    api_response = api_instance.list_runtime_environments(page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnvironmentsApi->list_runtime_environments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page offset in pagination. | [optional] [default to 0]

### Return type

[**dict(str, ERRORUNKNOWN)**](ERRORUNKNOWN.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

