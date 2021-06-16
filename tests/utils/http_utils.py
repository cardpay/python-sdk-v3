# coding: utf-8
import os

import urllib3
from cardpay.api_client import is_no_proxy_case
from config import create_logger

logger = create_logger(__name__)

proxy = os.getenv('HTTPS_PROXY', os.getenv('HTTP_PROXY'))

if proxy:
    http = urllib3.ProxyManager(proxy)
    no_proxy_http = urllib3.PoolManager()
else:
    http = urllib3.PoolManager()
    no_proxy_http = urllib3.PoolManager()


def do_get(url):
    if is_no_proxy_case(url):
        r = no_proxy_http.request('GET', url)
    else:
        r = http.request('GET', url)

    logger.info("%s %s", r.status, r._request_url)
