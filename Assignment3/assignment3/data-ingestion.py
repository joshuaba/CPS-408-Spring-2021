import sqlite3
import pandas as pd

conn = sqlite3.connect('./student.db')
mycursor = conn.cursor()

# student_data = pd.read_csv('./students.csv', header=None, skiprows=[0])
with open('./students.csv') as inputfile:
    column_names = inputfile.readline()
    student_data = inputfile.readlines() # read in all the lines in the students.csv file

# print(student_data)

for row in student_data:
    listOfStudents = []
    row_list = row.split(',') # split the values in the row into an array of values
    # int(row_list[5])
    # float(row_list[8])
    # for i in row_list:
    #     print(i)
    #     listOfStudents.append(i)
    conn.execute("INSERT INTO Student(FirstName, LastName, Address, City, State, ZipCode, MobilePhoneNumber, MAJOR, GPA) VALUES(?,?,?,?,?,?,?,?,?)", row_list)


conn.commit() #commit the SQL query above (on line 22)