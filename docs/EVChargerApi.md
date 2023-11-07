# openapi_client.EVChargerApi

All URIs are relative to *https://api.givenergy.cloud/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**evget_data_points**](EVChargerApi.md#evget_data_points) | **GET** /ev-charger/{charger_uuid}/meter-data | Get Data Points
[**get_charging_sessions**](EVChargerApi.md#get_charging_sessions) | **GET** /ev-charger/{charger_uuid}/charging-sessions | Get Charging Sessions
[**get_command_data**](EVChargerApi.md#get_command_data) | **GET** /ev-charger/{charger_uuid}/commands/{command_id} | Get Command Data
[**get_ev_charger_by_uuid**](EVChargerApi.md#get_ev_charger_by_uuid) | **GET** /ev-charger/{charger_uuid} | Get EV Charger by UUID
[**get_supported_commands**](EVChargerApi.md#get_supported_commands) | **GET** /ev-charger/{charger_uuid}/commands | Get Supported Commands
[**get_your_ev_chargers**](EVChargerApi.md#get_your_ev_chargers) | **GET** /ev-charger | Get Your EV Chargers
[**send_command**](EVChargerApi.md#send_command) | **POST** /ev-charger/{charger_uuid}/commands/{command_id} | Send Command


# **evget_data_points**
> EvgetDataPoints200Response evget_data_points(charger_uuid, start_time, end_time, measurands, meter_ids, page=page, page_size=page_size, authorization=authorization)

Get Data Points



### Example

* Bearer Authentication (default):
```python
import time
import os
import openapi_client
from openapi_client.models.evget_data_points200_response import EvgetDataPoints200Response
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
    api_instance = openapi_client.EVChargerApi(api_client)
    charger_uuid = '66529e01-d113-3473-8d6f-9e11e09332ea' # str | The UUID of the charger.
    start_time = '2023-06-01T00:00:00Z' # str | The time of the earliest data point. Must be a valid date. Must be a date before <code>now</code>.
    end_time = '2023-06-02T00:00:00Z' # str | The time of the latest data point. Must be a valid date. Must be a date after <code>start_time</code>.
    measurands = ['[1]'] # List[str] | One or more measurands to filter by.
    meter_ids = [[1]] # List[int] | The IDs of the measuring devices to fetch data for.
    page = 1 # int | Page number to return (optional)
    page_size = 56 # int | Number of items to return in a page. Defaults to 15 (optional)
    authorization = 'Bearer {YOUR_API_KEY}' # str |  (optional)

    try:
        # Get Data Points
        api_response = api_instance.evget_data_points(charger_uuid, start_time, end_time, measurands, meter_ids, page=page, page_size=page_size, authorization=authorization)
        print("The response of EVChargerApi->evget_data_points:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EVChargerApi->evget_data_points: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **charger_uuid** | **str**| The UUID of the charger. | 
 **start_time** | **str**| The time of the earliest data point. Must be a valid date. Must be a date before &lt;code&gt;now&lt;/code&gt;. | 
 **end_time** | **str**| The time of the latest data point. Must be a valid date. Must be a date after &lt;code&gt;start_time&lt;/code&gt;. | 
 **measurands** | [**List[str]**](str.md)| One or more measurands to filter by. | 
 **meter_ids** | [**List[int]**](int.md)| The IDs of the measuring devices to fetch data for. | 
 **page** | **int**| Page number to return | [optional] 
 **page_size** | **int**| Number of items to return in a page. Defaults to 15 | [optional] 
 **authorization** | **str**|  | [optional] 

### Return type

[**EvgetDataPoints200Response**](EvgetDataPoints200Response.md)

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

# **get_charging_sessions**
> GetChargingSessions200Response get_charging_sessions(charger_uuid, page=page, page_size=page_size, authorization=authorization, get_charging_sessions_request=get_charging_sessions_request)

Get Charging Sessions

Fetch a list of all charging sessions for the given EV charger

### Example

* Bearer Authentication (default):
```python
import time
import os
import openapi_client
from openapi_client.models.get_charging_sessions200_response import GetChargingSessions200Response
from openapi_client.models.get_charging_sessions_request import GetChargingSessionsRequest
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
    api_instance = openapi_client.EVChargerApi(api_client)
    charger_uuid = '66529e01-d113-3473-8d6f-9e11e09332ea' # str | The UUID of the charger.
    page = 1 # int | Page number to return (optional)
    page_size = 56 # int | Number of items to return in a page. Defaults to 15 (optional)
    authorization = 'Bearer {YOUR_API_KEY}' # str |  (optional)
    get_charging_sessions_request = openapi_client.GetChargingSessionsRequest() # GetChargingSessionsRequest |  (optional)

    try:
        # Get Charging Sessions
        api_response = api_instance.get_charging_sessions(charger_uuid, page=page, page_size=page_size, authorization=authorization, get_charging_sessions_request=get_charging_sessions_request)
        print("The response of EVChargerApi->get_charging_sessions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EVChargerApi->get_charging_sessions: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **charger_uuid** | **str**| The UUID of the charger. | 
 **page** | **int**| Page number to return | [optional] 
 **page_size** | **int**| Number of items to return in a page. Defaults to 15 | [optional] 
 **authorization** | **str**|  | [optional] 
 **get_charging_sessions_request** | [**GetChargingSessionsRequest**](GetChargingSessionsRequest.md)|  | [optional] 

### Return type

[**GetChargingSessions200Response**](GetChargingSessions200Response.md)

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

# **get_command_data**
> GetCommandData200Response get_command_data(charger_uuid, command_id, authorization=authorization)

Get Command Data

Fetch the current data for the given command and EV Charger  <aside class=\"notice\">A 422 error will be thrown if an invalid command ID is provided or if the given EV charger does not support the given command</aside>  The below response example is for the <code>change-mode</code> command

### Example

* Bearer Authentication (default):
```python
import time
import os
import openapi_client
from openapi_client.models.get_command_data200_response import GetCommandData200Response
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
    api_instance = openapi_client.EVChargerApi(api_client)
    charger_uuid = '66529e01-d113-3473-8d6f-9e11e09332ea' # str | The UUID of the charger.
    command_id = 'restart-charger' # str | The ID of the command.
    authorization = 'Bearer {YOUR_API_KEY}' # str |  (optional)

    try:
        # Get Command Data
        api_response = api_instance.get_command_data(charger_uuid, command_id, authorization=authorization)
        print("The response of EVChargerApi->get_command_data:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EVChargerApi->get_command_data: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **charger_uuid** | **str**| The UUID of the charger. | 
 **command_id** | **str**| The ID of the command. | 
 **authorization** | **str**|  | [optional] 

### Return type

[**GetCommandData200Response**](GetCommandData200Response.md)

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

# **get_ev_charger_by_uuid**
> GetEVChargerByUUID200Response get_ev_charger_by_uuid(charger_uuid, authorization=authorization)

Get EV Charger by UUID

Return information about a single EV charger by its UUID

### Example

* Bearer Authentication (default):
```python
import time
import os
import openapi_client
from openapi_client.models.get_ev_charger_by_uuid200_response import GetEVChargerByUUID200Response
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
    api_instance = openapi_client.EVChargerApi(api_client)
    charger_uuid = '66529e01-d113-3473-8d6f-9e11e09332ea' # str | The UUID of the charger.
    authorization = 'Bearer {YOUR_API_KEY}' # str |  (optional)

    try:
        # Get EV Charger by UUID
        api_response = api_instance.get_ev_charger_by_uuid(charger_uuid, authorization=authorization)
        print("The response of EVChargerApi->get_ev_charger_by_uuid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EVChargerApi->get_ev_charger_by_uuid: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **charger_uuid** | **str**| The UUID of the charger. | 
 **authorization** | **str**|  | [optional] 

### Return type

[**GetEVChargerByUUID200Response**](GetEVChargerByUUID200Response.md)

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

# **get_supported_commands**
> GetSupportedCommands200Response get_supported_commands(charger_uuid, authorization=authorization)

Get Supported Commands

Fetch a list of all commands that are supported for the given EV charger

### Example

* Bearer Authentication (default):
```python
import time
import os
import openapi_client
from openapi_client.models.get_supported_commands200_response import GetSupportedCommands200Response
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
    api_instance = openapi_client.EVChargerApi(api_client)
    charger_uuid = '66529e01-d113-3473-8d6f-9e11e09332ea' # str | The UUID of the charger.
    authorization = 'Bearer {YOUR_API_KEY}' # str |  (optional)

    try:
        # Get Supported Commands
        api_response = api_instance.get_supported_commands(charger_uuid, authorization=authorization)
        print("The response of EVChargerApi->get_supported_commands:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EVChargerApi->get_supported_commands: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **charger_uuid** | **str**| The UUID of the charger. | 
 **authorization** | **str**|  | [optional] 

### Return type

[**GetSupportedCommands200Response**](GetSupportedCommands200Response.md)

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

# **get_your_ev_chargers**
> GetYourEVChargers200Response get_your_ev_chargers(page=page, page_size=page_size, authorization=authorization)

Get Your EV Chargers

Return a list of EV chargers registered to your account

### Example

* Bearer Authentication (default):
```python
import time
import os
import openapi_client
from openapi_client.models.get_your_ev_chargers200_response import GetYourEVChargers200Response
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
    api_instance = openapi_client.EVChargerApi(api_client)
    page = 1 # int | Page number to return (optional)
    page_size = 56 # int | Number of items to return in a page. Defaults to 15 (optional)
    authorization = 'Bearer {YOUR_API_KEY}' # str |  (optional)

    try:
        # Get Your EV Chargers
        api_response = api_instance.get_your_ev_chargers(page=page, page_size=page_size, authorization=authorization)
        print("The response of EVChargerApi->get_your_ev_chargers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EVChargerApi->get_your_ev_chargers: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number to return | [optional] 
 **page_size** | **int**| Number of items to return in a page. Defaults to 15 | [optional] 
 **authorization** | **str**|  | [optional] 

### Return type

[**GetYourEVChargers200Response**](GetYourEVChargers200Response.md)

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

# **send_command**
> SendCommand200Response send_command(charger_uuid, command_id, authorization=authorization)

Send Command

Send a command to an EV Charger

### Example

* Bearer Authentication (default):
```python
import time
import os
import openapi_client
from openapi_client.models.send_command200_response import SendCommand200Response
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
    api_instance = openapi_client.EVChargerApi(api_client)
    charger_uuid = '66529e01-d113-3473-8d6f-9e11e09332ea' # str | The UUID of the charger.
    command_id = 'restart-charger' # str | The ID of the command.
    authorization = 'Bearer {YOUR_API_KEY}' # str |  (optional)

    try:
        # Send Command
        api_response = api_instance.send_command(charger_uuid, command_id, authorization=authorization)
        print("The response of EVChargerApi->send_command:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EVChargerApi->send_command: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **charger_uuid** | **str**| The UUID of the charger. | 
 **command_id** | **str**| The ID of the command. | 
 **authorization** | **str**|  | [optional] 

### Return type

[**SendCommand200Response**](SendCommand200Response.md)

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

