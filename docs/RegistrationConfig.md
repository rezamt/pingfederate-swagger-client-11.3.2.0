# RegistrationConfig

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**captcha_enabled** | **bool** | Whether CAPTCHA is enabled or not in the registration configuration. | [optional] 
**captcha_provider_ref** | [**ResourceLink**](ResourceLink.md) | Reference to the associated CAPTCHA provider. | [optional] 
**template_name** | **str** | The template name for the registration configuration. | 
**create_authn_session_after_registration** | **bool** | Whether to create an Authentication Session when registering a local account. Default is true. | [optional] 
**username_field** | **str** | When creating an Authentication Session after registering a local account, PingFederate will pass the Unique ID field&#39;s value as the username. If the Unique ID value is not the username, then override which field&#39;s value will be used as the username. | [optional] 
**this_is_my_device_enabled** | **bool** | Allows users to indicate whether their device is shared or private. In this mode, PingFederate Authentication Sessions will not be stored unless the user indicates the device is private. | [optional] 
**registration_workflow** | [**ResourceLink**](ResourceLink.md) | The policy fragment to be executed as part of the registration workflow. | [optional] 
**execute_workflow** | **str** | This setting indicates whether PingFederate should execute the workflow before or after account creation. The default is to run the registration workflow after account creation. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


