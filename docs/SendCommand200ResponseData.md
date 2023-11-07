# SendCommand200ResponseData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] 
**success** | **bool** |  | [optional] 
**message** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.send_command200_response_data import SendCommand200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of SendCommand200ResponseData from a JSON string
send_command200_response_data_instance = SendCommand200ResponseData.from_json(json)
# print the JSON string representation of the object
print SendCommand200ResponseData.to_json()

# convert the object into a dict
send_command200_response_data_dict = send_command200_response_data_instance.to_dict()
# create an instance of SendCommand200ResponseData from a dict
send_command200_response_data_form_dict = send_command200_response_data.from_dict(send_command200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


