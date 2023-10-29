# IssuanceCriteria

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conditional_criteria** | [**list[ConditionalIssuanceCriteriaEntry]**](ConditionalIssuanceCriteriaEntry.md) | A list of conditional issuance criteria where existing attributes must satisfy their conditions against expected values in order for the transaction to continue. | [optional] 
**expression_criteria** | [**list[ExpressionIssuanceCriteriaEntry]**](ExpressionIssuanceCriteriaEntry.md) | A list of expression issuance criteria where the OGNL expressions must evaluate to true in order for the transaction to continue. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


