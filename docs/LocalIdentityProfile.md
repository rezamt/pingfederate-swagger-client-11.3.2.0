# LocalIdentityProfile

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The persistent, unique ID for the local identity profile. It can be any combination of [a-zA-Z0-9._-]. This property is system-assigned if not specified. | [optional] 
**name** | **str** | The local identity profile name. Name is unique. | 
**apc_id** | [**ResourceLink**](ResourceLink.md) | The reference to the authentication policy contract to use for this local identity profile. | 
**auth_sources** | [**list[LocalIdentityAuthSource]**](LocalIdentityAuthSource.md) | The local identity authentication sources. Sources are unique. | [optional] 
**auth_source_update_policy** | [**LocalIdentityAuthSourceUpdatePolicy**](LocalIdentityAuthSourceUpdatePolicy.md) | The attribute update policy for authentication sources. | [optional] 
**registration_enabled** | **bool** | Whether the registration configuration is enabled or not. | [optional] 
**registration_config** | [**RegistrationConfig**](RegistrationConfig.md) | The local identity profile registration configuration. | [optional] 
**profile_config** | [**ProfileConfig**](ProfileConfig.md) | The local identity profile management configuration. | [optional] 
**field_config** | [**FieldConfig**](FieldConfig.md) | The local identity profile field configuration. | [optional] 
**email_verification_config** | [**EmailVerificationConfig**](EmailVerificationConfig.md) | The local identity email verification configuration. | [optional] 
**data_store_config** | [**DataStoreConfig**](DataStoreConfig.md) | The local identity profile data store configuration. | [optional] 
**profile_enabled** | **bool** | Whether the profile configuration is enabled or not. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


