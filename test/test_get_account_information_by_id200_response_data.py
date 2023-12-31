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

from openapi_client.models.get_account_information_by_id200_response_data import GetAccountInformationByID200ResponseData  # noqa: E501

class TestGetAccountInformationByID200ResponseData(unittest.TestCase):
    """GetAccountInformationByID200ResponseData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetAccountInformationByID200ResponseData:
        """Test GetAccountInformationByID200ResponseData
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetAccountInformationByID200ResponseData`
        """
        model = GetAccountInformationByID200ResponseData()  # noqa: E501
        if include_optional:
            return GetAccountInformationByID200ResponseData(
                id = 3,
                name = 'lewis.campbell',
                role = 'OWNER',
                email = 'adam98@yahoo.com',
                address = '56 Edwards Glen',
                postcode = 'GL1 2SZ',
                country = 'FRANCE',
                telephone_number = '(0075) 381 2360',
                timezone = 'GMT -9'
            )
        else:
            return GetAccountInformationByID200ResponseData(
        )
        """

    def testGetAccountInformationByID200ResponseData(self):
        """Test GetAccountInformationByID200ResponseData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
