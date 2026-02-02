import pytest
from util.formatting import express_as_percentage, express_as_dollars
# content of test_sample.py
# def inc(x):
#     return x + 1


def test_express_as_percentage():
    assert express_as_percentage(47.76) == "47.76%"

def test_express_as_dollars():
    assert express_as_dollars(52789.76) == "$52,789.76"
