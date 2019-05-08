# Info

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deployment_name** | **str** | Name of deployment. | [optional] 
**version** | **str** | Version of Thoth components deployed. A special value @dev signalizes a developer&#x27;s build. | [optional] 
**s3_endpoint_url** | **str** | S3 endpoint used for storing results. | [optional] 
**s3_bucket_prefix** | **str** | Bucket prefix used when storing results on S3 compatible API (Ceph). | [optional] 
**dgraph_host** | **str** | Dgraph instance to which the deployment talks to. | [optional] 
**amun_api_url** | **str** | Amun API host to which this deployment talks to (set to null if no Amun deployment is used). | [optional] 
**frontend_namespace** | **str** | Frontend namespace name. | [optional] 
**middletier_namespace** | **str** | Frontend namespace name. | [optional] 
**backend_namespace** | **str** | Frontend namespace name. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

