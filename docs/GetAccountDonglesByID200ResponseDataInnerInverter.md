# GetAccountDonglesByID200ResponseDataInnerInverter


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**serial** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**last_online** | **str** |  | [optional] 
**last_updated** | **str** |  | [optional] 
**commission_date** | **str** |  | [optional] 
**info** | [**GetAccountDonglesByID200ResponseDataInnerInverterInfo**](GetAccountDonglesByID200ResponseDataInnerInverterInfo.md) |  | [optional] 
**warranty** | [**GetAccountDonglesByID200ResponseDataInnerInverterWarranty**](GetAccountDonglesByID200ResponseDataInnerInverterWarranty.md) |  | [optional] 
**firmware_version** | [**GetAccountDonglesByID200ResponseDataInnerInverterFirmwareVersion**](GetAccountDonglesByID200ResponseDataInnerInverterFirmwareVersion.md) |  | [optional] 
**connections** | [**GetAccountDonglesByID200ResponseDataInnerInverterConnections**](GetAccountDonglesByID200ResponseDataInnerInverterConnections.md) |  | [optional] 

## Example

```python
from openapi_client.models.get_account_dongles_by_id200_response_data_inner_inverter import GetAccountDonglesByID200ResponseDataInnerInverter

# TODO update the JSON string below
json = "{}"
# create an instance of GetAccountDonglesByID200ResponseDataInnerInverter from a JSON string
get_account_dongles_by_id200_response_data_inner_inverter_instance = GetAccountDonglesByID200ResponseDataInnerInverter.from_json(json)
# print the JSON string representation of the object
print GetAccountDonglesByID200ResponseDataInnerInverter.to_json()

# convert the object into a dict
get_account_dongles_by_id200_response_data_inner_inverter_dict = get_account_dongles_by_id200_response_data_inner_inverter_instance.to_dict()
# create an instance of GetAccountDonglesByID200ResponseDataInnerInverter from a dict
get_account_dongles_by_id200_response_data_inner_inverter_form_dict = get_account_dongles_by_id200_response_data_inner_inverter.from_dict(get_account_dongles_by_id200_response_data_inner_inverter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


