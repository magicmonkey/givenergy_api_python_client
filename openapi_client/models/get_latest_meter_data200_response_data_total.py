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
from openapi_client.models.get_latest_meter_data200_response_data_total_battery import GetLatestMeterData200ResponseDataTotalBattery
from openapi_client.models.get_latest_meter_data200_response_data_total_grid import GetLatestMeterData200ResponseDataTotalGrid

class GetLatestMeterData200ResponseDataTotal(BaseModel):
    """
    GetLatestMeterData200ResponseDataTotal
    """
    solar: Optional[Union[StrictFloat, StrictInt]] = None
    grid: Optional[GetLatestMeterData200ResponseDataTotalGrid] = None
    battery: Optional[GetLatestMeterData200ResponseDataTotalBattery] = None
    consumption: Optional[Union[StrictFloat, StrictInt]] = None
    ac_charge: Optional[StrictInt] = None
    __properties = ["solar", "grid", "battery", "consumption", "ac_charge"]

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
    def from_json(cls, json_str: str) -> GetLatestMeterData200ResponseDataTotal:
        """Create an instance of GetLatestMeterData200ResponseDataTotal from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of grid
        if self.grid:
            _dict['grid'] = self.grid.to_dict()
        # override the default output from pydantic by calling `to_dict()` of battery
        if self.battery:
            _dict['battery'] = self.battery.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> GetLatestMeterData200ResponseDataTotal:
        """Create an instance of GetLatestMeterData200ResponseDataTotal from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return GetLatestMeterData200ResponseDataTotal.parse_obj(obj)

        _obj = GetLatestMeterData200ResponseDataTotal.parse_obj({
            "solar": obj.get("solar"),
            "grid": GetLatestMeterData200ResponseDataTotalGrid.from_dict(obj.get("grid")) if obj.get("grid") is not None else None,
            "battery": GetLatestMeterData200ResponseDataTotalBattery.from_dict(obj.get("battery")) if obj.get("battery") is not None else None,
            "consumption": obj.get("consumption"),
            "ac_charge": obj.get("ac_charge")
        })
        return _obj


