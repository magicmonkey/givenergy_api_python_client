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

from openapi_client.models.get_latest_system_data200_response_data_grid import GetLatestSystemData200ResponseDataGrid  # noqa: E501

class TestGetLatestSystemData200ResponseDataGrid(unittest.TestCase):
    """GetLatestSystemData200ResponseDataGrid unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetLatestSystemData200ResponseDataGrid:
        """Test GetLatestSystemData200ResponseDataGrid
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetLatestSystemData200ResponseDataGrid`
        """
        model = GetLatestSystemData200ResponseDataGrid()  # noqa: E501
        if include_optional:
            return GetLatestSystemData200ResponseDataGrid(
                voltage = 1509.2,
                current = 4814,
                power = -4863,
                frequency = 221.3
            )
        else:
            return GetLatestSystemData200ResponseDataGrid(
        )
        """

    def testGetLatestSystemData200ResponseDataGrid(self):
        """Test GetLatestSystemData200ResponseDataGrid"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()