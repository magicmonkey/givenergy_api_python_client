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

from openapi_client.models.get_your_ev_chargers200_response_data_inner import GetYourEVChargers200ResponseDataInner  # noqa: E501

class TestGetYourEVChargers200ResponseDataInner(unittest.TestCase):
    """GetYourEVChargers200ResponseDataInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetYourEVChargers200ResponseDataInner:
        """Test GetYourEVChargers200ResponseDataInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetYourEVChargers200ResponseDataInner`
        """
        model = GetYourEVChargers200ResponseDataInner()  # noqa: E501
        if include_optional:
            return GetYourEVChargers200ResponseDataInner(
                uuid = '3aa3a907-89a0-471c-9a51-e58669ef6b30',
                serial_number = '95687924114376',
                type = 'GivEnergy',
                alias = 'Garage',
                online = False,
                went_offline_at = '',
                status = 'Unavailable'
            )
        else:
            return GetYourEVChargers200ResponseDataInner(
        )
        """

    def testGetYourEVChargers200ResponseDataInner(self):
        """Test GetYourEVChargers200ResponseDataInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
