import pytest
from util.formulas import calculate_inflation_rate, calculate_loss_percentage, adjust_figure_with_inflation, calculate_timespan_months, lost_value_over_time
# content of test_sample.py
# def inc(x):
#     return x + 1

def test_calculate_inflation_rate():
    assert calculate_inflation_rate(50, 100) == 100

def test_calculate_loss_percentage():
    assert calculate_loss_percentage(50, 100) == 50

def test_adjust_figure_with_inflation():
    # amount, from_figure, to_figure
    assert adjust_figure_with_inflation(50, 100, 200) == 100

def test_calculate_timespan_months():
    # from_year, from_month, to_year, to_month
    assert calculate_timespan_months(2022, 0, 2022, 0) == 0
    assert calculate_timespan_months(2022, 0, 2022, 1) == 1
    assert calculate_timespan_months(2022, 0, 2023, 0) == 12
    assert calculate_timespan_months(2022, 0, 2023, 1) == 13

def test_lost_value_over_time():
    # from_year, to_year, from_month = 0, to_month = 0
    assert lost_value_over_time(2022, 2022, 0, 0) == [{'year':2022,'cpi':281.148,'value':1.0}]