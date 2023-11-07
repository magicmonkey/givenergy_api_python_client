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
from openapi_client.models.get_communication_device_information_by_serial_number200_response_data_inverter_info_battery import GetCommunicationDeviceInformationBySerialNumber200ResponseDataInverterInfoBattery

class GetCommunicationDeviceInformationBySerialNumber200ResponseDataInverterInfo(BaseModel):
    """
    GetCommunicationDeviceInformationBySerialNumber200ResponseDataInverterInfo
    """
    battery_type: Optional[StrictStr] = None
    battery: Optional[GetCommunicationDeviceInformationBySerialNumber200ResponseDataInverterInfoBattery] = None
    model: Optional[StrictStr] = None
    max_charge_rate: Optional[StrictInt] = None
    __properties = ["battery_type", "battery", "model", "max_charge_rate"]

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
    def from_json(cls, json_str: str) -> GetCommunicationDeviceInformationBySerialNumber200ResponseDataInverterInfo:
        """Create an instance of GetCommunicationDeviceInformationBySerialNumber200ResponseDataInverterInfo from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of battery
        if self.battery:
            _dict['battery'] = self.battery.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> GetCommunicationDeviceInformationBySerialNumber200ResponseDataInverterInfo:
        """Create an instance of GetCommunicationDeviceInformationBySerialNumber200ResponseDataInverterInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return GetCommunicationDeviceInformationBySerialNumber200ResponseDataInverterInfo.parse_obj(obj)

        _obj = GetCommunicationDeviceInformationBySerialNumber200ResponseDataInverterInfo.parse_obj({
            "battery_type": obj.get("battery_type"),
            "battery": GetCommunicationDeviceInformationBySerialNumber200ResponseDataInverterInfoBattery.from_dict(obj.get("battery")) if obj.get("battery") is not None else None,
            "model": obj.get("model"),
            "max_charge_rate": obj.get("max_charge_rate")
        })
        return _obj

