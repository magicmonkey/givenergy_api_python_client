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

from openapi_client.models.get_events200_response_data_inner import GetEvents200ResponseDataInner  # noqa: E501

class TestGetEvents200ResponseDataInner(unittest.TestCase):
    """GetEvents200ResponseDataInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetEvents200ResponseDataInner:
        """Test GetEvents200ResponseDataInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetEvents200ResponseDataInner`
        """
        model = GetEvents200ResponseDataInner()  # noqa: E501
        if include_optional:
            return GetEvents200ResponseDataInner(
                event = 'BMS Discharger Over Current',
                start_time = '2003-07-03T06:06:16Z',
                end_time = ''
            )
        else:
            return GetEvents200ResponseDataInner(
        )
        """

    def testGetEvents200ResponseDataInner(self):
        """Test GetEvents200ResponseDataInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
