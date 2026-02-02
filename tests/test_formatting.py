import pytest
from util.formatting import express_as_percentage, express_as_dollars, get_months, get_name_of_month
# content of test_sample.py
# def inc(x):
#     return x + 1


def test_express_as_percentage():
    assert express_as_percentage(47.76) == "47.76%"

def test_express_as_dollars():
    assert express_as_dollars(52789.76) == "$52,789.76"

def test_get_months():
    the_months = get_months()
    assert len(the_months) == 12
    assert the_months[0]['mo_name'] == 'January'
    assert the_months[0]['mo_num'] == 0
    assert the_months[1]['mo_name'] == 'February'
    assert the_months[1]['mo_num'] == 1
    assert the_months[2]['mo_name'] == 'March'
    assert the_months[2]['mo_num'] == 2
    assert the_months[3]['mo_name'] == 'April'
    assert the_months[3]['mo_num'] == 3
    assert the_months[4]['mo_name'] == 'May'
    assert the_months[4]['mo_num'] == 4
    assert the_months[5]['mo_name'] == 'June'
    assert the_months[5]['mo_num'] == 5
    assert the_months[6]['mo_name'] == 'July'
    assert the_months[6]['mo_num'] == 6
    assert the_months[7]['mo_name'] == 'August'
    assert the_months[7]['mo_num'] == 7
    assert the_months[8]['mo_name'] == 'September'
    assert the_months[8]['mo_num'] == 8
    assert the_months[9]['mo_name'] == 'October'
    assert the_months[9]['mo_num'] == 9
    assert the_months[10]['mo_name'] == 'November'
    assert the_months[10]['mo_num'] == 10
    assert the_months[11]['mo_name'] == 'December'
    assert the_months[11]['mo_num'] == 11

def test_get_name_of_month():
    assert get_name_of_month(0) == 'January'
    assert get_name_of_month(1) == 'February'
    assert get_name_of_month(2) == 'March'
    assert get_name_of_month(3) == 'April'
    assert get_name_of_month(4) == 'May'
    assert get_name_of_month(5) == 'June'
    assert get_name_of_month(6) == 'July'
    assert get_name_of_month(7) == 'August'
    assert get_name_of_month(8) == 'September'
    assert get_name_of_month(9) == 'October'
    assert get_name_of_month(10) == 'November'
    assert get_name_of_month(11) == 'December'
    assert get_name_of_month(12) == 'Not a Month'
