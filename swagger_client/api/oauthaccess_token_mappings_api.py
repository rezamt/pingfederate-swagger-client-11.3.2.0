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


class OauthaccessTokenMappingsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_mapping(self, body, **kwargs):  # noqa: E501
        """Create a new Access Token Mapping.  # noqa: E501

        Create a new Access Token Mapping. If the mapping is not properly configured, a 422 status code is returned along with a list of validation errors that must be corrected.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_mapping(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param AccessTokenMapping body: Configuration for the new Access Token Mapping. (required)
        :param bool x_bypass_external_validation: External validation will be bypassed when set to true. Default to false.
        :return: AccessTokenMapping
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_mapping_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.create_mapping_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def create_mapping_with_http_info(self, body, **kwargs):  # noqa: E501
        """Create a new Access Token Mapping.  # noqa: E501

        Create a new Access Token Mapping. If the mapping is not properly configured, a 422 status code is returned along with a list of validation errors that must be corrected.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_mapping_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param AccessTokenMapping body: Configuration for the new Access Token Mapping. (required)
        :param bool x_bypass_external_validation: External validation will be bypassed when set to true. Default to false.
        :return: AccessTokenMapping
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'x_bypass_external_validation']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_mapping" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if self.api_client.client_side_validation and ('body' not in params or
                                                       params['body'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `body` when calling `create_mapping`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_bypass_external_validation' in params:
            header_params['X-BypassExternalValidation'] = params['x_bypass_external_validation']  # noqa: E501

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
            '/oauth/accessTokenMappings', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AccessTokenMapping',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_mapping(self, id, **kwargs):  # noqa: E501
        """Delete an Access Token Mapping.  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_mapping(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: ID of the Access Token Mapping. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_mapping_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_mapping_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def delete_mapping_with_http_info(self, id, **kwargs):  # noqa: E501
        """Delete an Access Token Mapping.  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_mapping_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: ID of the Access Token Mapping. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_mapping" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in params or
                                                       params['id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `id` when calling `delete_mapping`")  # noqa: E501

        collection_formats = {}

        path_params = {}
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
            '/oauth/accessTokenMappings/{id}', 'DELETE',
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

    def get_mapping(self, id, **kwargs):  # noqa: E501
        """Find the Access Token Mapping by its ID.  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_mapping(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: ID of the Access Token Mapping. (required)
        :return: AccessTokenMapping
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_mapping_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_mapping_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def get_mapping_with_http_info(self, id, **kwargs):  # noqa: E501
        """Find the Access Token Mapping by its ID.  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_mapping_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: ID of the Access Token Mapping. (required)
        :return: AccessTokenMapping
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_mapping" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in params or
                                                       params['id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `id` when calling `get_mapping`")  # noqa: E501

        collection_formats = {}

        path_params = {}
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
            '/oauth/accessTokenMappings/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AccessTokenMapping',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_mappings(self, **kwargs):  # noqa: E501
        """Get the list of Access Token Mappings.  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_mappings(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: AccessTokenMappings
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_mappings_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_mappings_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_mappings_with_http_info(self, **kwargs):  # noqa: E501
        """Get the list of Access Token Mappings.  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_mappings_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: AccessTokenMappings
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_mappings" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

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
            '/oauth/accessTokenMappings', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AccessTokenMappings',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_mapping(self, id, body, **kwargs):  # noqa: E501
        """Update an Access Token Mapping.  # noqa: E501

        Update an Access Token Mapping with the matching ID. If the mapping is not properly configured, a 422 status code is returned along with a list of validation errors that must be corrected. Note: A 404 status code is returned for nonexistent mapping ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_mapping(id, body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: ID of the Access Token Mapping to update. (required)
        :param AccessTokenMapping body: Configuration for updated mapping. (required)
        :param bool x_bypass_external_validation: External validation will be bypassed when set to true. Default to false.
        :return: AccessTokenMapping
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_mapping_with_http_info(id, body, **kwargs)  # noqa: E501
        else:
            (data) = self.update_mapping_with_http_info(id, body, **kwargs)  # noqa: E501
            return data

    def update_mapping_with_http_info(self, id, body, **kwargs):  # noqa: E501
        """Update an Access Token Mapping.  # noqa: E501

        Update an Access Token Mapping with the matching ID. If the mapping is not properly configured, a 422 status code is returned along with a list of validation errors that must be corrected. Note: A 404 status code is returned for nonexistent mapping ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_mapping_with_http_info(id, body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: ID of the Access Token Mapping to update. (required)
        :param AccessTokenMapping body: Configuration for updated mapping. (required)
        :param bool x_bypass_external_validation: External validation will be bypassed when set to true. Default to false.
        :return: AccessTokenMapping
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'body', 'x_bypass_external_validation']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_mapping" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in params or
                                                       params['id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `id` when calling `update_mapping`")  # noqa: E501
        # verify the required parameter 'body' is set
        if self.api_client.client_side_validation and ('body' not in params or
                                                       params['body'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `body` when calling `update_mapping`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'x_bypass_external_validation' in params:
            header_params['X-BypassExternalValidation'] = params['x_bypass_external_validation']  # noqa: E501

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
            '/oauth/accessTokenMappings/{id}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AccessTokenMapping',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
