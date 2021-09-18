''' 
    Title: pysports_update_and_delete.py
    Author: Sigfredo Monge Villanueva
    Date: 18 September 2021
    Description: Program to insert, update and delete a player record on pysports 
'''
import mysql.connector
from mysql.connector import errorcode

config ={
    "user": "pysports_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "pysports",
    "raise_on_warnings": True
}

try:
    '''trying to connect'''

    db = mysql.connector.connect(**config) # connecting to the pysports database using the defined values in config
    
    cursor = db.cursor()

    '''INSERT NEW PLAYER'''
    cursor.execute("INSERT INTO player (first_name, last_name, team_id)VALUES('Smeagol','Shire Folk', 1) ")
    db.commit()
    cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id") 
    players = cursor.fetchall()
    print ("\n  -- DISPLAYING PLAYERS AFTER INSERT --")
    for player in players:
        print("  Player ID: {}\n  First Name: {}\n  Last Name: {}\n  Team ID: {}\n".format(player[0], player[1], player[2], player[3])) # output displaying the information gathered

    '''UPDATE PLAYER NAMED SMEAGOL'''
    cursor.execute("UPDATE player SET team_id = 2, first_name = 'Gollum', last_name = 'Ring Stealer' WHERE first_name = 'Smeagol'")
    cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id") 
    players = cursor.fetchall()
    print ("\n  -- DISPLAYING PLAYERS AFTER UPDATE --")
    for player in players:
        print("  Player ID: {}\n  First Name: {}\n  Last Name: {}\n  Team ID: {}\n".format(player[0], player[1], player[2], player[3])) # output displaying the information gathered

    '''DELETE PLAYER RECORD NAMED GOLLUM'''
    cursor.execute("DELETE FROM player WHERE first_name = 'Gollum'")
    db.commit()
    cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id") 
    players = cursor.fetchall()
    print ("\n  -- DISPLAYING PLAYERS AFTER DELETE --")
    for player in players:
        print("  Player ID: {}\n  First Name: {}\n  Last Name: {}\n  Team ID: {}\n".format(player[0], player[1], player[2], player[3])) # output displaying the information gathered

    input("\n\n  Press any key to continue... ")

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