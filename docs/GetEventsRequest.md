# GetEventsRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cleared** | **bool** |  | [optional] 
**start** | **str** | Must be a valid date. Must be a date before &lt;code&gt;tomorrow&lt;/code&gt;. | [optional] 
**end** | **str** | Must be a valid date. Must be a date after &lt;code&gt;start&lt;/code&gt;. | [optional] 

## Example

```python
from openapi_client.models.get_events_request import GetEventsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetEventsRequest from a JSON string
get_events_request_instance = GetEventsRequest.from_json(json)
# print the JSON string representation of the object
print GetEventsRequest.to_json()

# convert the object into a dict
get_events_request_dict = get_events_request_instance.to_dict()
# create an instance of GetEventsRequest from a dict
get_events_request_form_dict = get_events_request.from_dict(get_events_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


