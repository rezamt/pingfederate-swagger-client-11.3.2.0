# AccountManagementSettings

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_status_attribute_name** | **str** | The account status attribute name. | 
**account_status_algorithm** | **str** | The account status algorithm name.  ACCOUNT_STATUS_ALGORITHM_AD -  Algorithm name for Active Directory, which uses a bitmap for each user entry.  ACCOUNT_STATUS_ALGORITHM_FLAG - Algorithm name for Oracle Directory Server and other LDAP directories that use a separate attribute to store the user&#39;s status. When this option is selected, the Flag Comparison Value and Flag Comparison Status fields should be used. | 
**flag_comparison_value** | **str** | The flag that represents comparison value. | [optional] 
**flag_comparison_status** | **bool** | The flag that represents comparison status. | [optional] 
**default_status** | **bool** | The default status of the account. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


