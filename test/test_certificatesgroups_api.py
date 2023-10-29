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
from swagger_client.api.certificatesgroups_api import CertificatesgroupsApi  # noqa: E501
from swagger_client.rest import ApiException


class TestCertificatesgroupsApi(unittest.TestCase):
    """CertificatesgroupsApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.certificatesgroups_api.CertificatesgroupsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_delete_certificate_from_group(self):
        """Test case for delete_certificate_from_group

        Delete a certificate from a group.  # noqa: E501
        """
        pass

    def test_get_certificate_from_group(self):
        """Test case for get_certificate_from_group

        Retrieve details of a certificate.  # noqa: E501
        """
        pass

    def test_get_certificates_for_group(self):
        """Test case for get_certificates_for_group

        Get list of all certificates for a group.  # noqa: E501
        """
        pass

    def test_import_feature_cert(self):
        """Test case for import_feature_cert

        Import a new certificate to a group.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
