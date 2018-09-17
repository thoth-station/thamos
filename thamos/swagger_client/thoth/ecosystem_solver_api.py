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


class EcosystemSolverApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_solve_python(self, analysis_id, **kwargs):  # noqa: E501
        """Retrieve a solver result.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_solve_python(analysis_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str analysis_id: Document id to be retrieved. (required)
        :return: AnalysisResultResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_solve_python_with_http_info(analysis_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_solve_python_with_http_info(analysis_id, **kwargs)  # noqa: E501
            return data

    def get_solve_python_with_http_info(self, analysis_id, **kwargs):  # noqa: E501
        """Retrieve a solver result.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_solve_python_with_http_info(analysis_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str analysis_id: Document id to be retrieved. (required)
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
                    " to method get_solve_python" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'analysis_id' is set
        if ('analysis_id' not in params or
                params['analysis_id'] is None):
            raise ValueError("Missing the required parameter `analysis_id` when calling `get_solve_python`")  # noqa: E501

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
            '/solve/python/{analysis_id}', 'GET',
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

    def get_solve_python_log(self, analysis_id, **kwargs):  # noqa: E501
        """Retrieve a solver log.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_solve_python_log(analysis_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str analysis_id: An id of analysis for a solver run. (required)
        :return: AnalysisLogResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_solve_python_log_with_http_info(analysis_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_solve_python_log_with_http_info(analysis_id, **kwargs)  # noqa: E501
            return data

    def get_solve_python_log_with_http_info(self, analysis_id, **kwargs):  # noqa: E501
        """Retrieve a solver log.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_solve_python_log_with_http_info(analysis_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str analysis_id: An id of analysis for a solver run. (required)
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
                    " to method get_solve_python_log" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'analysis_id' is set
        if ('analysis_id' not in params or
                params['analysis_id'] is None):
            raise ValueError("Missing the required parameter `analysis_id` when calling `get_solve_python_log`")  # noqa: E501

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
            '/solve/python/{analysis_id}/log', 'GET',
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

    def get_solve_python_status(self, analysis_id, **kwargs):  # noqa: E501
        """Show status of an ecosystem solver.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_solve_python_status(analysis_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str analysis_id: An id of requested ecosystem solver run. (required)
        :return: AnalysisStatusResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_solve_python_status_with_http_info(analysis_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_solve_python_status_with_http_info(analysis_id, **kwargs)  # noqa: E501
            return data

    def get_solve_python_status_with_http_info(self, analysis_id, **kwargs):  # noqa: E501
        """Show status of an ecosystem solver.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_solve_python_status_with_http_info(analysis_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str analysis_id: An id of requested ecosystem solver run. (required)
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
                    " to method get_solve_python_status" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'analysis_id' is set
        if ('analysis_id' not in params or
                params['analysis_id'] is None):
            raise ValueError("Missing the required parameter `analysis_id` when calling `get_solve_python_status`")  # noqa: E501

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
            '/solve/python/{analysis_id}/status', 'GET',
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

    def list_solve_python_results(self, **kwargs):  # noqa: E501
        """Retrieve a list of document ids for solver results.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.list_solve_python_results(async=True)
        >>> result = thread.get()

        :param async bool
        :param int page: Page offset in pagination.
        :return: AnalysisListingResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.list_solve_python_results_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.list_solve_python_results_with_http_info(**kwargs)  # noqa: E501
            return data

    def list_solve_python_results_with_http_info(self, **kwargs):  # noqa: E501
        """Retrieve a list of document ids for solver results.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.list_solve_python_results_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param int page: Page offset in pagination.
        :return: AnalysisListingResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['page']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_solve_python_results" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501

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
            '/solve/python', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AnalysisListingResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_solvers(self, **kwargs):  # noqa: E501
        """Retrieve a list of solvers installed and available.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.list_solvers(async=True)
        >>> result = thread.get()

        :param async bool
        :return: dict(str, ERRORUNKNOWN)
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.list_solvers_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.list_solvers_with_http_info(**kwargs)  # noqa: E501
            return data

    def list_solvers_with_http_info(self, **kwargs):  # noqa: E501
        """Retrieve a list of solvers installed and available.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.list_solvers_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :return: dict(str, ERRORUNKNOWN)
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_solvers" % key
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

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/solvers', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='dict(str, ERRORUNKNOWN)',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def post_solve_python(self, packages, **kwargs):  # noqa: E501
        """Solve the given application stack.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.post_solve_python(packages, async=True)
        >>> result = thread.get()

        :param async bool
        :param Packages packages: Packages to be solved. (required)
        :param str solver: Name of solver to be triggered.
        :param bool debug: Run the given analyzer in a verbose mode so developers can debug analyzer. 
        :param bool transitive: Packages to be solved.
        :return: AnalysisResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.post_solve_python_with_http_info(packages, **kwargs)  # noqa: E501
        else:
            (data) = self.post_solve_python_with_http_info(packages, **kwargs)  # noqa: E501
            return data

    def post_solve_python_with_http_info(self, packages, **kwargs):  # noqa: E501
        """Solve the given application stack.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.post_solve_python_with_http_info(packages, async=True)
        >>> result = thread.get()

        :param async bool
        :param Packages packages: Packages to be solved. (required)
        :param str solver: Name of solver to be triggered.
        :param bool debug: Run the given analyzer in a verbose mode so developers can debug analyzer. 
        :param bool transitive: Packages to be solved.
        :return: AnalysisResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['packages', 'solver', 'debug', 'transitive']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_solve_python" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'packages' is set
        if ('packages' not in params or
                params['packages'] is None):
            raise ValueError("Missing the required parameter `packages` when calling `post_solve_python`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'solver' in params:
            query_params.append(('solver', params['solver']))  # noqa: E501
        if 'debug' in params:
            query_params.append(('debug', params['debug']))  # noqa: E501
        if 'transitive' in params:
            query_params.append(('transitive', params['transitive']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'packages' in params:
            body_params = params['packages']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/solve/python', 'POST',
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