# thamos.swagger_client.AdviseApi

All URIs are relative to *https://localhost/api/v1/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_advise_python**](AdviseApi.md#get_advise_python) | **GET** /advise/python/{analysis_id} | Get computeted adviser result based on its id.
[**get_advise_python_log**](AdviseApi.md#get_advise_python_log) | **GET** /advise/python/{analysis_id}/log | Retrieve a adviser run log.
[**get_advise_python_status**](AdviseApi.md#get_advise_python_status) | **GET** /advise/python/{analysis_id}/status | Show status of an adviser computing recomemendations.
[**list_advise_python**](AdviseApi.md#list_advise_python) | **GET** /advise/python | Get adviser results available.
[**post_advise_python**](AdviseApi.md#post_advise_python) | **POST** /advise/python | Get advise for Python ecosystem.


# **get_advise_python**
> AnalysisResultResponse get_advise_python(analysis_id)

Get computeted adviser result based on its id.

### Example
```python
from __future__ import print_function
import time
import thamos.swagger_client
from thamos.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = thamos.swagger_client.AdviseApi()
analysis_id = 'analysis_id_example' # str | Advise id returned on advise request.

try:
    # Get computeted adviser result based on its id.
    api_response = api_instance.get_advise_python(analysis_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdviseApi->get_advise_python: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analysis_id** | **str**| Advise id returned on advise request. | 

### Return type

[**AnalysisResultResponse**](AnalysisResultResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_advise_python_log**
> AnalysisLogResponse get_advise_python_log(analysis_id)

Retrieve a adviser run log.

### Example
```python
from __future__ import print_function
import time
import thamos.swagger_client
from thamos.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = thamos.swagger_client.AdviseApi()
analysis_id = 'analysis_id_example' # str | An id of analysis for which log should be retrieved.

try:
    # Retrieve a adviser run log.
    api_response = api_instance.get_advise_python_log(analysis_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdviseApi->get_advise_python_log: %s\n" % e)
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

# **get_advise_python_status**
> AnalysisStatusResponse get_advise_python_status(analysis_id)

Show status of an adviser computing recomemendations.

### Example
```python
from __future__ import print_function
import time
import thamos.swagger_client
from thamos.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = thamos.swagger_client.AdviseApi()
analysis_id = 'analysis_id_example' # str | An id of requested adviser run.

try:
    # Show status of an adviser computing recomemendations.
    api_response = api_instance.get_advise_python_status(analysis_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdviseApi->get_advise_python_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analysis_id** | **str**| An id of requested adviser run. | 

### Return type

[**AnalysisStatusResponse**](AnalysisStatusResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_advise_python**
> AnalysisListingResponse list_advise_python(page=page)

Get adviser results available.

### Example
```python
from __future__ import print_function
import time
import thamos.swagger_client
from thamos.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = thamos.swagger_client.AdviseApi()
page = 0 # int | Page offset in pagination. (optional) (default to 0)

try:
    # Get adviser results available.
    api_response = api_instance.list_advise_python(page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdviseApi->list_advise_python: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page offset in pagination. | [optional] [default to 0]

### Return type

[**AnalysisListingResponse**](AnalysisListingResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_advise_python**
> AnalysisResponse post_advise_python(application_stack, recommendation_type, runtime_environment=runtime_environment, debug=debug)

Get advise for Python ecosystem.

### Example
```python
from __future__ import print_function
import time
import thamos.swagger_client
from thamos.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = thamos.swagger_client.AdviseApi()
application_stack = thamos.swagger_client.PythonStack() # PythonStack | Specification of Python application stack.
recommendation_type = 'stable' # str | Recommendation type. (default to stable)
runtime_environment = 'runtime_environment_example' # str | Runtime environment in which the given stack will be run.  (optional)
debug = false # bool | Run the given adviser in a verbose mode so developers can debug it.  (optional) (default to false)

try:
    # Get advise for Python ecosystem.
    api_response = api_instance.post_advise_python(application_stack, recommendation_type, runtime_environment=runtime_environment, debug=debug)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdviseApi->post_advise_python: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_stack** | [**PythonStack**](PythonStack.md)| Specification of Python application stack. | 
 **recommendation_type** | **str**| Recommendation type. | [default to stable]
 **runtime_environment** | **str**| Runtime environment in which the given stack will be run.  | [optional] 
 **debug** | **bool**| Run the given adviser in a verbose mode so developers can debug it.  | [optional] [default to false]

### Return type

[**AnalysisResponse**](AnalysisResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

