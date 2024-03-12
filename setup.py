# coding: utf-8

import os
from codecs import open
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
os.chdir(here)

with open(os.path.join(here, "README.md"), "r", encoding="utf-8") as fp:
    long_description = fp.read()

setup(
    name="cardpay",
    version="3.65.15",
    description="Unlimit APIv3 Python SDK",
    author_email="",
    url="https://github.com/cardpay/python-sdk-v3.git",
    license="MIT",
    keywords=["cardpay", "APIv3", "CardPay REST API"],
    install_requires=[
        "certifi>=2019.11.28",
        "python-dateutil>=2.8.0",
        "six>=1.14.0",
        "urllib3>=1.25.8"
    ],
    packages=find_packages(exclude=["tests", "tests.*"]),
    include_package_data=True,
    long_description=long_description,
    long_description_content_type="text/markdown",
    python_requires=">=3",
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    project_urls={
        "Documentation": "https://integration.unlimit.com/",
        "Source Code": "https://github.com/cardpay/python-sdk-v3",
    }
)
