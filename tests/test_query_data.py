import pytest
from data.cpidata import CPI_DATA
from util.query_data import get_historical_cpi, get_latest_month_with_data, get_present_cpi

def newest_year_with_figures():
    years = [
        int(year) for year, figures in CPI_DATA.items()
        if any(figure is not None for figure in figures)
    ]
    return max(years)

def newest_month_with_a_figure(year):
    return max(month for month, figure in enumerate(CPI_DATA[str(year)]) if figure is not None)

def test_get_historical_cpi():
    assert get_historical_cpi(2022, 0) == 281.148

def test_get_latest_month_with_data():
    assert get_latest_month_with_data(0, 2022) == {'year':2022,'month':0}

def test_get_latest_month_with_data_walks_back_to_a_month_that_has_a_figure():
    # December is often published late, so asking for month 11 must walk back.
    newest_year = newest_year_with_figures()
    assert get_latest_month_with_data(11, newest_year) == {
        'year': newest_year,
        'month': newest_month_with_a_figure(newest_year),
    }

def test_get_present_cpi_reports_the_newest_published_figure():
    # Starting the search at January used to make this report January's figure.
    newest_year = newest_year_with_figures()
    assert get_present_cpi() == CPI_DATA[str(newest_year)][newest_month_with_a_figure(newest_year)]
