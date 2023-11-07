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

from openapi_client.models.get_data_points200_response_data_inner import GetDataPoints200ResponseDataInner  # noqa: E501

class TestGetDataPoints200ResponseDataInner(unittest.TestCase):
    """GetDataPoints200ResponseDataInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetDataPoints200ResponseDataInner:
        """Test GetDataPoints200ResponseDataInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetDataPoints200ResponseDataInner`
        """
        model = GetDataPoints200ResponseDataInner()  # noqa: E501
        if include_optional:
            return GetDataPoints200ResponseDataInner(
                time = '1996-09-06T10:29:52Z',
                power = openapi_client.models.get_data_points_200_response_data_inner_power.getDataPoints_200_response_data_inner_power(
                    solar = openapi_client.models.get_data_points_200_response_data_inner_power_solar.getDataPoints_200_response_data_inner_power_solar(
                        power = 4703, 
                        arrays = [{"array":1,"voltage":198.6,"current":3.3,"power":491},{"array":2,"voltage":170.8,"current":10,"power":2806}], ), 
                    grid = openapi_client.models.get_data_points_200_response_data_inner_power_grid.getDataPoints_200_response_data_inner_power_grid(
                        voltage = 128.3, 
                        current = 98.1, 
                        power = 19821, 
                        frequency = 49.25, ), 
                    battery = openapi_client.models.get_data_points_200_response_data_inner_power_battery.getDataPoints_200_response_data_inner_power_battery(
                        percent = 79, 
                        power = -2289, 
                        temperature = 12, ), 
                    consumption = openapi_client.models.get_data_points_200_response_data_inner_power_consumption.getDataPoints_200_response_data_inner_power_consumption(
                        power = 22636, ), 
                    inverter = openapi_client.models.get_data_points_200_response_data_inner_power_inverter.getDataPoints_200_response_data_inner_power_inverter(
                        temperature = 50, 
                        power = -9476, 
                        output_voltage = 144.7, 
                        output_frequency = 49.69, 
                        eps_power = 24672, ), ),
                today = openapi_client.models.get_data_points_200_response_data_inner_today.getDataPoints_200_response_data_inner_today(
                    solar = 4373.9, 
                    grid = openapi_client.models.get_data_points_200_response_data_inner_today_grid.getDataPoints_200_response_data_inner_today_grid(
                        import = 3168.4, 
                        export = 5384.4, ), 
                    battery = openapi_client.models.get_data_points_200_response_data_inner_today_battery.getDataPoints_200_response_data_inner_today_battery(
                        charge = 8691.3, 
                        discharge = 4350.4, ), 
                    consumption = 5673.7, 
                    ac_charge = 8021.5, ),
                total = openapi_client.models.get_data_points_200_response_data_inner_total.getDataPoints_200_response_data_inner_total(
                    solar = 4353.3, 
                    grid = openapi_client.models.get_data_points_200_response_data_inner_total_grid.getDataPoints_200_response_data_inner_total_grid(
                        import = 4625.8, 
                        export = 7045.8, ), 
                    battery = openapi_client.models.get_data_points_200_response_data_inner_total_battery.getDataPoints_200_response_data_inner_total_battery(
                        charge = 1034.1, 
                        discharge = 1034.1, ), 
                    consumption = -11905.4, 
                    ac_charge = 9568.8, ),
                is_metered = True
            )
        else:
            return GetDataPoints200ResponseDataInner(
        )
        """

    def testGetDataPoints200ResponseDataInner(self):
        """Test GetDataPoints200ResponseDataInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
