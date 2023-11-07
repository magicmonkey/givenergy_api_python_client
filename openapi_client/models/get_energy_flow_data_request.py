# coding: utf-8

"""
    GivEnergy API Documentation (v1.14.0)

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import List, Optional
from pydantic import BaseModel, Field, StrictInt, conlist

class GetEnergyFlowDataRequest(BaseModel):
    """
    GetEnergyFlowDataRequest
    """
    start_time: Datetime = Field(..., description="The start time of the query. Based on the inverter's local time")
    end_time: Datetime = Field(..., description="The end time of the query. Based on the inverter's local time")
    grouping: StrictInt = Field(..., description="The way in which to group the data. See the above table for a complete list of grouping IDs")
    types: Optional[conlist(StrictInt)] = Field(None, description="An array of type IDs. See the above table for a complete list of type IDs. Leave blank to fetch all types")
    __properties = ["start_time", "end_time", "grouping", "types"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> GetEnergyFlowDataRequest:
        """Create an instance of GetEnergyFlowDataRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of start_time
        if self.start_time:
            _dict['start_time'] = self.start_time.to_dict()
        # override the default output from pydantic by calling `to_dict()` of end_time
        if self.end_time:
            _dict['end_time'] = self.end_time.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> GetEnergyFlowDataRequest:
        """Create an instance of GetEnergyFlowDataRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return GetEnergyFlowDataRequest.parse_obj(obj)

        _obj = GetEnergyFlowDataRequest.parse_obj({
            "start_time": Datetime.from_dict(obj.get("start_time")) if obj.get("start_time") is not None else None,
            "end_time": Datetime.from_dict(obj.get("end_time")) if obj.get("end_time") is not None else None,
            "grouping": obj.get("grouping"),
            "types": obj.get("types")
        })
        return _obj

