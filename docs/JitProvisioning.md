# JitProvisioning

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_attributes** | [**JitProvisioningUserAttributes**](JitProvisioningUserAttributes.md) | Attributes from the SAML Assertion. | 
**user_repository** | [**DataStoreRepository**](DataStoreRepository.md) | The data store used as the local repository for user provisioning. | 
**event_trigger** | **str** | Specify when provisioning occurs during assertion processing. The default is &#39;NEW_USER_ONLY&#39;. | [optional] 
**error_handling** | **str** | Specify behavior when provisioning request fails. The default is &#39;CONTINUE_SSO&#39;. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


