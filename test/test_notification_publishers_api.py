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
from swagger_client.api.notification_publishers_api import NotificationPublishersApi  # noqa: E501
from swagger_client.rest import ApiException


class TestNotificationPublishersApi(unittest.TestCase):
    """NotificationPublishersApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.notification_publishers_api.NotificationPublishersApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_notification_publisher(self):
        """Test case for create_notification_publisher

        Create a notification publisher plugin instance.  # noqa: E501
        """
        pass

    def test_delete_notification_publisher(self):
        """Test case for delete_notification_publisher

        Delete a notification publisher plugin instance.  # noqa: E501
        """
        pass

    def test_get_action(self):
        """Test case for get_action

        Find an notification publisher plugin instance's action by ID.  # noqa: E501
        """
        pass

    def test_get_actions(self):
        """Test case for get_actions

        List the actions for a notification publisher plugin instance.  # noqa: E501
        """
        pass

    def test_get_notification_publisher(self):
        """Test case for get_notification_publisher

        Get a specific notification publisher plugin instance.  # noqa: E501
        """
        pass

    def test_get_notification_publisher_plugin_descriptor(self):
        """Test case for get_notification_publisher_plugin_descriptor

        Get the description of a notification publisher plugin descriptor.  # noqa: E501
        """
        pass

    def test_get_notification_publisher_plugin_descriptors(self):
        """Test case for get_notification_publisher_plugin_descriptors

        Get the list of available Notification Publisher Plugin descriptors.  # noqa: E501
        """
        pass

    def test_get_notification_publishers(self):
        """Test case for get_notification_publishers

        Get a list of notification publisher plugin instances.  # noqa: E501
        """
        pass

    def test_get_settings(self):
        """Test case for get_settings

        Get general notification publisher settings.  # noqa: E501
        """
        pass

    def test_invoke_action_with_options(self):
        """Test case for invoke_action_with_options

        Invokes an action for notification publisher plugin instance.  # noqa: E501
        """
        pass

    def test_update_notification_publisher(self):
        """Test case for update_notification_publisher

        Update a notification publisher plugin instance.  # noqa: E501
        """
        pass

    def test_update_settings(self):
        """Test case for update_settings

        Update general notification publisher settings.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
