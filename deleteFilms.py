from connectFilms import *

def delete_films():
    filmID = input("Enter the FilmID of the record to be deleted: ")
    dbCursor.execute(f"DELETE FROM tblFilms WHERE filmID = {filmID}")
    dbCon.commit()

    print(f"Record {filmID} was deleted from the film table!")



if __name__ == "__main__":
    delete_films()