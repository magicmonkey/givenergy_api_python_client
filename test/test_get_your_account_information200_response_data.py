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

from openapi_client.models.get_your_account_information200_response_data import GetYourAccountInformation200ResponseData  # noqa: E501

class TestGetYourAccountInformation200ResponseData(unittest.TestCase):
    """GetYourAccountInformation200ResponseData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetYourAccountInformation200ResponseData:
        """Test GetYourAccountInformation200ResponseData
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetYourAccountInformation200ResponseData`
        """
        model = GetYourAccountInformation200ResponseData()  # noqa: E501
        if include_optional:
            return GetYourAccountInformation200ResponseData(
                id = 2,
                name = 'francesca.holmes',
                role = 'ENGINEER',
                email = 'joshua94@martin.com',
                address = 'Flat 60
Kyle Lights',
                postcode = 'SP1 1NE',
                country = 'SOUTH_KOREA',
                telephone_number = '0738 286 7656',
                timezone = 'GMT +13'
            )
        else:
            return GetYourAccountInformation200ResponseData(
        )
        """

    def testGetYourAccountInformation200ResponseData(self):
        """Test GetYourAccountInformation200ResponseData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
