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

from openapi_client.models.create_smart_device_data_point_request import CreateSmartDeviceDataPointRequest  # noqa: E501

class TestCreateSmartDeviceDataPointRequest(unittest.TestCase):
    """CreateSmartDeviceDataPointRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreateSmartDeviceDataPointRequest:
        """Test CreateSmartDeviceDataPointRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateSmartDeviceDataPointRequest`
        """
        model = CreateSmartDeviceDataPointRequest()  # noqa: E501
        if include_optional:
            return CreateSmartDeviceDataPointRequest(
                time = consequatur,
                power = 17
            )
        else:
            return CreateSmartDeviceDataPointRequest(
                time = consequatur,
                power = 17,
        )
        """

    def testCreateSmartDeviceDataPointRequest(self):
        """Test CreateSmartDeviceDataPointRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
