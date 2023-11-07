# GetLatestMeterData200ResponseDataToday


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**solar** | **float** |  | [optional] 
**grid** | [**GetLatestMeterData200ResponseDataTodayGrid**](GetLatestMeterData200ResponseDataTodayGrid.md) |  | [optional] 
**battery** | [**GetLatestMeterData200ResponseDataTodayBattery**](GetLatestMeterData200ResponseDataTodayBattery.md) |  | [optional] 
**consumption** | **float** |  | [optional] 
**ac_charge** | **float** |  | [optional] 

## Example

```python
from openapi_client.models.get_latest_meter_data200_response_data_today import GetLatestMeterData200ResponseDataToday

# TODO update the JSON string below
json = "{}"
# create an instance of GetLatestMeterData200ResponseDataToday from a JSON string
get_latest_meter_data200_response_data_today_instance = GetLatestMeterData200ResponseDataToday.from_json(json)
# print the JSON string representation of the object
print GetLatestMeterData200ResponseDataToday.to_json()

# convert the object into a dict
get_latest_meter_data200_response_data_today_dict = get_latest_meter_data200_response_data_today_instance.to_dict()
# create an instance of GetLatestMeterData200ResponseDataToday from a dict
get_latest_meter_data200_response_data_today_form_dict = get_latest_meter_data200_response_data_today.from_dict(get_latest_meter_data200_response_data_today_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


