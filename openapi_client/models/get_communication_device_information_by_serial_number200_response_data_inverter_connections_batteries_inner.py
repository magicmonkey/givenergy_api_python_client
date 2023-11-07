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
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from openapi_client.models.get_communication_device_information_by_serial_number200_response_data_inverter_connections_batteries_inner_capacity import GetCommunicationDeviceInformationBySerialNumber200ResponseDataInverterConnectionsBatteriesInnerCapacity

class GetCommunicationDeviceInformationBySerialNumber200ResponseDataInverterConnectionsBatteriesInner(BaseModel):
    """
    GetCommunicationDeviceInformationBySerialNumber200ResponseDataInverterConnectionsBatteriesInner
    """
    serial: Optional[StrictStr] = None
    firmware_version: Optional[StrictStr] = None
    capacity: Optional[GetCommunicationDeviceInformationBySerialNumber200ResponseDataInverterConnectionsBatteriesInnerCapacity] = None
    cell_count: Optional[StrictInt] = None
    has_usb: Optional[StrictBool] = None
    __properties = ["serial", "firmware_version", "capacity", "cell_count", "has_usb"]

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
    def from_json(cls, json_str: str) -> GetCommunicationDeviceInformationBySerialNumber200ResponseDataInverterConnectionsBatteriesInner:
        """Create an instance of GetCommunicationDeviceInformationBySerialNumber200ResponseDataInverterConnectionsBatteriesInner from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of capacity
        if self.capacity:
            _dict['capacity'] = self.capacity.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> GetCommunicationDeviceInformationBySerialNumber200ResponseDataInverterConnectionsBatteriesInner:
        """Create an instance of GetCommunicationDeviceInformationBySerialNumber200ResponseDataInverterConnectionsBatteriesInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return GetCommunicationDeviceInformationBySerialNumber200ResponseDataInverterConnectionsBatteriesInner.parse_obj(obj)

        _obj = GetCommunicationDeviceInformationBySerialNumber200ResponseDataInverterConnectionsBatteriesInner.parse_obj({
            "serial": obj.get("serial"),
            "firmware_version": obj.get("firmware_version"),
            "capacity": GetCommunicationDeviceInformationBySerialNumber200ResponseDataInverterConnectionsBatteriesInnerCapacity.from_dict(obj.get("capacity")) if obj.get("capacity") is not None else None,
            "cell_count": obj.get("cell_count"),
            "has_usb": obj.get("has_usb")
        })
        return _obj


