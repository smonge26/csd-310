''' 
    Title: whatabook.py
    Author: Sigfredo Monge Villanueva
    Date: 26 September 2021
    Description: Program to interact with whatabook data base. 
'''
import sys
import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "whatabook_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "whatabook",
    "raise_on_warnings": True
}

'main menu function'
def mainMenu():

    print("\n 1. Display Books\n 2. Display Store Locations\n 3. My Account\n 4. Quit\n")

    mainMenuOptions = ["1", "2", "3", "4"]
    choice = input (" Please Enter a Menu Item: ")
    while choice not in mainMenuOptions:
        print("\nPlease Enter a Valid Option")
        print("\n 1. Display Books\n 2. Display Store Locations\n 3. My Account\n 4. Quit\n")
        choice = input(" Please Enter a Menu Item: ")
         
    if choice in mainMenuOptions:
        validChoice = int(choice)
        return validChoice

'display booklist function'
def displayBooks(_cursor):

    _cursor.execute("SELECT book_id, book_name, author, details FROM book")
    books = _cursor.fetchall()
    print("\n -- Book List --\n")
    for i in books:
        print(f" Book Name: {i[1]}\n Book Author: {i[2]}\n Book Details: {i[3]}\n")

'location function'
def displayLocations(_cursor):

    _cursor.execute("SELECT store_id, locale FROM store")
    stores = _cursor.fetchall()
    print("\n -- Current Store Location -- \n")
    for i in stores:
        print(f" Location: {i[1]}\n")

'user validation function'
def validateUser():

    print("\n -- Account  --\n")
    validUserIds = ["1", "2", "3"]
    userID = input("Please enter your user ID: ")
    while userID not in validUserIds:
        print("\nInvalid user ID\n")
        userID = input("Please enter your user ID: ")
    
    if userID in validUserIds:
        validUserID = int(userID)
        return userID

'user acccount menu function'
def displayAccountMenu():

    print("\n-- Account Menu --\n")
    print(" 1. Show Wishlist\n 2. Add A Book To Your Wishlist\n 3. Main Menu\n 4. Quit\n")

    
    validAccountOptions = ["1", "2", "3", "4"]
    accountOptions = input("\n Please Select a Menu Item --> ")

    
    while accountOptions not in validAccountOptions:
        print("\nPlease Select a Valid Option")
        accountOptions = input("\n Please Select a Menu Item --> ")
    
    if accountOptions in validAccountOptions:
        validAccountOption = int(accountOptions)
        return validAccountOption

'display books that can be added to wishlist function'
def displayBooksToAdd(_cursor, _user_id):

    availableBooks = ("SELECT book_id, book_name, author, details FROM book " +
                    "WHERE book_id NOT IN (SELECT book_id FROM wishlist WHERE user_id = {})".format(_user_id))
         
    _cursor.execute(availableBooks)
    booksThatCanBeAdded = _cursor.fetchall()

    print("\n -- Books That Can Be Added -- \n")
    for i in booksThatCanBeAdded:
        print(f"\n Book ID: {i[0]}\n Book Name: {i[1]}\n")
    
'function to add books to wishlist'
def addBookToWishlist(_cursor, _user_id, _book_id):

    _cursor.execute("INSERT INTO wishlist(user_id, book_id) VALUES({}, {})".format(_user_id, addBookID))

'function to display user wishlist'
def displayWishlist(_cursor, _user_id):

    _cursor.execute("SELECT user.user_id, user.first_name, user.last_name, book.book_id, book.book_name, book.author " + 
                    "FROM wishlist INNER JOIN user ON wishlist.user_id = user.user_id INNER JOIN book ON wishlist.book_id = book.book_id " + 
                    "WHERE user.user_id = {}".format(_user_id))

    wishlist = _cursor.fetchall()


    print("\n -- Your Wishlist Books --\n")
    for i in wishlist:
        print(f" Book Name: {i[4]}\n Author: {i[5]}\n")



try:

    db = mysql.connector.connect(**config)   
    cursor = db.cursor()
    print("\nWelcome to WhatABook! ")
    mainMenuSelection = mainMenu()
    while mainMenuSelection < 4:
        if mainMenuSelection == 1:
            displayBooks(cursor)    
        if mainMenuSelection == 2:
            displayLocations(cursor)         
        if mainMenuSelection == 3:
            myID = validateUser()
            accountOption = displayAccountMenu()
            while accountOption != 3:
                if accountOption == 1:
                    displayWishlist(cursor, myID)                       
                if accountOption == 2:
                    displayBooksToAdd(cursor, myID)
                    addBookID = input("\nPlease Enter the Book ID you want to add to your wishlist ")
                    validBookID = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
                    while addBookID not in validBookID:
                        print("\nInvlaid Book ID Please try again ")
                        addBookID = input("\nPlease Enter the Book ID you want to add to your wishlist ")
                    if addBookID in validBookID:
                        validBookID = int(addBookID)
                    addBookToWishlist(cursor, myID, validBookID)
                    db.commit()
                    print("\nYour Book was added to your wishlist!")
                if accountOption == 4:
                    print("\nCome Back Soon!")
                    sys.exit()
                accountOption = displayAccountMenu()
        mainMenuSelection = mainMenu()
        if mainMenuSelection == 4:
            print("\nCome Back Soon!")
            sys.exit()
      

except mysql.connector.Error as err:
    """ on error code """

    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The specified database does not exist")

    else:
        print(err)

finally:
    """ close the connection to MySQL """

    db.close()