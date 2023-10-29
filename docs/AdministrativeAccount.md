# AdministrativeAccount

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** | Username for the Administrative Account. | 
**password** | **str** | Password for the Account. This field is only applicable during a POST operation. | [optional] 
**encrypted_password** | **str** | For GET requests, this field contains the encrypted account password. For POST and PUT requests, if you wish to re-use the password from an API response to this endpoint, this field should be passed back unchanged. | [optional] 
**active** | **bool** | Indicates whether the account is active or not. | [optional] 
**description** | **str** | Description of the account. | [optional] 
**auditor** | **bool** | Indicates whether the account belongs to an Auditor. An Auditor has View-only permissions for all administrative functions. An Auditor cannot have any administrative roles. | [optional] 
**phone_number** | **str** | Phone number associated with the account. | [optional] 
**email_address** | **str** | Email address associated with the account. | [optional] 
**department** | **str** | The Department name of account user. | [optional] 
**roles** | **list[str]** | Roles available for an administrator. &lt;br&gt;USER_ADMINISTRATOR - Can create, deactivate or delete accounts and reset passwords. Additionally, install replacement license keys. &lt;br&gt; CRYPTO_ADMINISTRATOR - Can manage local keys and certificates. &lt;br&gt; ADMINISTRATOR - Can configure partner connections and most system settings (except the management of native accounts and the handling of local keys and certificates. &lt;br&gt;EXPRESSION_ADMINISTRATOR - Can add and update OGNL expressions. &lt;br&gt; | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


