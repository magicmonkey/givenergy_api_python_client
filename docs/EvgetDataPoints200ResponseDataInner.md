# EvgetDataPoints200ResponseDataInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meter_id** | **int** |  | [optional] 
**timestamp** | **str** |  | [optional] 
**measurements** | [**List[EvgetDataPoints200ResponseDataInnerMeasurementsInner]**](EvgetDataPoints200ResponseDataInnerMeasurementsInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.evget_data_points200_response_data_inner import EvgetDataPoints200ResponseDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of EvgetDataPoints200ResponseDataInner from a JSON string
evget_data_points200_response_data_inner_instance = EvgetDataPoints200ResponseDataInner.from_json(json)
# print the JSON string representation of the object
print EvgetDataPoints200ResponseDataInner.to_json()

# convert the object into a dict
evget_data_points200_response_data_inner_dict = evget_data_points200_response_data_inner_instance.to_dict()
# create an instance of EvgetDataPoints200ResponseDataInner from a dict
evget_data_points200_response_data_inner_form_dict = evget_data_points200_response_data_inner.from_dict(evget_data_points200_response_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


