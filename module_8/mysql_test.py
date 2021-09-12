
''' 
    Title: mysql_test.py
    Author: Sigfredo Monge Villanueva
    Date: 11 September 2021
    Description: Test program for connecting to MySQL.
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
    
    # output of a successful connection status 
    print("\n  Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"], config["database"]))

    input("\n\n  Press any key to continue...")

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