import pytest
from util.formulas import calculate_inflation_rate, calculate_loss_percentage, adjust_figure_with_inflation, calculate_timespan_months, lost_value_over_time, monthly_value_series
from util.query_data import get_historical_cpi
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

def test_monthly_value_series_covers_every_month_between_the_dates():
    # from_year, from_month, to_year, to_month
    series = monthly_value_series(2022, 10, 2023, 1)
    assert [(point['year'], point['month']) for point in series] == [
        (2022, 10), (2022, 11), (2023, 0), (2023, 1)
    ]

def test_monthly_value_series_starts_at_one_and_indexes_each_month_to_the_start():
    series = monthly_value_series(2022, 10, 2023, 1)
    start_cpi = get_historical_cpi(2022, 10)
    assert series[0]['value'] == 1.0
    for point in series:
        assert point['cpi'] == get_historical_cpi(point['year'], point['month'])
        assert point['value'] == pytest.approx(start_cpi / point['cpi'])

def test_monthly_value_series_of_a_single_month_is_one_point():
    assert monthly_value_series(2022, 0, 2022, 0) == [
        {'year': 2022, 'month': 0, 'cpi': 281.148, 'value': 1.0}
    ]