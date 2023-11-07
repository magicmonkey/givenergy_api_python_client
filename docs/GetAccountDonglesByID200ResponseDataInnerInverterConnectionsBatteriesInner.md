# GetAccountDonglesByID200ResponseDataInnerInverterConnectionsBatteriesInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**serial** | **str** |  | [optional] 
**firmware_version** | **str** |  | [optional] 
**capacity** | [**GetAccountDonglesByID200ResponseDataInnerInverterConnectionsBatteriesInnerCapacity**](GetAccountDonglesByID200ResponseDataInnerInverterConnectionsBatteriesInnerCapacity.md) |  | [optional] 
**cell_count** | **int** |  | [optional] 
**has_usb** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.get_account_dongles_by_id200_response_data_inner_inverter_connections_batteries_inner import GetAccountDonglesByID200ResponseDataInnerInverterConnectionsBatteriesInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetAccountDonglesByID200ResponseDataInnerInverterConnectionsBatteriesInner from a JSON string
get_account_dongles_by_id200_response_data_inner_inverter_connections_batteries_inner_instance = GetAccountDonglesByID200ResponseDataInnerInverterConnectionsBatteriesInner.from_json(json)
# print the JSON string representation of the object
print GetAccountDonglesByID200ResponseDataInnerInverterConnectionsBatteriesInner.to_json()

# convert the object into a dict
get_account_dongles_by_id200_response_data_inner_inverter_connections_batteries_inner_dict = get_account_dongles_by_id200_response_data_inner_inverter_connections_batteries_inner_instance.to_dict()
# create an instance of GetAccountDonglesByID200ResponseDataInnerInverterConnectionsBatteriesInner from a dict
get_account_dongles_by_id200_response_data_inner_inverter_connections_batteries_inner_form_dict = get_account_dongles_by_id200_response_data_inner_inverter_connections_batteries_inner.from_dict(get_account_dongles_by_id200_response_data_inner_inverter_connections_batteries_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


