# AdviserResultResponseMetadata

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**analyzer** | **str** | Analyzer name which handled analysis |
**analyzer_version** | **str** | Version of analyzer handling analysis |
**arguments** | **object** | Arguments passed to the analyzer |
**_datetime** | **str** | Date and time of analysis end in ISO format |
**distribution** | [**AnalysisResultResponseMetadataDistribution**](AnalysisResultResponseMetadataDistribution.md) |  |
**document_id** | **str** | A unique identifier of the document |
**duration** | **int** | Number of seconds for which the analyzer was running  |
**hostname** | **str** | Pod name where the analysis was done |
**os_release** | **object** |  |
**python** | [**AnalysisResultResponseMetadataPython**](AnalysisResultResponseMetadataPython.md) |  |
**thoth_deployment_name** | **str** | Name of Thoth&#x27;s deployment that computed results |
**timestamp** | **int** | Timestamp when results were computed |

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

