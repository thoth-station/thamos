# thamos.swagger_client.AdviseApi

All URIs are relative to https://test.thoth-station.ninja/api/v1

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_advise_python**](AdviseApi.md#get_advise_python) | **GET** /advise/python/{analysis_id} | Get computed adviser result based on its identifier
[**get_advise_python_log**](AdviseApi.md#get_advise_python_log) | **GET** /advise/python/{analysis_id}/log | Retrieve an adviser run log
[**get_advise_python_status**](AdviseApi.md#get_advise_python_status) | **GET** /advise/python/{analysis_id}/status | Show status of an adviser computing recommendations
[**post_advise_python**](AdviseApi.md#post_advise_python) | **POST** /advise/python | Get an advise for a Python application

# **get_advise_python**
> AdviserResultResponse get_advise_python(analysis_id)

Get computed adviser result based on its identifier

### Example
```python
from __future__ import print_function
import time
import thamos.swagger_client
from thamos.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = thamos.swagger_client.AdviseApi()
analysis_id = 'analysis_id_example' # str | An identifier of the requested analysis

try:
    # Get computed adviser result based on its identifier
    api_response = api_instance.get_advise_python(analysis_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdviseApi->get_advise_python: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analysis_id** | **str**| An identifier of the requested analysis |

### Return type

[**AdviserResultResponse**](AdviserResultResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_advise_python_log**
> AnalysisLogResponse get_advise_python_log(analysis_id)

Retrieve an adviser run log

### Example
```python
from __future__ import print_function
import time
import thamos.swagger_client
from thamos.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = thamos.swagger_client.AdviseApi()
analysis_id = 'analysis_id_example' # str | An identifier of the requested analysis

try:
    # Retrieve an adviser run log
    api_response = api_instance.get_advise_python_log(analysis_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdviseApi->get_advise_python_log: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analysis_id** | **str**| An identifier of the requested analysis |

### Return type

[**AnalysisLogResponse**](AnalysisLogResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_advise_python_status**
> AnalysisStatusResponse get_advise_python_status(analysis_id)

Show status of an adviser computing recommendations

### Example
```python
from __future__ import print_function
import time
import thamos.swagger_client
from thamos.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = thamos.swagger_client.AdviseApi()
analysis_id = 'analysis_id_example' # str | An identifier of the requested analysis

try:
    # Show status of an adviser computing recommendations
    api_response = api_instance.get_advise_python_status(analysis_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdviseApi->get_advise_python_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analysis_id** | **str**| An identifier of the requested analysis |

### Return type

[**AnalysisStatusResponse**](AnalysisStatusResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_advise_python**
> AnalysisWithAuthenticationResponse post_advise_python(body, recommendation_type, count=count, limit=limit, origin=origin, source_type=source_type, dev=dev, debug=debug, force=force, token=token)

Get an advise for a Python application

### Example
```python
from __future__ import print_function
import time
import thamos.swagger_client
from thamos.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = thamos.swagger_client.AdviseApi()
body = thamos.swagger_client.AdviseInput() # AdviseInput | Specification of Python application stack with runtime specific information
recommendation_type = 'latest' # str | Recommendation type (default to latest)
count = 56 # int | Number of software stacks that should be returned (optional)
limit = 56 # int | Limit number of software stacks scored (optional)
origin = 'origin_example' # str | A repository where the application stack is used  (optional)
source_type = 'source_type_example' # str | A flag marking what Thoth integration is requesting adviser: * cli: Thamos CLI * s2i: OpenShift's S2I (Source-to-Image) build * kebechet: Kebechet Bot * jupyter_notebook: Jupyter Notebook using jupyterlab-requirements  (optional)
dev = false # bool | Consider or do not consider development dependencies when resolving stacks  (optional) (default to false)
debug = false # bool | Run the given analyzer in a verbose mode so developers can debug it  (optional) (default to false)
force = false # bool | Do not use cached results, always run the analysis  (optional) (default to false)
token = 'token_example' # str | An API token for authenticated requests (optional)

try:
    # Get an advise for a Python application
    api_response = api_instance.post_advise_python(body, recommendation_type, count=count, limit=limit, origin=origin, source_type=source_type, dev=dev, debug=debug, force=force, token=token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdviseApi->post_advise_python: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AdviseInput**](AdviseInput.md)| Specification of Python application stack with runtime specific information |
 **recommendation_type** | **str**| Recommendation type | [default to latest]
 **count** | **int**| Number of software stacks that should be returned | [optional]
 **limit** | **int**| Limit number of software stacks scored | [optional]
 **origin** | **str**| A repository where the application stack is used  | [optional]
 **source_type** | **str**| A flag marking what Thoth integration is requesting adviser: * cli: Thamos CLI * s2i: OpenShift&#x27;s S2I (Source-to-Image) build * kebechet: Kebechet Bot * jupyter_notebook: Jupyter Notebook using jupyterlab-requirements  | [optional]
 **dev** | **bool**| Consider or do not consider development dependencies when resolving stacks  | [optional] [default to false]
 **debug** | **bool**| Run the given analyzer in a verbose mode so developers can debug it  | [optional] [default to false]
 **force** | **bool**| Do not use cached results, always run the analysis  | [optional] [default to false]
 **token** | **str**| An API token for authenticated requests | [optional]

### Return type

[**AnalysisWithAuthenticationResponse**](AnalysisWithAuthenticationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

