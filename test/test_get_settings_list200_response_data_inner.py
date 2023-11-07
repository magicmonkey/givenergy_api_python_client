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

from openapi_client.models.get_settings_list200_response_data_inner import GetSettingsList200ResponseDataInner  # noqa: E501

class TestGetSettingsList200ResponseDataInner(unittest.TestCase):
    """GetSettingsList200ResponseDataInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetSettingsList200ResponseDataInner:
        """Test GetSettingsList200ResponseDataInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetSettingsList200ResponseDataInner`
        """
        model = GetSettingsList200ResponseDataInner()  # noqa: E501
        if include_optional:
            return GetSettingsList200ResponseDataInner(
                id = 266,
                name = 'DC Discharge 3 End Time',
                validation = 'Value format should be HH:mm. Use correct time range for hour and minutes',
                validation_rules = ["date_format:H:i"]
            )
        else:
            return GetSettingsList200ResponseDataInner(
        )
        """

    def testGetSettingsList200ResponseDataInner(self):
        """Test GetSettingsList200ResponseDataInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
