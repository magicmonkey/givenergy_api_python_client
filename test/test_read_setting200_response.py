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

from openapi_client.models.read_setting200_response import ReadSetting200Response  # noqa: E501

class TestReadSetting200Response(unittest.TestCase):
    """ReadSetting200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ReadSetting200Response:
        """Test ReadSetting200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ReadSetting200Response`
        """
        model = ReadSetting200Response()  # noqa: E501
        if include_optional:
            return ReadSetting200Response(
                data = openapi_client.models.read_setting_200_response_data.readSetting_200_response_data(
                    value = True, )
            )
        else:
            return ReadSetting200Response(
        )
        """

    def testReadSetting200Response(self):
        """Test ReadSetting200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()