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

from openapi_client.models.get_smart_device_data_points_by_id200_response import GetSmartDeviceDataPointsByID200Response  # noqa: E501

class TestGetSmartDeviceDataPointsByID200Response(unittest.TestCase):
    """GetSmartDeviceDataPointsByID200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetSmartDeviceDataPointsByID200Response:
        """Test GetSmartDeviceDataPointsByID200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetSmartDeviceDataPointsByID200Response`
        """
        model = GetSmartDeviceDataPointsByID200Response()  # noqa: E501
        if include_optional:
            return GetSmartDeviceDataPointsByID200Response(
                data = [{"time":"1986-11-28T10:45:01Z","power":509},{"time":"2023-07-31T13:10:46Z","power":59}]
            )
        else:
            return GetSmartDeviceDataPointsByID200Response(
        )
        """

    def testGetSmartDeviceDataPointsByID200Response(self):
        """Test GetSmartDeviceDataPointsByID200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()