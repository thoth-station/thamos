# AnalysisResultResponseResult

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aicoe_ci** | [**AnalysisResultResponseResultAicoeci**](AnalysisResultResponseResultAicoeci.md) |  |
**cuda_version** | **object** | Nvidia CUDA version detected - path is the key and CUDA version is the object value  |
**deb** | [**list[AnalysisResultResponseResultDeb]**](AnalysisResultResponseResultDeb.md) | Debian packages detected (experimental) |
**deb_dependencies** | [**list[AnalysisResultResponseResultDebdependencies]**](AnalysisResultResponseResultDebdependencies.md) | Dependencies of Debian packages detected |
**image_size** | **int** | Size of the container image in bytes |
**layers** | **list[str]** | Container image layers, sorted based on the layer precedence  |
**mercator** | **object** | Mercator (TM) output |
**operating_system** | **object** | Operating System information |
**python_files** | [**list[AnalysisResultResponseResultPythonfiles]**](AnalysisResultResponseResultPythonfiles.md) | Python files detected in the container image |
**python_interpreters** | [**list[AnalysisResultResponseResultPythoninterpreters]**](AnalysisResultResponseResultPythoninterpreters.md) | Python interpreters detected inside the container image |
**python_packages** | [**list[AnalysisResultResponseResultPythonpackages]**](AnalysisResultResponseResultPythonpackages.md) | Detected Python packages inside the container image |
**rpm** | **list[str]** | A listing of container images found inside the analyzed container image  |
**rpm_dependencies** | **list[object]** | Information about RPM packages and their dependencies |
**skopeo_inspect** | **object** |  |
**system_symbols** | **object** | Systems symbols detected - a path mapping to exported symbols available  |

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

