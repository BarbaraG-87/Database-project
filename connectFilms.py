import sqlite3 as sql

dbCon = sql.connect("PYTHON/Python Project/filmflix.db")

dbCursor = dbCon.cursor()