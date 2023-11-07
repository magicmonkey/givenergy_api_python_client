# GetEnergyFlowDataRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_time** | [**Datetime**](Datetime.md) | The start time of the query. Based on the inverter&#39;s local time | 
**end_time** | [**Datetime**](Datetime.md) | The end time of the query. Based on the inverter&#39;s local time | 
**grouping** | **int** | The way in which to group the data. See the above table for a complete list of grouping IDs | 
**types** | **List[int]** | An array of type IDs. See the above table for a complete list of type IDs. Leave blank to fetch all types | [optional] 

## Example

```python
from openapi_client.models.get_energy_flow_data_request import GetEnergyFlowDataRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetEnergyFlowDataRequest from a JSON string
get_energy_flow_data_request_instance = GetEnergyFlowDataRequest.from_json(json)
# print the JSON string representation of the object
print GetEnergyFlowDataRequest.to_json()

# convert the object into a dict
get_energy_flow_data_request_dict = get_energy_flow_data_request_instance.to_dict()
# create an instance of GetEnergyFlowDataRequest from a dict
get_energy_flow_data_request_form_dict = get_energy_flow_data_request.from_dict(get_energy_flow_data_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


