# GetChargingSessions200ResponseDataInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**started_by** | **str** |  | [optional] 
**meter_start** | **float** |  | [optional] 
**started_at** | **str** |  | [optional] 
**stopped_by** | **str** |  | [optional] 
**meter_stop** | **str** |  | [optional] 
**stopped_at** | **str** |  | [optional] 
**stop_reason** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.get_charging_sessions200_response_data_inner import GetChargingSessions200ResponseDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetChargingSessions200ResponseDataInner from a JSON string
get_charging_sessions200_response_data_inner_instance = GetChargingSessions200ResponseDataInner.from_json(json)
# print the JSON string representation of the object
print GetChargingSessions200ResponseDataInner.to_json()

# convert the object into a dict
get_charging_sessions200_response_data_inner_dict = get_charging_sessions200_response_data_inner_instance.to_dict()
# create an instance of GetChargingSessions200ResponseDataInner from a dict
get_charging_sessions200_response_data_inner_form_dict = get_charging_sessions200_response_data_inner.from_dict(get_charging_sessions200_response_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


