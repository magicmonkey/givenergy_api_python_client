# coding: utf-8

"""
    GivEnergy API Documentation (v1.14.0)

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.api.ev_charger_api import EVChargerApi  # noqa: E501


class TestEVChargerApi(unittest.TestCase):
    """EVChargerApi unit test stubs"""

    def setUp(self) -> None:
        self.api = EVChargerApi()  # noqa: E501

    def tearDown(self) -> None:
        pass

    def test_evget_data_points(self) -> None:
        """Test case for evget_data_points

        Get Data Points  # noqa: E501
        """
        pass

    def test_get_charging_sessions(self) -> None:
        """Test case for get_charging_sessions

        Get Charging Sessions  # noqa: E501
        """
        pass

    def test_get_command_data(self) -> None:
        """Test case for get_command_data

        Get Command Data  # noqa: E501
        """
        pass

    def test_get_ev_charger_by_uuid(self) -> None:
        """Test case for get_ev_charger_by_uuid

        Get EV Charger by UUID  # noqa: E501
        """
        pass

    def test_get_supported_commands(self) -> None:
        """Test case for get_supported_commands

        Get Supported Commands  # noqa: E501
        """
        pass

    def test_get_your_ev_chargers(self) -> None:
        """Test case for get_your_ev_chargers

        Get Your EV Chargers  # noqa: E501
        """
        pass

    def test_send_command(self) -> None:
        """Test case for send_command

        Send Command  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
