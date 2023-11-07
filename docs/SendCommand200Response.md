# SendCommand200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**SendCommand200ResponseData**](SendCommand200ResponseData.md) |  | [optional] 

## Example

```python
from openapi_client.models.send_command200_response import SendCommand200Response

# TODO update the JSON string below
json = "{}"
# create an instance of SendCommand200Response from a JSON string
send_command200_response_instance = SendCommand200Response.from_json(json)
# print the JSON string representation of the object
print SendCommand200Response.to_json()

# convert the object into a dict
send_command200_response_dict = send_command200_response_instance.to_dict()
# create an instance of SendCommand200Response from a dict
send_command200_response_form_dict = send_command200_response.from_dict(send_command200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


