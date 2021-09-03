''' 
    Title: pytech_update.py
    Author: Sigfredo Monge Villanueva
    Date: 02 September 2021
    Description: Test program for updating the students information in the students collection
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

# update student_id 1007
result = students.update_one({"student_id": "1007"}, {"$set": {"last_name": "Not From State Farm"}})
 
# display message 
print("\n  -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")

# loop over the collection and output the results 
for doc in student_list:
    print("  Student ID: " + doc["student_id"] + "\n  First Name: " + doc["first_name"] + "\n  Last Name: " + doc["last_name"] + "\n")

# find the updated student document 
jake = students.find_one({"student_id": "1007"})

# display message
print("\n  -- DISPLAYING STUDENT DOCUMENT 1007 --")

# output the updated document to the terminal window
print("  Student ID: " + jake["student_id"] + "\n  First Name: " + jake["first_name"] + "\n  Last Name: " + jake["last_name"] + "\n")


input("\n\n  End of program, press any key to exit... ")