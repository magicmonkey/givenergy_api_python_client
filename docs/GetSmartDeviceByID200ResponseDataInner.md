# GetSmartDeviceByID200ResponseDataInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** |  | [optional] 
**alias** | **str** |  | [optional] 
**other_data** | [**GetSmartDeviceByID200ResponseDataInnerOtherData**](GetSmartDeviceByID200ResponseDataInnerOtherData.md) |  | [optional] 

## Example

```python
from openapi_client.models.get_smart_device_by_id200_response_data_inner import GetSmartDeviceByID200ResponseDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetSmartDeviceByID200ResponseDataInner from a JSON string
get_smart_device_by_id200_response_data_inner_instance = GetSmartDeviceByID200ResponseDataInner.from_json(json)
# print the JSON string representation of the object
print GetSmartDeviceByID200ResponseDataInner.to_json()

# convert the object into a dict
get_smart_device_by_id200_response_data_inner_dict = get_smart_device_by_id200_response_data_inner_instance.to_dict()
# create an instance of GetSmartDeviceByID200ResponseDataInner from a dict
get_smart_device_by_id200_response_data_inner_form_dict = get_smart_device_by_id200_response_data_inner.from_dict(get_smart_device_by_id200_response_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


