# coding: utf-8

"""
    Thoth user API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from thamos.swagger_client.api_client import ApiClient


class ProvenanceApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_provenance_python(self, analysis_id, **kwargs):  # noqa: E501
        """Retrieve a provenance check result.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_provenance_python(analysis_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str analysis_id: Id of analysis to be retrieved. (required)
        :return: AnalysisResultResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_provenance_python_with_http_info(analysis_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_provenance_python_with_http_info(analysis_id, **kwargs)  # noqa: E501
            return data

    def get_provenance_python_with_http_info(self, analysis_id, **kwargs):  # noqa: E501
        """Retrieve a provenance check result.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_provenance_python_with_http_info(analysis_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str analysis_id: Id of analysis to be retrieved. (required)
        :return: AnalysisResultResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['analysis_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_provenance_python" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'analysis_id' is set
        if ('analysis_id' not in params or
                params['analysis_id'] is None):
            raise ValueError("Missing the required parameter `analysis_id` when calling `get_provenance_python`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'analysis_id' in params:
            path_params['analysis_id'] = params['analysis_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/provenance/python/{analysis_id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AnalysisResultResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_provenance_python_log(self, analysis_id, **kwargs):  # noqa: E501
        """Show logs of a provenance checks.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_provenance_python_log(analysis_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str analysis_id: An id of requested analysis. (required)
        :return: AnalysisLogResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_provenance_python_log_with_http_info(analysis_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_provenance_python_log_with_http_info(analysis_id, **kwargs)  # noqa: E501
            return data

    def get_provenance_python_log_with_http_info(self, analysis_id, **kwargs):  # noqa: E501
        """Show logs of a provenance checks.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_provenance_python_log_with_http_info(analysis_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str analysis_id: An id of requested analysis. (required)
        :return: AnalysisLogResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['analysis_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_provenance_python_log" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'analysis_id' is set
        if ('analysis_id' not in params or
                params['analysis_id'] is None):
            raise ValueError("Missing the required parameter `analysis_id` when calling `get_provenance_python_log`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'analysis_id' in params:
            path_params['analysis_id'] = params['analysis_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/provenance/python/{analysis_id}/log', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AnalysisLogResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_provenance_python_status(self, analysis_id, **kwargs):  # noqa: E501
        """Show status of a provenance check.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_provenance_python_status(analysis_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str analysis_id: An id of requested provenance check. (required)
        :return: AnalysisStatusResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_provenance_python_status_with_http_info(analysis_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_provenance_python_status_with_http_info(analysis_id, **kwargs)  # noqa: E501
            return data

    def get_provenance_python_status_with_http_info(self, analysis_id, **kwargs):  # noqa: E501
        """Show status of a provenance check.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_provenance_python_status_with_http_info(analysis_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str analysis_id: An id of requested provenance check. (required)
        :return: AnalysisStatusResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['analysis_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_provenance_python_status" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'analysis_id' is set
        if ('analysis_id' not in params or
                params['analysis_id'] is None):
            raise ValueError("Missing the required parameter `analysis_id` when calling `get_provenance_python_status`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'analysis_id' in params:
            path_params['analysis_id'] = params['analysis_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/provenance/python/{analysis_id}/status', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AnalysisStatusResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def post_provenance_python(self, application_stack, **kwargs):  # noqa: E501
        """Check provenance of packages stated in an application stack.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.post_provenance_python(application_stack, async=True)
        >>> result = thread.get()

        :param async bool
        :param PythonStack application_stack: Pipfile and Pipfile.lock as used by pipenv. (required)
        :param bool debug: Run the provenance checker in a verbose mode so developers can debug it. 
        :param bool force: Do not use cached results, always run provenance checks. 
        :return: AnalysisResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.post_provenance_python_with_http_info(application_stack, **kwargs)  # noqa: E501
        else:
            (data) = self.post_provenance_python_with_http_info(application_stack, **kwargs)  # noqa: E501
            return data

    def post_provenance_python_with_http_info(self, application_stack, **kwargs):  # noqa: E501
        """Check provenance of packages stated in an application stack.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.post_provenance_python_with_http_info(application_stack, async=True)
        >>> result = thread.get()

        :param async bool
        :param PythonStack application_stack: Pipfile and Pipfile.lock as used by pipenv. (required)
        :param bool debug: Run the provenance checker in a verbose mode so developers can debug it. 
        :param bool force: Do not use cached results, always run provenance checks. 
        :return: AnalysisResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['application_stack', 'debug', 'force']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_provenance_python" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'application_stack' is set
        if ('application_stack' not in params or
                params['application_stack'] is None):
            raise ValueError("Missing the required parameter `application_stack` when calling `post_provenance_python`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'debug' in params:
            query_params.append(('debug', params['debug']))  # noqa: E501
        if 'force' in params:
            query_params.append(('force', params['force']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'application_stack' in params:
            body_params = params['application_stack']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/provenance/python', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AnalysisResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
