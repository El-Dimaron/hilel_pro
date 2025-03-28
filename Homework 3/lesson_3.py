import csv
import pandas as pd
from flask import Flask
from faker import Faker
from webargs.flaskparser import use_kwargs
from validator import generate_students_validator, get_bitcoin_value_value_validator
from http import HTTPStatus
import httpx

app = Flask(__name__)


@app.route('/generate_students')
@use_kwargs(generate_students_validator, location="query")
def generate_students(count, country):
    """Function is used to generate a list of students with random attributes for the provided length of 'count'."""
    try:
        student_instance = Faker(country)
    except AttributeError:
        return f"The country attribute '{country}' is not correct. Please check the code and try again."

    csv_file_name = "students.csv"

    with open(csv_file_name, "w") as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(("First Name", "Last Name", "Email", "Password", "Date of Birth"))
        for student in range(count):
            csv_writer.writerow((student_instance.first_name(),
                                 student_instance.last_name(),
                                 student_instance.email(),
                                 student_instance.password(),
                                 student_instance.date_of_birth(minimum_age=18, maximum_age=60)))

    df = pd.read_csv(csv_file_name)
    return pd.DataFrame(df).to_html(index=False, justify="center")


# http://127.0.0.1:5001/generate_students?count=100


@app.route('/get_bitcoin_value')
@use_kwargs(get_bitcoin_value_value_validator, location="query")
def get_bitcoin_value(currency, count):
    """Function is used to check the value of the bitcoin for the provided currency and amount.
    Note: works with basic non-crypto currencies (e.g. USD, UAH, GBP etc.)."""

    url_rate = f"https://bitpay.com/api/rates/{currency.lower()}"
    response_currency_rate = httpx.get(url_rate)

    if response_currency_rate.status_code != HTTPStatus.OK:
        return f"Error: something went wrong with {url_rate}."

    bitcoin_value = response_currency_rate.json().get("rate") * count

    url_currencies = "https://bitpay.com/currencies"
    response_currencies = httpx.get(url_currencies)
    currencies_symbols_dict = response_currencies.json()

    symbol = None
    for dictionary in currencies_symbols_dict["data"]:
        if dictionary.get("code") == currency:
            symbol = dictionary["symbol"]
            break

    if not symbol:
        return f"Error: currency code {currency} is not in the list of supported currencies. Please check the code."

    return f"The value of {count} bitcoin(s): {bitcoin_value}{symbol}"


# http://127.0.0.1:5001/get_bitcoin_value

app.run(port=5001, debug=True)
