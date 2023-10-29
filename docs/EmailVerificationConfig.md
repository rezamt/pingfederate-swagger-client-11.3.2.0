# EmailVerificationConfig

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email_verification_enabled** | **bool** | Whether the email ownership verification is enabled. | [optional] 
**verify_email_template_name** | **str** | The template name for verify email. The default is message-template-email-ownership-verification.html. | [optional] 
**email_verification_sent_template_name** | **str** | The template name for email verification sent. The default is local.identity.email.verification.sent.html.&lt;br&gt;Note:Only applicable if EmailVerificationType is OTL. | [optional] 
**email_verification_success_template_name** | **str** | The template name for email verification success. The default is local.identity.email.verification.success.html. | [optional] 
**email_verification_error_template_name** | **str** | The template name for email verification error.  The default is local.identity.email.verification.error.html. | [optional] 
**email_verification_type** | **str** | Email Verification Type. | [optional] 
**otp_length** | **int** | The OTP length generated for email verification. The default is 8.&lt;br&gt;Note: Only applicable if EmailVerificationType is OTP. | [optional] 
**otp_retry_attempts** | **int** | The number of OTP retry attempts for email verification. The default is 3.&lt;br&gt;Note: Only applicable if EmailVerificationType is OTP. | [optional] 
**allowed_otp_character_set** | **str** | The allowed character set used to generate the OTP. The default is 23456789BCDFGHJKMNPQRSTVWXZbcdfghjkmnpqrstvwxz.&lt;br&gt;Note: Only applicable if EmailVerificationType is OTP. | [optional] 
**otp_time_to_live** | **int** | Field used OTP time to live. The default is 15.&lt;br&gt;Note: Only applicable if EmailVerificationType is OTP. | [optional] 
**email_verification_otp_template_name** | **str** | The template name for email verification OTP verification.  The default is local.identity.email.verification.otp.html.&lt;br&gt;Note: Only applicable if EmailVerificationType is OTP. | [optional] 
**otl_time_to_live** | **int** | Field used OTL time to live. The default is 1440.&lt;br&gt;Note: Only applicable if EmailVerificationType is OTL. | [optional] 
**field_for_email_to_verify** | **str** | Field used for email ownership verification.&lt;br&gt;Note: Not required when emailVerificationEnabled is set to false. | 
**field_storing_verification_status** | **str** | Field used for storing email verification status.&lt;br&gt;Note: Not required when emailVerificationEnabled is set to false. | 
**notification_publisher_ref** | [**ResourceLink**](ResourceLink.md) | Reference to the associated notification publisher. | [optional] 
**require_verified_email** | **bool** | Whether the user must verify their email address before they can complete a single sign-on transaction. The default is false. | [optional] 
**require_verified_email_template_name** | **str** | The template to render when the user must verify their email address before they can complete a single sign-on transaction. The default is local.identity.email.verification.required.html.&lt;br&gt;Note:Only applicable if EmailVerificationType is OTL and requireVerifiedEmail is true. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


