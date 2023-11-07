# GetChargingSessionsRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_time** | **str** | Must be a valid date. Must be a date before or equal to &lt;code&gt;end_time&lt;/code&gt;. | [optional] 
**end_time** | **str** | Must be a valid date. Must be a date after or equal to &lt;code&gt;start_time&lt;/code&gt;. | [optional] 

## Example

```python
from openapi_client.models.get_charging_sessions_request import GetChargingSessionsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetChargingSessionsRequest from a JSON string
get_charging_sessions_request_instance = GetChargingSessionsRequest.from_json(json)
# print the JSON string representation of the object
print GetChargingSessionsRequest.to_json()

# convert the object into a dict
get_charging_sessions_request_dict = get_charging_sessions_request_instance.to_dict()
# create an instance of GetChargingSessionsRequest from a dict
get_charging_sessions_request_form_dict = get_charging_sessions_request.from_dict(get_charging_sessions_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


