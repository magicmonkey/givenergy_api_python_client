# GetSettingsList200ResponseDataInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**validation** | **str** |  | [optional] 
**validation_rules** | **List[str]** |  | [optional] 

## Example

```python
from openapi_client.models.get_settings_list200_response_data_inner import GetSettingsList200ResponseDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetSettingsList200ResponseDataInner from a JSON string
get_settings_list200_response_data_inner_instance = GetSettingsList200ResponseDataInner.from_json(json)
# print the JSON string representation of the object
print GetSettingsList200ResponseDataInner.to_json()

# convert the object into a dict
get_settings_list200_response_data_inner_dict = get_settings_list200_response_data_inner_instance.to_dict()
# create an instance of GetSettingsList200ResponseDataInner from a dict
get_settings_list200_response_data_inner_form_dict = get_settings_list200_response_data_inner.from_dict(get_settings_list200_response_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


