# GetLatestMeterData200ResponseData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time** | **str** |  | [optional] 
**today** | [**GetLatestMeterData200ResponseDataToday**](GetLatestMeterData200ResponseDataToday.md) |  | [optional] 
**total** | [**GetLatestMeterData200ResponseDataTotal**](GetLatestMeterData200ResponseDataTotal.md) |  | [optional] 
**is_metered** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.get_latest_meter_data200_response_data import GetLatestMeterData200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of GetLatestMeterData200ResponseData from a JSON string
get_latest_meter_data200_response_data_instance = GetLatestMeterData200ResponseData.from_json(json)
# print the JSON string representation of the object
print GetLatestMeterData200ResponseData.to_json()

# convert the object into a dict
get_latest_meter_data200_response_data_dict = get_latest_meter_data200_response_data_instance.to_dict()
# create an instance of GetLatestMeterData200ResponseData from a dict
get_latest_meter_data200_response_data_form_dict = get_latest_meter_data200_response_data.from_dict(get_latest_meter_data200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


