# GetLatestMeterData200ResponseDataTotal


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**solar** | **float** |  | [optional] 
**grid** | [**GetLatestMeterData200ResponseDataTotalGrid**](GetLatestMeterData200ResponseDataTotalGrid.md) |  | [optional] 
**battery** | [**GetLatestMeterData200ResponseDataTotalBattery**](GetLatestMeterData200ResponseDataTotalBattery.md) |  | [optional] 
**consumption** | **float** |  | [optional] 
**ac_charge** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.get_latest_meter_data200_response_data_total import GetLatestMeterData200ResponseDataTotal

# TODO update the JSON string below
json = "{}"
# create an instance of GetLatestMeterData200ResponseDataTotal from a JSON string
get_latest_meter_data200_response_data_total_instance = GetLatestMeterData200ResponseDataTotal.from_json(json)
# print the JSON string representation of the object
print GetLatestMeterData200ResponseDataTotal.to_json()

# convert the object into a dict
get_latest_meter_data200_response_data_total_dict = get_latest_meter_data200_response_data_total_instance.to_dict()
# create an instance of GetLatestMeterData200ResponseDataTotal from a dict
get_latest_meter_data200_response_data_total_form_dict = get_latest_meter_data200_response_data_total.from_dict(get_latest_meter_data200_response_data_total_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


