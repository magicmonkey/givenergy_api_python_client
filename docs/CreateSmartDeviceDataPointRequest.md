# CreateSmartDeviceDataPointRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time** | [**ISO8601Datetime**](ISO8601Datetime.md) | The date &amp; time that the data point was created | 
**power** | **int** |  | 

## Example

```python
from openapi_client.models.create_smart_device_data_point_request import CreateSmartDeviceDataPointRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSmartDeviceDataPointRequest from a JSON string
create_smart_device_data_point_request_instance = CreateSmartDeviceDataPointRequest.from_json(json)
# print the JSON string representation of the object
print CreateSmartDeviceDataPointRequest.to_json()

# convert the object into a dict
create_smart_device_data_point_request_dict = create_smart_device_data_point_request_instance.to_dict()
# create an instance of CreateSmartDeviceDataPointRequest from a dict
create_smart_device_data_point_request_form_dict = create_smart_device_data_point_request.from_dict(create_smart_device_data_point_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


