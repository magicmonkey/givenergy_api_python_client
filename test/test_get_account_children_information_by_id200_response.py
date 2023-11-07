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

from openapi_client.models.get_account_children_information_by_id200_response import GetAccountChildrenInformationByID200Response  # noqa: E501

class TestGetAccountChildrenInformationByID200Response(unittest.TestCase):
    """GetAccountChildrenInformationByID200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetAccountChildrenInformationByID200Response:
        """Test GetAccountChildrenInformationByID200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetAccountChildrenInformationByID200Response`
        """
        model = GetAccountChildrenInformationByID200Response()  # noqa: E501
        if include_optional:
            return GetAccountChildrenInformationByID200Response(
                data = [{"id":15,"name":"rose.phoebe","role":"OWNER","email":"adams.scott@gmail.com","address":"80 Collins Land","postcode":"MK9 2AD","country":"MICRONESIA","telephone_number":"+44(0)316836121","timezone":"GMT -4"},{"id":16,"name":"owen67","role":"VIEWER","email":"arthur94@gmail.com","address":"33 Sean Valley","postcode":"TW15 3EQ","country":"SVALBARD_AND_JAN_MAYAN","telephone_number":"+44(0)4011 038979","timezone":"GMT +9"}]
            )
        else:
            return GetAccountChildrenInformationByID200Response(
        )
        """

    def testGetAccountChildrenInformationByID200Response(self):
        """Test GetAccountChildrenInformationByID200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()