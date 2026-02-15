from flask import Flask, jsonify, request
from flask_cors import CORS

from util.formulas import calculate_timespan_months
from util.formulas import calculate_inflation_rate
from util.query_data import get_historical_cpi
from util.formulas import calculate_loss_percentage
from util.formulas import adjust_figure_with_inflation
from util.query_data import get_latest_month_with_data
from util.date_helpers import get_current_year_int, get_current_month_int

app = Flask(__name__)
CORS(app)

@app.route("/")
def usage():
    return """
    <p>Inflation Calculator API</p><p>Use the /cpi endpoint to calculate the inflation-adjusted value of a given amount of money.</p><p>Example: <a href="/cpi?starting_amount=1000&from_year=2000&from_month=1&to_year=2025&to_month=1">/cpi?starting_amount=1000&from_year=2000&from_month=1&to_year=2025&to_month=1</a></p>
    """

@app.route('/cpi', methods=['GET', 'POST'])
def cpi():
    if request.method == 'POST':
        data = request.get_json()
        starting_amount = data.get('starting_amount')
        from_year = data.get('from_year')
        to_year = data.get('to_year')
        from_month = data.get('from_month')
        to_month = data.get('to_month')
    else:
        starting_amount = request.args.get('starting_amount')
        from_year = request.args.get('from_year')
        to_year = request.args.get('to_year')
        from_month = request.args.get('from_month')
        to_month = request.args.get('to_month')

    if any(v is None for v in [starting_amount, from_year, to_year, from_month, to_month]):
        return jsonify(error="Missing required arguments"), 400

    try:
        starting_amount = float(starting_amount)
        from_year = int(from_year)
        to_year = int(to_year)
        from_month = int(from_month)
        to_month = int(to_month)
    except ValueError:
        return jsonify(error="Arguments must be numbers"), 400
    if from_year < 1913:
        from_year = 1913
    if to_year < 1913:
        to_year = 1913
    latest_data = get_latest_month_with_data(to_month, to_year)
    from_cpi = get_historical_cpi(from_year, from_month)
    to_month = latest_data['month']
    to_year = latest_data['year']
    to_cpi = get_historical_cpi(to_year, to_month)
    now_dollars = adjust_figure_with_inflation(starting_amount, from_cpi, to_cpi)
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
    return 'None'

def main():
    app.run(debug=True, port=5000)

if __name__ == "__main__":
    main()
