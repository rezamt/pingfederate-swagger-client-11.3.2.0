# EncryptionPolicy

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**encrypt_assertion** | **bool** | Whether the outgoing SAML assertion will be encrypted. | [optional] 
**encrypted_attributes** | **list[str]** | The list of outgoing SAML assertion attributes that will be encrypted. The &#39;encryptAssertion&#39; property takes precedence over this. | [optional] 
**encrypt_slo_subject_name_id** | **bool** | Encrypt the name-identifier attribute in outbound SLO messages.  This can be set if the name id is encrypted. | [optional] 
**slo_subject_name_id_encrypted** | **bool** | Allow the encryption of the name-identifier attribute for inbound SLO messages. This can be set if SP initiated SLO is enabled. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


