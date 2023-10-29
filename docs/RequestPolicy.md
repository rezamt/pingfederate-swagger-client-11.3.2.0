# RequestPolicy

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The request policy ID. ID is unique. | 
**name** | **str** | The request policy name. Name is unique. | 
**authenticator_ref** | [**ResourceLink**](ResourceLink.md) | Reference to the associated authenticator. | 
**user_code_pcv_ref** | [**ResourceLink**](ResourceLink.md) | Reference to the associated password credential validator. | [optional] 
**transaction_lifetime** | **int** | The transaction lifetime in seconds. | [optional] 
**allow_unsigned_login_hint_token** | **bool** | Allow unsigned login hint token. | [optional] 
**require_token_for_identity_hint** | **bool** | Require token for identity hint. | [optional] 
**alternative_login_hint_token_issuers** | [**list[AlternativeLoginHintTokenIssuer]**](AlternativeLoginHintTokenIssuer.md) | Alternative login hint token issuers. | [optional] 
**identity_hint_contract** | [**IdentityHintContract**](IdentityHintContract.md) | Identity hint attribute contract. | 
**identity_hint_contract_fulfillment** | [**AttributeMapping**](AttributeMapping.md) | Identity hint attribute contract fulfillment. | [optional] 
**identity_hint_mapping** | [**AttributeMapping**](AttributeMapping.md) | Identity hint contract to request policy mapping. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


