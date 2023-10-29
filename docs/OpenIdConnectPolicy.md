# OpenIdConnectPolicy

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The policy ID used internally. | 
**name** | **str** | The name used for display in UI screens. | 
**access_token_manager_ref** | [**ResourceLink**](ResourceLink.md) | The access token manager associated with this Open ID Connect policy. | 
**id_token_lifetime** | **int** | The ID Token Lifetime, in minutes. The default value is 5. | [optional] 
**include_sri_in_id_token** | **bool** | Determines whether a Session Reference Identifier is included in the ID token. | [optional] 
**include_user_info_in_id_token** | **bool** | Determines whether the User Info is always included in the ID token. | [optional] 
**include_s_hash_in_id_token** | **bool** | Determines whether the State Hash should be included in the ID token. | [optional] 
**include_x5t_in_id_token** | **bool** | Determines whether the X.509 thumbprint header should be included in the ID Token. | [optional] 
**id_token_typ_header_value** | **str** | ID Token Type (typ) Header Value. | [optional] 
**return_id_token_on_refresh_grant** | **bool** | Determines whether an ID Token should be returned when refresh grant is requested or not. | [optional] 
**reissue_id_token_in_hybrid_flow** | **bool** | Determines whether a new ID Token should be returned during token request of the hybrid flow. | [optional] 
**attribute_contract** | [**OpenIdConnectAttributeContract**](OpenIdConnectAttributeContract.md) | The list of attributes that will be returned to OAuth clients in response to requests received at the PingFederate UserInfo endpoint. | 
**attribute_mapping** | [**AttributeMapping**](AttributeMapping.md) | The attributes mapping from attribute sources to attribute targets. | 
**scope_attribute_mappings** | [**dict(str, ParameterValues)**](ParameterValues.md) | The attribute scope mappings from scopes to attribute names. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


