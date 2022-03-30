# thamos.swagger_client.KebechetApi

All URIs are relative to https://test.thoth-station.ninja/api/v1

Method | HTTP request | Description
------------- | ------------- | -------------
[**initialize_repo**](KebechetApi.md#initialize_repo) | **POST** /repo-init | Initialize the user&#x27;s provided repository.
[**schedule_kebechet_webhook**](KebechetApi.md#schedule_kebechet_webhook) | **POST** /kebechet-webhook | Schedule kebechet instance from webhook, this endpoint is not intended for users

# **initialize_repo**
> initialize_repo(body)

Initialize the user's provided repository.

### Example
```python
from __future__ import print_function
import time
import thamos.swagger_client
from thamos.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = thamos.swagger_client.KebechetApi()
body = thamos.swagger_client.RepoInitInput() # RepoInitInput |

try:
    # Initialize the user's provided repository.
    api_instance.initialize_repo(body)
except ApiException as e:
    print("Exception when calling KebechetApi->initialize_repo: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RepoInitInput**](RepoInitInput.md)|  |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **schedule_kebechet_webhook**
> schedule_kebechet_webhook(body)

Schedule kebechet instance from webhook, this endpoint is not intended for users

### Example
```python
from __future__ import print_function
import time
import thamos.swagger_client
from thamos.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = thamos.swagger_client.KebechetApi()
body = thamos.swagger_client.KebechetWebhookInput() # KebechetWebhookInput | Body of a git service webhook

try:
    # Schedule kebechet instance from webhook, this endpoint is not intended for users
    api_instance.schedule_kebechet_webhook(body)
except ApiException as e:
    print("Exception when calling KebechetApi->schedule_kebechet_webhook: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**KebechetWebhookInput**](KebechetWebhookInput.md)| Body of a git service webhook |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

