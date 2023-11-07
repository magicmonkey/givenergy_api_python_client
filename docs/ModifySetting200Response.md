# ModifySetting200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ModifySetting200ResponseData**](ModifySetting200ResponseData.md) |  | [optional] 

## Example

```python
from openapi_client.models.modify_setting200_response import ModifySetting200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ModifySetting200Response from a JSON string
modify_setting200_response_instance = ModifySetting200Response.from_json(json)
# print the JSON string representation of the object
print ModifySetting200Response.to_json()

# convert the object into a dict
modify_setting200_response_dict = modify_setting200_response_instance.to_dict()
# create an instance of ModifySetting200Response from a dict
modify_setting200_response_form_dict = modify_setting200_response.from_dict(modify_setting200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


