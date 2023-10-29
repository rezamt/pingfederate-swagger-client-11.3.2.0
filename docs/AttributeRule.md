# AttributeRule

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attribute_source** | [**SourceTypeIdKey**](SourceTypeIdKey.md) | The source of the attribute, if the attribute source is not provided then it is defaulted to be the previous authentication source. | [optional] 
**attribute_name** | **str** | The name of the attribute to use in this attribute rule. This field is required if the Attribute Source type is not &#39;EXPRESSION&#39;. | [optional] 
**condition** | **str** | The condition that will be applied to the attribute&#39;s expected value. This field is required if the Attribute Source type is not &#39;EXPRESSION&#39;. | [optional] 
**expected_value** | **str** | The expected value of this attribute rule. This field is required if the Attribute Source type is not &#39;EXPRESSION&#39;. | [optional] 
**expression** | **str** | The expression of this attribute rule. This field is required if the Attribute Source type is &#39;EXPRESSION&#39;. | [optional] 
**result** | **str** | The result of this attribute rule. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


