# RuntimeEnvironment

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_image** | **str** | A base container image used to run the application | [optional]
**cuda_version** | **str** | Nvidia CUDA version which the application uses | [optional]
**cudnn_version** | **str** | NVIDIA cuDNN version used, if any | [optional]
**hardware** | [**RuntimeEnvironmentHardware**](RuntimeEnvironmentHardware.md) |  | [optional]
**mkl_version** | **str** | Intel® Math Kernel Library version used, if any | [optional]
**name** | **str** | User defined name of the runtime environment | [optional]
**openblas_version** | **str** | OpenBLAS version used, if any | [optional]
**openmpi_version** | **str** | Open MPI version used, if any | [optional]
**operating_system** | [**RuntimeEnvironmentOperatingSystem**](RuntimeEnvironmentOperatingSystem.md) |  | [optional]
**platform** | **list[str]** | Platform used - corresponds to sysconfig.get_platform() call | [optional]
**python_version** | **str** | Python version on which the application runs on | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

