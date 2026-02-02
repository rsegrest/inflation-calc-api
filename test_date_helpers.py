import pytest
from util.date_helpers import get_current_year_int, get_current_year_string

def test_get_current_year_int():
    assert get_current_year_int() == 2026

def test_get_current_year_string():
    assert get_current_year_string() == "2026"