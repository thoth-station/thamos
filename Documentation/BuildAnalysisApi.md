# thamos.swagger_client.BuildAnalysisApi

All URIs are relative to *https://test.thoth-station.ninja/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**post_build**](BuildAnalysisApi.md#post_build) | **POST** /build-analysis | Analyze the given build imagestream and log.

# **post_build**
> BuildAnalysisResponse post_build(body, registry_user=registry_user, registry_password=registry_password, environment_type=environment_type, origin=origin, debug=debug, registry_verify_tls=registry_verify_tls, force=force)

Analyze the given build imagestream and log.

### Example
```python
from __future__ import print_function
import time
import thamos.swagger_client
from thamos.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = thamos.swagger_client.BuildAnalysisApi()
body = thamos.swagger_client.Build() # Build | Fill up the Build details such as output imagestream, base imagestream, and build log.
registry_user = 'registry_user_example' # str | Registry user to be used for pulling images from registry.  (optional)
registry_password = 'registry_password_example' # str | Registry password or token to be used for pulling images from registry.  (optional)
environment_type = 'runtime' # str | Type of environment (runtime or buildtime) which is being analyzed.  (optional) (default to runtime)
origin = 'origin_example' # str | A remote where the image is being used. This is used for tracking as well as for automated reporting when results are available.  (optional)
debug = false # bool | Run the given analyzer in a verbose mode so developers can debug analyzer.  (optional) (default to false)
registry_verify_tls = true # bool | Verify TLS certificates of registry from where images are pulled from.  (optional) (default to true)
force = false # bool | Do not use cached results, always run analysis.  (optional) (default to false)

try:
    # Analyze the given build imagestream and log.
    api_response = api_instance.post_build(body, registry_user=registry_user, registry_password=registry_password, environment_type=environment_type, origin=origin, debug=debug, registry_verify_tls=registry_verify_tls, force=force)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildAnalysisApi->post_build: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Build**](Build.md)| Fill up the Build details such as output imagestream, base imagestream, and build log. | 
 **registry_user** | **str**| Registry user to be used for pulling images from registry.  | [optional] 
 **registry_password** | **str**| Registry password or token to be used for pulling images from registry.  | [optional] 
 **environment_type** | **str**| Type of environment (runtime or buildtime) which is being analyzed.  | [optional] [default to runtime]
 **origin** | **str**| A remote where the image is being used. This is used for tracking as well as for automated reporting when results are available.  | [optional] 
 **debug** | **bool**| Run the given analyzer in a verbose mode so developers can debug analyzer.  | [optional] [default to false]
 **registry_verify_tls** | **bool**| Verify TLS certificates of registry from where images are pulled from.  | [optional] [default to true]
 **force** | **bool**| Do not use cached results, always run analysis.  | [optional] [default to false]

### Return type

[**BuildAnalysisResponse**](BuildAnalysisResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

