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

from openapi_client.models.modify_setting200_response import ModifySetting200Response  # noqa: E501

class TestModifySetting200Response(unittest.TestCase):
    """ModifySetting200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ModifySetting200Response:
        """Test ModifySetting200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ModifySetting200Response`
        """
        model = ModifySetting200Response()  # noqa: E501
        if include_optional:
            return ModifySetting200Response(
                data = openapi_client.models.modify_setting_200_response_data.modifySetting_200_response_data(
                    value = True, 
                    success = True, 
                    message = 'Read Successfully', )
            )
        else:
            return ModifySetting200Response(
        )
        """

    def testModifySetting200Response(self):
        """Test ModifySetting200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
