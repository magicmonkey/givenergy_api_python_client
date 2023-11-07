# GetAccountInformationByID200ResponseData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**role** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**address** | **str** |  | [optional] 
**postcode** | **str** |  | [optional] 
**country** | **str** |  | [optional] 
**telephone_number** | **str** |  | [optional] 
**timezone** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.get_account_information_by_id200_response_data import GetAccountInformationByID200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of GetAccountInformationByID200ResponseData from a JSON string
get_account_information_by_id200_response_data_instance = GetAccountInformationByID200ResponseData.from_json(json)
# print the JSON string representation of the object
print GetAccountInformationByID200ResponseData.to_json()

# convert the object into a dict
get_account_information_by_id200_response_data_dict = get_account_information_by_id200_response_data_instance.to_dict()
# create an instance of GetAccountInformationByID200ResponseData from a dict
get_account_information_by_id200_response_data_form_dict = get_account_information_by_id200_response_data.from_dict(get_account_information_by_id200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


