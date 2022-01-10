# AdviserResultResponseResultReport

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | **str** | Error message describing advise failure | [optional]
**accepted_final_states_count** | **int** | Number of resolved states that were accepted | [optional]
**discarded_final_states_count** | **int** | Number of states that were discarded during the resolution | [optional]
**pipeline** | [**AdviserResultResponseResultReportPipeline**](AdviserResultResponseResultReportPipeline.md) |  | [optional]
**products** | [**list[AdviserResultResponseResultReportProducts]**](AdviserResultResponseResultReportProducts.md) | Products computed in the deployment, always holds only one item  | [optional]
**resolver_iterations** | **int** | Number of iterations done by the resolver to compute products  | [optional]
**stack_info** | [**StackInfo**](StackInfo.md) |  |

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

