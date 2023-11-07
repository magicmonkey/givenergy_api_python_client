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


from typing import Optional
from pydantic import BaseModel, StrictInt, StrictStr
from openapi_client.models.get_latest_system_data200_response_data_battery import GetLatestSystemData200ResponseDataBattery
from openapi_client.models.get_latest_system_data200_response_data_grid import GetLatestSystemData200ResponseDataGrid
from openapi_client.models.get_latest_system_data200_response_data_inverter import GetLatestSystemData200ResponseDataInverter
from openapi_client.models.get_latest_system_data200_response_data_solar import GetLatestSystemData200ResponseDataSolar

class GetLatestSystemData200ResponseData(BaseModel):
    """
    GetLatestSystemData200ResponseData
    """
    time: Optional[StrictStr] = None
    solar: Optional[GetLatestSystemData200ResponseDataSolar] = None
    grid: Optional[GetLatestSystemData200ResponseDataGrid] = None
    battery: Optional[GetLatestSystemData200ResponseDataBattery] = None
    inverter: Optional[GetLatestSystemData200ResponseDataInverter] = None
    consumption: Optional[StrictInt] = None
    __properties = ["time", "solar", "grid", "battery", "inverter", "consumption"]

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
    def from_json(cls, json_str: str) -> GetLatestSystemData200ResponseData:
        """Create an instance of GetLatestSystemData200ResponseData from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of solar
        if self.solar:
            _dict['solar'] = self.solar.to_dict()
        # override the default output from pydantic by calling `to_dict()` of grid
        if self.grid:
            _dict['grid'] = self.grid.to_dict()
        # override the default output from pydantic by calling `to_dict()` of battery
        if self.battery:
            _dict['battery'] = self.battery.to_dict()
        # override the default output from pydantic by calling `to_dict()` of inverter
        if self.inverter:
            _dict['inverter'] = self.inverter.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> GetLatestSystemData200ResponseData:
        """Create an instance of GetLatestSystemData200ResponseData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return GetLatestSystemData200ResponseData.parse_obj(obj)

        _obj = GetLatestSystemData200ResponseData.parse_obj({
            "time": obj.get("time"),
            "solar": GetLatestSystemData200ResponseDataSolar.from_dict(obj.get("solar")) if obj.get("solar") is not None else None,
            "grid": GetLatestSystemData200ResponseDataGrid.from_dict(obj.get("grid")) if obj.get("grid") is not None else None,
            "battery": GetLatestSystemData200ResponseDataBattery.from_dict(obj.get("battery")) if obj.get("battery") is not None else None,
            "inverter": GetLatestSystemData200ResponseDataInverter.from_dict(obj.get("inverter")) if obj.get("inverter") is not None else None,
            "consumption": obj.get("consumption")
        })
        return _obj


