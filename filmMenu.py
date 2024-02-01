import addFilms, updateFilms, deleteFilms, readFilms

def films_menu_file():
    with open("PYTHON/Python Project/filmMenu.txt") as filmsMenu:
        mainMenu = filmsMenu.read()
    return mainMenu

def films_menu():
    menuOption = 0
    optionsMainMenuList = ["1","2","3","4","5"]

    mainMenuChoices = films_menu_file()

    while menuOption not in optionsMainMenuList:
        print(mainMenuChoices)

        menuOption = input("Enter an option from the films main menu: ")
        if menuOption not in optionsMainMenuList:
            print(f"{menuOption} is not available, please enter the correct option number")
    return menuOption      
 
mainProgram = True

while mainProgram:
    mainMenu = films_menu()
    if mainMenu == "1":
        addFilms.add_films()
    elif mainMenu == "2":
        deleteFilms.delete_films()
    elif mainMenu == "3":
        updateFilms.update_films()        
    elif mainMenu == "4":
        readFilms.read_films()  
    else:
        mainProgram = False  
input("Press the 'Enter' key to quit the films app")