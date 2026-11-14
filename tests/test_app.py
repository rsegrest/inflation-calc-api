import pytest
from app import app
from util.date_helpers import get_current_month_int, get_current_year_int
from util.query_data import get_historical_cpi, get_latest_month_with_data

@pytest.fixture
def client():
    return app.test_client()

def test_cpi_data(client):
    response = client.get('/cpi-data')
    assert response.status_code == 200
    data = response.get_json()
    assert data['2022'][0] == 281.148

def test_cpi_returns_the_aggregate_figures_for_a_closed_date_range(client):
    response = client.get('/cpi?starting_amount=1000&from_year=2000&from_month=0&to_year=2022&to_month=0')
    assert response.status_code == 200
    data = response.get_json()
    assert data['historical_start_cpi'] == 168.8
    assert data['historical_end_cpi'] == 281.148
    assert data['now_dollars'] == 1666
    assert data['inflation_rate'] == 66.56
    assert data['lost_value'] == 39.96
    assert data['time_period_in_months'] == 264

def test_cpi_returns_a_monthly_series_spanning_the_range(client):
    response = client.get('/cpi?starting_amount=1000&from_year=2022&from_month=0&to_year=2022&to_month=2')
    assert response.status_code == 200
    data = response.get_json()
    assert [(point['year'], point['month']) for point in data['series']] == [
        (2022, 0), (2022, 1), (2022, 2)
    ]
    assert data['series'][0]['value'] == 1.0
    assert [point['cpi'] for point in data['series']] == [281.148, 283.716, 287.504]
    assert len(data['series']) == data['time_period_in_months'] + 1

def test_cpi_series_honours_an_explicit_end_date_instead_of_latest_data(client):
    response = client.get('/cpi?starting_amount=1000&from_year=2021&from_month=0&to_year=2021&to_month=0')
    assert response.status_code == 200
    data = response.get_json()
    assert (data['end_year'], data['end_month']) == (2021, 0)
    assert len(data['series']) == 1

def test_latest_data_reports_the_most_recent_month_holding_a_cpi_figure(client):
    response = client.get('/latest-data')
    assert response.status_code == 200
    data = response.get_json()
    latest = get_latest_month_with_data(get_current_month_int(), get_current_year_int())
    assert data['year'] == latest['year']
    assert data['month'] == latest['month']
    assert get_historical_cpi(data['year'], data['month']) is not None
