from src.util.formulas import calculate_timespan_months
from src.util.formulas import calculate_inflation_rate
from src.util.query_data import get_historical_cpi
from src.util.formulas import calculate_loss_percentage
from src.util.formulas import adjust_figure_with_inflation
from src.util.query_data import get_latest_month_with_data
from src.util.date_helpers import get_current_year_int, get_current_month_int
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

# @app.route('/cpi/<from_year>/<to_year>/<from_month>/<to_month>')
@app.route('/cpi/<starting_amount>/<from_year>', defaults={'to_year': get_current_year_int(), 'from_month': 0, 'to_month': get_current_month_int()})
@app.route('/cpi/<starting_amount>/<from_year>/<to_year>', defaults={'from_month': 0, 'to_month': 0})
@app.route('/cpi/<starting_amount>/<from_year>/<to_year>/<from_month>', defaults={'to_month': 0})
@app.route('/cpi/<starting_amount>/<from_year>/<to_year>/<from_month>/<to_month>')
def cpi(starting_amount=1000, from_year=2022, to_year=2025, from_month=0, to_month=0):
    starting_amount = int(starting_amount)
    from_year = int(from_year)
    to_year = int(to_year)
    from_month = int(from_month)
    to_month = int(to_month)
    if from_year > to_year:
        from_year = to_year
    if from_month > 11:
        from_month = 11
    if to_month > 11:
        to_month = 11
    if from_year < 1913:
        from_year = 1913
    if to_year < 1913:
        to_year = 1913
    # return {
    #     'starting_amount': starting_amount,
    #     'from_year': from_year,
    #     'to_year': to_year,
    #     'from_month': from_month,
    #     'to_month': to_month,
    # }
    latest_data = get_latest_month_with_data(to_month, to_year)
    now_dollars = adjust_figure_with_inflation(starting_amount, get_historical_cpi(from_year, from_month), get_historical_cpi(to_year, to_month))
    lost_value = calculate_loss_percentage(get_historical_cpi(from_year, from_month), get_historical_cpi(to_year, to_month))
    historical_start_cpi = get_historical_cpi(from_year, from_month)
    historical_end_cpi = get_historical_cpi(to_year, to_month)
    inflation_rate = calculate_inflation_rate(historical_start_cpi, historical_end_cpi)
    time_period_in_months = calculate_timespan_months(from_year, from_month, to_year, to_month)

    return {
        'starting_amount': starting_amount,
        'start_year': from_year,
        'end_year': to_year,
        'start_month': from_month,
        'end_month': to_month,
        'latest_data_month': latest_data['month'],
        'latest_data_year': latest_data['year'],
        'lost_value': lost_value,
        'now_dollars': now_dollars,
        'historical_start_cpi': historical_start_cpi,
        'historical_end_cpi': historical_end_cpi,
        'inflation_rate': inflation_rate,
        'time_period_in_months': time_period_in_months,
    }

if __name__ == "__main__":
    app.run(debug=True)


#     const [timePeriodInMonths, setTimePeriodInMonths] = React.useState(calculateTimespanMonths(startYear, startZeroBasedMonth, endYear, endZeroBasedMonth));
#     const [lostValue, setLostValue] = React.useState(calculateLossPercentage(historicalStartCpi, historicalEndCpi));

