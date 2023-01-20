import sqlite3 as lite
import sys

con = lite.connect('our_products_in_stock.db')
with con:
    cur = con.cursor()
    cur.execute ("SELECT * FROM our_products_in_stock")
    rows = cur.fetchall()

    for row in rows:
        print (row)