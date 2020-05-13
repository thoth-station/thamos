# thamos.swagger_client.ProvenanceApi

All URIs are relative to *https://test.thoth-station.ninja/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_provenance_python**](ProvenanceApi.md#get_provenance_python) | **GET** /provenance/python/{analysis_id} | Retrieve a provenance check result.
[**get_provenance_python_log**](ProvenanceApi.md#get_provenance_python_log) | **GET** /provenance/python/{analysis_id}/log | Show logs of a provenance checks.
[**get_provenance_python_status**](ProvenanceApi.md#get_provenance_python_status) | **GET** /provenance/python/{analysis_id}/status | Show status of a provenance check.
[**post_provenance_python**](ProvenanceApi.md#post_provenance_python) | **POST** /provenance/python | Check provenance of packages stated in an application stack.

# **get_provenance_python**
> AnalysisResultResponse get_provenance_python(analysis_id)

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
analysis_id = 'analysis_id_example' # str | An id of requested analysis.

try:
    # Retrieve a provenance check result.
    api_response = api_instance.get_provenance_python(analysis_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProvenanceApi->get_provenance_python: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analysis_id** | **str**| An id of requested analysis. | 

### Return type

[**AnalysisResultResponse**](AnalysisResultResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_provenance_python_log**
> AnalysisLogResponse get_provenance_python_log(analysis_id)

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
    api_response = api_instance.get_provenance_python_log(analysis_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProvenanceApi->get_provenance_python_log: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analysis_id** | **str**| An id of requested analysis. | 

### Return type

[**AnalysisLogResponse**](AnalysisLogResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_provenance_python_status**
> AnalysisStatusResponse get_provenance_python_status(analysis_id)

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
    api_response = api_instance.get_provenance_python_status(analysis_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProvenanceApi->get_provenance_python_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analysis_id** | **str**| An id of requested provenance check. | 

### Return type

[**AnalysisStatusResponse**](AnalysisStatusResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_provenance_python**
> AnalysisResponse post_provenance_python(body, origin=origin, debug=debug, force=force)

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
body = thamos.swagger_client.PythonStack() # PythonStack | Pipfile and Pipfile.lock as used by pipenv.
origin = 'origin_example' # str | A repository where the application stack is used. This is used for tracking as well as for automated reporting when results are available.  (optional)
debug = false # bool | Run the provenance checker in a verbose mode so developers can debug it.  (optional) (default to false)
force = false # bool | Do not use cached results, always run provenance checks.  (optional) (default to false)

try:
    # Check provenance of packages stated in an application stack.
    api_response = api_instance.post_provenance_python(body, origin=origin, debug=debug, force=force)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProvenanceApi->post_provenance_python: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PythonStack**](PythonStack.md)| Pipfile and Pipfile.lock as used by pipenv. | 
 **origin** | **str**| A repository where the application stack is used. This is used for tracking as well as for automated reporting when results are available.  | [optional] 
 **debug** | **bool**| Run the provenance checker in a verbose mode so developers can debug it.  | [optional] [default to false]
 **force** | **bool**| Do not use cached results, always run provenance checks.  | [optional] [default to false]

### Return type

[**AnalysisResponse**](AnalysisResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

