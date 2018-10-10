# thamos.swagger_client.DependencyMonkeyApi

All URIs are relative to *https://localhost/api/v1/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_dependency_monkey_python_log**](DependencyMonkeyApi.md#get_dependency_monkey_python_log) | **GET** /dependency-monkey/python/{analysis_id}/log | Retrieve a Dependency Monkey run log.
[**get_dependency_monkey_python_status**](DependencyMonkeyApi.md#get_dependency_monkey_python_status) | **GET** /dependency-monkey/python/{analysis_id}/status | Show status of a Dependency Monkey run.
[**post_dependency_monkey_python**](DependencyMonkeyApi.md#post_dependency_monkey_python) | **POST** /dependency-monkey/python | Run Dependency Monkey on the given application stack.


# **get_dependency_monkey_python_log**
> AnalysisLogResponse get_dependency_monkey_python_log(analysis_id)

Retrieve a Dependency Monkey run log.

### Example
```python
from __future__ import print_function
import time
import thamos.swagger_client
from thamos.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = thamos.swagger_client.DependencyMonkeyApi()
analysis_id = 'analysis_id_example' # str | An id of analysis for which log should be retrieved.

try:
    # Retrieve a Dependency Monkey run log.
    api_response = api_instance.get_dependency_monkey_python_log(analysis_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DependencyMonkeyApi->get_dependency_monkey_python_log: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analysis_id** | **str**| An id of analysis for which log should be retrieved. | 

### Return type

[**AnalysisLogResponse**](AnalysisLogResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dependency_monkey_python_status**
> AnalysisStatusResponse get_dependency_monkey_python_status(analysis_id)

Show status of a Dependency Monkey run.

### Example
```python
from __future__ import print_function
import time
import thamos.swagger_client
from thamos.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = thamos.swagger_client.DependencyMonkeyApi()
analysis_id = 'analysis_id_example' # str | An id of requested Dependency Monkey run.

try:
    # Show status of a Dependency Monkey run.
    api_response = api_instance.get_dependency_monkey_python_status(analysis_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DependencyMonkeyApi->get_dependency_monkey_python_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analysis_id** | **str**| An id of requested Dependency Monkey run. | 

### Return type

[**AnalysisStatusResponse**](AnalysisStatusResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_dependency_monkey_python**
> AnalysisResponse post_dependency_monkey_python(application_stack, runtime_environment=runtime_environment, debug=debug)

Run Dependency Monkey on the given application stack.

### Example
```python
from __future__ import print_function
import time
import thamos.swagger_client
from thamos.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = thamos.swagger_client.DependencyMonkeyApi()
application_stack = thamos.swagger_client.PythonStack() # PythonStack | Specification of Python application stack.
runtime_environment = 'runtime_environment_example' # str | Runtime environment in which the given stack will be run.  (optional)
debug = false # bool | Run the given analysis in a verbose mode so developers can debug it.  (optional) (default to false)

try:
    # Run Dependency Monkey on the given application stack.
    api_response = api_instance.post_dependency_monkey_python(application_stack, runtime_environment=runtime_environment, debug=debug)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DependencyMonkeyApi->post_dependency_monkey_python: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_stack** | [**PythonStack**](PythonStack.md)| Specification of Python application stack. | 
 **runtime_environment** | **str**| Runtime environment in which the given stack will be run.  | [optional] 
 **debug** | **bool**| Run the given analysis in a verbose mode so developers can debug it.  | [optional] [default to false]

### Return type

[**AnalysisResponse**](AnalysisResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

