# thamos.swagger_client.BuildlogsApi

All URIs are relative to *https://localhost/api/v1/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_buildlog**](BuildlogsApi.md#get_buildlog) | **GET** /buildlog/{document_id} | Retrieve the given build log.
[**list_buildlogs**](BuildlogsApi.md#list_buildlogs) | **GET** /buildlog | Retrieve a list of document ids for stored build logs.
[**parse_log**](BuildlogsApi.md#parse_log) | **POST** /parse-log | Parse Docker build log or installation log and show installed packages. 
[**post_buildlog**](BuildlogsApi.md#post_buildlog) | **POST** /buildlog | Store the given build log.


# **get_buildlog**
> get_buildlog(document_id)

Retrieve the given build log.

### Example
```python
from __future__ import print_function
import time
import thamos.swagger_client
from thamos.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = thamos.swagger_client.BuildlogsApi()
document_id = 'document_id_example' # str | Build log to be retrieved.

try:
    # Retrieve the given build log.
    api_instance.get_buildlog(document_id)
except ApiException as e:
    print("Exception when calling BuildlogsApi->get_buildlog: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_id** | **str**| Build log to be retrieved. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_buildlogs**
> list_buildlogs(page=page)

Retrieve a list of document ids for stored build logs.

### Example
```python
from __future__ import print_function
import time
import thamos.swagger_client
from thamos.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = thamos.swagger_client.BuildlogsApi()
page = 0 # int | Page offset in pagination. (optional) (default to 0)

try:
    # Retrieve a list of document ids for stored build logs.
    api_instance.list_buildlogs(page=page)
except ApiException as e:
    print("Exception when calling BuildlogsApi->list_buildlogs: %s\n" % e)
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

# **parse_log**
> parse_log(log_info)

Parse Docker build log or installation log and show installed packages. 

### Example
```python
from __future__ import print_function
import time
import thamos.swagger_client
from thamos.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = thamos.swagger_client.BuildlogsApi()
log_info = thamos.swagger_client.Log() # Log | A full log.

try:
    # Parse Docker build log or installation log and show installed packages. 
    api_instance.parse_log(log_info)
except ApiException as e:
    print("Exception when calling BuildlogsApi->parse_log: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **log_info** | [**Log**](Log.md)| A full log. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_buildlog**
> post_buildlog(log_info)

Store the given build log.

### Example
```python
from __future__ import print_function
import time
import thamos.swagger_client
from thamos.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = thamos.swagger_client.BuildlogsApi()
log_info = thamos.swagger_client.Log() # Log | Build log to be stored.

try:
    # Store the given build log.
    api_instance.post_buildlog(log_info)
except ApiException as e:
    print("Exception when calling BuildlogsApi->post_buildlog: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **log_info** | [**Log**](Log.md)| Build log to be stored. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

