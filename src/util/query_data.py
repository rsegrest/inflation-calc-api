import json
from data.cpidata import CPI_DATA
from util.date_helpers import get_current_year_int

def get_historical_cpi(year, month):
    cpi_data_string = json.dumps(CPI_DATA)
    cpi_data = json.loads(cpi_data_string)
    cpi_year_data_array = cpi_data[str(year)]
    cpi_month_data = cpi_year_data_array[month]
    return cpi_month_data

def get_latest_month_with_data(current_month, year):
    latest_month = current_month
    latest_year = year
    while (get_historical_cpi(latest_year,latest_month) == None):
        latest_month -= 1
        if (latest_month < 0):
            latest_year -= 1
            latest_month = 11
    return {'year':latest_year,'month':latest_month}

def get_present_cpi():
    current_month = 0
    latest_date_with_data = get_latest_month_with_data(current_month, get_current_year_int())
    return get_historical_cpi(latest_date_with_data['year'], latest_date_with_data['month'])
