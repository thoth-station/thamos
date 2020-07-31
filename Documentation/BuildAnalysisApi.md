# thamos.swagger_client.BuildAnalysisApi

All URIs are relative to *https://test.thoth-station.ninja/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**post_build**](BuildAnalysisApi.md#post_build) | **POST** /build-analysis | Analyze the given build imagestream and log.


# **post_build**
> BuildAnalysisResponse post_build(build, registry_user=registry_user, registry_password=registry_password, environment_type=environment_type, origin=origin, debug=debug, registry_verify_tls=registry_verify_tls, force=force)

Analyze the given build imagestream and log.

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
    api_instance = thamos.swagger_client.BuildAnalysisApi(api_client)
    build = thamos.swagger_client.Build() # Build | Fill up the Build details such as output imagestream, base imagestream, and build log.
registry_user = 'registry_user_example' # str | Registry user to be used for pulling images from registry.  (optional)
registry_password = 'registry_password_example' # str | Registry password or token to be used for pulling images from registry.  (optional)
environment_type = 'runtime' # str | Type of environment (runtime or buildtime) which is being analyzed.  (optional) (default to 'runtime')
origin = 'origin_example' # str | A remote where the image is being used. This is used for tracking as well as for automated reporting when results are available.  (optional)
debug = False # bool | Run the given analyzer in a verbose mode so developers can debug analyzer.  (optional) (default to False)
registry_verify_tls = True # bool | Verify TLS certificates of registry from where images are pulled from.  (optional) (default to True)
force = False # bool | Do not use cached results, always run analysis.  (optional) (default to False)

    try:
        # Analyze the given build imagestream and log.
        api_response = api_instance.post_build(build, registry_user=registry_user, registry_password=registry_password, environment_type=environment_type, origin=origin, debug=debug, registry_verify_tls=registry_verify_tls, force=force)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BuildAnalysisApi->post_build: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **build** | [**Build**](Build.md)| Fill up the Build details such as output imagestream, base imagestream, and build log. |
 **registry_user** | **str**| Registry user to be used for pulling images from registry.  | [optional]
 **registry_password** | **str**| Registry password or token to be used for pulling images from registry.  | [optional]
 **environment_type** | **str**| Type of environment (runtime or buildtime) which is being analyzed.  | [optional] [default to &#39;runtime&#39;]
 **origin** | **str**| A remote where the image is being used. This is used for tracking as well as for automated reporting when results are available.  | [optional]
 **debug** | **bool**| Run the given analyzer in a verbose mode so developers can debug analyzer.  | [optional] [default to False]
 **registry_verify_tls** | **bool**| Verify TLS certificates of registry from where images are pulled from.  | [optional] [default to True]
 **force** | **bool**| Do not use cached results, always run analysis.  | [optional] [default to False]

### Return type

[**BuildAnalysisResponse**](BuildAnalysisResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Successful response with analyzer id. |  -  |
**400** | On invalid request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
