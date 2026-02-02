from datetime import datetime

def get_current_year_int():
    return int(get_current_year_string())

def get_current_year_string():
    return str(datetime.now().year)

def get_year_range():
    year_array = []
    current_year = get_current_year_int()
    for i in range(current_year, 1913, -1):
        year_array.append(i)
    return year_array