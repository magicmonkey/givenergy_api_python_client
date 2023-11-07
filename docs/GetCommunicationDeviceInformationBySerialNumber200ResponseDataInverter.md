# GetCommunicationDeviceInformationBySerialNumber200ResponseDataInverter


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**serial** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**last_online** | **str** |  | [optional] 
**last_updated** | **str** |  | [optional] 
**commission_date** | **str** |  | [optional] 
**info** | [**GetCommunicationDeviceInformationBySerialNumber200ResponseDataInverterInfo**](GetCommunicationDeviceInformationBySerialNumber200ResponseDataInverterInfo.md) |  | [optional] 
**warranty** | [**GetCommunicationDeviceInformationBySerialNumber200ResponseDataInverterWarranty**](GetCommunicationDeviceInformationBySerialNumber200ResponseDataInverterWarranty.md) |  | [optional] 
**firmware_version** | [**GetCommunicationDeviceInformationBySerialNumber200ResponseDataInverterFirmwareVersion**](GetCommunicationDeviceInformationBySerialNumber200ResponseDataInverterFirmwareVersion.md) |  | [optional] 
**connections** | [**GetCommunicationDeviceInformationBySerialNumber200ResponseDataInverterConnections**](GetCommunicationDeviceInformationBySerialNumber200ResponseDataInverterConnections.md) |  | [optional] 

## Example

```python
from openapi_client.models.get_communication_device_information_by_serial_number200_response_data_inverter import GetCommunicationDeviceInformationBySerialNumber200ResponseDataInverter

# TODO update the JSON string below
json = "{}"
# create an instance of GetCommunicationDeviceInformationBySerialNumber200ResponseDataInverter from a JSON string
get_communication_device_information_by_serial_number200_response_data_inverter_instance = GetCommunicationDeviceInformationBySerialNumber200ResponseDataInverter.from_json(json)
# print the JSON string representation of the object
print GetCommunicationDeviceInformationBySerialNumber200ResponseDataInverter.to_json()

# convert the object into a dict
get_communication_device_information_by_serial_number200_response_data_inverter_dict = get_communication_device_information_by_serial_number200_response_data_inverter_instance.to_dict()
# create an instance of GetCommunicationDeviceInformationBySerialNumber200ResponseDataInverter from a dict
get_communication_device_information_by_serial_number200_response_data_inverter_form_dict = get_communication_device_information_by_serial_number200_response_data_inverter.from_dict(get_communication_device_information_by_serial_number200_response_data_inverter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


