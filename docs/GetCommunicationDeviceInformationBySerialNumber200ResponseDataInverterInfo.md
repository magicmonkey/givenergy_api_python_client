# GetCommunicationDeviceInformationBySerialNumber200ResponseDataInverterInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**battery_type** | **str** |  | [optional] 
**battery** | [**GetCommunicationDeviceInformationBySerialNumber200ResponseDataInverterInfoBattery**](GetCommunicationDeviceInformationBySerialNumber200ResponseDataInverterInfoBattery.md) |  | [optional] 
**model** | **str** |  | [optional] 
**max_charge_rate** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.get_communication_device_information_by_serial_number200_response_data_inverter_info import GetCommunicationDeviceInformationBySerialNumber200ResponseDataInverterInfo

# TODO update the JSON string below
json = "{}"
# create an instance of GetCommunicationDeviceInformationBySerialNumber200ResponseDataInverterInfo from a JSON string
get_communication_device_information_by_serial_number200_response_data_inverter_info_instance = GetCommunicationDeviceInformationBySerialNumber200ResponseDataInverterInfo.from_json(json)
# print the JSON string representation of the object
print GetCommunicationDeviceInformationBySerialNumber200ResponseDataInverterInfo.to_json()

# convert the object into a dict
get_communication_device_information_by_serial_number200_response_data_inverter_info_dict = get_communication_device_information_by_serial_number200_response_data_inverter_info_instance.to_dict()
# create an instance of GetCommunicationDeviceInformationBySerialNumber200ResponseDataInverterInfo from a dict
get_communication_device_information_by_serial_number200_response_data_inverter_info_form_dict = get_communication_device_information_by_serial_number200_response_data_inverter_info.from_dict(get_communication_device_information_by_serial_number200_response_data_inverter_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


