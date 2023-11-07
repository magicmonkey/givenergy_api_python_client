# GetDataPoints200ResponseDataInnerTotal


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**solar** | **float** |  | [optional] 
**grid** | [**GetDataPoints200ResponseDataInnerTotalGrid**](GetDataPoints200ResponseDataInnerTotalGrid.md) |  | [optional] 
**battery** | [**GetDataPoints200ResponseDataInnerTotalBattery**](GetDataPoints200ResponseDataInnerTotalBattery.md) |  | [optional] 
**consumption** | **float** |  | [optional] 
**ac_charge** | **float** |  | [optional] 

## Example

```python
from openapi_client.models.get_data_points200_response_data_inner_total import GetDataPoints200ResponseDataInnerTotal

# TODO update the JSON string below
json = "{}"
# create an instance of GetDataPoints200ResponseDataInnerTotal from a JSON string
get_data_points200_response_data_inner_total_instance = GetDataPoints200ResponseDataInnerTotal.from_json(json)
# print the JSON string representation of the object
print GetDataPoints200ResponseDataInnerTotal.to_json()

# convert the object into a dict
get_data_points200_response_data_inner_total_dict = get_data_points200_response_data_inner_total_instance.to_dict()
# create an instance of GetDataPoints200ResponseDataInnerTotal from a dict
get_data_points200_response_data_inner_total_form_dict = get_data_points200_response_data_inner_total.from_dict(get_data_points200_response_data_inner_total_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


