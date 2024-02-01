from connectFilms import *

def films_report_file():
    with open("PYTHON/Python Project/filmReportMenu.txt") as filmsReportMenu:
        reportOptions = filmsReportMenu.read()
    return reportOptions

def films_report_menu():
    option = 0
    optionsList = ["1","2","3","4","5"]

    menuChoices = films_report_file()

    while option not in optionsList:
        print(menuChoices)

        option = input("Enter an option from the films report menu: ")
        if option not in optionsList:
            print(f"{option} is not available, please enter the correct option number")
    return option      
 
reportProgram = True

while reportProgram:
    reportMenu = films_report_menu()
    if reportMenu == "1":
        dbCursor.execute("SELECT * FROM tblFilms")
        allFilms = dbCursor.fetchall()
        for aFilm in allFilms:
            print(aFilm)
    elif reportMenu == "2":
        genre = input("Enter the film genre: ")
        dbCursor.execute(f"SELECT * FROM tblFilms WHERE genre LIKE '{genre}'")
        allFilms = dbCursor.fetchall()
        for aFilm in allFilms:
            print(aFilm)
    elif reportMenu == "3":
        year = input("Enter the year of release: ")
        dbCursor.execute(f"SELECT * FROM tblFilms WHERE yearReleased LIKE '{year}'")
        allFilms = dbCursor.fetchall()
        for aFilm in allFilms:
            print(aFilm)     
    elif reportMenu == "4":
        rating = input("Enter the film rating (G, PG, R): ")
        dbCursor.execute(f"SELECT * FROM tblFilms WHERE rating LIKE '{rating}'")
        allFilms = dbCursor.fetchall()
        for aFilm in allFilms:
            print(aFilm) 
    else:
        reportProgram = False  
    

input("Press the 'Enter' key to quit the films app")









