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
from pydantic import BaseModel, Field, StrictStr

class GetCommunicationDeviceInformationBySerialNumber200ResponseDataInverterFirmwareVersion(BaseModel):
    """
    GetCommunicationDeviceInformationBySerialNumber200ResponseDataInverterFirmwareVersion
    """
    arm: Optional[StrictStr] = Field(None, alias="ARM")
    dsp: Optional[StrictStr] = Field(None, alias="DSP")
    __properties = ["ARM", "DSP"]

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
    def from_json(cls, json_str: str) -> GetCommunicationDeviceInformationBySerialNumber200ResponseDataInverterFirmwareVersion:
        """Create an instance of GetCommunicationDeviceInformationBySerialNumber200ResponseDataInverterFirmwareVersion from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> GetCommunicationDeviceInformationBySerialNumber200ResponseDataInverterFirmwareVersion:
        """Create an instance of GetCommunicationDeviceInformationBySerialNumber200ResponseDataInverterFirmwareVersion from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return GetCommunicationDeviceInformationBySerialNumber200ResponseDataInverterFirmwareVersion.parse_obj(obj)

        _obj = GetCommunicationDeviceInformationBySerialNumber200ResponseDataInverterFirmwareVersion.parse_obj({
            "arm": obj.get("ARM"),
            "dsp": obj.get("DSP")
        })
        return _obj


