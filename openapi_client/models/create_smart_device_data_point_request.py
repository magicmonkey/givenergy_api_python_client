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



from pydantic import BaseModel, Field, StrictInt

class CreateSmartDeviceDataPointRequest(BaseModel):
    """
    CreateSmartDeviceDataPointRequest
    """
    time: ISO8601Datetime = Field(..., description="The date & time that the data point was created")
    power: StrictInt = Field(...)
    __properties = ["time", "power"]

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
    def from_json(cls, json_str: str) -> CreateSmartDeviceDataPointRequest:
        """Create an instance of CreateSmartDeviceDataPointRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of time
        if self.time:
            _dict['time'] = self.time.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CreateSmartDeviceDataPointRequest:
        """Create an instance of CreateSmartDeviceDataPointRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CreateSmartDeviceDataPointRequest.parse_obj(obj)

        _obj = CreateSmartDeviceDataPointRequest.parse_obj({
            "time": ISO8601Datetime.from_dict(obj.get("time")) if obj.get("time") is not None else None,
            "power": obj.get("power")
        })
        return _obj


