# thamos.swagger_client.KebechetApi

All URIs are relative to *https://test.thoth-station.ninja/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**schedule_kebechet**](KebechetApi.md#schedule_kebechet) | **POST** /kebechet | Schedule kebechet instance from webhook
[**schedule_kebechet_webhook**](KebechetApi.md#schedule_kebechet_webhook) | **POST** /kebechet-webhook | Schedule kebechet instance from webhook


# **schedule_kebechet**
> schedule_kebechet(request_body)

Schedule kebechet instance from webhook

### Example

```python
from __future__ import print_function
import time
import thamos.swagger_client
from thamos.swagger_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://test.thoth-station.ninja/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = thamos.swagger_client.Configuration(
    host = "https://test.thoth-station.ninja/api/v1"
)


# Enter a context with an instance of the API client
with thamos.swagger_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = thamos.swagger_client.KebechetApi(api_client)
    request_body = None # dict(str, object) | Body of a git service webhook

    try:
        # Schedule kebechet instance from webhook
        api_instance.schedule_kebechet(request_body)
    except ApiException as e:
        print("Exception when calling KebechetApi->schedule_kebechet: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**dict(str, object)**](object.md)| Body of a git service webhook | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**400** | Invalid |  -  |
**501** | Functionality not supported |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **schedule_kebechet_webhook**
> schedule_kebechet_webhook(body)

Schedule kebechet instance from webhook

### Example

```python
from __future__ import print_function
import time
import thamos.swagger_client
from thamos.swagger_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://test.thoth-station.ninja/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = thamos.swagger_client.Configuration(
    host = "https://test.thoth-station.ninja/api/v1"
)


# Enter a context with an instance of the API client
with thamos.swagger_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = thamos.swagger_client.KebechetApi(api_client)
    body = None # object | Body of a git service webhook

    try:
        # Schedule kebechet instance from webhook
        api_instance.schedule_kebechet_webhook(body)
    except ApiException as e:
        print("Exception when calling KebechetApi->schedule_kebechet_webhook: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **object**| Body of a git service webhook | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**400** | Invalid |  -  |
**501** | Functionality not supported |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

