# GetLatestSystemData200ResponseDataSolar


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**power** | **int** |  | [optional] 
**arrays** | [**List[GetLatestSystemData200ResponseDataSolarArraysInner]**](GetLatestSystemData200ResponseDataSolarArraysInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.get_latest_system_data200_response_data_solar import GetLatestSystemData200ResponseDataSolar

# TODO update the JSON string below
json = "{}"
# create an instance of GetLatestSystemData200ResponseDataSolar from a JSON string
get_latest_system_data200_response_data_solar_instance = GetLatestSystemData200ResponseDataSolar.from_json(json)
# print the JSON string representation of the object
print GetLatestSystemData200ResponseDataSolar.to_json()

# convert the object into a dict
get_latest_system_data200_response_data_solar_dict = get_latest_system_data200_response_data_solar_instance.to_dict()
# create an instance of GetLatestSystemData200ResponseDataSolar from a dict
get_latest_system_data200_response_data_solar_form_dict = get_latest_system_data200_response_data_solar.from_dict(get_latest_system_data200_response_data_solar_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


