# IdpAdapterAssertionMapping

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**idp_adapter_ref** | [**ResourceLink**](ResourceLink.md) | Reference to the associated IdP adapter.&lt;br&gt;Note: This is ignored if adapter overrides for this mapping exists. In this case, the override&#39;s parent adapter reference is used. | 
**restrict_virtual_entity_ids** | **bool** | Restricts this mapping to specific virtual entity IDs. | [optional] 
**restricted_virtual_entity_ids** | **list[str]** | The list of virtual server IDs that this mapping is restricted to. | [optional] 
**adapter_override_settings** | [**IdpAdapter**](IdpAdapter.md) | Connection specific configuration overrides for the mapped adapter instance. | [optional] 
**abort_sso_transaction_as_fail_safe** | **bool** | If set to true, SSO transaction will be aborted as a fail-safe when the data-store&#39;s attribute mappings fail to complete the attribute contract. Otherwise, the attribute contract with default values is used. By default, this value is false. | [optional] 
**attribute_sources** | [**list[AttributeSource]**](AttributeSource.md) | A list of configured data stores to look up attributes from. | [optional] 
**attribute_contract_fulfillment** | [**dict(str, AttributeFulfillmentValue)**](AttributeFulfillmentValue.md) | A list of mappings from attribute names to their fulfillment values. | 
**issuance_criteria** | [**IssuanceCriteria**](IssuanceCriteria.md) | The issuance criteria that this transaction must meet before the corresponding attribute contract is fulfilled. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


