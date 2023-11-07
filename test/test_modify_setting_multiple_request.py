# coding: utf-8

"""
    GivEnergy API Documentation (v1.14.0)

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from openapi_client.models.modify_setting_multiple_request import ModifySettingMultipleRequest  # noqa: E501

class TestModifySettingMultipleRequest(unittest.TestCase):
    """ModifySettingMultipleRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ModifySettingMultipleRequest:
        """Test ModifySettingMultipleRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ModifySettingMultipleRequest`
        """
        model = ModifySettingMultipleRequest()  # noqa: E501
        if include_optional:
            return ModifySettingMultipleRequest(
                inverter_serials = ["SERIAL_1","SERIAL_2"],
                setting_id = 17,
                value = 1
            )
        else:
            return ModifySettingMultipleRequest(
                inverter_serials = ["SERIAL_1","SERIAL_2"],
                setting_id = 17,
                value = 1,
        )
        """

    def testModifySettingMultipleRequest(self):
        """Test ModifySettingMultipleRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()