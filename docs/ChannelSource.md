# ChannelSource

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_source** | [**ResourceLink**](ResourceLink.md) | Reference to an LDAP datastore. | 
**guid_attribute_name** | **str** | the GUID attribute name. | 
**guid_binary** | **bool** | Indicates whether the GUID is stored in binary format. | 
**change_detection_settings** | [**ChangeDetectionSettings**](ChangeDetectionSettings.md) | Settings to detect a during provisioning. | 
**group_membership_detection** | [**GroupMembershipDetection**](GroupMembershipDetection.md) | Settings to detect group memberships. | 
**account_management_settings** | [**AccountManagementSettings**](AccountManagementSettings.md) | Account management settings that includes the status and algorithms. | 
**base_dn** | **str** | The base DN where the user records are located. | 
**user_source_location** | [**ChannelSourceLocation**](ChannelSourceLocation.md) | The user provisioning source location settings. | 
**group_source_location** | [**ChannelSourceLocation**](ChannelSourceLocation.md) | The group provisioning source location settings. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


