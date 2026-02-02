import pytest
from util.query_data import get_historical_cpi, get_latest_month_with_data, get_present_cpi

def test_get_historical_cpi():
    assert get_historical_cpi(2022, 0) == 281.148

def test_get_latest_month_with_data():
    assert get_latest_month_with_data(0, 2022) == {'year':2022,'month':0}

def test_get_present_cpi():
    assert get_present_cpi() == 324.054