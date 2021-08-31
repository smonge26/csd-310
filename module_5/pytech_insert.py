''' 
    Title: pytech_insert.py
    Author: Sigfredo Monge Villanueva
    Date: 30 August 2021
    Description: Test program for inserting students information into the students collection
'''

""" import statements """
from pymongo import MongoClient

# MongoDB connection string 
url = "mongodb+srv://admin:admin@cluster0.mbmui.mongodb.net/pytech?retryWrites=true&w=majority"

# connect to the MongoDB cluster 
client = MongoClient(url)

# connect pytech database
db = client.pytech

""" three student documents"""
# Students one data document 
jake = {
    "student_id": "1007",
    "first_name": "Jake",
    "last_name": "FromStateFarm"
}

# Student two data document 
flo = {
    "student_id": "1008",
    "first_name": "Flo",
    "last_name": "FromProgressive"
}

# Student three data document
guy = {
    "student_id": "1009",
    "first_name": "Guy",
    "last_name": "FromAllState"
}

# get the students collection 
students = db.students

# insert statements with output 
print("\n -- INSERT STATEMENTS --")
jake_id = students.insert_one(jake).inserted_id
print("Inserted student record Jake FromStateFarm into the students collection with document_id : " + str(jake_id))

flo_id = students.insert_one(flo).inserted_id
print("Inserted student record Flo FromProgressive into the students collection with document_id : " + str(flo_id))

guy_id = students.insert_one(guy).inserted_id
print("Inserted student record Guy FromAllState into the students collection with document_id : " + str(guy_id))

input("\n\n  End of program, press any key to exit... ")