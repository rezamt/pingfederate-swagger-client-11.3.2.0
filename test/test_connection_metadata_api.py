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
from swagger_client.api.connection_metadata_api import ConnectionMetadataApi  # noqa: E501
from swagger_client.rest import ApiException


class TestConnectionMetadataApi(unittest.TestCase):
    """ConnectionMetadataApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.connection_metadata_api.ConnectionMetadataApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_convert(self):
        """Test case for convert

        Convert a partner's SAML metadata into a JSON representation.  # noqa: E501
        """
        pass

    def test_export(self):
        """Test case for export

        Export a connection's SAML metadata that can be given to a partner.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
