from datetime import datetime
from util.formatting import get_name_of_month

def get_current_year_int():
    return int(get_current_year_string())

def get_current_year_string():
    return str(datetime.now().year)

def get_current_month_int():
    return int((datetime.now().month-1))

def get_current_month_string():
    return get_name_of_month(get_current_month_int())

# TODO: is this needed?
def get_year_range():
    year_array = []
    current_year = get_current_year_int()
    for i in range(current_year, 1913, -1):
        year_array.append(i)
    return year_array
