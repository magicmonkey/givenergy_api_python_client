# GetSmartDeviceByID200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[GetSmartDeviceByID200ResponseDataInner]**](GetSmartDeviceByID200ResponseDataInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.get_smart_device_by_id200_response import GetSmartDeviceByID200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetSmartDeviceByID200Response from a JSON string
get_smart_device_by_id200_response_instance = GetSmartDeviceByID200Response.from_json(json)
# print the JSON string representation of the object
print GetSmartDeviceByID200Response.to_json()

# convert the object into a dict
get_smart_device_by_id200_response_dict = get_smart_device_by_id200_response_instance.to_dict()
# create an instance of GetSmartDeviceByID200Response from a dict
get_smart_device_by_id200_response_form_dict = get_smart_device_by_id200_response.from_dict(get_smart_device_by_id200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


