# coding: utf-8
import logging
import os

CARDPAY_API_URL = os.getenv('CARDPAY_API_URL', 'https://sandbox.cardpay.com')

TERMINAL_CURRENCY = os.getenv('TERMINAL_CURRENCY', 'USD')

PAYMENTPAGE_TERMINAL_CODE = os.getenv('PAYMENTPAGE_TERMINAL_CODE', '18397')
PAYMENTPAGE_PASSWORD = os.getenv('PAYMENTPAGE_PASSWORD', 'FpK2cy143POj')

GATEWAY_TERMINAL_CODE = os.getenv('GATEWAY_TERMINAL_CODE', '18833')
GATEWAY_PASSWORD = os.getenv('GATEWAY_PASSWORD', 'pzQf529Wa0AV')

GATEWAY_POSTPONED_TERMINAL_CODE = os.getenv("GATEWAY_POSTPONED_TERMINAL_CODE", "18399")
GATEWAY_POSTPONED_PASSWORD = os.getenv("GATEWAY_POSTPONED_PASSWORD", "jehE149L7bHU")

EMAILS_DOMAIN = os.getenv("EMAILS_DOMAIN", "mailinator.com")

DEBUG_MODE = bool(os.getenv('DEBUG_MODE', ''))

SUCCESS_URL = 'https://httpbin.org/get?result=success'
DECLINE_URL = 'https://httpbin.org/get?result=decline'
CANCEL_URL = 'https://httpbin.org/get?result=cancel'
INPROCESS_URL = 'https://httpbin.org/get?result=inprocess'

if DEBUG_MODE:
    logging.basicConfig(format='%(asctime)s %(message)s', level=logging.INFO)


def create_logger(name):
    logger = logging.getLogger(name)
    return logger
