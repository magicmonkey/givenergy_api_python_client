# ReadSetting200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ReadSetting200ResponseData**](ReadSetting200ResponseData.md) |  | [optional] 

## Example

```python
from openapi_client.models.read_setting200_response import ReadSetting200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ReadSetting200Response from a JSON string
read_setting200_response_instance = ReadSetting200Response.from_json(json)
# print the JSON string representation of the object
print ReadSetting200Response.to_json()

# convert the object into a dict
read_setting200_response_dict = read_setting200_response_instance.to_dict()
# create an instance of ReadSetting200Response from a dict
read_setting200_response_form_dict = read_setting200_response.from_dict(read_setting200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


