# openapi_client.CommunicationDeviceApi

All URIs are relative to *https://api.givenergy.cloud/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_communication_device_information_by_serial_number**](CommunicationDeviceApi.md#get_communication_device_information_by_serial_number) | **GET** /communication-device/{communicationDevice_serial_number} | Get Communication Device Information by Serial Number


# **get_communication_device_information_by_serial_number**
> GetCommunicationDeviceInformationBySerialNumber200Response get_communication_device_information_by_serial_number(communication_device_serial_number, authorization=authorization)

Get Communication Device Information by Serial Number

Get a communication device's information by serial number

### Example

* Bearer Authentication (default):
```python
import time
import os
import openapi_client
from openapi_client.models.get_communication_device_information_by_serial_number200_response import GetCommunicationDeviceInformationBySerialNumber200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.givenergy.cloud/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.givenergy.cloud/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: default
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.CommunicationDeviceApi(api_client)
    communication_device_serial_number = 'consequatur' # str | The serial number of the communicationDevice.
    authorization = 'Bearer {YOUR_API_KEY}' # str |  (optional)

    try:
        # Get Communication Device Information by Serial Number
        api_response = api_instance.get_communication_device_information_by_serial_number(communication_device_serial_number, authorization=authorization)
        print("The response of CommunicationDeviceApi->get_communication_device_information_by_serial_number:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommunicationDeviceApi->get_communication_device_information_by_serial_number: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **communication_device_serial_number** | **str**| The serial number of the communicationDevice. | 
 **authorization** | **str**|  | [optional] 

### Return type

[**GetCommunicationDeviceInformationBySerialNumber200Response**](GetCommunicationDeviceInformationBySerialNumber200Response.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

