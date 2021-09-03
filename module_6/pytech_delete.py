''' 
    Title: pytech_delete.py
    Author: Sigfredo Monge Villanueva
    Date: 02 September 2021
    Description: Test program for deleting students information from the students collection
'''

""" import statements """
from pymongo import MongoClient

# MongoDB connection string 
url = "mongodb+srv://admin:admin@cluster0.mbmui.mongodb.net/pytech?retryWrites=true&w=majority"

# connect to the MongoDB cluster 
client = MongoClient(url)

# connect pytech database
db = client.pytech

# get the students collection 
students = db.students

# find all students in the collection 
student_list = students.find({})

# display message 
print("\n  -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")

# loop over the collection and output the results 
for doc in student_list:
    print("  Student ID: " + doc["student_id"] + "\n  First Name: " + doc["first_name"] + "\n  Last Name: " + doc["last_name"] + "\n")

# Test Student data document to be deleted
eraseme = {
    "student_id": "1010",
    "first_name": "Iam",
    "last_name": "ToBeDeleted"
}

# insert statements with output for student delete test 
print("\n -- INSERT STATEMENTS --")
eraseme_id = students.insert_one(eraseme).inserted_id
print("Inserted student record into the students collection with document_id : " + str(eraseme_id))

# display the results 
print("\n  -- DISPLAYING STUDENT TEST DOC -- ")
print("  Student ID: " + eraseme["student_id"] + "\n  First Name: " + eraseme["first_name"] + "\n  Last Name: " + eraseme["last_name"] + "\n")

# find the test student document to be deleted 
eraseme = students.find_one({"student_id": "1010"})

# the delete_one method to remove the test student document
deleted_student_test_doc = students.delete_one({"student_id": "1010"})

# find all students in the collection again to verify deletion 
student_list = students.find({})

# display message 
print("\n  -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")

# loop over the collection and output the results 
for doc in student_list:
    print("  Student ID: " + doc["student_id"] + "\n  First Name: " + doc["first_name"] + "\n  Last Name: " + doc["last_name"] + "\n")


input("\n\n  End of program, press any key to exit... ")