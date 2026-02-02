import json
from data.cpidata import CPI_DATA

# FORMULAS:
# calculateCompoundInterest: CI = P x (1 + r/n)^nt
# futureValueOfASeries : FV = PMT x (((1 + r/n)^nt - 1) / (r/n))
# totalAmount : T = CI + FV

# P = Principal investment amount
# PMT = Additional payment per period
# r = Annual rate of interest
# n = Compound frequency per year
# t = Investment time in years

def calculate_inflation_rate(start_cpi, end_cpi):
    return round(((end_cpi - start_cpi) / start_cpi) * 10000)/100

def calculate_loss_percentage(start_cpi, end_cpi):
    return (round((((end_cpi-start_cpi)/end_cpi)*10000)))/100

def adjust_figure_with_inflation(amount, from_figure, to_figure):
    inflated_figure = (amount / from_figure) * to_figure
    return round(inflated_figure)

def calculate_timespan_months(start_year, start_month, end_year, end_month):
    total_months = 0
    total_months = end_month - start_month
    total_months += ((end_year - start_year) * 12)
    return total_months

def lost_value_over_time(from_year, to_year, from_month = 0, to_month = 0):
    value_array = []
    first_cpi_value = get_historical_cpi(from_year, from_month)
    for i in range(from_year, to_year + 1):
        this_cpi = get_historical_cpi(i, to_month)
        value_array.append({
            year: i,
            cpi: this_cpi,
            value: (first_cpi_value / this_cpi),
        })
    return value_array

# fromFigure = getHistoricalCpi(2019,2);
# toFigure = getHistoricalCpi(2022,0);
# inflationRate = calculateInflationRate(fromFigure, toFigure);