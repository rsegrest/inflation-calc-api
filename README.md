# inflation-calc-api

This is a Python-Flask API that, given a start date and a starting amount, and optionally an end date, will return the following calculations:

* Total rate of inflation there has been during the timespan
* How much value the starting amount of money has lost during that time
* How much the original amount would buy then, in today's dollars
* The CPI figure from the start and end dates

If no end date is given, the API will make calculations based on the latest available data.

## Installation

Create a virtual environment, install the dependencies from requirements.txt, and then run the Flask server.

### Linux / MacOS
```bash
python -m pip venv {name_of_venv}
. ./{name_of_venv}/bin/activate
pip install -r requirements.txt
python ./src/app.py
```
### Windows Powershell
```bash
python -m pip venv {name_of_venv}
.\{name_of_venv}\bin\Activate.ps1
pip install -r requirements.txt
python ./src/app.py
```

## Docker Installation

```bash
docker build -t inflation-calc-api .
docker run -p 5000:5000 inflation-calc-api
```

## Usage

```text
http://127.0.0.1:5000/cpi?starting_amount=10000&from_month=0&from_year=2019&to_month=2&to_year=2026
```

If no end date is given, or the requested end month holds no CPI figure yet, the
calculation is made against the latest month with data. The response reports the
range actually used (`start_year`, `start_month`, `end_year`, `end_month`) plus
`latest_data_year` / `latest_data_month`.

This endpoint is the single source of truth for the GUI: it returns every figure
the front end displays, so no client needs its own inflation arithmetic.

| Field | Meaning |
| --- | --- |
| `now_dollars` | What the starting amount is worth at the end of the range |
| `inflation_rate` | Total inflation across the range, as a percentage |
| `lost_value` | Share of purchasing power lost, as a percentage |
| `historical_start_cpi` / `historical_end_cpi` | CPI figures at each end |
| `time_period_in_months` | Length of the range in months |
| `series` | One entry per month from start to end: `{year, month, cpi, value}`, where `value` is what one dollar of the start month is worth that month (start month is `1.0`) |

### Endpoints

| Endpoint | Returns |
| --- | --- |
| `GET /` | Usage note |
| `GET /latest-data` | `{year, month}` for the newest month holding a CPI figure |
| `GET /cpi` | The figures and monthly series for a starting amount and date range |
| `GET /cpi-data` | The full CPI table by year |
