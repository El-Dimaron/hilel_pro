from http import HTTPStatus
from flask import Flask, jsonify
from webargs import fields
from webargs.flaskparser import use_kwargs
from database_handler import execute_query, query

app = Flask(__name__)


@app.errorhandler(HTTPStatus.UNPROCESSABLE_ENTITY)
def error_handler(error):
    headers = error.data.get("headers", None)
    message = error.data.get("message", ["Please enter a valid genre name in a text format"])

    if headers:
        return jsonify({"errors": message}, error.data, headers)

    return jsonify({"errors": message}, error.code)


@app.route("/stats-by-city")
@use_kwargs({"style": fields.Str(required=True)}, location='query')
def stats_by_city(style: str) -> str:
    """Function receives a genre name as a parameter and returns the name of the city (cities) where the genre is being
    listened to the most"""

    if not style:
        return "Please specify a genre name"

    cities_list: list = execute_query(query, (style,))

    if not cities_list:
        return "The genre name is not in the list. Please check the entered name."

    result: list = [cities_list[0][0]]
    quantity: int = cities_list[0][2]
    for city in cities_list[1:]:
        if city[2] == quantity:
            result.append(city[0])
        else:
            break

    message = f"Top {style} {"city" if len(result) == 1 else "cities"}: {', '.join(result)} ({quantity})"
    return message


app.run(port=5001, debug=True)
