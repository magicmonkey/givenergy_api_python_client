# GetEvents200ResponseDataInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event** | **str** |  | [optional] 
**start_time** | **str** |  | [optional] 
**end_time** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.get_events200_response_data_inner import GetEvents200ResponseDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetEvents200ResponseDataInner from a JSON string
get_events200_response_data_inner_instance = GetEvents200ResponseDataInner.from_json(json)
# print the JSON string representation of the object
print GetEvents200ResponseDataInner.to_json()

# convert the object into a dict
get_events200_response_data_inner_dict = get_events200_response_data_inner_instance.to_dict()
# create an instance of GetEvents200ResponseDataInner from a dict
get_events200_response_data_inner_form_dict = get_events200_response_data_inner.from_dict(get_events200_response_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


