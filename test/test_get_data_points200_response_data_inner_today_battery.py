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

from openapi_client.models.get_data_points200_response_data_inner_today_battery import GetDataPoints200ResponseDataInnerTodayBattery  # noqa: E501

class TestGetDataPoints200ResponseDataInnerTodayBattery(unittest.TestCase):
    """GetDataPoints200ResponseDataInnerTodayBattery unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetDataPoints200ResponseDataInnerTodayBattery:
        """Test GetDataPoints200ResponseDataInnerTodayBattery
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetDataPoints200ResponseDataInnerTodayBattery`
        """
        model = GetDataPoints200ResponseDataInnerTodayBattery()  # noqa: E501
        if include_optional:
            return GetDataPoints200ResponseDataInnerTodayBattery(
                charge = 8691.3,
                discharge = 4350.4
            )
        else:
            return GetDataPoints200ResponseDataInnerTodayBattery(
        )
        """

    def testGetDataPoints200ResponseDataInnerTodayBattery(self):
        """Test GetDataPoints200ResponseDataInnerTodayBattery"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
