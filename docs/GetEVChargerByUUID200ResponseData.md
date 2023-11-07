# GetEVChargerByUUID200ResponseData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** |  | [optional] 
**serial_number** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**alias** | **str** |  | [optional] 
**online** | **bool** |  | [optional] 
**went_offline_at** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.get_ev_charger_by_uuid200_response_data import GetEVChargerByUUID200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of GetEVChargerByUUID200ResponseData from a JSON string
get_ev_charger_by_uuid200_response_data_instance = GetEVChargerByUUID200ResponseData.from_json(json)
# print the JSON string representation of the object
print GetEVChargerByUUID200ResponseData.to_json()

# convert the object into a dict
get_ev_charger_by_uuid200_response_data_dict = get_ev_charger_by_uuid200_response_data_instance.to_dict()
# create an instance of GetEVChargerByUUID200ResponseData from a dict
get_ev_charger_by_uuid200_response_data_form_dict = get_ev_charger_by_uuid200_response_data.from_dict(get_ev_charger_by_uuid200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


