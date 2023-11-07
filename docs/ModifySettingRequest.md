# ModifySettingRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**Mixed**](Mixed.md) | The value of the setting | 

## Example

```python
from openapi_client.models.modify_setting_request import ModifySettingRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ModifySettingRequest from a JSON string
modify_setting_request_instance = ModifySettingRequest.from_json(json)
# print the JSON string representation of the object
print ModifySettingRequest.to_json()

# convert the object into a dict
modify_setting_request_dict = modify_setting_request_instance.to_dict()
# create an instance of ModifySettingRequest from a dict
modify_setting_request_form_dict = modify_setting_request.from_dict(modify_setting_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


