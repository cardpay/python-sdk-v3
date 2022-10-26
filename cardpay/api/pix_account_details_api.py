# coding: utf-8

"""
    CardPay REST API

    Welcome to the CardPay REST API. The CardPay API uses HTTP verbs and a [REST](https://en.wikipedia.org/wiki/Representational_state_transfer) resources endpoint structure (see more info about REST). Request and response payloads are formatted as JSON. Merchant uses API to create payments, refunds, payouts or recurrings, check or update transaction status and get information about created transactions. In API authentication process based on [OAuth 2.0](https://oauth.net/2/) standard. For recent changes see changelog section.  # noqa: E501

    OpenAPI spec version: 3.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from cardpay.api_client import ApiClient


class PixAccountDetailsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def account_details(self, details_request, **kwargs):  # noqa: E501
        """Get pix account details  # noqa: E501

        :param PixAccountDetailsRequest details_request: detailsRequest (required)
        :return: PixAccountDetailsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True

        (data) = self.account_details_with_http_info(
            details_request, **kwargs
        )  # noqa: E501
        return data

    def account_details_with_http_info(self, details_request, **kwargs):  # noqa: E501
        """Get pix account details  # noqa: E501

        :param PixAccountDetailsRequest details_request: detailsRequest (required)
        :return: PixAccountDetailsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["details_request"]  # noqa: E501
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method account_details" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'details_request' is set
        if "details_request" not in params or params["details_request"] is None:
            raise ValueError(
                "Missing the required parameter `details_request` when calling `account_details`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if "details_request" in params:
            body_params = params["details_request"]
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )  # noqa: E501
        # HTTP header `Content-Type`
        header_params[
            "Content-Type"
        ] = self.api_client.select_header_content_type(  # noqa: E501
            ["application/json"]
        )  # noqa: E501

        return self.api_client.call_api(
            "/api/account_details/pix",
            "POST",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="PixAccountDetailsResponse",  # noqa: E501
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )
