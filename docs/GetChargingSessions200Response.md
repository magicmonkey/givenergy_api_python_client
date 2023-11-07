# GetChargingSessions200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[GetChargingSessions200ResponseDataInner]**](GetChargingSessions200ResponseDataInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.get_charging_sessions200_response import GetChargingSessions200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetChargingSessions200Response from a JSON string
get_charging_sessions200_response_instance = GetChargingSessions200Response.from_json(json)
# print the JSON string representation of the object
print GetChargingSessions200Response.to_json()

# convert the object into a dict
get_charging_sessions200_response_dict = get_charging_sessions200_response_instance.to_dict()
# create an instance of GetChargingSessions200Response from a dict
get_charging_sessions200_response_form_dict = get_charging_sessions200_response.from_dict(get_charging_sessions200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


