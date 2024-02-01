from connectFilms import *

def update_films():
    filmID = input("Enter the Film ID number of the record you want to update: ")
    filmCategory = input("Enter the category you want to update (title, yearReleased, rating, duration, genre): ")
    newValue = input(f"Enter the new value for {filmCategory} category: ")

    newValue = "'"+newValue+"'"

    dbCursor.execute(f"UPDATE tblFilms SET {filmCategory} = {newValue} WHERE filmID = {filmID}")
    dbCon.commit()

    print(f"Record - {filmID} - was updated in the films table")

if __name__ == "__main__":
    update_films() 