# GetDataPoints200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[GetDataPoints200ResponseDataInner]**](GetDataPoints200ResponseDataInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.get_data_points200_response import GetDataPoints200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetDataPoints200Response from a JSON string
get_data_points200_response_instance = GetDataPoints200Response.from_json(json)
# print the JSON string representation of the object
print GetDataPoints200Response.to_json()

# convert the object into a dict
get_data_points200_response_dict = get_data_points200_response_instance.to_dict()
# create an instance of GetDataPoints200Response from a dict
get_data_points200_response_form_dict = get_data_points200_response.from_dict(get_data_points200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


