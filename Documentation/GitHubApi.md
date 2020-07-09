# thamos.swagger_client.GitHubApi

All URIs are relative to *https://test.thoth-station.ninja/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**schedule_thamos_advise**](GitHubApi.md#schedule_thamos_advise) | **POST** /qeb-hwt | Schedule Thamos advise for GitHub App.

# **schedule_thamos_advise**
> AnalysisResponse schedule_thamos_advise(body)

Schedule Thamos advise for GitHub App.

### Example
```python
from __future__ import print_function
import time
import thamos.swagger_client
from thamos.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = thamos.swagger_client.GitHubApi()
body = thamos.swagger_client.QebHwtThamosAdviseInput() # QebHwtThamosAdviseInput | Thamos advise inputs.

try:
    # Schedule Thamos advise for GitHub App.
    api_response = api_instance.schedule_thamos_advise(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GitHubApi->schedule_thamos_advise: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**QebHwtThamosAdviseInput**](QebHwtThamosAdviseInput.md)| Thamos advise inputs. |

### Return type

[**AnalysisResponse**](AnalysisResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
