# GetDataPoints200ResponseDataInnerToday


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**solar** | **float** |  | [optional] 
**grid** | [**GetDataPoints200ResponseDataInnerTodayGrid**](GetDataPoints200ResponseDataInnerTodayGrid.md) |  | [optional] 
**battery** | [**GetDataPoints200ResponseDataInnerTodayBattery**](GetDataPoints200ResponseDataInnerTodayBattery.md) |  | [optional] 
**consumption** | **float** |  | [optional] 
**ac_charge** | **float** |  | [optional] 

## Example

```python
from openapi_client.models.get_data_points200_response_data_inner_today import GetDataPoints200ResponseDataInnerToday

# TODO update the JSON string below
json = "{}"
# create an instance of GetDataPoints200ResponseDataInnerToday from a JSON string
get_data_points200_response_data_inner_today_instance = GetDataPoints200ResponseDataInnerToday.from_json(json)
# print the JSON string representation of the object
print GetDataPoints200ResponseDataInnerToday.to_json()

# convert the object into a dict
get_data_points200_response_data_inner_today_dict = get_data_points200_response_data_inner_today_instance.to_dict()
# create an instance of GetDataPoints200ResponseDataInnerToday from a dict
get_data_points200_response_data_inner_today_form_dict = get_data_points200_response_data_inner_today.from_dict(get_data_points200_response_data_inner_today_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


