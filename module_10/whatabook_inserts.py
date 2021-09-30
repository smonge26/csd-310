''' 
    Title: whatabook_inserts.py
    Author: Sigfredo Monge Villanueva
    Date: 18 September 2021
    Description: Program to insert information of store, books, users and wishlist into whatabook database. 
'''
import mysql.connector
from mysql.connector import errorcode

config ={
    "user": "whatabook_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "whatabook",
    "raise_on_warnings": True
}


try:
    db = mysql.connector.connect(**config) 
    
    cursor = db.cursor()

    '''store info insert'''
    cursor.execute("INSERT INTO store (locale)VALUES('5701 Sunset Dr. Ste 196, Miami, FL 33143') ")
 
    
    '''books info insert'''
    cursor.execute("INSERT INTO book(book_name, author, details)VALUES('ANNIHILATION', 'Jeff VanderMeer', 'In Annihilation, The first volume of Jeff VanderMeer’s Southern Reach trilogy, we join the twelfth expedition to Area X.')  ")
   
    cursor.execute("INSERT INTO book(book_name, author, details)VALUES('AUTHORITY', 'Jeff VanderMeer', 'In Authority, The New York Times bestselling second volume of Jeff VanderMeer’s Southern Reach trilogy, Area X’s most disturbing questions are answered . . . but the answers are far from reassuring.') ")

    cursor.execute("INSERT INTO book(book_name, author, details)VALUES('ACCEPTANCE', 'Jeff VanderMeer', 'In this New York Times bestselling final installment of Jeff VanderMeer’s Southern Reach trilogy, the mysteries of Area X may be solved, but their consequences and implications are no less profound — or terrifying.') ")
   
    cursor.execute("INSERT INTO book(book_name, author, details)VALUES('The Alchemists of Loom.', 'Elise Kova', 'Her vengeance. His vision. The first book in the Loom Saga.') ")
 
    cursor.execute("INSERT INTO book(book_name, author, details)VALUES('The Dragons Of Nova', 'Elise Kova', 'The second book in the Loom Saga.') ")
  
    cursor.execute("INSERT INTO book(book_name, author, details)VALUES('The Rebels Of Gold', 'Elise Kova', 'This is the final installment of USA Today bestselling author Elise Kova’s Loom Saga, THE REBELS OF GOLD will reveal the fate of Loom’s brilliantly contrasting world and its beloved inhabitants.') ")
  
    cursor.execute("INSERT INTO book(book_name, author, details)VALUES('Binti', 'Nnedi Okorafor', 'Her name is Binti, and she is the first of the Himba people ever to be offered a place at Oomza University, the finest institution of higher learning in the galaxy. But to accept the offer will mean giving up her place in her family to travel between the stars among strangers who do not share her ways or respect her customs.') ")
  
    cursor.execute("INSERT INTO book(book_name, author, details)VALUES('Home', 'Nnedi Okorafor', 'It’s been a year since Binti and Okwu enrolled at Oomza University. A year since Binti was declared a hero for uniting two warring planets. A year since she found friendship in the unlikeliest of places.') ")
  
    cursor.execute("INSERT INTO book(book_name, author, details)VALUES('The Night Masquerade', 'Nnedi Okorafor', 'Binti has returned to her home planet, believing that the violence of the Meduse has been left behind. Unfortunately, although her people are peaceful on the whole, the same cannot be said for the Khoush, who fan the flames of their ancient rivalry with the Meduse.') ")

    
    '''users info insert'''
    cursor.execute("INSERT INTO user(first_name, last_name)VALUES('Ross', 'Geller') ")
   
    cursor.execute("INSERT INTO user(first_name, last_name)VALUES('Rachel', 'Green') ")

    cursor.execute("INSERT INTO user(first_name, last_name)VALUES('Chandler', 'Bing') ")
 

    '''wishlist info insert'''
    cursor.execute("INSERT INTO wishlist(user_id, book_id)VALUES((SELECT user_id FROM user WHERE first_name = 'Ross'),(SELECT book_id FROM book WHERE book_name = 'ACCEPTANCE')) ")
  
    cursor.execute("INSERT INTO wishlist(user_id, book_id)VALUES((SELECT user_id FROM user WHERE first_name = 'Rachel'),(SELECT book_id FROM book WHERE book_name = 'Binti')) ")
   
    cursor.execute("INSERT INTO wishlist(user_id, book_id)VALUES((SELECT user_id FROM user WHERE first_name = 'Chandler'),(SELECT book_id FROM book WHERE book_name = 'The Dragons Of Nova')) ")
 
    db.commit()

except mysql.connector.Error as err:  
    ''' on error code '''

    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The specified database does not exist")

    else:
        print(err)

finally:
    '''closing database connection'''
    db.close()