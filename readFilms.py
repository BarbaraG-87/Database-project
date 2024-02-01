from connectFilms import *

def read_films():
    dbCursor.execute("SELECT * FROM tblFilms")

    allFilms = dbCursor.fetchall()

    for aFilm in allFilms:
        print(aFilm)

if __name__ == "__main__":
    read_films()