# GetAccountDonglesByID200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[GetAccountDonglesByID200ResponseDataInner]**](GetAccountDonglesByID200ResponseDataInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.get_account_dongles_by_id200_response import GetAccountDonglesByID200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetAccountDonglesByID200Response from a JSON string
get_account_dongles_by_id200_response_instance = GetAccountDonglesByID200Response.from_json(json)
# print the JSON string representation of the object
print GetAccountDonglesByID200Response.to_json()

# convert the object into a dict
get_account_dongles_by_id200_response_dict = get_account_dongles_by_id200_response_instance.to_dict()
# create an instance of GetAccountDonglesByID200Response from a dict
get_account_dongles_by_id200_response_form_dict = get_account_dongles_by_id200_response.from_dict(get_account_dongles_by_id200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


