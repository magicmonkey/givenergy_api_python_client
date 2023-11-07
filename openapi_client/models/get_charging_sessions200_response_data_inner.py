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


from typing import Optional, Union
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr

class GetChargingSessions200ResponseDataInner(BaseModel):
    """
    GetChargingSessions200ResponseDataInner
    """
    started_by: Optional[StrictStr] = None
    meter_start: Optional[Union[StrictFloat, StrictInt]] = None
    started_at: Optional[StrictStr] = None
    stopped_by: Optional[StrictStr] = None
    meter_stop: Optional[StrictStr] = None
    stopped_at: Optional[StrictStr] = None
    stop_reason: Optional[StrictStr] = None
    __properties = ["started_by", "meter_start", "started_at", "stopped_by", "meter_stop", "stopped_at", "stop_reason"]

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
    def from_json(cls, json_str: str) -> GetChargingSessions200ResponseDataInner:
        """Create an instance of GetChargingSessions200ResponseDataInner from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> GetChargingSessions200ResponseDataInner:
        """Create an instance of GetChargingSessions200ResponseDataInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return GetChargingSessions200ResponseDataInner.parse_obj(obj)

        _obj = GetChargingSessions200ResponseDataInner.parse_obj({
            "started_by": obj.get("started_by"),
            "meter_start": obj.get("meter_start"),
            "started_at": obj.get("started_at"),
            "stopped_by": obj.get("stopped_by"),
            "meter_stop": obj.get("meter_stop"),
            "stopped_at": obj.get("stopped_at"),
            "stop_reason": obj.get("stop_reason")
        })
        return _obj


