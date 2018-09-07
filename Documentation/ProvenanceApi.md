# thamos.swagger_client.ProvenanceApi

All URIs are relative to *https://localhost/api/v1/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_provenance_python**](ProvenanceApi.md#get_provenance_python) | **GET** /provenance/python/{analysis_id} | Retrieve a provenance check result.
[**get_provenance_python_log**](ProvenanceApi.md#get_provenance_python_log) | **GET** /provenance/python/{analysis_id}/log | Show logs of a provenance checks.
[**get_provenance_python_status**](ProvenanceApi.md#get_provenance_python_status) | **GET** /provenance/python/{analysis_id}/status | Show status of a provenance check.
[**post_provenance_python**](ProvenanceApi.md#post_provenance_python) | **POST** /provenance/python | Check provenance of packages stated in an application stack.


# **get_provenance_python**
> get_provenance_python(analysis_id)

Retrieve a provenance check result.

### Example
```python
from __future__ import print_function
import time
import thamos.swagger_client
from thamos.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = thamos.swagger_client.ProvenanceApi()
analysis_id = 'analysis_id_example' # str | Id of analysis to be retrieved.

try:
    # Retrieve a provenance check result.
    api_instance.get_provenance_python(analysis_id)
except ApiException as e:
    print("Exception when calling ProvenanceApi->get_provenance_python: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analysis_id** | **str**| Id of analysis to be retrieved. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_provenance_python_log**
> get_provenance_python_log(analysis_id)

Show logs of a provenance checks.

### Example
```python
from __future__ import print_function
import time
import thamos.swagger_client
from thamos.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = thamos.swagger_client.ProvenanceApi()
analysis_id = 'analysis_id_example' # str | An id of requested analysis.

try:
    # Show logs of a provenance checks.
    api_instance.get_provenance_python_log(analysis_id)
except ApiException as e:
    print("Exception when calling ProvenanceApi->get_provenance_python_log: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analysis_id** | **str**| An id of requested analysis. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_provenance_python_status**
> get_provenance_python_status(analysis_id)

Show status of a provenance check.

### Example
```python
from __future__ import print_function
import time
import thamos.swagger_client
from thamos.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = thamos.swagger_client.ProvenanceApi()
analysis_id = 'analysis_id_example' # str | An id of requested provenance check.

try:
    # Show status of a provenance check.
    api_instance.get_provenance_python_status(analysis_id)
except ApiException as e:
    print("Exception when calling ProvenanceApi->get_provenance_python_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analysis_id** | **str**| An id of requested provenance check. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_provenance_python**
> post_provenance_python(application_stack)

Check provenance of packages stated in an application stack.

### Example
```python
from __future__ import print_function
import time
import thamos.swagger_client
from thamos.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = thamos.swagger_client.ProvenanceApi()
application_stack = thamos.swagger_client.PythonStack() # PythonStack | Pipfile and Pipfile.lock as used by pipenv.

try:
    # Check provenance of packages stated in an application stack.
    api_instance.post_provenance_python(application_stack)
except ApiException as e:
    print("Exception when calling ProvenanceApi->post_provenance_python: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_stack** | [**PythonStack**](PythonStack.md)| Pipfile and Pipfile.lock as used by pipenv. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

