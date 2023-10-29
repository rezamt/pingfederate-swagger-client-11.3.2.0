# swagger_client.ServerSettingsApi

All URIs are relative to *https://localhost:9999/pf-admin-api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_certificate**](ServerSettingsApi.md#delete_certificate) | **DELETE** /serverSettings/wsTrustStsSettings/issuerCertificates/{id} | Delete a certificate from WS-Trust STS Settings.
[**get_captcha_settings**](ServerSettingsApi.md#get_captcha_settings) | **GET** /serverSettings/captchaSettings | (Deprecated) Gets the CAPTCHA settings.
[**get_cert**](ServerSettingsApi.md#get_cert) | **GET** /serverSettings/wsTrustStsSettings/issuerCertificates/{id} | Retrieve details of a certificate.
[**get_certs**](ServerSettingsApi.md#get_certs) | **GET** /serverSettings/wsTrustStsSettings/issuerCertificates | Get the list of certificates for WS-Trust STS Settings.
[**get_email_server_settings**](ServerSettingsApi.md#get_email_server_settings) | **GET** /serverSettings/emailServer | (Deprecated) Gets the email server settings
[**get_general_settings**](ServerSettingsApi.md#get_general_settings) | **GET** /serverSettings/generalSettings | Gets the general settings.
[**get_log_settings**](ServerSettingsApi.md#get_log_settings) | **GET** /serverSettings/logSettings | Gets the log settings.
[**get_notification_settings**](ServerSettingsApi.md#get_notification_settings) | **GET** /serverSettings/notifications | Gets the notification settings
[**get_out_bound_provisioning_settings**](ServerSettingsApi.md#get_out_bound_provisioning_settings) | **GET** /serverSettings/outboundProvisioning | Get database used for outbound provisioning
[**get_server_settings**](ServerSettingsApi.md#get_server_settings) | **GET** /serverSettings | Gets the server settings
[**get_system_keys**](ServerSettingsApi.md#get_system_keys) | **GET** /serverSettings/systemKeys | Get the system keys.
[**get_ws_trust_sts_settings**](ServerSettingsApi.md#get_ws_trust_sts_settings) | **GET** /serverSettings/wsTrustStsSettings | Get the current WS-Trust STS Settings.
[**import_certificate**](ServerSettingsApi.md#import_certificate) | **POST** /serverSettings/wsTrustStsSettings/issuerCertificates | Import a new certificate.
[**rotate_system_keys**](ServerSettingsApi.md#rotate_system_keys) | **POST** /serverSettings/systemKeys/rotate | Rotate the system keys.
[**update_captcha_settings**](ServerSettingsApi.md#update_captcha_settings) | **PUT** /serverSettings/captchaSettings | (Deprecated) Update the CAPTCHA settings.
[**update_email_server_settings**](ServerSettingsApi.md#update_email_server_settings) | **PUT** /serverSettings/emailServer | (Deprecated) Update the email server settings
[**update_general_settings**](ServerSettingsApi.md#update_general_settings) | **PUT** /serverSettings/generalSettings | Update general settings.
[**update_log_settings**](ServerSettingsApi.md#update_log_settings) | **PUT** /serverSettings/logSettings | Update log settings.
[**update_notification_settings**](ServerSettingsApi.md#update_notification_settings) | **PUT** /serverSettings/notifications | Update the notification settings.
[**update_out_bound_provisioning_settings**](ServerSettingsApi.md#update_out_bound_provisioning_settings) | **PUT** /serverSettings/outboundProvisioning | Update database used for outbound provisioning
[**update_server_settings**](ServerSettingsApi.md#update_server_settings) | **PUT** /serverSettings | Update the server settings.
[**update_system_keys**](ServerSettingsApi.md#update_system_keys) | **PUT** /serverSettings/systemKeys | Update the system keys.
[**update_ws_trust_sts_settings**](ServerSettingsApi.md#update_ws_trust_sts_settings) | **PUT** /serverSettings/wsTrustStsSettings | Update WS-Trust STS Settings.


# **delete_certificate**
> delete_certificate(id)

Delete a certificate from WS-Trust STS Settings.

If the request is successful, the response body is empty. If the request fails, an ApiResult is returned with details of the error.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ServerSettingsApi()
id = 'id_example' # str | ID of the certificate to delete

try:
    # Delete a certificate from WS-Trust STS Settings.
    api_instance.delete_certificate(id)
except ApiException as e:
    print("Exception when calling ServerSettingsApi->delete_certificate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the certificate to delete | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_captcha_settings**
> CaptchaSettings get_captcha_settings()

(Deprecated) Gets the CAPTCHA settings.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ServerSettingsApi()

try:
    # (Deprecated) Gets the CAPTCHA settings.
    api_response = api_instance.get_captcha_settings()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServerSettingsApi->get_captcha_settings: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**CaptchaSettings**](CaptchaSettings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cert**
> IssuerCert get_cert(id)

Retrieve details of a certificate.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ServerSettingsApi()
id = 'id_example' # str | ID of the certificate to retrieve.

try:
    # Retrieve details of a certificate.
    api_response = api_instance.get_cert(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServerSettingsApi->get_cert: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the certificate to retrieve. | 

### Return type

[**IssuerCert**](IssuerCert.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_certs**
> IssuerCerts get_certs()

Get the list of certificates for WS-Trust STS Settings.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ServerSettingsApi()

try:
    # Get the list of certificates for WS-Trust STS Settings.
    api_response = api_instance.get_certs()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServerSettingsApi->get_certs: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**IssuerCerts**](IssuerCerts.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_email_server_settings**
> EmailServerSettings get_email_server_settings()

(Deprecated) Gets the email server settings



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ServerSettingsApi()

try:
    # (Deprecated) Gets the email server settings
    api_response = api_instance.get_email_server_settings()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServerSettingsApi->get_email_server_settings: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**EmailServerSettings**](EmailServerSettings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_general_settings**
> GeneralSettings get_general_settings()

Gets the general settings.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ServerSettingsApi()

try:
    # Gets the general settings.
    api_response = api_instance.get_general_settings()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServerSettingsApi->get_general_settings: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GeneralSettings**](GeneralSettings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_log_settings**
> LogSettings get_log_settings()

Gets the log settings.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ServerSettingsApi()

try:
    # Gets the log settings.
    api_response = api_instance.get_log_settings()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServerSettingsApi->get_log_settings: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**LogSettings**](LogSettings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_notification_settings**
> NotificationSettings get_notification_settings()

Gets the notification settings



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ServerSettingsApi()

try:
    # Gets the notification settings
    api_response = api_instance.get_notification_settings()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServerSettingsApi->get_notification_settings: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NotificationSettings**](NotificationSettings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_out_bound_provisioning_settings**
> OutboundProvisionDatabase get_out_bound_provisioning_settings()

Get database used for outbound provisioning

Get the settings for database used internally to facilitate outbound provisioning to service providers.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ServerSettingsApi()

try:
    # Get database used for outbound provisioning
    api_response = api_instance.get_out_bound_provisioning_settings()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServerSettingsApi->get_out_bound_provisioning_settings: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**OutboundProvisionDatabase**](OutboundProvisionDatabase.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_server_settings**
> ServerSettings get_server_settings()

Gets the server settings



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ServerSettingsApi()

try:
    # Gets the server settings
    api_response = api_instance.get_server_settings()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServerSettingsApi->get_server_settings: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ServerSettings**](ServerSettings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_system_keys**
> SystemKeys get_system_keys()

Get the system keys.

For each key, only encryptedKeyData and not keyData will be returned

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ServerSettingsApi()

try:
    # Get the system keys.
    api_response = api_instance.get_system_keys()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServerSettingsApi->get_system_keys: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SystemKeys**](SystemKeys.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ws_trust_sts_settings**
> WsTrustStsSettings get_ws_trust_sts_settings()

Get the current WS-Trust STS Settings.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ServerSettingsApi()

try:
    # Get the current WS-Trust STS Settings.
    api_response = api_instance.get_ws_trust_sts_settings()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServerSettingsApi->get_ws_trust_sts_settings: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**WsTrustStsSettings**](WsTrustStsSettings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_certificate**
> IssuerCert import_certificate(body)

Import a new certificate.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ServerSettingsApi()
body = swagger_client.X509File() # X509File | File data to import.

try:
    # Import a new certificate.
    api_response = api_instance.import_certificate(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServerSettingsApi->import_certificate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**X509File**](X509File.md)| File data to import. | 

### Return type

[**IssuerCert**](IssuerCert.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rotate_system_keys**
> SystemKeys rotate_system_keys()

Rotate the system keys.

Upon rotation, previous key will be replaced by the current key, the current key will be replaced by the pending key, while the newly generated key replaces the pending key. Periodic rotation can ensure optimal security of your environment.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ServerSettingsApi()

try:
    # Rotate the system keys.
    api_response = api_instance.rotate_system_keys()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServerSettingsApi->rotate_system_keys: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SystemKeys**](SystemKeys.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_captcha_settings**
> CaptchaSettings update_captcha_settings(body)

(Deprecated) Update the CAPTCHA settings.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ServerSettingsApi()
body = swagger_client.CaptchaSettings() # CaptchaSettings | CAPTCHA settings.

try:
    # (Deprecated) Update the CAPTCHA settings.
    api_response = api_instance.update_captcha_settings(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServerSettingsApi->update_captcha_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CaptchaSettings**](CaptchaSettings.md)| CAPTCHA settings. | 

### Return type

[**CaptchaSettings**](CaptchaSettings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_email_server_settings**
> EmailServerSettings update_email_server_settings(body, validation_email=validation_email, validate_only=validate_only)

(Deprecated) Update the email server settings

(Deprecated) If the validationEmail is provided, an email will be sent to the validationEmail using the provided email server settings.  The settings will be saved if the test email is successfully sent.<br>

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ServerSettingsApi()
body = swagger_client.EmailServerSettings() # EmailServerSettings | Configuration for email server settings.
validation_email = 'validation_email_example' # str | The email address used to validate the email server settings. (optional)
validate_only = true # bool | Only validation will be performed.  Email server settings will not be saved. (optional)

try:
    # (Deprecated) Update the email server settings
    api_response = api_instance.update_email_server_settings(body, validation_email=validation_email, validate_only=validate_only)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServerSettingsApi->update_email_server_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EmailServerSettings**](EmailServerSettings.md)| Configuration for email server settings. | 
 **validation_email** | **str**| The email address used to validate the email server settings. | [optional] 
 **validate_only** | **bool**| Only validation will be performed.  Email server settings will not be saved. | [optional] 

### Return type

[**EmailServerSettings**](EmailServerSettings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_general_settings**
> GeneralSettings update_general_settings(body)

Update general settings.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ServerSettingsApi()
body = swagger_client.GeneralSettings() # GeneralSettings | Configuration for general settings.

try:
    # Update general settings.
    api_response = api_instance.update_general_settings(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServerSettingsApi->update_general_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GeneralSettings**](GeneralSettings.md)| Configuration for general settings. | 

### Return type

[**GeneralSettings**](GeneralSettings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_log_settings**
> LogSettings update_log_settings(body)

Update log settings.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ServerSettingsApi()
body = swagger_client.LogSettings() # LogSettings | Configuration for log settings.

try:
    # Update log settings.
    api_response = api_instance.update_log_settings(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServerSettingsApi->update_log_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LogSettings**](LogSettings.md)| Configuration for log settings. | 

### Return type

[**LogSettings**](LogSettings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_notification_settings**
> NotificationSettings update_notification_settings(body)

Update the notification settings.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ServerSettingsApi()
body = swagger_client.NotificationSettings() # NotificationSettings | Notification settings.

try:
    # Update the notification settings.
    api_response = api_instance.update_notification_settings(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServerSettingsApi->update_notification_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NotificationSettings**](NotificationSettings.md)| Notification settings. | 

### Return type

[**NotificationSettings**](NotificationSettings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_out_bound_provisioning_settings**
> OutboundProvisionDatabase update_out_bound_provisioning_settings(body)

Update database used for outbound provisioning

Update the settings for database used internally to facilitate outbound provisioning to service providers.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ServerSettingsApi()
body = swagger_client.OutboundProvisionDatabase() # OutboundProvisionDatabase | The Outbound Provision Database settings.

try:
    # Update database used for outbound provisioning
    api_response = api_instance.update_out_bound_provisioning_settings(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServerSettingsApi->update_out_bound_provisioning_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OutboundProvisionDatabase**](OutboundProvisionDatabase.md)| The Outbound Provision Database settings. | 

### Return type

[**OutboundProvisionDatabase**](OutboundProvisionDatabase.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_server_settings**
> ServerSettings update_server_settings(body)

Update the server settings.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ServerSettingsApi()
body = swagger_client.ServerSettings() # ServerSettings | Configuration for server settings.

try:
    # Update the server settings.
    api_response = api_instance.update_server_settings(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServerSettingsApi->update_server_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ServerSettings**](ServerSettings.md)| Configuration for server settings. | 

### Return type

[**ServerSettings**](ServerSettings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_system_keys**
> SystemKeys update_system_keys(body)

Update the system keys.

For each key, either encryptedKeyData or keyData must be provided.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ServerSettingsApi()
body = swagger_client.SystemKeys() # SystemKeys | System keys.

try:
    # Update the system keys.
    api_response = api_instance.update_system_keys(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServerSettingsApi->update_system_keys: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SystemKeys**](SystemKeys.md)| System keys. | 

### Return type

[**SystemKeys**](SystemKeys.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_ws_trust_sts_settings**
> WsTrustStsSettings update_ws_trust_sts_settings(body)

Update WS-Trust STS Settings.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ServerSettingsApi()
body = swagger_client.WsTrustStsSettings() # WsTrustStsSettings | Configuration for WS-Trust STS Settings.

try:
    # Update WS-Trust STS Settings.
    api_response = api_instance.update_ws_trust_sts_settings(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServerSettingsApi->update_ws_trust_sts_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**WsTrustStsSettings**](WsTrustStsSettings.md)| Configuration for WS-Trust STS Settings. | 

### Return type

[**WsTrustStsSettings**](WsTrustStsSettings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

