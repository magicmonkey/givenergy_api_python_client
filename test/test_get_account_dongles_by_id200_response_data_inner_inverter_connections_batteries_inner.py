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

from openapi_client.models.get_account_dongles_by_id200_response_data_inner_inverter_connections_batteries_inner import GetAccountDonglesByID200ResponseDataInnerInverterConnectionsBatteriesInner  # noqa: E501

class TestGetAccountDonglesByID200ResponseDataInnerInverterConnectionsBatteriesInner(unittest.TestCase):
    """GetAccountDonglesByID200ResponseDataInnerInverterConnectionsBatteriesInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetAccountDonglesByID200ResponseDataInnerInverterConnectionsBatteriesInner:
        """Test GetAccountDonglesByID200ResponseDataInnerInverterConnectionsBatteriesInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetAccountDonglesByID200ResponseDataInnerInverterConnectionsBatteriesInner`
        """
        model = GetAccountDonglesByID200ResponseDataInnerInverterConnectionsBatteriesInner()  # noqa: E501
        if include_optional:
            return GetAccountDonglesByID200ResponseDataInnerInverterConnectionsBatteriesInner(
                serial = 'ki1513g952',
                firmware_version = '22210',
                capacity = openapi_client.models.get_account_dongles_by_id_200_response_data_inner_inverter_connections_batteries_inner_capacity.getAccountDonglesByID_200_response_data_inner_inverter_connections_batteries_inner_capacity(
                    full = 191.39, 
                    design = 186, ),
                cell_count = 16,
                has_usb = False
            )
        else:
            return GetAccountDonglesByID200ResponseDataInnerInverterConnectionsBatteriesInner(
        )
        """

    def testGetAccountDonglesByID200ResponseDataInnerInverterConnectionsBatteriesInner(self):
        """Test GetAccountDonglesByID200ResponseDataInnerInverterConnectionsBatteriesInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
