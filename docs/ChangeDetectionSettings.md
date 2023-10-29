# ChangeDetectionSettings

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_object_class** | **str** | The user object class. | 
**group_object_class** | **str** | The group object class. | 
**changed_users_algorithm** | **str** | The changed user algorithm.  ACTIVE_DIRECTORY_USN - For Active Directory only, this algorithm queries for update sequence numbers on user records that are larger than the last time records were checked.  TIMESTAMP - Queries for timestamps on user records that are not older than the last time records were checked. This check is more efficient from the point of view of the PingFederate provisioner but can be more time consuming on the LDAP side, particularly with the Oracle Directory Server.  TIMESTAMP_NO_NEGATION - Queries for timestamps on user records that are newer than the last time records were checked. This algorithm is recommended for the Oracle Directory Server. | 
**usn_attribute_name** | **str** | The USN attribute name. | [optional] 
**time_stamp_attribute_name** | **str** | The timestamp attribute name. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


