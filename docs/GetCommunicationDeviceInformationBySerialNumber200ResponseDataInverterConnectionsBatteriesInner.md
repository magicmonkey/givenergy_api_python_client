# GetCommunicationDeviceInformationBySerialNumber200ResponseDataInverterConnectionsBatteriesInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**serial** | **str** |  | [optional] 
**firmware_version** | **str** |  | [optional] 
**capacity** | [**GetCommunicationDeviceInformationBySerialNumber200ResponseDataInverterConnectionsBatteriesInnerCapacity**](GetCommunicationDeviceInformationBySerialNumber200ResponseDataInverterConnectionsBatteriesInnerCapacity.md) |  | [optional] 
**cell_count** | **int** |  | [optional] 
**has_usb** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.get_communication_device_information_by_serial_number200_response_data_inverter_connections_batteries_inner import GetCommunicationDeviceInformationBySerialNumber200ResponseDataInverterConnectionsBatteriesInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetCommunicationDeviceInformationBySerialNumber200ResponseDataInverterConnectionsBatteriesInner from a JSON string
get_communication_device_information_by_serial_number200_response_data_inverter_connections_batteries_inner_instance = GetCommunicationDeviceInformationBySerialNumber200ResponseDataInverterConnectionsBatteriesInner.from_json(json)
# print the JSON string representation of the object
print GetCommunicationDeviceInformationBySerialNumber200ResponseDataInverterConnectionsBatteriesInner.to_json()

# convert the object into a dict
get_communication_device_information_by_serial_number200_response_data_inverter_connections_batteries_inner_dict = get_communication_device_information_by_serial_number200_response_data_inverter_connections_batteries_inner_instance.to_dict()
# create an instance of GetCommunicationDeviceInformationBySerialNumber200ResponseDataInverterConnectionsBatteriesInner from a dict
get_communication_device_information_by_serial_number200_response_data_inverter_connections_batteries_inner_form_dict = get_communication_device_information_by_serial_number200_response_data_inverter_connections_batteries_inner.from_dict(get_communication_device_information_by_serial_number200_response_data_inverter_connections_batteries_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


