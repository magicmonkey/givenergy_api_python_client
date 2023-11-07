# openapi_client.AccountApi

All URIs are relative to *https://api.givenergy.cloud/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_account_children_information_by_id**](AccountApi.md#get_account_children_information_by_id) | **GET** /account-children/{user_id} | Get Account Children Information by ID
[**get_account_dongles_by_id**](AccountApi.md#get_account_dongles_by_id) | **GET** /account/{user_username}/devices | Get Account Dongles by ID
[**get_account_information_by_id**](AccountApi.md#get_account_information_by_id) | **GET** /account/{user_id} | Get Account Information by ID
[**get_account_information_by_username**](AccountApi.md#get_account_information_by_username) | **GET** /account/search/{user_username} | Get Account Information by Username
[**get_your_account_children_information**](AccountApi.md#get_your_account_children_information) | **GET** /account-children | Get Your Account Children Information
[**get_your_account_information**](AccountApi.md#get_your_account_information) | **GET** /account | Get Your Account Information


# **get_account_children_information_by_id**
> GetAccountChildrenInformationByID200Response get_account_children_information_by_id(user_id, page=page, page_size=page_size, authorization=authorization)

Get Account Children Information by ID

Retrieves a list of accounts that the specified account has access to

### Example

* Bearer Authentication (default):
```python
import time
import os
import openapi_client
from openapi_client.models.get_account_children_information_by_id200_response import GetAccountChildrenInformationByID200Response
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
    api_instance = openapi_client.AccountApi(api_client)
    user_id = '1234' # str | The ID of the user.
    page = 1 # int | Page number to return (optional)
    page_size = 56 # int | Number of items to return in a page. Defaults to 15 (optional)
    authorization = 'Bearer {YOUR_API_KEY}' # str |  (optional)

    try:
        # Get Account Children Information by ID
        api_response = api_instance.get_account_children_information_by_id(user_id, page=page, page_size=page_size, authorization=authorization)
        print("The response of AccountApi->get_account_children_information_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->get_account_children_information_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The ID of the user. | 
 **page** | **int**| Page number to return | [optional] 
 **page_size** | **int**| Number of items to return in a page. Defaults to 15 | [optional] 
 **authorization** | **str**|  | [optional] 

### Return type

[**GetAccountChildrenInformationByID200Response**](GetAccountChildrenInformationByID200Response.md)

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

# **get_account_dongles_by_id**
> GetAccountDonglesByID200Response get_account_dongles_by_id(user_username, page=page, page_size=page_size, authorization=authorization)

Get Account Dongles by ID

Retrieves a list of dongles for an account by its ID

### Example

* Bearer Authentication (default):
```python
import time
import os
import openapi_client
from openapi_client.models.get_account_dongles_by_id200_response import GetAccountDonglesByID200Response
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
    api_instance = openapi_client.AccountApi(api_client)
    user_username = 'qkunze' # str | The username of the user.
    page = 1 # int | Page number to return (optional)
    page_size = 56 # int | Number of items to return in a page. Defaults to 15 (optional)
    authorization = 'Bearer {YOUR_API_KEY}' # str |  (optional)

    try:
        # Get Account Dongles by ID
        api_response = api_instance.get_account_dongles_by_id(user_username, page=page, page_size=page_size, authorization=authorization)
        print("The response of AccountApi->get_account_dongles_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->get_account_dongles_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_username** | **str**| The username of the user. | 
 **page** | **int**| Page number to return | [optional] 
 **page_size** | **int**| Number of items to return in a page. Defaults to 15 | [optional] 
 **authorization** | **str**|  | [optional] 

### Return type

[**GetAccountDonglesByID200Response**](GetAccountDonglesByID200Response.md)

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

# **get_account_information_by_id**
> GetAccountInformationByID200Response get_account_information_by_id(user_id, authorization=authorization)

Get Account Information by ID

Retrieves the information of a specific account by its ID

### Example

* Bearer Authentication (default):
```python
import time
import os
import openapi_client
from openapi_client.models.get_account_information_by_id200_response import GetAccountInformationByID200Response
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
    api_instance = openapi_client.AccountApi(api_client)
    user_id = '1234' # str | The ID of the user.
    authorization = 'Bearer {YOUR_API_KEY}' # str |  (optional)

    try:
        # Get Account Information by ID
        api_response = api_instance.get_account_information_by_id(user_id, authorization=authorization)
        print("The response of AccountApi->get_account_information_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->get_account_information_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The ID of the user. | 
 **authorization** | **str**|  | [optional] 

### Return type

[**GetAccountInformationByID200Response**](GetAccountInformationByID200Response.md)

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

# **get_account_information_by_username**
> GetAccountInformationByUsername200Response get_account_information_by_username(user_username, authorization=authorization)

Get Account Information by Username

Retrieves the information of a specific account by its username

### Example

* Bearer Authentication (default):
```python
import time
import os
import openapi_client
from openapi_client.models.get_account_information_by_username200_response import GetAccountInformationByUsername200Response
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
    api_instance = openapi_client.AccountApi(api_client)
    user_username = 'qkunze' # str | The username of the user.
    authorization = 'Bearer {YOUR_API_KEY}' # str |  (optional)

    try:
        # Get Account Information by Username
        api_response = api_instance.get_account_information_by_username(user_username, authorization=authorization)
        print("The response of AccountApi->get_account_information_by_username:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->get_account_information_by_username: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_username** | **str**| The username of the user. | 
 **authorization** | **str**|  | [optional] 

### Return type

[**GetAccountInformationByUsername200Response**](GetAccountInformationByUsername200Response.md)

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

# **get_your_account_children_information**
> GetYourAccountChildrenInformation200Response get_your_account_children_information(page=page, page_size=page_size, authorization=authorization)

Get Your Account Children Information

Retrieves a list of accounts that your account has access to

### Example

* Bearer Authentication (default):
```python
import time
import os
import openapi_client
from openapi_client.models.get_your_account_children_information200_response import GetYourAccountChildrenInformation200Response
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
    api_instance = openapi_client.AccountApi(api_client)
    page = 1 # int | Page number to return (optional)
    page_size = 56 # int | Number of items to return in a page. Defaults to 15 (optional)
    authorization = 'Bearer {YOUR_API_KEY}' # str |  (optional)

    try:
        # Get Your Account Children Information
        api_response = api_instance.get_your_account_children_information(page=page, page_size=page_size, authorization=authorization)
        print("The response of AccountApi->get_your_account_children_information:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->get_your_account_children_information: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number to return | [optional] 
 **page_size** | **int**| Number of items to return in a page. Defaults to 15 | [optional] 
 **authorization** | **str**|  | [optional] 

### Return type

[**GetYourAccountChildrenInformation200Response**](GetYourAccountChildrenInformation200Response.md)

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

# **get_your_account_information**
> GetYourAccountInformation200Response get_your_account_information(authorization=authorization)

Get Your Account Information

Retrieves your account information

### Example

* Bearer Authentication (default):
```python
import time
import os
import openapi_client
from openapi_client.models.get_your_account_information200_response import GetYourAccountInformation200Response
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
    api_instance = openapi_client.AccountApi(api_client)
    authorization = 'Bearer {YOUR_API_KEY}' # str |  (optional)

    try:
        # Get Your Account Information
        api_response = api_instance.get_your_account_information(authorization=authorization)
        print("The response of AccountApi->get_your_account_information:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->get_your_account_information: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [optional] 

### Return type

[**GetYourAccountInformation200Response**](GetYourAccountInformation200Response.md)

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

