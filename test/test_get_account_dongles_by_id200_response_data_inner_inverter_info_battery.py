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

from openapi_client.models.get_account_dongles_by_id200_response_data_inner_inverter_info_battery import GetAccountDonglesByID200ResponseDataInnerInverterInfoBattery  # noqa: E501

class TestGetAccountDonglesByID200ResponseDataInnerInverterInfoBattery(unittest.TestCase):
    """GetAccountDonglesByID200ResponseDataInnerInverterInfoBattery unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetAccountDonglesByID200ResponseDataInnerInverterInfoBattery:
        """Test GetAccountDonglesByID200ResponseDataInnerInverterInfoBattery
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetAccountDonglesByID200ResponseDataInnerInverterInfoBattery`
        """
        model = GetAccountDonglesByID200ResponseDataInnerInverterInfoBattery()  # noqa: E501
        if include_optional:
            return GetAccountDonglesByID200ResponseDataInnerInverterInfoBattery(
                nominal_capacity = 110,
                nominal_voltage = 307
            )
        else:
            return GetAccountDonglesByID200ResponseDataInnerInverterInfoBattery(
        )
        """

    def testGetAccountDonglesByID200ResponseDataInnerInverterInfoBattery(self):
        """Test GetAccountDonglesByID200ResponseDataInnerInverterInfoBattery"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
