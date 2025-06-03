# Unlimit APIv3 Python SDK

You can sign up for a Unlimit account at https://www.unlimit.com

## Getting Started

Please follow the [installation](#installation) instruction and take a look at [usage examples](tests).


## Requirements

Python 3+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/cardpay/python-sdk-v3.git --upgrade
```
or

```sh
pip install 'cardpay>=4.2.13' --upgrade
```

Then import the package:
```python
from cardpay import *
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```

Then import the package:
```python
from cardpay import *
```

## Usage examples

Example for Auth
```python
import os
from cardpay import *

CARDPAY_API_URL = os.getenv('CARDPAY_API_URL', 'https://sandbox.cardpay.com')
GATEWAY_TERMINAL_CODE = os.getenv('GATEWAY_TERMINAL_CODE', '00000')
GATEWAY_PASSWORD = os.getenv('GATEWAY_PASSWORD', 'password')

auth = AuthApi(ApiClient(baseUrl=CARDPAY_API_URL))

result = auth.obtain_tokens(
    grant_type="password",
    terminal_code=GATEWAY_TERMINAL_CODE,
    password=GATEWAY_PASSWORD
)

access_token = result.access_token
refresh_token = result.refresh_token

print('access_token:',access_token)
print('refresh_token:', refresh_token)
```

Example for payment
```python
import os
from cardpay import *

CARDPAY_API_URL = os.getenv('CARDPAY_API_URL', 'https://sandbox.cardpay.com')
GATEWAY_TERMINAL_CODE = os.getenv('GATEWAY_TERMINAL_CODE', '00000')
GATEWAY_PASSWORD = os.getenv('GATEWAY_PASSWORD', 'password')

config = Configuration(
    base_url=CARDPAY_API_URL,
    terminal_code=GATEWAY_TERMINAL_CODE,
    password=GATEWAY_PASSWORD
)
payments = PaymentsApi(ApiClient(config))

request = PaymentRequest(
    request=ApiClient.uuid_request(),
    merchant_order=PaymentRequestMerchantOrder(
        id='merchant order id',
        description='merchant description'
    ),
    card_account=PaymentRequestCardAccount(
        card=PaymentRequestCard(
            pan='card pan',
            holder='cardholder in Upper Case',
            expiration='expiration date',
            security_code='123'
        ),
        billing_address = BillingAddress(
            country='USA',
            state='NY',
            zip='10001',
            city='New York',
            addr_line_1='address1',
            addr_line_2='address2'
        )
    ),
    customer=PaymentRequestCustomer(
        id='000',
        full_name='full name',
        birth_date='birth date',
        email='e-mail',
        phone='+###########',
        work_phone='+###########',
        home_phone='+###########',
        locale='en'
    ),
    payment_method="BANKCARD",
    payment_data=PaymentRequestPaymentData(
        currency="currency",
        amount=1.23
    )
)

create_payment_response = payments.create_payment(request)
payment_id = create_payment_response.payment_data.id
redirect_url = create_payment_response.redirect_url

print("payment_id:", payment_id);
print("redirect_url:", redirect_url);

payment_response = payments.get_payment(payment_id)
print('payment_response:', payment_response)
print('payment_status:', payment_response.payment_data.status)
```


## Proxy usage

The SDK will automatically use a proxy if the `HTTPS_PROXY` or `HTTP_PROXY` environment variable is set.

If the `NO_PROXY` env variable is set, the SDK won't use the proxy for hosts from this variable. The format of
`NO_PROXY`: comma separated domain names (e.g. "cardpay.com,.example.com").
