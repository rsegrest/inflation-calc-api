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
docker run -p 5050:5050 inflation-calc-api
```

## Usage

```text
http://127.0.0.1:5050/cpi?starting_amount=10000&from_month=0&from_year=2019&to_month=2&to_year=2026
```
