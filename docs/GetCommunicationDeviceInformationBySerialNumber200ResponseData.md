# GetCommunicationDeviceInformationBySerialNumber200ResponseData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**serial_number** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**commission_date** | **str** |  | [optional] 
**inverter** | [**GetCommunicationDeviceInformationBySerialNumber200ResponseDataInverter**](GetCommunicationDeviceInformationBySerialNumber200ResponseDataInverter.md) |  | [optional] 

## Example

```python
from openapi_client.models.get_communication_device_information_by_serial_number200_response_data import GetCommunicationDeviceInformationBySerialNumber200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of GetCommunicationDeviceInformationBySerialNumber200ResponseData from a JSON string
get_communication_device_information_by_serial_number200_response_data_instance = GetCommunicationDeviceInformationBySerialNumber200ResponseData.from_json(json)
# print the JSON string representation of the object
print GetCommunicationDeviceInformationBySerialNumber200ResponseData.to_json()

# convert the object into a dict
get_communication_device_information_by_serial_number200_response_data_dict = get_communication_device_information_by_serial_number200_response_data_instance.to_dict()
# create an instance of GetCommunicationDeviceInformationBySerialNumber200ResponseData from a dict
get_communication_device_information_by_serial_number200_response_data_form_dict = get_communication_device_information_by_serial_number200_response_data.from_dict(get_communication_device_information_by_serial_number200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


