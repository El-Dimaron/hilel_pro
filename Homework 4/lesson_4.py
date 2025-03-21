from database_handler import execute_query
from flask import Flask
from webargs.flaskparser import use_kwargs
from validator import order_price_validator, track_validator

app = Flask(__name__)


@app.route("/order-price")
@use_kwargs(order_price_validator, location='query')
def order_price(country) -> str:
    """The function displays total sales value from chinook.db.
    If the Country value is specified, the function returns the total value for that country."""

    query = (f"SELECT BillingCountry, SUM(UnitPrice * Quantity) AS SALES FROM invoice_items LEFT JOIN invoices "
             f"ON invoice_items.InvoiceId = invoices.InvoiceId")

    if country:
        country = country.title()
        query += f" WHERE BillingCountry = '{country}'"
        records: list = execute_query(query)
        country_name: str = records[0][0]
        country_sales: float = records[0][1]
        return f"{country_name} total sales: {country_sales}"
    else:
        records: list = execute_query(query)
        print(records)
        total_sales: float = records[0][1]
        return f"Total sales: {total_sales}"


# http://127.0.0.1:5001/order-price


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

    def time_representation(time_ms: int) -> str:
        """Converts miliseconds to hours and minutes."""
        time_h = time_ms / (1000 * 60 * 60)
        result_time_h = int(time_h)
        result_time_m = int((time_h - result_time_h) * 60)
        return f"The total time is {result_time_h}h {result_time_m}m"

    time_query = query.replace("*", "sum(Milliseconds)")
    time: int = execute_query(time_query)[0][0]
    time: str = time_representation(time)
    records.insert(0, time)

    return records


# http://127.0.0.1:5001/get-all-info-about-track

app.run(port=5001, debug=True)
