# coding: utf-8

"""
    Administrative API Documentation

    The PingFederate Administrative API is a REST-based interface that provides a programmatic way to make configuration changes to PingFederate as an alternative to using the administrative console.<br/><br/>Expand the resources below to display implementation details on that resource such as the available endpoints, the parameter and response models for the operation, and the model structure of the resources themselves. Each resource operation comes with the ability to interact with the API. You are prompted for proper administration credentials when you try to perform an API operation.  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class CertificatesgroupsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def delete_certificate_from_group(self, group_name, id, **kwargs):  # noqa: E501
        """Delete a certificate from a group.  # noqa: E501

        If the request is successful, the response body is empty. If the request fails, an ApiResult is returned with details of the error.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_certificate_from_group(group_name, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str group_name: Name of the group to retrieve certificates for. (required)
        :param str id: ID of the certificate to retrieve. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_certificate_from_group_with_http_info(group_name, id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_certificate_from_group_with_http_info(group_name, id, **kwargs)  # noqa: E501
            return data

    def delete_certificate_from_group_with_http_info(self, group_name, id, **kwargs):  # noqa: E501
        """Delete a certificate from a group.  # noqa: E501

        If the request is successful, the response body is empty. If the request fails, an ApiResult is returned with details of the error.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_certificate_from_group_with_http_info(group_name, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str group_name: Name of the group to retrieve certificates for. (required)
        :param str id: ID of the certificate to retrieve. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['group_name', 'id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_certificate_from_group" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'group_name' is set
        if self.api_client.client_side_validation and ('group_name' not in params or
                                                       params['group_name'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `group_name` when calling `delete_certificate_from_group`")  # noqa: E501
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in params or
                                                       params['id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `id` when calling `delete_certificate_from_group`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'group_name' in params:
            path_params['groupName'] = params['group_name']  # noqa: E501
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/certificates/groups/{groupName}/{id}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_certificate_from_group(self, group_name, id, **kwargs):  # noqa: E501
        """Retrieve details of a certificate.  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_certificate_from_group(group_name, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str group_name: Name of the group to retrieve certificates for. (required)
        :param str id: ID of the certificate to retrieve. (required)
        :return: CertView
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_certificate_from_group_with_http_info(group_name, id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_certificate_from_group_with_http_info(group_name, id, **kwargs)  # noqa: E501
            return data

    def get_certificate_from_group_with_http_info(self, group_name, id, **kwargs):  # noqa: E501
        """Retrieve details of a certificate.  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_certificate_from_group_with_http_info(group_name, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str group_name: Name of the group to retrieve certificates for. (required)
        :param str id: ID of the certificate to retrieve. (required)
        :return: CertView
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['group_name', 'id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_certificate_from_group" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'group_name' is set
        if self.api_client.client_side_validation and ('group_name' not in params or
                                                       params['group_name'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `group_name` when calling `get_certificate_from_group`")  # noqa: E501
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in params or
                                                       params['id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `id` when calling `get_certificate_from_group`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'group_name' in params:
            path_params['groupName'] = params['group_name']  # noqa: E501
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/certificates/groups/{groupName}/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CertView',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_certificates_for_group(self, group_name, **kwargs):  # noqa: E501
        """Get list of all certificates for a group.  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_certificates_for_group(group_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str group_name: Name of the group to retrieve certificates for. (required)
        :return: CertViews
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_certificates_for_group_with_http_info(group_name, **kwargs)  # noqa: E501
        else:
            (data) = self.get_certificates_for_group_with_http_info(group_name, **kwargs)  # noqa: E501
            return data

    def get_certificates_for_group_with_http_info(self, group_name, **kwargs):  # noqa: E501
        """Get list of all certificates for a group.  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_certificates_for_group_with_http_info(group_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str group_name: Name of the group to retrieve certificates for. (required)
        :return: CertViews
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['group_name']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_certificates_for_group" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'group_name' is set
        if self.api_client.client_side_validation and ('group_name' not in params or
                                                       params['group_name'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `group_name` when calling `get_certificates_for_group`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'group_name' in params:
            path_params['groupName'] = params['group_name']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/certificates/groups/{groupName}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CertViews',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def import_feature_cert(self, group_name, body, **kwargs):  # noqa: E501
        """Import a new certificate to a group.  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.import_feature_cert(group_name, body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str group_name: Name of the group to retrieve certificates for. (required)
        :param X509File body: File data to import. (required)
        :return: CertView
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.import_feature_cert_with_http_info(group_name, body, **kwargs)  # noqa: E501
        else:
            (data) = self.import_feature_cert_with_http_info(group_name, body, **kwargs)  # noqa: E501
            return data

    def import_feature_cert_with_http_info(self, group_name, body, **kwargs):  # noqa: E501
        """Import a new certificate to a group.  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.import_feature_cert_with_http_info(group_name, body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str group_name: Name of the group to retrieve certificates for. (required)
        :param X509File body: File data to import. (required)
        :return: CertView
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['group_name', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method import_feature_cert" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'group_name' is set
        if self.api_client.client_side_validation and ('group_name' not in params or
                                                       params['group_name'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `group_name` when calling `import_feature_cert`")  # noqa: E501
        # verify the required parameter 'body' is set
        if self.api_client.client_side_validation and ('body' not in params or
                                                       params['body'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `body` when calling `import_feature_cert`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'group_name' in params:
            path_params['groupName'] = params['group_name']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/certificates/groups/{groupName}/import', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CertView',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
