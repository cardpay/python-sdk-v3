# coding: utf-8

"""
    CardPay REST API

    Welcome to the CardPay REST API. The CardPay API uses HTTP verbs and a REST resources endpoint structure (see more info about REST). Request and response payloads are formatted as JSON. Merchant uses API to create payments, refunds, payouts or recurrings, check or update transaction status and get information about created transactions. In API authentication process based on OAuth 2.0 standard. For recent changes see changelog section.  # noqa: E501

    OpenAPI spec version: 3.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from cardpay.api_client import ApiClient


class PaymentsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_payment(self, payment_request, **kwargs):  # noqa: E501
        """Create payment  # noqa: E501

        Endpoint for creation payments. Request example presented for Gateway mode.  # noqa: E501
        :param PaymentRequest payment_request: paymentRequest (required)
        :return: PaymentCreationResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True

        (data) = self.create_payment_with_http_info(payment_request, **kwargs)  # noqa: E501
        return data

    def create_payment_with_http_info(self, payment_request, **kwargs):  # noqa: E501
        """Create payment  # noqa: E501

        Endpoint for creation payments. Request example presented for Gateway mode.  # noqa: E501
        :param PaymentRequest payment_request: paymentRequest (required)
        :return: PaymentCreationResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['payment_request']  # noqa: E501
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_payment" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'payment_request' is set
        if ('payment_request' not in params or
                params['payment_request'] is None):
            raise ValueError("Missing the required parameter `payment_request` when calling `create_payment`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'payment_request' in params:
            body_params = params['payment_request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        return self.api_client.call_api(
            '/api/payments', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PaymentCreationResponse',  # noqa: E501
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_payment(self, payment_id, **kwargs):  # noqa: E501
        """Get payment information  # noqa: E501

        :param str payment_id: Payment ID (required)
        :return: PaymentResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True

        (data) = self.get_payment_with_http_info(payment_id, **kwargs)  # noqa: E501
        return data

    def get_payment_with_http_info(self, payment_id, **kwargs):  # noqa: E501
        """Get payment information  # noqa: E501

        :param str payment_id: Payment ID (required)
        :return: PaymentResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['payment_id']  # noqa: E501
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_payment" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'payment_id' is set
        if ('payment_id' not in params or
                params['payment_id'] is None):
            raise ValueError("Missing the required parameter `payment_id` when calling `get_payment`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'payment_id' in params:
            path_params['paymentId'] = params['payment_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        return self.api_client.call_api(
            '/api/payments/{paymentId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PaymentResponse',  # noqa: E501
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_payments(self, request_id, **kwargs):  # noqa: E501
        """Get payments information  # noqa: E501

        :param str request_id: Request ID (required)
        :param str currency: [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) currency code of transactions currency
        :param datetime end_time: Date and time up to milliseconds (in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format) when requested period ends (not inclusive), UTC time, must be less than 7 days after 'start_time', default is current time (format: yyyy-MM-dd'T'HH:mm:ss'Z')
        :param int max_count: Limit number of returned transactions (must be less than 10000, default is 1000)
        :param str merchant_order_id: Merchant order number from the merchant system
        :param str payment_method: Used payment method type name from payment methods list
        :param str sort_order: Sort based on order of results. `asc` for ascending order or `desc` for descending order (default value)
        :param datetime start_time: Date and time up to milliseconds (in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format) when requested period starts (inclusive), UTC time, default is 24 hours before 'end_time' (format: yyyy-MM-dd'T'HH:mm:ss'Z')
        :return: PaymentsList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True

        (data) = self.get_payments_with_http_info(request_id, **kwargs)  # noqa: E501
        return data

    def get_payments_with_http_info(self, request_id, **kwargs):  # noqa: E501
        """Get payments information  # noqa: E501

        :param str request_id: Request ID (required)
        :param str currency: [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) currency code of transactions currency
        :param datetime end_time: Date and time up to milliseconds (in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format) when requested period ends (not inclusive), UTC time, must be less than 7 days after 'start_time', default is current time (format: yyyy-MM-dd'T'HH:mm:ss'Z')
        :param int max_count: Limit number of returned transactions (must be less than 10000, default is 1000)
        :param str merchant_order_id: Merchant order number from the merchant system
        :param str payment_method: Used payment method type name from payment methods list
        :param str sort_order: Sort based on order of results. `asc` for ascending order or `desc` for descending order (default value)
        :param datetime start_time: Date and time up to milliseconds (in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format) when requested period starts (inclusive), UTC time, default is 24 hours before 'end_time' (format: yyyy-MM-dd'T'HH:mm:ss'Z')
        :return: PaymentsList
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['request_id', 'currency', 'end_time', 'max_count', 'merchant_order_id', 'payment_method', 'sort_order', 'start_time']  # noqa: E501
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_payments" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'request_id' is set
        if ('request_id' not in params or
                params['request_id'] is None):
            raise ValueError("Missing the required parameter `request_id` when calling `get_payments`")  # noqa: E501

        if ('request_id' in params and
                len(params['request_id']) > 50):
            raise ValueError("Invalid value for parameter `request_id` when calling `get_payments`, length must be less than or equal to `50`")  # noqa: E501
        if ('request_id' in params and
                len(params['request_id']) < 0):
            raise ValueError("Invalid value for parameter `request_id` when calling `get_payments`, length must be greater than or equal to `0`")  # noqa: E501
        if 'max_count' in params and params['max_count'] > 10000:  # noqa: E501
            raise ValueError("Invalid value for parameter `max_count` when calling `get_payments`, must be a value less than or equal to `10000`")  # noqa: E501
        if ('merchant_order_id' in params and
                len(params['merchant_order_id']) > 50):
            raise ValueError("Invalid value for parameter `merchant_order_id` when calling `get_payments`, length must be less than or equal to `50`")  # noqa: E501
        if ('merchant_order_id' in params and
                len(params['merchant_order_id']) < 0):
            raise ValueError("Invalid value for parameter `merchant_order_id` when calling `get_payments`, length must be greater than or equal to `0`")  # noqa: E501
        if ('payment_method' in params and
                len(params['payment_method']) > 100):
            raise ValueError("Invalid value for parameter `payment_method` when calling `get_payments`, length must be less than or equal to `100`")  # noqa: E501
        if ('payment_method' in params and
                len(params['payment_method']) < 0):
            raise ValueError("Invalid value for parameter `payment_method` when calling `get_payments`, length must be greater than or equal to `0`")  # noqa: E501
        if 'sort_order' in params and not re.search(r'asc|desc', params['sort_order']):  # noqa: E501
            raise ValueError("Invalid value for parameter `sort_order` when calling `get_payments`, must conform to the pattern `/asc|desc/`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'currency' in params:
            query_params.append(('currency', params['currency']))  # noqa: E501
        if 'end_time' in params:
            query_params.append(('end_time', params['end_time']))  # noqa: E501
        if 'max_count' in params:
            query_params.append(('max_count', params['max_count']))  # noqa: E501
        if 'merchant_order_id' in params:
            query_params.append(('merchant_order_id', params['merchant_order_id']))  # noqa: E501
        if 'payment_method' in params:
            query_params.append(('payment_method', params['payment_method']))  # noqa: E501
        if 'request_id' in params:
            query_params.append(('request_id', params['request_id']))  # noqa: E501
        if 'sort_order' in params:
            query_params.append(('sort_order', params['sort_order']))  # noqa: E501
        if 'start_time' in params:
            query_params.append(('start_time', params['start_time']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        return self.api_client.call_api(
            '/api/payments', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PaymentsList',  # noqa: E501
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_payment(self, payment_id, payment_patch_request, **kwargs):  # noqa: E501
        """Update payment  # noqa: E501

        :param str payment_id: Payment ID (required)
        :param PaymentPatchRequest payment_patch_request: paymentPatchRequest (required)
        :return: PaymentUpdateResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True

        (data) = self.update_payment_with_http_info(payment_id, payment_patch_request, **kwargs)  # noqa: E501
        return data

    def update_payment_with_http_info(self, payment_id, payment_patch_request, **kwargs):  # noqa: E501
        """Update payment  # noqa: E501

        :param str payment_id: Payment ID (required)
        :param PaymentPatchRequest payment_patch_request: paymentPatchRequest (required)
        :return: PaymentUpdateResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['payment_id', 'payment_patch_request']  # noqa: E501
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_payment" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'payment_id' is set
        if ('payment_id' not in params or
                params['payment_id'] is None):
            raise ValueError("Missing the required parameter `payment_id` when calling `update_payment`")  # noqa: E501
        # verify the required parameter 'payment_patch_request' is set
        if ('payment_patch_request' not in params or
                params['payment_patch_request'] is None):
            raise ValueError("Missing the required parameter `payment_patch_request` when calling `update_payment`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'payment_id' in params:
            path_params['paymentId'] = params['payment_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'payment_patch_request' in params:
            body_params = params['payment_patch_request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        return self.api_client.call_api(
            '/api/payments/{paymentId}', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PaymentUpdateResponse',  # noqa: E501
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
