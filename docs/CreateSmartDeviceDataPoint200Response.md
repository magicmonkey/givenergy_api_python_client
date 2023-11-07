# CreateSmartDeviceDataPoint200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[CreateSmartDeviceDataPoint200ResponseDataInner]**](CreateSmartDeviceDataPoint200ResponseDataInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.create_smart_device_data_point200_response import CreateSmartDeviceDataPoint200Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSmartDeviceDataPoint200Response from a JSON string
create_smart_device_data_point200_response_instance = CreateSmartDeviceDataPoint200Response.from_json(json)
# print the JSON string representation of the object
print CreateSmartDeviceDataPoint200Response.to_json()

# convert the object into a dict
create_smart_device_data_point200_response_dict = create_smart_device_data_point200_response_instance.to_dict()
# create an instance of CreateSmartDeviceDataPoint200Response from a dict
create_smart_device_data_point200_response_form_dict = create_smart_device_data_point200_response.from_dict(create_smart_device_data_point200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


