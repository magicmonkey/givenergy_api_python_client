# EvgetDataPoints200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[EvgetDataPoints200ResponseDataInner]**](EvgetDataPoints200ResponseDataInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.evget_data_points200_response import EvgetDataPoints200Response

# TODO update the JSON string below
json = "{}"
# create an instance of EvgetDataPoints200Response from a JSON string
evget_data_points200_response_instance = EvgetDataPoints200Response.from_json(json)
# print the JSON string representation of the object
print EvgetDataPoints200Response.to_json()

# convert the object into a dict
evget_data_points200_response_dict = evget_data_points200_response_instance.to_dict()
# create an instance of EvgetDataPoints200Response from a dict
evget_data_points200_response_form_dict = evget_data_points200_response.from_dict(evget_data_points200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


