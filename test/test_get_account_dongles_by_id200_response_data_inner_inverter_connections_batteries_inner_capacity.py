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

from openapi_client.models.get_account_dongles_by_id200_response_data_inner_inverter_connections_batteries_inner_capacity import GetAccountDonglesByID200ResponseDataInnerInverterConnectionsBatteriesInnerCapacity  # noqa: E501

class TestGetAccountDonglesByID200ResponseDataInnerInverterConnectionsBatteriesInnerCapacity(unittest.TestCase):
    """GetAccountDonglesByID200ResponseDataInnerInverterConnectionsBatteriesInnerCapacity unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetAccountDonglesByID200ResponseDataInnerInverterConnectionsBatteriesInnerCapacity:
        """Test GetAccountDonglesByID200ResponseDataInnerInverterConnectionsBatteriesInnerCapacity
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetAccountDonglesByID200ResponseDataInnerInverterConnectionsBatteriesInnerCapacity`
        """
        model = GetAccountDonglesByID200ResponseDataInnerInverterConnectionsBatteriesInnerCapacity()  # noqa: E501
        if include_optional:
            return GetAccountDonglesByID200ResponseDataInnerInverterConnectionsBatteriesInnerCapacity(
                full = 191.39,
                design = 186
            )
        else:
            return GetAccountDonglesByID200ResponseDataInnerInverterConnectionsBatteriesInnerCapacity(
        )
        """

    def testGetAccountDonglesByID200ResponseDataInnerInverterConnectionsBatteriesInnerCapacity(self):
        """Test GetAccountDonglesByID200ResponseDataInnerInverterConnectionsBatteriesInnerCapacity"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
