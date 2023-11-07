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

from openapi_client.models.get_latest_meter_data200_response_data_today import GetLatestMeterData200ResponseDataToday  # noqa: E501

class TestGetLatestMeterData200ResponseDataToday(unittest.TestCase):
    """GetLatestMeterData200ResponseDataToday unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetLatestMeterData200ResponseDataToday:
        """Test GetLatestMeterData200ResponseDataToday
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetLatestMeterData200ResponseDataToday`
        """
        model = GetLatestMeterData200ResponseDataToday()  # noqa: E501
        if include_optional:
            return GetLatestMeterData200ResponseDataToday(
                solar = 9931.7,
                grid = openapi_client.models.get_latest_meter_data_200_response_data_today_grid.getLatestMeterData_200_response_data_today_grid(
                    import = 1538, 
                    export = 2383.1, ),
                battery = openapi_client.models.get_latest_meter_data_200_response_data_today_battery.getLatestMeterData_200_response_data_today_battery(
                    charge = 51444.7, 
                    discharge = 87978.9, ),
                consumption = 9086.6,
                ac_charge = 606174
            )
        else:
            return GetLatestMeterData200ResponseDataToday(
        )
        """

    def testGetLatestMeterData200ResponseDataToday(self):
        """Test GetLatestMeterData200ResponseDataToday"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()