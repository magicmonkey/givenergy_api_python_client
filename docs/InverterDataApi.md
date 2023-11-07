# openapi_client.InverterDataApi

All URIs are relative to *https://api.givenergy.cloud/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_data_points**](InverterDataApi.md#get_data_points) | **GET** /inverter/{inverter_serial_number}/data-points/{date} | Get Data Points
[**get_events**](InverterDataApi.md#get_events) | **GET** /inverter/{inverter_serial_number}/events | Get Events
[**get_latest_meter_data**](InverterDataApi.md#get_latest_meter_data) | **GET** /inverter/{inverter_serial_number}/meter-data/latest | Get Latest Meter Data
[**get_latest_system_data**](InverterDataApi.md#get_latest_system_data) | **GET** /inverter/{inverter_serial_number}/system-data/latest | Get Latest System Data


# **get_data_points**
> GetDataPoints200Response get_data_points(inverter_serial_number, var_date, page=page, page_size=page_size, authorization=authorization)

Get Data Points

Displays the entire data packet set from the chosen date

### Example

* Bearer Authentication (default):
```python
import time
import os
import openapi_client
from openapi_client.models.get_data_points200_response import GetDataPoints200Response
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
    api_instance = openapi_client.InverterDataApi(api_client)
    inverter_serial_number = 'CE1234G567' # str | The serial number of the inverter.
    var_date = '' # str | Optional parameter. ISO8601-date required The date to fetch the data. This assumes the date at the system's local time
    page = 1 # int | Page number to return (optional)
    page_size = 56 # int | Number of items to return in a page. Defaults to 15 (optional)
    authorization = 'Bearer {YOUR_API_KEY}' # str |  (optional)

    try:
        # Get Data Points
        api_response = api_instance.get_data_points(inverter_serial_number, var_date, page=page, page_size=page_size, authorization=authorization)
        print("The response of InverterDataApi->get_data_points:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InverterDataApi->get_data_points: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inverter_serial_number** | **str**| The serial number of the inverter. | 
 **var_date** | **str**| Optional parameter. ISO8601-date required The date to fetch the data. This assumes the date at the system&#39;s local time | 
 **page** | **int**| Page number to return | [optional] 
 **page_size** | **int**| Number of items to return in a page. Defaults to 15 | [optional] 
 **authorization** | **str**|  | [optional] 

### Return type

[**GetDataPoints200Response**](GetDataPoints200Response.md)

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

# **get_events**
> GetEvents200Response get_events(inverter_serial_number, start=start, end=end, cleared=cleared, page=page, page_size=page_size, authorization=authorization, get_events_request=get_events_request)

Get Events

Retrieves a list of faults that were triggered from the inverter and when they were cleared

### Example

* Bearer Authentication (default):
```python
import time
import os
import openapi_client
from openapi_client.models.get_events200_response import GetEvents200Response
from openapi_client.models.get_events_request import GetEventsRequest
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
    api_instance = openapi_client.InverterDataApi(api_client)
    inverter_serial_number = 'CE1234G567' # str | The serial number of the inverter.
    start = 'consequatur' # str | ISO8601-datetime Start time (optional)
    end = 'consequatur' # str | ISO8601-datetime End time (optional)
    cleared = false # bool | Whether 'cleared' events should be included with the data. Default is false (optional)
    page = 1 # int | Page number to return (optional)
    page_size = 56 # int | Number of items to return in a page. Defaults to 15 (optional)
    authorization = 'Bearer {YOUR_API_KEY}' # str |  (optional)
    get_events_request = openapi_client.GetEventsRequest() # GetEventsRequest |  (optional)

    try:
        # Get Events
        api_response = api_instance.get_events(inverter_serial_number, start=start, end=end, cleared=cleared, page=page, page_size=page_size, authorization=authorization, get_events_request=get_events_request)
        print("The response of InverterDataApi->get_events:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InverterDataApi->get_events: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inverter_serial_number** | **str**| The serial number of the inverter. | 
 **start** | **str**| ISO8601-datetime Start time | [optional] 
 **end** | **str**| ISO8601-datetime End time | [optional] 
 **cleared** | **bool**| Whether &#39;cleared&#39; events should be included with the data. Default is false | [optional] 
 **page** | **int**| Page number to return | [optional] 
 **page_size** | **int**| Number of items to return in a page. Defaults to 15 | [optional] 
 **authorization** | **str**|  | [optional] 
 **get_events_request** | [**GetEventsRequest**](GetEventsRequest.md)|  | [optional] 

### Return type

[**GetEvents200Response**](GetEvents200Response.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_latest_meter_data**
> GetLatestMeterData200Response get_latest_meter_data(inverter_serial_number, authorization=authorization)

Get Latest Meter Data

Retrieves the latest meter data from the inverter

### Example

* Bearer Authentication (default):
```python
import time
import os
import openapi_client
from openapi_client.models.get_latest_meter_data200_response import GetLatestMeterData200Response
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
    api_instance = openapi_client.InverterDataApi(api_client)
    inverter_serial_number = 'CE1234G567' # str | The serial number of the inverter.
    authorization = 'Bearer {YOUR_API_KEY}' # str |  (optional)

    try:
        # Get Latest Meter Data
        api_response = api_instance.get_latest_meter_data(inverter_serial_number, authorization=authorization)
        print("The response of InverterDataApi->get_latest_meter_data:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InverterDataApi->get_latest_meter_data: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inverter_serial_number** | **str**| The serial number of the inverter. | 
 **authorization** | **str**|  | [optional] 

### Return type

[**GetLatestMeterData200Response**](GetLatestMeterData200Response.md)

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

# **get_latest_system_data**
> GetLatestSystemData200Response get_latest_system_data(inverter_serial_number, authorization=authorization)

Get Latest System Data

Retrieves the latest system data from the inverter

### Example

* Bearer Authentication (default):
```python
import time
import os
import openapi_client
from openapi_client.models.get_latest_system_data200_response import GetLatestSystemData200Response
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
    api_instance = openapi_client.InverterDataApi(api_client)
    inverter_serial_number = 'CE1234G567' # str | The serial number of the inverter.
    authorization = 'Bearer {YOUR_API_KEY}' # str |  (optional)

    try:
        # Get Latest System Data
        api_response = api_instance.get_latest_system_data(inverter_serial_number, authorization=authorization)
        print("The response of InverterDataApi->get_latest_system_data:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InverterDataApi->get_latest_system_data: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inverter_serial_number** | **str**| The serial number of the inverter. | 
 **authorization** | **str**|  | [optional] 

### Return type

[**GetLatestSystemData200Response**](GetLatestSystemData200Response.md)

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

