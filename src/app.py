from src.util.date_helpers import get_current_year_int, get_current_month_int
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

# @app.route('/cpi/<from_year>/<to_year>/<from_month>/<to_month>')
@app.route('/cpi/<from_year>', defaults={'to_year': get_current_year_int(), 'from_month': 0, 'to_month': get_current_month_int()})
@app.route('/cpi/<from_year>/<to_year>', defaults={'from_month': 0, 'to_month': 0})
@app.route('/cpi/<from_year>/<to_year>/<from_month>', defaults={'to_month': 0})
@app.route('/cpi/<from_year>/<to_year>/<from_month>/<to_month>')
def cpi(from_year=2022, to_year=2025, from_month=0, to_month=0):
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
    return f'from_year: {from_year} to_year: {to_year} from_month: {from_month} to_month: {to_month}'

if __name__ == "__main__":
    app.run(debug=True)
