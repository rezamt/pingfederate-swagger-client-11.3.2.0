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
from swagger_client.api.idpsts_request_parameters_contracts_api import IdpstsRequestParametersContractsApi  # noqa: E501
from swagger_client.rest import ApiException


class TestIdpstsRequestParametersContractsApi(unittest.TestCase):
    """IdpstsRequestParametersContractsApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.idpsts_request_parameters_contracts_api.IdpstsRequestParametersContractsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_sts_request_param_contract(self):
        """Test case for create_sts_request_param_contract

        Create a new STS Request Parameters Contract.  # noqa: E501
        """
        pass

    def test_delete_sts_request_param_contract_by_id(self):
        """Test case for delete_sts_request_param_contract_by_id

        Delete a STS Request Parameters Contract.  # noqa: E501
        """
        pass

    def test_get_sts_request_param_contract_by_id(self):
        """Test case for get_sts_request_param_contract_by_id

        Get a STS Request Parameters Contract.  # noqa: E501
        """
        pass

    def test_get_sts_request_param_contracts(self):
        """Test case for get_sts_request_param_contracts

        Get the list of STS Request Parameters Contracts.  # noqa: E501
        """
        pass

    def test_update_sts_request_param_contract_by_id(self):
        """Test case for update_sts_request_param_contract_by_id

        Update a STS Request Parameters Contract.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()