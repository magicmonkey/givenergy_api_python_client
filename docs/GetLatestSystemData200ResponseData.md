# GetLatestSystemData200ResponseData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time** | **str** |  | [optional] 
**solar** | [**GetLatestSystemData200ResponseDataSolar**](GetLatestSystemData200ResponseDataSolar.md) |  | [optional] 
**grid** | [**GetLatestSystemData200ResponseDataGrid**](GetLatestSystemData200ResponseDataGrid.md) |  | [optional] 
**battery** | [**GetLatestSystemData200ResponseDataBattery**](GetLatestSystemData200ResponseDataBattery.md) |  | [optional] 
**inverter** | [**GetLatestSystemData200ResponseDataInverter**](GetLatestSystemData200ResponseDataInverter.md) |  | [optional] 
**consumption** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.get_latest_system_data200_response_data import GetLatestSystemData200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of GetLatestSystemData200ResponseData from a JSON string
get_latest_system_data200_response_data_instance = GetLatestSystemData200ResponseData.from_json(json)
# print the JSON string representation of the object
print GetLatestSystemData200ResponseData.to_json()

# convert the object into a dict
get_latest_system_data200_response_data_dict = get_latest_system_data200_response_data_instance.to_dict()
# create an instance of GetLatestSystemData200ResponseData from a dict
get_latest_system_data200_response_data_form_dict = get_latest_system_data200_response_data.from_dict(get_latest_system_data200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


