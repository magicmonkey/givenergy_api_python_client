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

from openapi_client.models.get_events_request import GetEventsRequest  # noqa: E501

class TestGetEventsRequest(unittest.TestCase):
    """GetEventsRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetEventsRequest:
        """Test GetEventsRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetEventsRequest`
        """
        model = GetEventsRequest()  # noqa: E501
        if include_optional:
            return GetEventsRequest(
                cleared = False,
                start = '2018-03-05',
                end = '2104-12-06'
            )
        else:
            return GetEventsRequest(
        )
        """

    def testGetEventsRequest(self):
        """Test GetEventsRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
