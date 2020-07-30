# thamos.swagger_client.ImageAnalysisApi

All URIs are relative to *https://test.thoth-station.ninja/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_analyze**](ImageAnalysisApi.md#get_analyze) | **GET** /analyze/{analysis_id} | Retrieve an analyzer result.
[**get_analyze_by_hash**](ImageAnalysisApi.md#get_analyze_by_hash) | **GET** /analyze/by-hash/{image_hash} | Retrieve an analyzer result.
[**get_analyze_log**](ImageAnalysisApi.md#get_analyze_log) | **GET** /analyze/{analysis_id}/log | Show logs of an analysis.
[**get_analyze_status**](ImageAnalysisApi.md#get_analyze_status) | **GET** /analyze/{analysis_id}/status | Show analysis status.
[**list_analyze**](ImageAnalysisApi.md#list_analyze) | **GET** /analyze | Retrieve a list of document ids for analyzer results.
[**list_software_environment_analyses_for_build**](ImageAnalysisApi.md#list_software_environment_analyses_for_build) | **GET** /build-software-environment/analyses/{environment_name} | List analyses for the given software environment for build.
[**list_software_environment_analyses_for_run**](ImageAnalysisApi.md#list_software_environment_analyses_for_run) | **GET** /run-software-environment/analyses/{environment_name} | List analyses for the given software environment for run.
[**list_software_environments_for_build**](ImageAnalysisApi.md#list_software_environments_for_build) | **GET** /build-software-environment | Retrieve a list of software environments analyzed for build.
[**list_software_environments_for_run**](ImageAnalysisApi.md#list_software_environments_for_run) | **GET** /run-software-environment | Retrieve a list of software environments analyzed for run.
[**post_analyze**](ImageAnalysisApi.md#post_analyze) | **POST** /analyze | Analyze the given image asynchronously.
[**post_image_metadata**](ImageAnalysisApi.md#post_image_metadata) | **POST** /image/metadata | Get metadata for the given image

# **get_analyze**
> AnalysisResultResponse get_analyze(analysis_id)

Retrieve an analyzer result.

### Example
```python
from __future__ import print_function
import time
import thamos.swagger_client
from thamos.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = thamos.swagger_client.ImageAnalysisApi()
analysis_id = 'analysis_id_example' # str | Id of analysis that results should be retrieved.

try:
    # Retrieve an analyzer result.
    api_response = api_instance.get_analyze(analysis_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageAnalysisApi->get_analyze: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analysis_id** | **str**| Id of analysis that results should be retrieved. | 

### Return type

[**AnalysisResultResponse**](AnalysisResultResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_analyze_by_hash**
> AnalysisResultResponse get_analyze_by_hash(image_hash)

Retrieve an analyzer result.

### Example
```python
from __future__ import print_function
import time
import thamos.swagger_client
from thamos.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = thamos.swagger_client.ImageAnalysisApi()
image_hash = 'image_hash_example' # str | Image hash for identifying image (including hash type, now supported only \"sha256\").

try:
    # Retrieve an analyzer result.
    api_response = api_instance.get_analyze_by_hash(image_hash)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageAnalysisApi->get_analyze_by_hash: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_hash** | **str**| Image hash for identifying image (including hash type, now supported only \&quot;sha256\&quot;). | 

### Return type

[**AnalysisResultResponse**](AnalysisResultResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_analyze_log**
> AnalysisLogResponse get_analyze_log(analysis_id)

Show logs of an analysis.

### Example
```python
from __future__ import print_function
import time
import thamos.swagger_client
from thamos.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = thamos.swagger_client.ImageAnalysisApi()
analysis_id = 'analysis_id_example' # str | An id of requested analysis.

try:
    # Show logs of an analysis.
    api_response = api_instance.get_analyze_log(analysis_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageAnalysisApi->get_analyze_log: %s\n" % e)
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

# **get_analyze_status**
> AnalysisStatusResponse get_analyze_status(analysis_id)

Show analysis status.

### Example
```python
from __future__ import print_function
import time
import thamos.swagger_client
from thamos.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = thamos.swagger_client.ImageAnalysisApi()
analysis_id = 'analysis_id_example' # str | An id of requested analysis.

try:
    # Show analysis status.
    api_response = api_instance.get_analyze_status(analysis_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageAnalysisApi->get_analyze_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analysis_id** | **str**| An id of requested analysis. | 

### Return type

[**AnalysisStatusResponse**](AnalysisStatusResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_analyze**
> AnalysisListingResponse list_analyze(page=page)

Retrieve a list of document ids for analyzer results.

### Example
```python
from __future__ import print_function
import time
import thamos.swagger_client
from thamos.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = thamos.swagger_client.ImageAnalysisApi()
page = 0 # int | Page offset in pagination. (optional) (default to 0)

try:
    # Retrieve a list of document ids for analyzer results.
    api_response = api_instance.list_analyze(page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageAnalysisApi->list_analyze: %s\n" % e)
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

# **list_software_environment_analyses_for_build**
> object list_software_environment_analyses_for_build(environment_name)

List analyses for the given software environment for build.

### Example
```python
from __future__ import print_function
import time
import thamos.swagger_client
from thamos.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = thamos.swagger_client.ImageAnalysisApi()
environment_name = 'environment_name_example' # str | Software environment name for run for which analyses should be retrieved. 

try:
    # List analyses for the given software environment for build.
    api_response = api_instance.list_software_environment_analyses_for_build(environment_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageAnalysisApi->list_software_environment_analyses_for_build: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment_name** | **str**| Software environment name for run for which analyses should be retrieved.  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_software_environment_analyses_for_run**
> object list_software_environment_analyses_for_run(environment_name)

List analyses for the given software environment for run.

### Example
```python
from __future__ import print_function
import time
import thamos.swagger_client
from thamos.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = thamos.swagger_client.ImageAnalysisApi()
environment_name = 'environment_name_example' # str | Software environment name for run for which analyses should be retrieved. 

try:
    # List analyses for the given software environment for run.
    api_response = api_instance.list_software_environment_analyses_for_run(environment_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageAnalysisApi->list_software_environment_analyses_for_run: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment_name** | **str**| Software environment name for run for which analyses should be retrieved.  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_software_environments_for_build**
> object list_software_environments_for_build(page=page)

Retrieve a list of software environments analyzed for build.

### Example
```python
from __future__ import print_function
import time
import thamos.swagger_client
from thamos.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = thamos.swagger_client.ImageAnalysisApi()
page = 0 # int | Page offset in pagination. (optional) (default to 0)

try:
    # Retrieve a list of software environments analyzed for build.
    api_response = api_instance.list_software_environments_for_build(page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageAnalysisApi->list_software_environments_for_build: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page offset in pagination. | [optional] [default to 0]

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_software_environments_for_run**
> object list_software_environments_for_run(page=page)

Retrieve a list of software environments analyzed for run.

### Example
```python
from __future__ import print_function
import time
import thamos.swagger_client
from thamos.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = thamos.swagger_client.ImageAnalysisApi()
page = 0 # int | Page offset in pagination. (optional) (default to 0)

try:
    # Retrieve a list of software environments analyzed for run.
    api_response = api_instance.list_software_environments_for_run(page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageAnalysisApi->list_software_environments_for_run: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page offset in pagination. | [optional] [default to 0]

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_analyze**
> AnalysisResponse post_analyze(image, registry_user=registry_user, registry_password=registry_password, environment_type=environment_type, origin=origin, debug=debug, verify_tls=verify_tls, force=force)

Analyze the given image asynchronously.

### Example
```python
from __future__ import print_function
import time
import thamos.swagger_client
from thamos.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = thamos.swagger_client.ImageAnalysisApi()
image = 'image_example' # str | Name of image - can also specify remote registry to pull image from. 
registry_user = 'registry_user_example' # str | Registry user to be used for pulling images from registry.  (optional)
registry_password = 'registry_password_example' # str | Registry password or token to be used for pulling images from registry.  (optional)
environment_type = 'runtime' # str | Type of environment (runtime or buildtime) which is being analyzed.  (optional) (default to runtime)
origin = 'origin_example' # str | A remote where the image is being used. This is used for tracking as well as for automated reporting when results are available.  (optional)
debug = false # bool | Run the given analyzer in a verbose mode so developers can debug analyzer.  (optional) (default to false)
verify_tls = true # bool | Verify TLS certificates of registry from where images are pulled from.  (optional) (default to true)
force = false # bool | Do not use cached results, always run analysis.  (optional) (default to false)

try:
    # Analyze the given image asynchronously.
    api_response = api_instance.post_analyze(image, registry_user=registry_user, registry_password=registry_password, environment_type=environment_type, origin=origin, debug=debug, verify_tls=verify_tls, force=force)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageAnalysisApi->post_analyze: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image** | **str**| Name of image - can also specify remote registry to pull image from.  | 
 **registry_user** | **str**| Registry user to be used for pulling images from registry.  | [optional] 
 **registry_password** | **str**| Registry password or token to be used for pulling images from registry.  | [optional] 
 **environment_type** | **str**| Type of environment (runtime or buildtime) which is being analyzed.  | [optional] [default to runtime]
 **origin** | **str**| A remote where the image is being used. This is used for tracking as well as for automated reporting when results are available.  | [optional] 
 **debug** | **bool**| Run the given analyzer in a verbose mode so developers can debug analyzer.  | [optional] [default to false]
 **verify_tls** | **bool**| Verify TLS certificates of registry from where images are pulled from.  | [optional] [default to true]
 **force** | **bool**| Do not use cached results, always run analysis.  | [optional] [default to false]

### Return type

[**AnalysisResponse**](AnalysisResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_image_metadata**
> ImageMetadataResponse post_image_metadata(image, registry_user=registry_user, registry_password=registry_password, verify_tls=verify_tls)

Get metadata for the given image

### Example
```python
from __future__ import print_function
import time
import thamos.swagger_client
from thamos.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = thamos.swagger_client.ImageAnalysisApi()
image = 'image_example' # str | Name of image - can also specify remote registry to pull image from. 
registry_user = 'registry_user_example' # str | Registry user to be used for pulling images from registry.  (optional)
registry_password = 'registry_password_example' # str | Registry password or token to be used for pulling images from registry.  (optional)
verify_tls = true # bool | Verify TLS certificates of registry from where images are pulled from.  (optional) (default to true)

try:
    # Get metadata for the given image
    api_response = api_instance.post_image_metadata(image, registry_user=registry_user, registry_password=registry_password, verify_tls=verify_tls)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageAnalysisApi->post_image_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image** | **str**| Name of image - can also specify remote registry to pull image from.  | 
 **registry_user** | **str**| Registry user to be used for pulling images from registry.  | [optional] 
 **registry_password** | **str**| Registry password or token to be used for pulling images from registry.  | [optional] 
 **verify_tls** | **bool**| Verify TLS certificates of registry from where images are pulled from.  | [optional] [default to true]

### Return type

[**ImageMetadataResponse**](ImageMetadataResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

