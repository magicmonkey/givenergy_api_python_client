# GetAccountDonglesByID200ResponseDataInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**serial_number** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**commission_date** | **str** |  | [optional] 
**inverter** | [**GetAccountDonglesByID200ResponseDataInnerInverter**](GetAccountDonglesByID200ResponseDataInnerInverter.md) |  | [optional] 

## Example

```python
from openapi_client.models.get_account_dongles_by_id200_response_data_inner import GetAccountDonglesByID200ResponseDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetAccountDonglesByID200ResponseDataInner from a JSON string
get_account_dongles_by_id200_response_data_inner_instance = GetAccountDonglesByID200ResponseDataInner.from_json(json)
# print the JSON string representation of the object
print GetAccountDonglesByID200ResponseDataInner.to_json()

# convert the object into a dict
get_account_dongles_by_id200_response_data_inner_dict = get_account_dongles_by_id200_response_data_inner_instance.to_dict()
# create an instance of GetAccountDonglesByID200ResponseDataInner from a dict
get_account_dongles_by_id200_response_data_inner_form_dict = get_account_dongles_by_id200_response_data_inner.from_dict(get_account_dongles_by_id200_response_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


