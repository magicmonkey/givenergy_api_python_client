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

from openapi_client.models.get_latest_system_data200_response import GetLatestSystemData200Response  # noqa: E501

class TestGetLatestSystemData200Response(unittest.TestCase):
    """GetLatestSystemData200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetLatestSystemData200Response:
        """Test GetLatestSystemData200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetLatestSystemData200Response`
        """
        model = GetLatestSystemData200Response()  # noqa: E501
        if include_optional:
            return GetLatestSystemData200Response(
                data = openapi_client.models.get_latest_system_data_200_response_data.getLatestSystemData_200_response_data(
                    time = '1985-05-02T08:13:44Z', 
                    solar = openapi_client.models.get_latest_system_data_200_response_data_solar.getLatestSystemData_200_response_data_solar(
                        power = 3762, 
                        arrays = [{"array":1,"voltage":202.9,"current":788.7,"power":393},{"array":2,"voltage":626.5,"current":206.8,"power":2245}], ), 
                    grid = openapi_client.models.get_latest_system_data_200_response_data_grid.getLatestSystemData_200_response_data_grid(
                        voltage = 1509.2, 
                        current = 4814, 
                        power = -4863, 
                        frequency = 221.3, ), 
                    battery = openapi_client.models.get_latest_system_data_200_response_data_battery.getLatestSystemData_200_response_data_battery(
                        percent = 65, 
                        power = 1344, 
                        temperature = 2.6, ), 
                    inverter = openapi_client.models.get_latest_system_data_200_response_data_inverter.getLatestSystemData_200_response_data_inverter(
                        temperature = 43.5, 
                        power = 86477, 
                        output_voltage = 237.4, 
                        output_frequency = 50.74, 
                        eps_power = 4785, ), 
                    consumption = 36915, )
            )
        else:
            return GetLatestSystemData200Response(
        )
        """

    def testGetLatestSystemData200Response(self):
        """Test GetLatestSystemData200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()