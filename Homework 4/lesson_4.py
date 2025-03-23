from database_handler import execute_query
from flask import Flask
from webargs.flaskparser import use_kwargs
from validator import order_price_validator, track_validator
from utilities import time_representation

app = Flask(__name__)


@app.route("/order-price")
@use_kwargs(order_price_validator, location='query')
def order_price(country) -> str:
    """The function displays total sales value from chinook.db.
    If the Country value is specified, the function returns the total value for that country."""

    query = (f"SELECT BillingCountry, SUM(UnitPrice * Quantity) AS SALES FROM invoice_items LEFT JOIN invoices "
             f"ON invoice_items.InvoiceId = invoices.InvoiceId")

    message = "Total sales: {}"

    if country:
        query += f" WHERE BillingCountry = '{country.title()}'"

    records: list = execute_query(query)
    country_name: str = records[0][0]
    country_sales: float = records[0][1]

    if country:
        message = message.replace("T", "{} t")
        message = message.format(country_name, country_sales)
    else:
        message = message.format(country_sales)

    return message


@app.route("/get-all-info-about-track")
@use_kwargs(track_validator, location='query')
def get_all_info_about_track(track_id) -> list:
    """The function displays all the information about the track (including its time) when track_id is specified.
    If no track_id is specified, the function returns the list of all available tracks and their total time."""

    query = ("SELECT * FROM tracks "
             "LEFT JOIN albums ON tracks.AlbumId = albums.AlbumId "
             "LEFT JOIN artists ON albums.ArtistId = artists.ArtistId "
             "LEFT JOIN media_types on tracks.MediaTypeId = media_types.MediaTypeId "
             "LEFT JOIN genres ON tracks.GenreId = genres.GenreId")

    if track_id:
        query += f" WHERE TrackId = {track_id}"

    records: list = execute_query(query)

    time_query = query.replace("*", "sum(Milliseconds)")
    time: int = execute_query(time_query)[0][0]
    time: str = time_representation(time)
    records.insert(0, time)

    return records


app.run(port=5001, debug=True)
