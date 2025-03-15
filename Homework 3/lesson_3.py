import csv
import pandas as pd
from flask import Flask
from faker import Faker
from webargs.flaskparser import use_kwargs
from validator import generate_students_validator, get_bitcoin_value_value_validator
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
    """Function is used to check the value of the bitcoin for the provided currency and amount."""

    url_rates = "https://bitpay.com/api/rates"
    response_rates = httpx.get(url_rates)

    rates_dict = response_rates.json()

    for dictionary in rates_dict:
        if dictionary.get("code") == currency:
            bitcoin_value = dictionary["rate"] * count
            break

    url_currencies = "https://test.bitpay.com/currencies"
    response_currencies = httpx.get(url_currencies)

    currencies_symbols_dict = response_currencies.json()

    for dictionary in currencies_symbols_dict["data"]:
        if dictionary.get("code") == currency:
            symbol = dictionary["symbol"]
            break
        else:
            return f"Error: currency code {currency} is not in the list of supported currencies. Please check the code."

    return f"The value of {count} bitcoin(s): {bitcoin_value}{symbol}"


# http://127.0.0.1:5001/generate_students?currency=UAH&count=10

app.run(port=5001, debug=True)
