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

from openapi_client.models.get_latest_meter_data200_response_data_total_battery import GetLatestMeterData200ResponseDataTotalBattery  # noqa: E501

class TestGetLatestMeterData200ResponseDataTotalBattery(unittest.TestCase):
    """GetLatestMeterData200ResponseDataTotalBattery unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetLatestMeterData200ResponseDataTotalBattery:
        """Test GetLatestMeterData200ResponseDataTotalBattery
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetLatestMeterData200ResponseDataTotalBattery`
        """
        model = GetLatestMeterData200ResponseDataTotalBattery()  # noqa: E501
        if include_optional:
            return GetLatestMeterData200ResponseDataTotalBattery(
                charge = 30813.3,
                discharge = 30813.3
            )
        else:
            return GetLatestMeterData200ResponseDataTotalBattery(
        )
        """

    def testGetLatestMeterData200ResponseDataTotalBattery(self):
        """Test GetLatestMeterData200ResponseDataTotalBattery"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
