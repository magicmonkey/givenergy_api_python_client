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

from openapi_client.models.get_data_points200_response_data_inner_power_grid import GetDataPoints200ResponseDataInnerPowerGrid  # noqa: E501

class TestGetDataPoints200ResponseDataInnerPowerGrid(unittest.TestCase):
    """GetDataPoints200ResponseDataInnerPowerGrid unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetDataPoints200ResponseDataInnerPowerGrid:
        """Test GetDataPoints200ResponseDataInnerPowerGrid
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetDataPoints200ResponseDataInnerPowerGrid`
        """
        model = GetDataPoints200ResponseDataInnerPowerGrid()  # noqa: E501
        if include_optional:
            return GetDataPoints200ResponseDataInnerPowerGrid(
                voltage = 128.3,
                current = 98.1,
                power = 19821,
                frequency = 49.25
            )
        else:
            return GetDataPoints200ResponseDataInnerPowerGrid(
        )
        """

    def testGetDataPoints200ResponseDataInnerPowerGrid(self):
        """Test GetDataPoints200ResponseDataInnerPowerGrid"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()