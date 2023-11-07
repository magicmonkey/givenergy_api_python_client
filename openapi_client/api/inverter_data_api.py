# coding: utf-8

"""
    GivEnergy API Documentation (v1.14.0)

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import re  # noqa: F401
import io
import warnings

from pydantic import validate_arguments, ValidationError

from typing_extensions import Annotated
from pydantic import Field, StrictBool, StrictInt, StrictStr

from typing import Optional

from openapi_client.models.get_data_points200_response import GetDataPoints200Response
from openapi_client.models.get_events200_response import GetEvents200Response
from openapi_client.models.get_events_request import GetEventsRequest
from openapi_client.models.get_latest_meter_data200_response import GetLatestMeterData200Response
from openapi_client.models.get_latest_system_data200_response import GetLatestSystemData200Response

from openapi_client.api_client import ApiClient
from openapi_client.api_response import ApiResponse
from openapi_client.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class InverterDataApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_arguments
    def get_data_points(self, inverter_serial_number : Annotated[StrictStr, Field(..., description="The serial number of the inverter.")], var_date : Annotated[StrictStr, Field(..., description="Optional parameter. ISO8601-date required The date to fetch the data. This assumes the date at the system's local time")], page : Annotated[Optional[StrictInt], Field(description="Page number to return")] = None, page_size : Annotated[Optional[StrictInt], Field(description="Number of items to return in a page. Defaults to 15")] = None, authorization : Optional[StrictStr] = None, **kwargs) -> GetDataPoints200Response:  # noqa: E501
        """Get Data Points  # noqa: E501

        Displays the entire data packet set from the chosen date  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_data_points(inverter_serial_number, var_date, page, page_size, authorization, async_req=True)
        >>> result = thread.get()

        :param inverter_serial_number: The serial number of the inverter. (required)
        :type inverter_serial_number: str
        :param var_date: Optional parameter. ISO8601-date required The date to fetch the data. This assumes the date at the system's local time (required)
        :type var_date: str
        :param page: Page number to return
        :type page: int
        :param page_size: Number of items to return in a page. Defaults to 15
        :type page_size: int
        :param authorization: 
        :type authorization: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: GetDataPoints200Response
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the get_data_points_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.get_data_points_with_http_info(inverter_serial_number, var_date, page, page_size, authorization, **kwargs)  # noqa: E501

    @validate_arguments
    def get_data_points_with_http_info(self, inverter_serial_number : Annotated[StrictStr, Field(..., description="The serial number of the inverter.")], var_date : Annotated[StrictStr, Field(..., description="Optional parameter. ISO8601-date required The date to fetch the data. This assumes the date at the system's local time")], page : Annotated[Optional[StrictInt], Field(description="Page number to return")] = None, page_size : Annotated[Optional[StrictInt], Field(description="Number of items to return in a page. Defaults to 15")] = None, authorization : Optional[StrictStr] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """Get Data Points  # noqa: E501

        Displays the entire data packet set from the chosen date  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_data_points_with_http_info(inverter_serial_number, var_date, page, page_size, authorization, async_req=True)
        >>> result = thread.get()

        :param inverter_serial_number: The serial number of the inverter. (required)
        :type inverter_serial_number: str
        :param var_date: Optional parameter. ISO8601-date required The date to fetch the data. This assumes the date at the system's local time (required)
        :type var_date: str
        :param page: Page number to return
        :type page: int
        :param page_size: Number of items to return in a page. Defaults to 15
        :type page_size: int
        :param authorization: 
        :type authorization: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(GetDataPoints200Response, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'inverter_serial_number',
            'var_date',
            'page',
            'page_size',
            'authorization'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_data_points" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['inverter_serial_number']:
            _path_params['inverter_serial_number'] = _params['inverter_serial_number']

        if _params['var_date']:
            _path_params['date'] = _params['var_date']


        # process the query parameters
        _query_params = []
        if _params.get('page') is not None:  # noqa: E501
            _query_params.append(('page', _params['page']))

        if _params.get('page_size') is not None:  # noqa: E501
            _query_params.append(('pageSize', _params['page_size']))

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        if _params['authorization']:
            _header_params['Authorization'] = _params['authorization']

        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['default']  # noqa: E501

        _response_types_map = {
            '200': "GetDataPoints200Response",
        }

        return self.api_client.call_api(
            '/inverter/{inverter_serial_number}/data-points/{date}', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def get_events(self, inverter_serial_number : Annotated[StrictStr, Field(..., description="The serial number of the inverter.")], start : Annotated[Optional[StrictStr], Field(description="ISO8601-datetime Start time")] = None, end : Annotated[Optional[StrictStr], Field(description="ISO8601-datetime End time")] = None, cleared : Annotated[Optional[StrictBool], Field(description="Whether 'cleared' events should be included with the data. Default is false")] = None, page : Annotated[Optional[StrictInt], Field(description="Page number to return")] = None, page_size : Annotated[Optional[StrictInt], Field(description="Number of items to return in a page. Defaults to 15")] = None, authorization : Optional[StrictStr] = None, get_events_request : Optional[GetEventsRequest] = None, **kwargs) -> GetEvents200Response:  # noqa: E501
        """Get Events  # noqa: E501

        Retrieves a list of faults that were triggered from the inverter and when they were cleared  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_events(inverter_serial_number, start, end, cleared, page, page_size, authorization, get_events_request, async_req=True)
        >>> result = thread.get()

        :param inverter_serial_number: The serial number of the inverter. (required)
        :type inverter_serial_number: str
        :param start: ISO8601-datetime Start time
        :type start: str
        :param end: ISO8601-datetime End time
        :type end: str
        :param cleared: Whether 'cleared' events should be included with the data. Default is false
        :type cleared: bool
        :param page: Page number to return
        :type page: int
        :param page_size: Number of items to return in a page. Defaults to 15
        :type page_size: int
        :param authorization: 
        :type authorization: str
        :param get_events_request:
        :type get_events_request: GetEventsRequest
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: GetEvents200Response
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the get_events_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.get_events_with_http_info(inverter_serial_number, start, end, cleared, page, page_size, authorization, get_events_request, **kwargs)  # noqa: E501

    @validate_arguments
    def get_events_with_http_info(self, inverter_serial_number : Annotated[StrictStr, Field(..., description="The serial number of the inverter.")], start : Annotated[Optional[StrictStr], Field(description="ISO8601-datetime Start time")] = None, end : Annotated[Optional[StrictStr], Field(description="ISO8601-datetime End time")] = None, cleared : Annotated[Optional[StrictBool], Field(description="Whether 'cleared' events should be included with the data. Default is false")] = None, page : Annotated[Optional[StrictInt], Field(description="Page number to return")] = None, page_size : Annotated[Optional[StrictInt], Field(description="Number of items to return in a page. Defaults to 15")] = None, authorization : Optional[StrictStr] = None, get_events_request : Optional[GetEventsRequest] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """Get Events  # noqa: E501

        Retrieves a list of faults that were triggered from the inverter and when they were cleared  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_events_with_http_info(inverter_serial_number, start, end, cleared, page, page_size, authorization, get_events_request, async_req=True)
        >>> result = thread.get()

        :param inverter_serial_number: The serial number of the inverter. (required)
        :type inverter_serial_number: str
        :param start: ISO8601-datetime Start time
        :type start: str
        :param end: ISO8601-datetime End time
        :type end: str
        :param cleared: Whether 'cleared' events should be included with the data. Default is false
        :type cleared: bool
        :param page: Page number to return
        :type page: int
        :param page_size: Number of items to return in a page. Defaults to 15
        :type page_size: int
        :param authorization: 
        :type authorization: str
        :param get_events_request:
        :type get_events_request: GetEventsRequest
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(GetEvents200Response, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'inverter_serial_number',
            'start',
            'end',
            'cleared',
            'page',
            'page_size',
            'authorization',
            'get_events_request'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_events" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['inverter_serial_number']:
            _path_params['inverter_serial_number'] = _params['inverter_serial_number']


        # process the query parameters
        _query_params = []
        if _params.get('start') is not None:  # noqa: E501
            _query_params.append(('start', _params['start']))

        if _params.get('end') is not None:  # noqa: E501
            _query_params.append(('end', _params['end']))

        if _params.get('cleared') is not None:  # noqa: E501
            _query_params.append(('cleared', _params['cleared']))

        if _params.get('page') is not None:  # noqa: E501
            _query_params.append(('page', _params['page']))

        if _params.get('page_size') is not None:  # noqa: E501
            _query_params.append(('pageSize', _params['page_size']))

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        if _params['authorization']:
            _header_params['Authorization'] = _params['authorization']

        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        if _params['get_events_request'] is not None:
            _body_params = _params['get_events_request']

        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # set the HTTP header `Content-Type`
        _content_types_list = _params.get('_content_type',
            self.api_client.select_header_content_type(
                ['application/json']))
        if _content_types_list:
                _header_params['Content-Type'] = _content_types_list

        # authentication setting
        _auth_settings = ['default']  # noqa: E501

        _response_types_map = {
            '200': "GetEvents200Response",
        }

        return self.api_client.call_api(
            '/inverter/{inverter_serial_number}/events', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def get_latest_meter_data(self, inverter_serial_number : Annotated[StrictStr, Field(..., description="The serial number of the inverter.")], authorization : Optional[StrictStr] = None, **kwargs) -> GetLatestMeterData200Response:  # noqa: E501
        """Get Latest Meter Data  # noqa: E501

        Retrieves the latest meter data from the inverter  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_latest_meter_data(inverter_serial_number, authorization, async_req=True)
        >>> result = thread.get()

        :param inverter_serial_number: The serial number of the inverter. (required)
        :type inverter_serial_number: str
        :param authorization: 
        :type authorization: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: GetLatestMeterData200Response
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the get_latest_meter_data_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.get_latest_meter_data_with_http_info(inverter_serial_number, authorization, **kwargs)  # noqa: E501

    @validate_arguments
    def get_latest_meter_data_with_http_info(self, inverter_serial_number : Annotated[StrictStr, Field(..., description="The serial number of the inverter.")], authorization : Optional[StrictStr] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """Get Latest Meter Data  # noqa: E501

        Retrieves the latest meter data from the inverter  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_latest_meter_data_with_http_info(inverter_serial_number, authorization, async_req=True)
        >>> result = thread.get()

        :param inverter_serial_number: The serial number of the inverter. (required)
        :type inverter_serial_number: str
        :param authorization: 
        :type authorization: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(GetLatestMeterData200Response, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'inverter_serial_number',
            'authorization'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_latest_meter_data" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['inverter_serial_number']:
            _path_params['inverter_serial_number'] = _params['inverter_serial_number']


        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        if _params['authorization']:
            _header_params['Authorization'] = _params['authorization']

        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['default']  # noqa: E501

        _response_types_map = {
            '200': "GetLatestMeterData200Response",
        }

        return self.api_client.call_api(
            '/inverter/{inverter_serial_number}/meter-data/latest', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def get_latest_system_data(self, inverter_serial_number : Annotated[StrictStr, Field(..., description="The serial number of the inverter.")], authorization : Optional[StrictStr] = None, **kwargs) -> GetLatestSystemData200Response:  # noqa: E501
        """Get Latest System Data  # noqa: E501

        Retrieves the latest system data from the inverter  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_latest_system_data(inverter_serial_number, authorization, async_req=True)
        >>> result = thread.get()

        :param inverter_serial_number: The serial number of the inverter. (required)
        :type inverter_serial_number: str
        :param authorization: 
        :type authorization: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: GetLatestSystemData200Response
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the get_latest_system_data_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.get_latest_system_data_with_http_info(inverter_serial_number, authorization, **kwargs)  # noqa: E501

    @validate_arguments
    def get_latest_system_data_with_http_info(self, inverter_serial_number : Annotated[StrictStr, Field(..., description="The serial number of the inverter.")], authorization : Optional[StrictStr] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """Get Latest System Data  # noqa: E501

        Retrieves the latest system data from the inverter  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_latest_system_data_with_http_info(inverter_serial_number, authorization, async_req=True)
        >>> result = thread.get()

        :param inverter_serial_number: The serial number of the inverter. (required)
        :type inverter_serial_number: str
        :param authorization: 
        :type authorization: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(GetLatestSystemData200Response, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'inverter_serial_number',
            'authorization'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_latest_system_data" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['inverter_serial_number']:
            _path_params['inverter_serial_number'] = _params['inverter_serial_number']


        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        if _params['authorization']:
            _header_params['Authorization'] = _params['authorization']

        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['default']  # noqa: E501

        _response_types_map = {
            '200': "GetLatestSystemData200Response",
        }

        return self.api_client.call_api(
            '/inverter/{inverter_serial_number}/system-data/latest', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))
