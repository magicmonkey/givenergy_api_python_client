# GetDataPoints200ResponseDataInnerPower


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**solar** | [**GetDataPoints200ResponseDataInnerPowerSolar**](GetDataPoints200ResponseDataInnerPowerSolar.md) |  | [optional] 
**grid** | [**GetDataPoints200ResponseDataInnerPowerGrid**](GetDataPoints200ResponseDataInnerPowerGrid.md) |  | [optional] 
**battery** | [**GetDataPoints200ResponseDataInnerPowerBattery**](GetDataPoints200ResponseDataInnerPowerBattery.md) |  | [optional] 
**consumption** | [**GetDataPoints200ResponseDataInnerPowerConsumption**](GetDataPoints200ResponseDataInnerPowerConsumption.md) |  | [optional] 
**inverter** | [**GetDataPoints200ResponseDataInnerPowerInverter**](GetDataPoints200ResponseDataInnerPowerInverter.md) |  | [optional] 

## Example

```python
from openapi_client.models.get_data_points200_response_data_inner_power import GetDataPoints200ResponseDataInnerPower

# TODO update the JSON string below
json = "{}"
# create an instance of GetDataPoints200ResponseDataInnerPower from a JSON string
get_data_points200_response_data_inner_power_instance = GetDataPoints200ResponseDataInnerPower.from_json(json)
# print the JSON string representation of the object
print GetDataPoints200ResponseDataInnerPower.to_json()

# convert the object into a dict
get_data_points200_response_data_inner_power_dict = get_data_points200_response_data_inner_power_instance.to_dict()
# create an instance of GetDataPoints200ResponseDataInnerPower from a dict
get_data_points200_response_data_inner_power_form_dict = get_data_points200_response_data_inner_power.from_dict(get_data_points200_response_data_inner_power_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


