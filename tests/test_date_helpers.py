from datetime import datetime
from util.date_helpers import get_current_year_int, get_current_year_string, get_current_month_int, get_current_month_string, get_year_range

# These read the wall clock, so they assert the relationship to it instead of a
# snapshot of one month -- hard-coding "February" is what made them fail.
EXPECTED_MONTH_NAMES = [
    'January', 'February', 'March', 'April', 'May', 'June',
    'July', 'August', 'September', 'October', 'November', 'December',
]
EARLIEST_YEAR = 1914

def test_get_current_year_int():
    assert get_current_year_int() == datetime.now().year

def test_get_current_year_string():
    assert get_current_year_string() == str(datetime.now().year)

def test_get_current_month_int_is_zero_based():
    assert get_current_month_int() == datetime.now().month - 1

def test_get_current_month_string():
    assert get_current_month_string() == EXPECTED_MONTH_NAMES[datetime.now().month - 1]

def test_get_year_range_runs_from_this_year_back_to_the_earliest():
    assert get_year_range() == list(range(datetime.now().year, EARLIEST_YEAR - 1, -1))
