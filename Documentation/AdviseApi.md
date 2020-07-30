# thamos.swagger_client.AdviseApi

All URIs are relative to *https://test.thoth-station.ninja/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_advise_python**](AdviseApi.md#get_advise_python) | **GET** /advise/python/{analysis_id} | Get computed adviser result based on its id.
[**get_advise_python_log**](AdviseApi.md#get_advise_python_log) | **GET** /advise/python/{analysis_id}/log | Retrieve a adviser run log.
[**get_advise_python_status**](AdviseApi.md#get_advise_python_status) | **GET** /advise/python/{analysis_id}/status | Show status of an adviser computing recommendations.
[**list_advise_python**](AdviseApi.md#list_advise_python) | **GET** /advise/python | Get adviser results available.
[**post_advise_python**](AdviseApi.md#post_advise_python) | **POST** /advise/python | Get advise for Python ecosystem.

# **get_advise_python**
> AnalysisResultResponse get_advise_python(analysis_id)

Get computed adviser result based on its id.

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
    # Get computed adviser result based on its id.
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

 - **Content-Type**: Not defined
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

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_advise_python_status**
> AnalysisStatusResponse get_advise_python_status(analysis_id)

Show status of an adviser computing recommendations.

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
    # Show status of an adviser computing recommendations.
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

 - **Content-Type**: Not defined
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

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_advise_python**
> AnalysisResponse post_advise_python(body, recommendation_type, count=count, limit=limit, origin=origin, source_type=source_type, dev=dev, debug=debug, force=force, github_event_type=github_event_type, github_check_run_id=github_check_run_id, github_installation_id=github_installation_id, github_base_repo_url=github_base_repo_url)

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
body = thamos.swagger_client.AdviseInput() # AdviseInput | Specification of Python application stack with runtime specific information.
recommendation_type = 'stable' # str | Recommendation type. (default to stable)
count = 56 # int | Number of software stacks that should be returned. (optional)
limit = 56 # int | Limit number of software stacks scored. (optional)
origin = 'origin_example' # str | A repository where the application stack is used. This is used for tracking as well as for automated reporting when results are available.  (optional)
source_type = 'source_type_example' # str | A flag marking what Thoth integration is requesting adviser:   - cli: Thamos CLI.   - s2i: OpenShift's S2I (Source-to-Image) build.   - github_app: Qeb-Hwt GitHub App.   - kebechet: Kebechet Bot.   - jupyter_notebook: Jupyter Notebook (nb-requirements).  (optional)
dev = false # bool | Consider or do not consider development dependencies when resolving stacks.  (optional) (default to false)
debug = false # bool | Run the given adviser in a verbose mode so developers can debug it.  (optional) (default to false)
force = false # bool | Do not use cached results, always run adviser.  (optional) (default to false)
github_event_type = 'github_event_type_example' # str | GitHub's event type. (optional)
github_check_run_id = 56 # int | GitHub's event id. (optional)
github_installation_id = 56 # int | GitHub's installation id. (optional)
github_base_repo_url = 'github_base_repo_url_example' # str | URL of the GitHub repository containing the Pull Request. (optional)

try:
    # Get advise for Python ecosystem.
    api_response = api_instance.post_advise_python(body, recommendation_type, count=count, limit=limit, origin=origin, source_type=source_type, dev=dev, debug=debug, force=force, github_event_type=github_event_type, github_check_run_id=github_check_run_id, github_installation_id=github_installation_id, github_base_repo_url=github_base_repo_url)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdviseApi->post_advise_python: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AdviseInput**](AdviseInput.md)| Specification of Python application stack with runtime specific information. |
 **recommendation_type** | **str**| Recommendation type. | [default to stable]
 **count** | **int**| Number of software stacks that should be returned. | [optional]
 **limit** | **int**| Limit number of software stacks scored. | [optional]
 **origin** | **str**| A repository where the application stack is used. This is used for tracking as well as for automated reporting when results are available.  | [optional]
 **source_type** | **str**| A flag marking what Thoth integration is requesting adviser:   - cli: Thamos CLI.   - s2i: OpenShift&#x27;s S2I (Source-to-Image) build.   - github_app: Qeb-Hwt GitHub App.   - kebechet: Kebechet Bot.   - jupyter_notebook: Jupyter Notebook (nb-requirements).  | [optional]
 **dev** | **bool**| Consider or do not consider development dependencies when resolving stacks.  | [optional] [default to false]
 **debug** | **bool**| Run the given adviser in a verbose mode so developers can debug it.  | [optional] [default to false]
 **force** | **bool**| Do not use cached results, always run adviser.  | [optional] [default to false]
 **github_event_type** | **str**| GitHub&#x27;s event type. | [optional]
 **github_check_run_id** | **int**| GitHub&#x27;s event id. | [optional]
 **github_installation_id** | **int**| GitHub&#x27;s installation id. | [optional]
 **github_base_repo_url** | **str**| URL of the GitHub repository containing the Pull Request. | [optional]

### Return type

[**AnalysisResponse**](AnalysisResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
