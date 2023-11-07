# GetDataPoints200ResponseDataInnerPowerInverter


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
from openapi_client.models.get_data_points200_response_data_inner_power_inverter import GetDataPoints200ResponseDataInnerPowerInverter

# TODO update the JSON string below
json = "{}"
# create an instance of GetDataPoints200ResponseDataInnerPowerInverter from a JSON string
get_data_points200_response_data_inner_power_inverter_instance = GetDataPoints200ResponseDataInnerPowerInverter.from_json(json)
# print the JSON string representation of the object
print GetDataPoints200ResponseDataInnerPowerInverter.to_json()

# convert the object into a dict
get_data_points200_response_data_inner_power_inverter_dict = get_data_points200_response_data_inner_power_inverter_instance.to_dict()
# create an instance of GetDataPoints200ResponseDataInnerPowerInverter from a dict
get_data_points200_response_data_inner_power_inverter_form_dict = get_data_points200_response_data_inner_power_inverter.from_dict(get_data_points200_response_data_inner_power_inverter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


