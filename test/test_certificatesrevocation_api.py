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
from swagger_client.api.certificatesrevocation_api import CertificatesrevocationApi  # noqa: E501
from swagger_client.rest import ApiException


class TestCertificatesrevocationApi(unittest.TestCase):
    """CertificatesrevocationApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.certificatesrevocation_api.CertificatesrevocationApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_delete_ocsp_certificate_by_id(self):
        """Test case for delete_ocsp_certificate_by_id

        Delete an OCSP responder signature verification certificate by ID.  # noqa: E501
        """
        pass

    def test_get_ocsp_certificate_by_id(self):
        """Test case for get_ocsp_certificate_by_id

        Get an OCSP responder signature verification certificate by ID.  # noqa: E501
        """
        pass

    def test_get_ocsp_certificates(self):
        """Test case for get_ocsp_certificates

        Get the list of available OCSP responder signature verification certificates.  # noqa: E501
        """
        pass

    def test_get_revocation_settings(self):
        """Test case for get_revocation_settings

        Get certificate revocation settings.  # noqa: E501
        """
        pass

    def test_import_ocsp_certificate(self):
        """Test case for import_ocsp_certificate

        Import an OCSP responder signature verification certificate.  # noqa: E501
        """
        pass

    def test_update_revocation_settings(self):
        """Test case for update_revocation_settings

        Update certificate revocation settings.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
