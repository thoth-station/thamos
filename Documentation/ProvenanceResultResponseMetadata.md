# ProvenanceResultResponseMetadata

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**analyzer** | **str** | Name of the component used to check provenance  |
**analyzer_version** | **str** | Version of the component used to check provenance  |
**arguments** | **object** | Arguments passed to the provenance checker |
**_datetime** | **str** | Date and time of analysis end in ISO format |
**distribution** | [**ProvenanceResultResponseMetadataDistribution**](ProvenanceResultResponseMetadataDistribution.md) |  |
**document_id** | **str** | A unique identifier of the document |
**duration** | **int** | Number of seconds for which the provenance-checker was running  |
**hostname** | **str** | Pod name where the provenance checks were done |
**os_release** | **object** |  |
**python** | [**AnalysisResultResponseMetadataPython**](AnalysisResultResponseMetadataPython.md) |  |
**thoth_deployment_name** | **str** | Name of Thoth&#x27;s deployment that computed results |
**timestamp** | **int** | Timestamp when results were computed |

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

