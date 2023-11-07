# openapi_client.InverterControlApi

All URIs are relative to *https://api.givenergy.cloud/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_setting_presets**](InverterControlApi.md#get_setting_presets) | **GET** /inverter/{inverter_serial_number}/presets | Get Setting Presets
[**get_settings_list**](InverterControlApi.md#get_settings_list) | **GET** /inverter/{inverter_serial_number}/settings | Get Settings List
[**modify_preset**](InverterControlApi.md#modify_preset) | **POST** /inverter/{inverter_serial_number}/presets/{preset} | Modify Preset
[**modify_setting**](InverterControlApi.md#modify_setting) | **POST** /inverter/{inverter_serial_number}/settings/{setting_id}/write | Modify Setting
[**modify_setting_multiple**](InverterControlApi.md#modify_setting_multiple) | **POST** /multi-control/write | Modify Setting (Multiple)
[**read_setting**](InverterControlApi.md#read_setting) | **POST** /inverter/{inverter_serial_number}/settings/{setting_id}/read | Read Setting
[**read_setting_multiple**](InverterControlApi.md#read_setting_multiple) | **POST** /multi-control/read | Read Setting (Multiple)


# **get_setting_presets**
> str get_setting_presets(inverter_serial_number, authorization=authorization)

Get Setting Presets

Retrieves a list of available setting presets for a given inverter

### Example

* Bearer Authentication (default):
```python
import time
import os
import openapi_client
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
    api_instance = openapi_client.InverterControlApi(api_client)
    inverter_serial_number = 'CE1234G567' # str | The serial number of the inverter.
    authorization = 'Bearer {YOUR_API_KEY}' # str |  (optional)

    try:
        # Get Setting Presets
        api_response = api_instance.get_setting_presets(inverter_serial_number, authorization=authorization)
        print("The response of InverterControlApi->get_setting_presets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InverterControlApi->get_setting_presets: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inverter_serial_number** | **str**| The serial number of the inverter. | 
 **authorization** | **str**|  | [optional] 

### Return type

**str**

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_settings_list**
> GetSettingsList200Response get_settings_list(inverter_serial_number, authorization=authorization)

Get Settings List

Returns a set of inverter settings available to your account

### Example

* Bearer Authentication (default):
```python
import time
import os
import openapi_client
from openapi_client.models.get_settings_list200_response import GetSettingsList200Response
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
    api_instance = openapi_client.InverterControlApi(api_client)
    inverter_serial_number = 'CE1234G567' # str | The serial number of the inverter.
    authorization = 'Bearer {YOUR_API_KEY}' # str |  (optional)

    try:
        # Get Settings List
        api_response = api_instance.get_settings_list(inverter_serial_number, authorization=authorization)
        print("The response of InverterControlApi->get_settings_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InverterControlApi->get_settings_list: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inverter_serial_number** | **str**| The serial number of the inverter. | 
 **authorization** | **str**|  | [optional] 

### Return type

[**GetSettingsList200Response**](GetSettingsList200Response.md)

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

# **modify_preset**
> ModifyPreset200Response modify_preset(inverter_serial_number, preset, authorization=authorization)

Modify Preset

Modify one or more inverter settings using a given preset

### Example

* Bearer Authentication (default):
```python
import time
import os
import openapi_client
from openapi_client.models.modify_preset200_response import ModifyPreset200Response
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
    api_instance = openapi_client.InverterControlApi(api_client)
    inverter_serial_number = 'CE1234G567' # str | The serial number of the inverter.
    preset = 'consequatur' # str | The preset.
    authorization = 'Bearer {YOUR_API_KEY}' # str |  (optional)

    try:
        # Modify Preset
        api_response = api_instance.modify_preset(inverter_serial_number, preset, authorization=authorization)
        print("The response of InverterControlApi->modify_preset:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InverterControlApi->modify_preset: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inverter_serial_number** | **str**| The serial number of the inverter. | 
 **preset** | **str**| The preset. | 
 **authorization** | **str**|  | [optional] 

### Return type

[**ModifyPreset200Response**](ModifyPreset200Response.md)

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

# **modify_setting**
> ModifySetting200Response modify_setting(inverter_serial_number, setting_id, modify_setting_request, authorization=authorization)

Modify Setting

Write a value to the setting on the inverter

### Example

* Bearer Authentication (default):
```python
import time
import os
import openapi_client
from openapi_client.models.modify_setting200_response import ModifySetting200Response
from openapi_client.models.modify_setting_request import ModifySettingRequest
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
    api_instance = openapi_client.InverterControlApi(api_client)
    inverter_serial_number = 'CE1234G567' # str | The serial number of the inverter.
    setting_id = 17 # int | The ID of the setting.
    modify_setting_request = openapi_client.ModifySettingRequest() # ModifySettingRequest | 
    authorization = 'Bearer {YOUR_API_KEY}' # str |  (optional)

    try:
        # Modify Setting
        api_response = api_instance.modify_setting(inverter_serial_number, setting_id, modify_setting_request, authorization=authorization)
        print("The response of InverterControlApi->modify_setting:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InverterControlApi->modify_setting: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inverter_serial_number** | **str**| The serial number of the inverter. | 
 **setting_id** | **int**| The ID of the setting. | 
 **modify_setting_request** | [**ModifySettingRequest**](ModifySettingRequest.md)|  | 
 **authorization** | **str**|  | [optional] 

### Return type

[**ModifySetting200Response**](ModifySetting200Response.md)

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

# **modify_setting_multiple**
> str modify_setting_multiple(modify_setting_multiple_request, authorization=authorization)

Modify Setting (Multiple)

Write a value to a setting on multiple inverters <aside class=\"warning\">Only attempt to modify the setting for inverters that you are certain exist and which you have access to. Improper use of this endpoint may lead to restrictions being imposed on your account</aside>

### Example

* Bearer Authentication (default):
```python
import time
import os
import openapi_client
from openapi_client.models.modify_setting_multiple_request import ModifySettingMultipleRequest
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
    api_instance = openapi_client.InverterControlApi(api_client)
    modify_setting_multiple_request = openapi_client.ModifySettingMultipleRequest() # ModifySettingMultipleRequest | 
    authorization = 'Bearer {YOUR_API_KEY}' # str |  (optional)

    try:
        # Modify Setting (Multiple)
        api_response = api_instance.modify_setting_multiple(modify_setting_multiple_request, authorization=authorization)
        print("The response of InverterControlApi->modify_setting_multiple:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InverterControlApi->modify_setting_multiple: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **modify_setting_multiple_request** | [**ModifySettingMultipleRequest**](ModifySettingMultipleRequest.md)|  | 
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

# **read_setting**
> ReadSetting200Response read_setting(inverter_serial_number, setting_id, authorization=authorization)

Read Setting

Read a specific setting on the inverter

### Example

* Bearer Authentication (default):
```python
import time
import os
import openapi_client
from openapi_client.models.read_setting200_response import ReadSetting200Response
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
    api_instance = openapi_client.InverterControlApi(api_client)
    inverter_serial_number = 'CE1234G567' # str | The serial number of the inverter.
    setting_id = 17 # int | The ID of the setting.
    authorization = 'Bearer {YOUR_API_KEY}' # str |  (optional)

    try:
        # Read Setting
        api_response = api_instance.read_setting(inverter_serial_number, setting_id, authorization=authorization)
        print("The response of InverterControlApi->read_setting:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InverterControlApi->read_setting: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inverter_serial_number** | **str**| The serial number of the inverter. | 
 **setting_id** | **int**| The ID of the setting. | 
 **authorization** | **str**|  | [optional] 

### Return type

[**ReadSetting200Response**](ReadSetting200Response.md)

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

# **read_setting_multiple**
> str read_setting_multiple(read_setting_multiple_request, authorization=authorization)

Read Setting (Multiple)

Read a specific setting on multiple inverters <aside class=\"warning\">Only attempt to read the setting for inverters that you are certain exist and which you have access to. Improper use of this endpoint may lead to restrictions being imposed on your account</aside>

### Example

* Bearer Authentication (default):
```python
import time
import os
import openapi_client
from openapi_client.models.read_setting_multiple_request import ReadSettingMultipleRequest
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
    api_instance = openapi_client.InverterControlApi(api_client)
    read_setting_multiple_request = openapi_client.ReadSettingMultipleRequest() # ReadSettingMultipleRequest | 
    authorization = 'Bearer {YOUR_API_KEY}' # str |  (optional)

    try:
        # Read Setting (Multiple)
        api_response = api_instance.read_setting_multiple(read_setting_multiple_request, authorization=authorization)
        print("The response of InverterControlApi->read_setting_multiple:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InverterControlApi->read_setting_multiple: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **read_setting_multiple_request** | [**ReadSettingMultipleRequest**](ReadSettingMultipleRequest.md)|  | 
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

