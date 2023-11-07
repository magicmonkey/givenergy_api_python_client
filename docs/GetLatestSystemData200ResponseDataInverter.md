# GetLatestSystemData200ResponseDataInverter


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**temperature** | **float** |  | [optional] 
**power** | **int** |  | [optional] 
**output_voltage** | **float** |  | [optional] 
**output_frequency** | **float** |  | [optional] 
**eps_power** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.get_latest_system_data200_response_data_inverter import GetLatestSystemData200ResponseDataInverter

# TODO update the JSON string below
json = "{}"
# create an instance of GetLatestSystemData200ResponseDataInverter from a JSON string
get_latest_system_data200_response_data_inverter_instance = GetLatestSystemData200ResponseDataInverter.from_json(json)
# print the JSON string representation of the object
print GetLatestSystemData200ResponseDataInverter.to_json()

# convert the object into a dict
get_latest_system_data200_response_data_inverter_dict = get_latest_system_data200_response_data_inverter_instance.to_dict()
# create an instance of GetLatestSystemData200ResponseDataInverter from a dict
get_latest_system_data200_response_data_inverter_form_dict = get_latest_system_data200_response_data_inverter.from_dict(get_latest_system_data200_response_data_inverter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


