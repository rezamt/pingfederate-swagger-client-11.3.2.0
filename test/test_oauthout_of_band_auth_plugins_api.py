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
from swagger_client.api.oauthout_of_band_auth_plugins_api import OauthoutOfBandAuthPluginsApi  # noqa: E501
from swagger_client.rest import ApiException


class TestOauthoutOfBandAuthPluginsApi(unittest.TestCase):
    """OauthoutOfBandAuthPluginsApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.oauthout_of_band_auth_plugins_api.OauthoutOfBandAuthPluginsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_oob_authenticator(self):
        """Test case for create_oob_authenticator

        Create an Out of Band authenticator plugin instance.  # noqa: E501
        """
        pass

    def test_delete_oob_authenticator(self):
        """Test case for delete_oob_authenticator

        Delete an Out of Band authenticator plugin instance.  # noqa: E501
        """
        pass

    def test_get_action(self):
        """Test case for get_action

        Find an Out of Band authenticator plugin instance's action by ID.  # noqa: E501
        """
        pass

    def test_get_actions(self):
        """Test case for get_actions

        List of actions for an Out of Band authenticator plugin instance.  # noqa: E501
        """
        pass

    def test_get_oob_auth_plugin_descriptor(self):
        """Test case for get_oob_auth_plugin_descriptor

        Get the descriptor of an Out of Band authenticator plugin.  # noqa: E501
        """
        pass

    def test_get_oob_auth_plugin_descriptors(self):
        """Test case for get_oob_auth_plugin_descriptors

        Get the list of available Out of Band authenticator plugin descriptors.  # noqa: E501
        """
        pass

    def test_get_oob_authenticator(self):
        """Test case for get_oob_authenticator

        Get a specific Out of Band authenticator plugin instance.  # noqa: E501
        """
        pass

    def test_get_oob_authenticators(self):
        """Test case for get_oob_authenticators

        Get a list of Out of Band authenticator plugin instances.  # noqa: E501
        """
        pass

    def test_invoke_action_with_options(self):
        """Test case for invoke_action_with_options

        Invokes an action for Out of Band authenticator plugin instance.  # noqa: E501
        """
        pass

    def test_update_oob_authenticator(self):
        """Test case for update_oob_authenticator

        Update an Out of Band authenticator plugin instance.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
