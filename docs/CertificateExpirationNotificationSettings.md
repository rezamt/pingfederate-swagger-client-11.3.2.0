# CertificateExpirationNotificationSettings

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email_address** | **str** | Email address where notifications are sent. | 
**initial_warning_period** | **int** | Time before certificate expiration when initial warning is sent (in days). | [optional] 
**final_warning_period** | **int** | Time before certificate expiration when final warning is sent (in days). | 
**notification_publisher_ref** | [**ResourceLink**](ResourceLink.md) | Reference to the associated notification publisher. | [optional] 
**notification_mode** | **str** | The mode of notification. Set to NOTIFICATION_PUBLISHER to enable email notifications and server log messages. Set to LOGGING_ONLY to enable server log messages. Defaults to NOTIFICATION_PUBLISHER. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


