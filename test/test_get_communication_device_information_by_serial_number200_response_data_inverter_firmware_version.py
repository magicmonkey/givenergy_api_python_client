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

from openapi_client.models.get_communication_device_information_by_serial_number200_response_data_inverter_firmware_version import GetCommunicationDeviceInformationBySerialNumber200ResponseDataInverterFirmwareVersion  # noqa: E501

class TestGetCommunicationDeviceInformationBySerialNumber200ResponseDataInverterFirmwareVersion(unittest.TestCase):
    """GetCommunicationDeviceInformationBySerialNumber200ResponseDataInverterFirmwareVersion unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetCommunicationDeviceInformationBySerialNumber200ResponseDataInverterFirmwareVersion:
        """Test GetCommunicationDeviceInformationBySerialNumber200ResponseDataInverterFirmwareVersion
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetCommunicationDeviceInformationBySerialNumber200ResponseDataInverterFirmwareVersion`
        """
        model = GetCommunicationDeviceInformationBySerialNumber200ResponseDataInverterFirmwareVersion()  # noqa: E501
        if include_optional:
            return GetCommunicationDeviceInformationBySerialNumber200ResponseDataInverterFirmwareVersion(
                arm = '',
                dsp = ''
            )
        else:
            return GetCommunicationDeviceInformationBySerialNumber200ResponseDataInverterFirmwareVersion(
        )
        """

    def testGetCommunicationDeviceInformationBySerialNumber200ResponseDataInverterFirmwareVersion(self):
        """Test GetCommunicationDeviceInformationBySerialNumber200ResponseDataInverterFirmwareVersion"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
