# RedirectValidationSettingsWhitelistEntry

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target_resource_sso** | **bool** | Enable this target resource for SSO redirect validation. | [optional] 
**target_resource_slo** | **bool** | Enable this target resource for SLO redirect validation. | [optional] 
**in_error_resource** | **bool** | Enable this target resource for in error resource validation. | [optional] 
**idp_discovery** | **bool** | Enable this target resource for IdP discovery validation. | [optional] 
**valid_domain** | **str** | Domain of a valid resource. | 
**valid_path** | **str** | Path of a valid resource. | [optional] 
**allow_query_and_fragment** | **bool** | Allow any query parameters and fragment in the resource. | [optional] 
**require_https** | **bool** | Require HTTPS for accessing this resource. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


