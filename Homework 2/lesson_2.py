import string
from random import randint, choice, shuffle
import pandas as pd
from flask import Flask

app = Flask(__name__)


@app.route("/generate_password")
def generate_password() -> str:
    """Function used to generate a password which:
    1. Will be 10 to 20 characters long (random length)
    2. Will contain at least one lowercase, uppercase, special characters and a digit
    3. Will fill out any spaces left with random characters from the list above"""

    pass_length = randint(10, 20)
    str_lower: str = string.ascii_letters[:26]
    str_upper: str = string.ascii_letters[26:]
    numbers: str = "0123456789"
    special: str = "!@#$%^&*()+"
    requirements = (str_lower, str_upper, numbers, special)

    pass_list = [choice(req) for req in requirements]

    while len(pass_list) < pass_length:
        pass_list.append(choice(choice(requirements)))

    shuffle(pass_list)
    password = "".join(pass_list)
    return password


@app.route("/calculate_average")
def calculate_average(path: str = "hw.csv") -> str:
    """Used to calculate the average height and weight of the students in the csv file"""

    df = pd.read_csv(path)
    mean_height = round(df[" Height(Inches)"].mean(), 2)
    mean_weight = round(df[" Weight(Pounds)"].mean(), 2)
    msg = f"""Mean height: {mean_height} in.\nMean weight: {mean_weight} lbs."""
    return msg


app.run(port=5001, debug=True)
