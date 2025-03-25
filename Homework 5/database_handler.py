import sqlite3


def execute_query(query, args=()):
    with sqlite3.connect("../Homework 4/chinook.db") as connection:
        cursor = connection.cursor()
        print(args)
        print(type(args))
        print(len(args))
        cursor.execute(query, args)

        connection.commit()
        records = cursor.fetchall()

    return records


query = """SELECT City, Name, Counter FROM (
SELECT customers.City, genres.Name, COUNT(*) AS Counter, MAX(COUNT(*)) OVER () AS MaxCounter FROM genres
JOIN tracks on genres.GenreId = tracks.GenreId
JOIN invoice_items on tracks.TrackId = invoice_items.TrackId
JOIN invoices on invoice_items.InvoiceId = invoices.InvoiceId
JOIN customers on invoices.CustomerId = customers.CustomerId
WHERE genres.Name = ?
GROUP BY customers.City, genres.Name
)
WHERE Counter = MaxCounter;"""
