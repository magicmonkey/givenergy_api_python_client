# ReadSettingMultipleRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inverter_serials** | **List[str]** | An array of inverter serial numbers to send the command to with a maximum length of 1000 | 
**setting_id** | **int** | The ID of the setting to modify | 

## Example

```python
from openapi_client.models.read_setting_multiple_request import ReadSettingMultipleRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ReadSettingMultipleRequest from a JSON string
read_setting_multiple_request_instance = ReadSettingMultipleRequest.from_json(json)
# print the JSON string representation of the object
print ReadSettingMultipleRequest.to_json()

# convert the object into a dict
read_setting_multiple_request_dict = read_setting_multiple_request_instance.to_dict()
# create an instance of ReadSettingMultipleRequest from a dict
read_setting_multiple_request_form_dict = read_setting_multiple_request.from_dict(read_setting_multiple_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


