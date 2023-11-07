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

from openapi_client.models.get_command_data200_response import GetCommandData200Response  # noqa: E501

class TestGetCommandData200Response(unittest.TestCase):
    """GetCommandData200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetCommandData200Response:
        """Test GetCommandData200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetCommandData200Response`
        """
        model = GetCommandData200Response()  # noqa: E501
        if include_optional:
            return GetCommandData200Response(
                data = openapi_client.models.get_command_data_200_response_data.getCommandData_200_response_data(
                    active = 'EcoPlus', 
                    available = ["Eco","EcoPlus","Boost"], )
            )
        else:
            return GetCommandData200Response(
        )
        """

    def testGetCommandData200Response(self):
        """Test GetCommandData200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
