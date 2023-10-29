# IdpInboundProvisioning

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_support** | **bool** | Specify support for provisioning of groups. | 
**user_repository** | [**InboundProvisioningUserRepository**](InboundProvisioningUserRepository.md) | The local repository for user accounts and groups requiring provisioning. | 
**custom_schema** | [**Schema**](Schema.md) | The Custom SCIM Attributes configuration. | 
**users** | [**Users**](Users.md) | User creation and read configuration. | 
**groups** | [**Groups**](Groups.md) | Group creation and read configuration. | 
**action_on_delete** | **str** | Specify behavior of how SCIM DELETE requests are handled. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


