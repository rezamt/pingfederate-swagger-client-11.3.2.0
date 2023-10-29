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
from swagger_client.api.idpadapters_api import IdpadaptersApi  # noqa: E501
from swagger_client.rest import ApiException


class TestIdpadaptersApi(unittest.TestCase):
    """IdpadaptersApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.idpadapters_api.IdpadaptersApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_idp_adapter(self):
        """Test case for create_idp_adapter

        Create a new IdP adapter instance.  # noqa: E501
        """
        pass

    def test_delete_idp_adapter(self):
        """Test case for delete_idp_adapter

        Delete an IdP adapter instance.  # noqa: E501
        """
        pass

    def test_get_action(self):
        """Test case for get_action

        Find an IdP adapter instance's action by ID.  # noqa: E501
        """
        pass

    def test_get_actions(self):
        """Test case for get_actions

        List the actions for an IdP adapter instance.  # noqa: E501
        """
        pass

    def test_get_idp_adapter(self):
        """Test case for get_idp_adapter

        Find an IdP adapter instance by ID.  # noqa: E501
        """
        pass

    def test_get_idp_adapter_descriptors(self):
        """Test case for get_idp_adapter_descriptors

        Get the list of available IdP adapter descriptors.  # noqa: E501
        """
        pass

    def test_get_idp_adapter_descriptors_by_id(self):
        """Test case for get_idp_adapter_descriptors_by_id

        Get the description of an IdP adapter plugin by ID.  # noqa: E501
        """
        pass

    def test_get_idp_adapters(self):
        """Test case for get_idp_adapters

        Get the list of configured IdP adapter instances.  # noqa: E501
        """
        pass

    def test_invoke_action_with_options(self):
        """Test case for invoke_action_with_options

        Invokes an action for an IdP adapter instance.  # noqa: E501
        """
        pass

    def test_update_idp_adapter(self):
        """Test case for update_idp_adapter

        Update an IdP adapter instance.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
