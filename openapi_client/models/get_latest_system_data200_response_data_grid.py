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
from pydantic import BaseModel, StrictFloat, StrictInt

class GetLatestSystemData200ResponseDataGrid(BaseModel):
    """
    GetLatestSystemData200ResponseDataGrid
    """
    voltage: Optional[Union[StrictFloat, StrictInt]] = None
    current: Optional[Union[StrictFloat, StrictInt]] = None
    power: Optional[StrictInt] = None
    frequency: Optional[Union[StrictFloat, StrictInt]] = None
    __properties = ["voltage", "current", "power", "frequency"]

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
    def from_json(cls, json_str: str) -> GetLatestSystemData200ResponseDataGrid:
        """Create an instance of GetLatestSystemData200ResponseDataGrid from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> GetLatestSystemData200ResponseDataGrid:
        """Create an instance of GetLatestSystemData200ResponseDataGrid from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return GetLatestSystemData200ResponseDataGrid.parse_obj(obj)

        _obj = GetLatestSystemData200ResponseDataGrid.parse_obj({
            "voltage": obj.get("voltage"),
            "current": obj.get("current"),
            "power": obj.get("power"),
            "frequency": obj.get("frequency")
        })
        return _obj


