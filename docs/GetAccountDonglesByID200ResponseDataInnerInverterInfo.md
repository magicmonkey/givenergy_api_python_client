# GetAccountDonglesByID200ResponseDataInnerInverterInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**battery_type** | **str** |  | [optional] 
**battery** | [**GetAccountDonglesByID200ResponseDataInnerInverterInfoBattery**](GetAccountDonglesByID200ResponseDataInnerInverterInfoBattery.md) |  | [optional] 
**model** | **str** |  | [optional] 
**max_charge_rate** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.get_account_dongles_by_id200_response_data_inner_inverter_info import GetAccountDonglesByID200ResponseDataInnerInverterInfo

# TODO update the JSON string below
json = "{}"
# create an instance of GetAccountDonglesByID200ResponseDataInnerInverterInfo from a JSON string
get_account_dongles_by_id200_response_data_inner_inverter_info_instance = GetAccountDonglesByID200ResponseDataInnerInverterInfo.from_json(json)
# print the JSON string representation of the object
print GetAccountDonglesByID200ResponseDataInnerInverterInfo.to_json()

# convert the object into a dict
get_account_dongles_by_id200_response_data_inner_inverter_info_dict = get_account_dongles_by_id200_response_data_inner_inverter_info_instance.to_dict()
# create an instance of GetAccountDonglesByID200ResponseDataInnerInverterInfo from a dict
get_account_dongles_by_id200_response_data_inner_inverter_info_form_dict = get_account_dongles_by_id200_response_data_inner_inverter_info.from_dict(get_account_dongles_by_id200_response_data_inner_inverter_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


