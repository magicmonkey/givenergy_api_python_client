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

from openapi_client.models.get_latest_system_data200_response_data_inverter import GetLatestSystemData200ResponseDataInverter  # noqa: E501

class TestGetLatestSystemData200ResponseDataInverter(unittest.TestCase):
    """GetLatestSystemData200ResponseDataInverter unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetLatestSystemData200ResponseDataInverter:
        """Test GetLatestSystemData200ResponseDataInverter
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetLatestSystemData200ResponseDataInverter`
        """
        model = GetLatestSystemData200ResponseDataInverter()  # noqa: E501
        if include_optional:
            return GetLatestSystemData200ResponseDataInverter(
                temperature = 43.5,
                power = 86477,
                output_voltage = 237.4,
                output_frequency = 50.74,
                eps_power = 4785
            )
        else:
            return GetLatestSystemData200ResponseDataInverter(
        )
        """

    def testGetLatestSystemData200ResponseDataInverter(self):
        """Test GetLatestSystemData200ResponseDataInverter"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
