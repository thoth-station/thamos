# thamos.swagger_client.EcosystemSolverApi

All URIs are relative to *https://localhost/api/v1/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_solve_python**](EcosystemSolverApi.md#get_solve_python) | **GET** /solve/python/{analysis_id} | Retrieve a solver result.
[**get_solve_python_log**](EcosystemSolverApi.md#get_solve_python_log) | **GET** /solve/python/{analysis_id}/log | Retrieve a solver log.
[**get_solve_python_status**](EcosystemSolverApi.md#get_solve_python_status) | **GET** /solve/python/{analysis_id}/status | Show status of an ecosystem solver.
[**list_solve_python_results**](EcosystemSolverApi.md#list_solve_python_results) | **GET** /solve/python | Retrieve a list of document ids for solver results.
[**list_solvers**](EcosystemSolverApi.md#list_solvers) | **GET** /solvers | Retrieve a list of solvers installed and available.
[**post_solve_python**](EcosystemSolverApi.md#post_solve_python) | **POST** /solve/python | Solve the given application stack.


# **get_solve_python**
> get_solve_python(analysis_id)

Retrieve a solver result.

### Example
```python
from __future__ import print_function
import time
import thamos.swagger_client
from thamos.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = thamos.swagger_client.EcosystemSolverApi()
analysis_id = 'analysis_id_example' # str | Document id to be retrieved.

try:
    # Retrieve a solver result.
    api_instance.get_solve_python(analysis_id)
except ApiException as e:
    print("Exception when calling EcosystemSolverApi->get_solve_python: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analysis_id** | **str**| Document id to be retrieved. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_solve_python_log**
> get_solve_python_log(analysis_id)

Retrieve a solver log.

### Example
```python
from __future__ import print_function
import time
import thamos.swagger_client
from thamos.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = thamos.swagger_client.EcosystemSolverApi()
analysis_id = 'analysis_id_example' # str | An id of analysis for a solver run.

try:
    # Retrieve a solver log.
    api_instance.get_solve_python_log(analysis_id)
except ApiException as e:
    print("Exception when calling EcosystemSolverApi->get_solve_python_log: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analysis_id** | **str**| An id of analysis for a solver run. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_solve_python_status**
> get_solve_python_status(analysis_id)

Show status of an ecosystem solver.

### Example
```python
from __future__ import print_function
import time
import thamos.swagger_client
from thamos.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = thamos.swagger_client.EcosystemSolverApi()
analysis_id = 'analysis_id_example' # str | An id of requested ecosystem solver run.

try:
    # Show status of an ecosystem solver.
    api_instance.get_solve_python_status(analysis_id)
except ApiException as e:
    print("Exception when calling EcosystemSolverApi->get_solve_python_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analysis_id** | **str**| An id of requested ecosystem solver run. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_solve_python_results**
> list_solve_python_results(page=page)

Retrieve a list of document ids for solver results.

### Example
```python
from __future__ import print_function
import time
import thamos.swagger_client
from thamos.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = thamos.swagger_client.EcosystemSolverApi()
page = 0 # int | Page offset in pagination. (optional) (default to 0)

try:
    # Retrieve a list of document ids for solver results.
    api_instance.list_solve_python_results(page=page)
except ApiException as e:
    print("Exception when calling EcosystemSolverApi->list_solve_python_results: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page offset in pagination. | [optional] [default to 0]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_solvers**
> list_solvers()

Retrieve a list of solvers installed and available.

### Example
```python
from __future__ import print_function
import time
import thamos.swagger_client
from thamos.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = thamos.swagger_client.EcosystemSolverApi()

try:
    # Retrieve a list of solvers installed and available.
    api_instance.list_solvers()
except ApiException as e:
    print("Exception when calling EcosystemSolverApi->list_solvers: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_solve_python**
> post_solve_python(packages, solver=solver, debug=debug, transitive=transitive)

Solve the given application stack.

### Example
```python
from __future__ import print_function
import time
import thamos.swagger_client
from thamos.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = thamos.swagger_client.EcosystemSolverApi()
packages = thamos.swagger_client.Packages() # Packages | Packages to be solved.
solver = 'solver_example' # str | Name of solver to be triggered. (optional)
debug = false # bool | Run the given analyzer in a verbose mode so developers can debug analyzer.  (optional) (default to false)
transitive = true # bool | Packages to be solved. (optional) (default to true)

try:
    # Solve the given application stack.
    api_instance.post_solve_python(packages, solver=solver, debug=debug, transitive=transitive)
except ApiException as e:
    print("Exception when calling EcosystemSolverApi->post_solve_python: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **packages** | [**Packages**](Packages.md)| Packages to be solved. | 
 **solver** | **str**| Name of solver to be triggered. | [optional] 
 **debug** | **bool**| Run the given analyzer in a verbose mode so developers can debug analyzer.  | [optional] [default to false]
 **transitive** | **bool**| Packages to be solved. | [optional] [default to true]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

