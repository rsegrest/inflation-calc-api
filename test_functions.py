import pytest
from util.formulas import calculate_inflation_rate, calculate_loss_percentage
# content of test_sample.py
# def inc(x):
#     return x + 1

def test_calculate_inflation_rate():
    assert calculate_inflation_rate(50, 100) == 100

def test_calculate_loss_percentage():
    assert calculate_loss_percentage(50, 100) == 50

# def test_get_present_cpi():
#     assert get_present_cpi() == 281.148