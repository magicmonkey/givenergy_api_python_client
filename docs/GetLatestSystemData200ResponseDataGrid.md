# GetLatestSystemData200ResponseDataGrid


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**voltage** | **float** |  | [optional] 
**current** | **float** |  | [optional] 
**power** | **int** |  | [optional] 
**frequency** | **float** |  | [optional] 

## Example

```python
from openapi_client.models.get_latest_system_data200_response_data_grid import GetLatestSystemData200ResponseDataGrid

# TODO update the JSON string below
json = "{}"
# create an instance of GetLatestSystemData200ResponseDataGrid from a JSON string
get_latest_system_data200_response_data_grid_instance = GetLatestSystemData200ResponseDataGrid.from_json(json)
# print the JSON string representation of the object
print GetLatestSystemData200ResponseDataGrid.to_json()

# convert the object into a dict
get_latest_system_data200_response_data_grid_dict = get_latest_system_data200_response_data_grid_instance.to_dict()
# create an instance of GetLatestSystemData200ResponseDataGrid from a dict
get_latest_system_data200_response_data_grid_form_dict = get_latest_system_data200_response_data_grid.from_dict(get_latest_system_data200_response_data_grid_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


