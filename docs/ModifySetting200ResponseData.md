# ModifySetting200ResponseData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **bool** |  | [optional] 
**success** | **bool** |  | [optional] 
**message** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.modify_setting200_response_data import ModifySetting200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of ModifySetting200ResponseData from a JSON string
modify_setting200_response_data_instance = ModifySetting200ResponseData.from_json(json)
# print the JSON string representation of the object
print ModifySetting200ResponseData.to_json()

# convert the object into a dict
modify_setting200_response_data_dict = modify_setting200_response_data_instance.to_dict()
# create an instance of ModifySetting200ResponseData from a dict
modify_setting200_response_data_form_dict = modify_setting200_response_data.from_dict(modify_setting200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


