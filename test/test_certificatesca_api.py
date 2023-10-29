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
from swagger_client.api.certificatesca_api import CertificatescaApi  # noqa: E501
from swagger_client.rest import ApiException


class TestCertificatescaApi(unittest.TestCase):
    """CertificatescaApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.certificatesca_api.CertificatescaApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_delete_trusted_ca(self):
        """Test case for delete_trusted_ca

        Delete a trusted certificate authority.  # noqa: E501
        """
        pass

    def test_export_certificate_file(self):
        """Test case for export_certificate_file

        Download the certificate from a given trusted certificate authority.  # noqa: E501
        """
        pass

    def test_get_trusted_cas(self):
        """Test case for get_trusted_cas

        Get list of trusted certificate authorities.  # noqa: E501
        """
        pass

    def test_get_trusted_cert(self):
        """Test case for get_trusted_cert

        Retrieve details of a trusted certificate authority.  # noqa: E501
        """
        pass

    def test_import_trusted_ca(self):
        """Test case for import_trusted_ca

        Import a new trusted certificate authority.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
