# PingOneConnection

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The persistent, unique ID of the connection. This property is system-assigned if not specified. | [optional] 
**name** | **str** | The name of the PingOne connection. | 
**description** | **str** | A description for the PingOne connection. | [optional] 
**active** | **bool** | Whether or not this connection is active. Defaults to true. | [optional] 
**credential** | **str** | The credential for the PingOne connection. To update the credential, specify the plaintext value of the credential in this field. This field will not be populated for GET requests. | [optional] 
**encrypted_credential** | **str** | The encrypted credential for the PingOne connection. For POST and PUT requests, if you wish to keep the existing credential, this field should be passed back unchanged. | [optional] 
**credential_id** | **str** | The ID of the PingOne credential. This field is read only. | [optional] 
**ping_one_connection_id** | **str** | The ID of the PingOne connection. This field is read only. | [optional] 
**environment_id** | **str** | The ID of the environment of the PingOne credential. This field is read only. | [optional] 
**creation_date** | **datetime** | The creation date of the PingOne connection. This field is read only. | [optional] 
**organization_name** | **str** | The name of the organization associated with this PingOne connection. This field is read only. | [optional] 
**region** | **str** | The region of the PingOne connection. This field is read only. | [optional] 
**ping_one_management_api_endpoint** | **str** | The PingOne management API endpoint. This field is read only. | [optional] 
**ping_one_authentication_api_endpoint** | **str** | The PingOne authentication API endpoint. This field is read only. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


