# ModifySettingMultipleRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inverter_serials** | **List[str]** | An array of inverter serial numbers to send the command to with a maximum length of 1000 | 
**setting_id** | **int** | The ID of the setting to modify | 
**value** | [**Mixed**](Mixed.md) | The value of the setting | 

## Example

```python
from openapi_client.models.modify_setting_multiple_request import ModifySettingMultipleRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ModifySettingMultipleRequest from a JSON string
modify_setting_multiple_request_instance = ModifySettingMultipleRequest.from_json(json)
# print the JSON string representation of the object
print ModifySettingMultipleRequest.to_json()

# convert the object into a dict
modify_setting_multiple_request_dict = modify_setting_multiple_request_instance.to_dict()
# create an instance of ModifySettingMultipleRequest from a dict
modify_setting_multiple_request_form_dict = modify_setting_multiple_request.from_dict(modify_setting_multiple_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


