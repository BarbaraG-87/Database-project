from connectFilms import *

def add_films():
    filmTitle = input("Enter film Title: ")
    yearReleased = input("Enter the year of film release: ")
    filmRating = input("Enter the film rating (PG,G,R): ")
    filmDuration = input("Enter the film duration (min): ")
    filmGenre = input("Enter film Genre: ")

    dbCursor.execute("INSERT INTO tblFilms(title, yearReleased, rating, duration, genre) VALUES(?,?,?,?,?)",(filmTitle,yearReleased,filmRating,filmDuration,filmGenre))

    dbCon.commit()

    print(f" - {filmTitle} - was added in the films table.")

if __name__ == "__main__":
    add_films()  