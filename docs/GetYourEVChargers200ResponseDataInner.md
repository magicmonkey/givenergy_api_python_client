# GetYourEVChargers200ResponseDataInner


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
from openapi_client.models.get_your_ev_chargers200_response_data_inner import GetYourEVChargers200ResponseDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetYourEVChargers200ResponseDataInner from a JSON string
get_your_ev_chargers200_response_data_inner_instance = GetYourEVChargers200ResponseDataInner.from_json(json)
# print the JSON string representation of the object
print GetYourEVChargers200ResponseDataInner.to_json()

# convert the object into a dict
get_your_ev_chargers200_response_data_inner_dict = get_your_ev_chargers200_response_data_inner_instance.to_dict()
# create an instance of GetYourEVChargers200ResponseDataInner from a dict
get_your_ev_chargers200_response_data_inner_form_dict = get_your_ev_chargers200_response_data_inner.from_dict(get_your_ev_chargers200_response_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


