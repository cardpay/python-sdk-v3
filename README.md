# Unlimint APIv3 Python SDK

You can sign up for a Unlimint account at https://www.unlimint.com.

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
pip install 'cardpay>=3.0.5' --upgrade
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

## Proxy usage

The SDK will automatically use a proxy if the `HTTPS_PROXY` or `HTTP_PROXY` environment variable is set.

If the `NO_PROXY` env variable is set, the SDK won't use the proxy for hosts from this variable. The format of
`NO_PROXY`: comma separated domain names (e.g. "cardpay.com,.example.com").
