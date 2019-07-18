# coding: utf-8

import urllib3
from config import create_logger

logger = create_logger(__name__)

http = urllib3.PoolManager()


def do_get(url):
    r = http.request('GET', url)
    logger.info("%s %s", r.status, r._request_url)
