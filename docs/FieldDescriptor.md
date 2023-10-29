# FieldDescriptor

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of field descriptor. | [optional] 
**name** | **str** | Name of the field. | [optional] 
**description** | **str** | Description of the field. | [optional] 
**default_value** | **str** | Default value of the field. This is the value pre-populated in the UI on new plugin instance configuration. This is also the value used to populate the field if it is missing in a POST or PUT request and no &#39;defaultForLegacyConfig&#39; is defined. | [optional] 
**default_for_legacy_config** | **str** | Default value of the field when it is missing from the configuration (e.g. in upgrade scenarios). This is the value pre-populated in the UI for existing plugin configurations without values for the field. This is also the value used to populate the field if it is missing in a POST or PUT request. If &#39;defaultForLegacyConfig&#39; is not defined, PingFederate will fall back to applying the &#39;defaultValue&#39; to the field. | [optional] 
**advanced** | **bool** | Whether this is an advanced field or not. | [optional] 
**required** | **bool** | Whether a value is required for this field or not. | [optional] 
**label** | **str** | Label of the field to be displayed in the administrative console. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


