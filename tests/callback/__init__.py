# coding: utf-8

from __future__ import absolute_import
import os

here = os.path.abspath(os.path.dirname(__file__))
os.chdir(here)


def read_file(filename):
    with open(os.path.join(here, filename), "r") as fp:
        result = fp.read()
    return result
