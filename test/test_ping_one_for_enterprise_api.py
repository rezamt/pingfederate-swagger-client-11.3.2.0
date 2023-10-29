# coding: utf-8

"""
    Administrative API Documentation

    The PingFederate Administrative API is a REST-based interface that provides a programmatic way to make configuration changes to PingFederate as an alternative to using the administrative console.<br/><br/>Expand the resources below to display implementation details on that resource such as the available endpoints, the parameter and response models for the operation, and the model structure of the resources themselves. Each resource operation comes with the ability to interact with the API. You are prompted for proper administration credentials when you try to perform an API operation.  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.ping_one_for_enterprise_api import PingOneForEnterpriseApi  # noqa: E501
from swagger_client.rest import ApiException


class TestPingOneForEnterpriseApi(unittest.TestCase):
    """PingOneForEnterpriseApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.ping_one_for_enterprise_api.PingOneForEnterpriseApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_disconnect(self):
        """Test case for disconnect

        Disconnect from PingOne for Enterprise  # noqa: E501
        """
        pass

    def test_get_key_pairs(self):
        """Test case for get_key_pairs

        Get the PingOne for Enterprise key pair settings  # noqa: E501
        """
        pass

    def test_get_ping_one_for_enterprise_settings(self):
        """Test case for get_ping_one_for_enterprise_settings

        Get the PingOne for Enterprise settings  # noqa: E501
        """
        pass

    def test_rotate_keys(self):
        """Test case for rotate_keys

        Rotate the authentication key  # noqa: E501
        """
        pass

    def test_update_ping_one_for_enterprise_identity_repository(self):
        """Test case for update_ping_one_for_enterprise_identity_repository

        Update the PingOne Identity Repository  # noqa: E501
        """
        pass

    def test_update_ping_one_settings(self):
        """Test case for update_ping_one_settings

        Update the PingOne for Enterprise settings.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()