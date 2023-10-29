# LicenseView

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the person the license was issued to. | [optional] 
**id** | **str** | Unique identifier of a license. | [optional] 
**max_connections** | **int** | Maximum number of connections that can be created under this license (if applicable). | [optional] 
**used_connections** | **int** | Number of used connections under this license. | [optional] 
**tier** | **str** | The tier value from the license file. The possible values are FREE, PERPETUAL or SUBSCRIPTION. | [optional] 
**issue_date** | **datetime** | The issue date value from the license file. | [optional] 
**expiration_date** | **datetime** | The expiration date value from the license file (if applicable). | [optional] 
**enforcement_type** | **str** | The enforcement type is a 3-bit binary value, expressed as a decimal digit. The bits from left to right are: &lt;br&gt;1: Shutdown on expire &lt;br&gt;2: Notify on expire &lt;br&gt;4: Enforce minor version &lt;br&gt;if all three enforcements are active, the enforcement type will be 7 (1 + 2 + 4); if only the first two are active, you have an enforcement type of 3 (1 + 2).  | [optional] 
**version** | **str** | The Ping Identity product version from the license file. | [optional] 
**product** | **str** | The Ping Identity product value from the license file. | [optional] 
**organization** | **str** | The organization value from the license file. | [optional] 
**grace_period** | **int** | Number of days provided as grace period, past the expiration date (if applicable). | [optional] 
**node_limit** | **int** | Maximum number of clustered nodes allowed under this license (if applicable). | [optional] 
**license_groups** | [**list[ConnectionGroupLicenseView]**](ConnectionGroupLicenseView.md) | License connection groups, if applicable. | [optional] 
**oauth_enabled** | **bool** | Indicates whether OAuth role is enabled for this license. | [optional] 
**ws_trust_enabled** | **bool** | Indicates whether WS-Trust role is enabled for this license. | [optional] 
**provisioning_enabled** | **bool** | Indicates whether Provisioning role is enabled for this license. | [optional] 
**bridge_mode** | **bool** | Indicates whether this license is a bridge license or not. | [optional] 
**features** | [**list[LicenseFeatureView]**](LicenseFeatureView.md) | Other licence features, if applicable. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


