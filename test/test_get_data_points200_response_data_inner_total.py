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

from openapi_client.models.get_data_points200_response_data_inner_total import GetDataPoints200ResponseDataInnerTotal  # noqa: E501

class TestGetDataPoints200ResponseDataInnerTotal(unittest.TestCase):
    """GetDataPoints200ResponseDataInnerTotal unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetDataPoints200ResponseDataInnerTotal:
        """Test GetDataPoints200ResponseDataInnerTotal
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetDataPoints200ResponseDataInnerTotal`
        """
        model = GetDataPoints200ResponseDataInnerTotal()  # noqa: E501
        if include_optional:
            return GetDataPoints200ResponseDataInnerTotal(
                solar = 4353.3,
                grid = openapi_client.models.get_data_points_200_response_data_inner_total_grid.getDataPoints_200_response_data_inner_total_grid(
                    import = 4625.8, 
                    export = 7045.8, ),
                battery = openapi_client.models.get_data_points_200_response_data_inner_total_battery.getDataPoints_200_response_data_inner_total_battery(
                    charge = 1034.1, 
                    discharge = 1034.1, ),
                consumption = -11905.4,
                ac_charge = 9568.8
            )
        else:
            return GetDataPoints200ResponseDataInnerTotal(
        )
        """

    def testGetDataPoints200ResponseDataInnerTotal(self):
        """Test GetDataPoints200ResponseDataInnerTotal"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
