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

class GetAccountInformationByUsername200ResponseData(BaseModel):
    """
    GetAccountInformationByUsername200ResponseData
    """
    id: Optional[StrictInt] = None
    name: Optional[StrictStr] = None
    role: Optional[StrictStr] = None
    email: Optional[StrictStr] = None
    address: Optional[StrictStr] = None
    postcode: Optional[StrictStr] = None
    country: Optional[StrictStr] = None
    telephone_number: Optional[StrictStr] = None
    timezone: Optional[StrictStr] = None
    __properties = ["id", "name", "role", "email", "address", "postcode", "country", "telephone_number", "timezone"]

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
    def from_json(cls, json_str: str) -> GetAccountInformationByUsername200ResponseData:
        """Create an instance of GetAccountInformationByUsername200ResponseData from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> GetAccountInformationByUsername200ResponseData:
        """Create an instance of GetAccountInformationByUsername200ResponseData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return GetAccountInformationByUsername200ResponseData.parse_obj(obj)

        _obj = GetAccountInformationByUsername200ResponseData.parse_obj({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "role": obj.get("role"),
            "email": obj.get("email"),
            "address": obj.get("address"),
            "postcode": obj.get("postcode"),
            "country": obj.get("country"),
            "telephone_number": obj.get("telephone_number"),
            "timezone": obj.get("timezone")
        })
        return _obj

