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
from swagger_client.api.secret_managers_api import SecretManagersApi  # noqa: E501
from swagger_client.rest import ApiException


class TestSecretManagersApi(unittest.TestCase):
    """SecretManagersApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.secret_managers_api.SecretManagersApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_secret_manager(self):
        """Test case for create_secret_manager

        Create a secret manager plugin instance.  # noqa: E501
        """
        pass

    def test_delete_secret_manager(self):
        """Test case for delete_secret_manager

        Delete a secret manager plugin instance.  # noqa: E501
        """
        pass

    def test_get_action(self):
        """Test case for get_action

        Get a secret manager plugin instance's action by ID.  # noqa: E501
        """
        pass

    def test_get_actions(self):
        """Test case for get_actions

        Get a list of actions for a secret manager plugin instance.  # noqa: E501
        """
        pass

    def test_get_secret_manager(self):
        """Test case for get_secret_manager

        Get a specific secret manager plugin instance.  # noqa: E501
        """
        pass

    def test_get_secret_manager_plugin_descriptor(self):
        """Test case for get_secret_manager_plugin_descriptor

        Get a secret manager plugin descriptor.  # noqa: E501
        """
        pass

    def test_get_secret_manager_plugin_descriptors(self):
        """Test case for get_secret_manager_plugin_descriptors

        Get a list of available secret manager plugin descriptors.  # noqa: E501
        """
        pass

    def test_get_secret_managers(self):
        """Test case for get_secret_managers

        Get a list of secret manager plugin instances.  # noqa: E501
        """
        pass

    def test_invoke_action_with_options(self):
        """Test case for invoke_action_with_options

        Invokes an action for secret manager plugin instance.  # noqa: E501
        """
        pass

    def test_update_secret_manager(self):
        """Test case for update_secret_manager

        Update a secret manager plugin instance.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
