# OcspSettings

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**requester_add_nonce** | **bool** | Do not allow responder to use cached responses. This setting defaults to disabled. | [optional] 
**responder_url** | **str** | Default responder URL. This URL is used if the certificate being checked does not specify an OCSP responder URL. | [optional] 
**responder_cert_reference** | [**ResourceLink**](ResourceLink.md) | Resource link to OCSP responder signature verification certificate. A previously selected certificate will be deselected if this attribute is not defined. | [optional] 
**current_update_grace_period** | **int** | Current update grace period in minutes. This value defaults to \&quot;5\&quot;. | [optional] 
**next_update_grace_period** | **int** | Next update grace period in minutes. This value defaults to \&quot;5\&quot;. | [optional] 
**response_cache_period** | **int** | Response cache period in hours. This value defaults to \&quot;48\&quot;. | [optional] 
**responder_timeout** | **int** | Responder connection timeout in seconds. This value defaults to \&quot;5\&quot;. | [optional] 
**action_on_responder_unavailable** | **str** | Action on responder unavailable. This value defaults to  \&quot;CONTINUE\&quot;. | [optional] 
**action_on_status_unknown** | **str** | Action on status unknown. This value defaults to  \&quot;FAIL\&quot;. | [optional] 
**action_on_unsuccessful_response** | **str** | Action on unsuccessful response. This value defaults to  \&quot;FAIL\&quot;. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


