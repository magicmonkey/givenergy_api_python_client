# GetYourAccountChildrenInformation200ResponseDataInner


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
from openapi_client.models.get_your_account_children_information200_response_data_inner import GetYourAccountChildrenInformation200ResponseDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetYourAccountChildrenInformation200ResponseDataInner from a JSON string
get_your_account_children_information200_response_data_inner_instance = GetYourAccountChildrenInformation200ResponseDataInner.from_json(json)
# print the JSON string representation of the object
print GetYourAccountChildrenInformation200ResponseDataInner.to_json()

# convert the object into a dict
get_your_account_children_information200_response_data_inner_dict = get_your_account_children_information200_response_data_inner_instance.to_dict()
# create an instance of GetYourAccountChildrenInformation200ResponseDataInner from a dict
get_your_account_children_information200_response_data_inner_form_dict = get_your_account_children_information200_response_data_inner.from_dict(get_your_account_children_information200_response_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


