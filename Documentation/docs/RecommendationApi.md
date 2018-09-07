# thamos.swagger_client.RecommendationApi

All URIs are relative to *https://localhost/api/v1/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_recommend_python**](RecommendationApi.md#get_recommend_python) | **GET** /recommend/python/{analysis_id} | Get computeted recommendation based on its id.
[**get_recommend_python_log**](RecommendationApi.md#get_recommend_python_log) | **GET** /recommend/python/{analysis_id}/log | Retrieve a recommendation log.
[**get_recommend_python_status**](RecommendationApi.md#get_recommend_python_status) | **GET** /recommend/python/{analysis_id}/status | Show status of an adviser computing recommendations.
[**list_recommend_python**](RecommendationApi.md#list_recommend_python) | **GET** /recommend/python | Get recommendation results available.
[**post_recommend_python**](RecommendationApi.md#post_recommend_python) | **POST** /recommend/python | Get recommendation for Python ecosystem.


# **get_recommend_python**
> get_recommend_python(analysis_id)

Get computeted recommendation based on its id.

### Example
```python
from __future__ import print_function
import time
import thamos.swagger_client
from thamos.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = thamos.swagger_client.RecommendationApi()
analysis_id = 'analysis_id_example' # str | Recommendation ID returned on recommendation request.

try:
    # Get computeted recommendation based on its id.
    api_instance.get_recommend_python(analysis_id)
except ApiException as e:
    print("Exception when calling RecommendationApi->get_recommend_python: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analysis_id** | **str**| Recommendation ID returned on recommendation request. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_recommend_python_log**
> get_recommend_python_log(analysis_id)

Retrieve a recommendation log.

### Example
```python
from __future__ import print_function
import time
import thamos.swagger_client
from thamos.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = thamos.swagger_client.RecommendationApi()
analysis_id = 'analysis_id_example' # str | An id of analysis for which log should be retrieved.

try:
    # Retrieve a recommendation log.
    api_instance.get_recommend_python_log(analysis_id)
except ApiException as e:
    print("Exception when calling RecommendationApi->get_recommend_python_log: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analysis_id** | **str**| An id of analysis for which log should be retrieved. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_recommend_python_status**
> get_recommend_python_status(analysis_id)

Show status of an adviser computing recommendations.

### Example
```python
from __future__ import print_function
import time
import thamos.swagger_client
from thamos.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = thamos.swagger_client.RecommendationApi()
analysis_id = 'analysis_id_example' # str | An id of requested recommendation.

try:
    # Show status of an adviser computing recommendations.
    api_instance.get_recommend_python_status(analysis_id)
except ApiException as e:
    print("Exception when calling RecommendationApi->get_recommend_python_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analysis_id** | **str**| An id of requested recommendation. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_recommend_python**
> list_recommend_python(page=page)

Get recommendation results available.

### Example
```python
from __future__ import print_function
import time
import thamos.swagger_client
from thamos.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = thamos.swagger_client.RecommendationApi()
page = 0 # int | Page offset in pagination. (optional) (default to 0)

try:
    # Get recommendation results available.
    api_instance.list_recommend_python(page=page)
except ApiException as e:
    print("Exception when calling RecommendationApi->list_recommend_python: %s\n" % e)
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

# **post_recommend_python**
> post_recommend_python(application_stack, type, runtime_environment=runtime_environment, debug=debug)

Get recommendation for Python ecosystem.

### Example
```python
from __future__ import print_function
import time
import thamos.swagger_client
from thamos.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = thamos.swagger_client.RecommendationApi()
application_stack = thamos.swagger_client.PythonStack() # PythonStack | Specification of Python application stack.
type = 'stable' # str | Recommendation type. (default to stable)
runtime_environment = 'runtime_environment_example' # str | Runtime environment in which the given stack will be run. (optional)
debug = false # bool | Run the given recommendation engine in a verbose mode so developers can debug it.  (optional) (default to false)

try:
    # Get recommendation for Python ecosystem.
    api_instance.post_recommend_python(application_stack, type, runtime_environment=runtime_environment, debug=debug)
except ApiException as e:
    print("Exception when calling RecommendationApi->post_recommend_python: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_stack** | [**PythonStack**](PythonStack.md)| Specification of Python application stack. | 
 **type** | **str**| Recommendation type. | [default to stable]
 **runtime_environment** | **str**| Runtime environment in which the given stack will be run. | [optional] 
 **debug** | **bool**| Run the given recommendation engine in a verbose mode so developers can debug it.  | [optional] [default to false]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

