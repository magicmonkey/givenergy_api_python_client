# GetDataPoints200ResponseDataInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time** | **str** |  | [optional] 
**power** | [**GetDataPoints200ResponseDataInnerPower**](GetDataPoints200ResponseDataInnerPower.md) |  | [optional] 
**today** | [**GetDataPoints200ResponseDataInnerToday**](GetDataPoints200ResponseDataInnerToday.md) |  | [optional] 
**total** | [**GetDataPoints200ResponseDataInnerTotal**](GetDataPoints200ResponseDataInnerTotal.md) |  | [optional] 
**is_metered** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.get_data_points200_response_data_inner import GetDataPoints200ResponseDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetDataPoints200ResponseDataInner from a JSON string
get_data_points200_response_data_inner_instance = GetDataPoints200ResponseDataInner.from_json(json)
# print the JSON string representation of the object
print GetDataPoints200ResponseDataInner.to_json()

# convert the object into a dict
get_data_points200_response_data_inner_dict = get_data_points200_response_data_inner_instance.to_dict()
# create an instance of GetDataPoints200ResponseDataInner from a dict
get_data_points200_response_data_inner_form_dict = get_data_points200_response_data_inner.from_dict(get_data_points200_response_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


