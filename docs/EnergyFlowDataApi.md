# openapi_client.EnergyFlowDataApi

All URIs are relative to *https://api.givenergy.cloud/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_energy_flow_data**](EnergyFlowDataApi.md#get_energy_flow_data) | **POST** /inverter/{inverter_serial_number}/energy-flows | Get Energy Flow Data


# **get_energy_flow_data**
> str get_energy_flow_data(inverter_serial_number, get_energy_flow_data_request, authorization=authorization)

Get Energy Flow Data

Fetches the energy flow data for a given inverter between 2 times

### Example

* Bearer Authentication (default):
```python
import time
import os
import openapi_client
from openapi_client.models.get_energy_flow_data_request import GetEnergyFlowDataRequest
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
    api_instance = openapi_client.EnergyFlowDataApi(api_client)
    inverter_serial_number = 'CE1234G567' # str | The serial number of the inverter.
    get_energy_flow_data_request = openapi_client.GetEnergyFlowDataRequest() # GetEnergyFlowDataRequest | 
    authorization = 'Bearer {YOUR_API_KEY}' # str |  (optional)

    try:
        # Get Energy Flow Data
        api_response = api_instance.get_energy_flow_data(inverter_serial_number, get_energy_flow_data_request, authorization=authorization)
        print("The response of EnergyFlowDataApi->get_energy_flow_data:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnergyFlowDataApi->get_energy_flow_data: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inverter_serial_number** | **str**| The serial number of the inverter. | 
 **get_energy_flow_data_request** | [**GetEnergyFlowDataRequest**](GetEnergyFlowDataRequest.md)|  | 
 **authorization** | **str**|  | [optional] 

### Return type

**str**

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

