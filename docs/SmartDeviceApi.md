# openapi_client.SmartDeviceApi

All URIs are relative to *https://api.givenergy.cloud/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_smart_device_data_point**](SmartDeviceApi.md#create_smart_device_data_point) | **POST** /smart-device/{smartDevice_uuid}/data | Create Smart Device Data Point
[**get_smart_device_by_id**](SmartDeviceApi.md#get_smart_device_by_id) | **GET** /smart-device/{smartDevice_uuid} | Get Smart Device by ID
[**get_smart_device_data_points_by_id**](SmartDeviceApi.md#get_smart_device_data_points_by_id) | **GET** /smart-device/{smartDevice_uuid}/data | Get Smart Device Data Points by ID


# **create_smart_device_data_point**
> CreateSmartDeviceDataPoint200Response create_smart_device_data_point(smart_device_uuid, create_smart_device_data_point_request, authorization=authorization)

Create Smart Device Data Point

Store a data point against a smart device

### Example

* Bearer Authentication (default):
```python
import time
import os
import openapi_client
from openapi_client.models.create_smart_device_data_point200_response import CreateSmartDeviceDataPoint200Response
from openapi_client.models.create_smart_device_data_point_request import CreateSmartDeviceDataPointRequest
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
    api_instance = openapi_client.SmartDeviceApi(api_client)
    smart_device_uuid = '66529e01-d113-3473-8d6f-9e11e09332ea' # str | The UUID of the smartDevice.
    create_smart_device_data_point_request = openapi_client.CreateSmartDeviceDataPointRequest() # CreateSmartDeviceDataPointRequest | 
    authorization = 'Bearer {YOUR_API_KEY}' # str |  (optional)

    try:
        # Create Smart Device Data Point
        api_response = api_instance.create_smart_device_data_point(smart_device_uuid, create_smart_device_data_point_request, authorization=authorization)
        print("The response of SmartDeviceApi->create_smart_device_data_point:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SmartDeviceApi->create_smart_device_data_point: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **smart_device_uuid** | **str**| The UUID of the smartDevice. | 
 **create_smart_device_data_point_request** | [**CreateSmartDeviceDataPointRequest**](CreateSmartDeviceDataPointRequest.md)|  | 
 **authorization** | **str**|  | [optional] 

### Return type

[**CreateSmartDeviceDataPoint200Response**](CreateSmartDeviceDataPoint200Response.md)

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

# **get_smart_device_by_id**
> GetSmartDeviceByID200Response get_smart_device_by_id(smart_device_uuid, authorization=authorization)

Get Smart Device by ID

Get a smart device's information

### Example

* Bearer Authentication (default):
```python
import time
import os
import openapi_client
from openapi_client.models.get_smart_device_by_id200_response import GetSmartDeviceByID200Response
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
    api_instance = openapi_client.SmartDeviceApi(api_client)
    smart_device_uuid = '66529e01-d113-3473-8d6f-9e11e09332ea' # str | The UUID of the smartDevice.
    authorization = 'Bearer {YOUR_API_KEY}' # str |  (optional)

    try:
        # Get Smart Device by ID
        api_response = api_instance.get_smart_device_by_id(smart_device_uuid, authorization=authorization)
        print("The response of SmartDeviceApi->get_smart_device_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SmartDeviceApi->get_smart_device_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **smart_device_uuid** | **str**| The UUID of the smartDevice. | 
 **authorization** | **str**|  | [optional] 

### Return type

[**GetSmartDeviceByID200Response**](GetSmartDeviceByID200Response.md)

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

# **get_smart_device_data_points_by_id**
> GetSmartDeviceDataPointsByID200Response get_smart_device_data_points_by_id(smart_device_uuid, page=page, page_size=page_size, authorization=authorization)

Get Smart Device Data Points by ID

Get a list of a smart device's data points

### Example

* Bearer Authentication (default):
```python
import time
import os
import openapi_client
from openapi_client.models.get_smart_device_data_points_by_id200_response import GetSmartDeviceDataPointsByID200Response
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
    api_instance = openapi_client.SmartDeviceApi(api_client)
    smart_device_uuid = '66529e01-d113-3473-8d6f-9e11e09332ea' # str | The UUID of the smartDevice.
    page = 1 # int | Page number to return (optional)
    page_size = 56 # int | Number of items to return in a page. Defaults to 15 (optional)
    authorization = 'Bearer {YOUR_API_KEY}' # str |  (optional)

    try:
        # Get Smart Device Data Points by ID
        api_response = api_instance.get_smart_device_data_points_by_id(smart_device_uuid, page=page, page_size=page_size, authorization=authorization)
        print("The response of SmartDeviceApi->get_smart_device_data_points_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SmartDeviceApi->get_smart_device_data_points_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **smart_device_uuid** | **str**| The UUID of the smartDevice. | 
 **page** | **int**| Page number to return | [optional] 
 **page_size** | **int**| Number of items to return in a page. Defaults to 15 | [optional] 
 **authorization** | **str**|  | [optional] 

### Return type

[**GetSmartDeviceDataPointsByID200Response**](GetSmartDeviceDataPointsByID200Response.md)

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

