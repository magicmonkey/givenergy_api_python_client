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


from typing import List
from pydantic import BaseModel, Field, StrictInt, StrictStr, conlist

class ReadSettingMultipleRequest(BaseModel):
    """
    ReadSettingMultipleRequest
    """
    inverter_serials: conlist(StrictStr) = Field(..., description="An array of inverter serial numbers to send the command to with a maximum length of 1000")
    setting_id: StrictInt = Field(..., description="The ID of the setting to modify")
    __properties = ["inverter_serials", "setting_id"]

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
    def from_json(cls, json_str: str) -> ReadSettingMultipleRequest:
        """Create an instance of ReadSettingMultipleRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ReadSettingMultipleRequest:
        """Create an instance of ReadSettingMultipleRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ReadSettingMultipleRequest.parse_obj(obj)

        _obj = ReadSettingMultipleRequest.parse_obj({
            "inverter_serials": obj.get("inverter_serials"),
            "setting_id": obj.get("setting_id")
        })
        return _obj

