import mysql.connector
from faker import Faker
import csv
import datetime
import pandas as pd
import pymysql

db = mysql.connector.connect(
    host="34.94.39.105",
    user="mydbappuser",
    password="4IserveHim!!",
    database="Assignments"
)

dbcon = pymysql.connect("34.94.39.105", "mydbappuser", "4IserveHim!!", "Assignments")

mycursor = db.cursor(buffered=True)

def findIDOfCorrespondingCourse(courseName):

    # courseCode = []
    # courseCode.append("CPSC 231")
    # courseID = mycursor.execute("SELECT * FROM Courses C WHERE C.CourseCode = ?;", courseCode)
    # db.commit()
    # return courseID

    mycursor.execute("SELECT * FROM Assignments")
    results = mycursor.fetchall()

    print(results)

    return results

# foundCourseIDs = findIDOfCorrespondingCourse("CPSC 231")

def printAllAssignments():
    mycursor.execute("SELECT * FROM Assignments WHERE isDeleted = 0")
    results = mycursor.fetchall()

    print("Assignment ID     Assignment Name/Title     ID of Corresponding Course      Assignment Due Date")
    for i in results:
        for j in i:
            print(j, end = ' ')
            print("     ", end = ' ')
        print() # formatting


    # in the below for loops we modify the due date so that it display in the following format: MM/DD/YY instead of showing up as a datetime object
    # for i in results:
    #     iasList = list(i) # convert the tuple i into a list
    #     for j in iasList: # for each element in the list iasList (j are essentially the fields in the tuple)
    #         if isinstance(j, datetime.date): # if j is a datetime.date object --> this should only apply to the last field, DueDate
    #             iasList.remove(j)
    #             j = j.strftime('%m/%d/%y') # convert j from displaying as a datetime object into a string
    #             iasList.append(j) # append the new value of j to the list
    #     iasTuple = tuple(iasList) # convert iasList back into a tuple, the original type of i
    #     print(iasTuple)

def returnAssignments():
    try:
        SQL_Query = pd.read_sql_query(
            '''select
              *
              from Assignments''', dbcon)

        df = pd.DataFrame(SQL_Query, columns=['AssignmentID', 'CourseID', 'AssignmentName', 'AssignmentDueDate', 'isDeleted'])
        results = df.to_csv('assignments.csv')
    except:
        print("Error: unable to convert the data")


    return


def returnCourses():
    mycursor.execute('SELECT * FROM Courses')
    results = mycursor.fetchall()

    return results


def returnFaculty():
    mycursor.execute('SELECT * FROM Faculty')
    results = mycursor.fetchall()

    return results


def returnDepartment():
    mycursor.execute('SELECT * FROM Department')
    results = mycursor.fetchall()

    return results


def returnSchool():
    mycursor.execute('SELECT * FROM universitySchools')
    results = mycursor.fetchall()

    return results

def displayCourseData():
    mycursor.execute('SELECT * FROM Courses')
    results = mycursor.fetchall()

    for i in results:
        print(i)

def displaySchoolData():
    mycursor.execute('SELECT * FROM universitySchools')
    results = mycursor.fetchall()

    for i in results:
        print(i)

def displayFacultyData():
    mycursor.execute('SELECT * FROM Faculty')
    results = mycursor.fetchall()

    for i in results:
        print(i)


def displayDepartmentData():
    mycursor.execute('SELECT * FROM Department')
    results = mycursor.fetchall()

    for i in results:
        print(i)

def addAssignment(courseid, name, dueDate):
    mycursor.execute(
        'Insert into Assignments(CourseID, AssignmentName, AssignmentDueDate) VALUES (?,?,?)',
        (courseid, name, dueDate,))
    db.commit()
    return

def addCourse(instructorID, dept, courseName, courseCode):
    mycursor.execute(
        'Insert into Assignments(CourseInstructorID, DepartmentOfCourse, CourseName, CourseCode) VALUES (?,?,?,?)',
        (instructorID, dept, courseName, courseCode,))
    db.commit()
    return

def addDepartment(name, collegeid):
    mycursor.execute(
        'Insert into Assignments(DepartmentName, CollegeID) VALUES (?,?)',
        (name, collegeid,))
    db.commit()
    return

def addFaculty(departmentID, name, rank, tenure):
    mycursor.execute(
        'Insert into Faculty(DepartmentID, FacultyName, FacultyRank, isTenured) VALUES (?,?,?,?)',
        (departmentID, name, rank, tenure,))
    db.commit()
    return

def addCollege(name, NumMajors, NumMinors, grad):
    mycursor.execute(
        'Insert into Assignments(CollegeName, NumOfMajors, NumOfMinors, gradDegreeOffered) VALUES (?,?,?,?)',
        (name, NumMajors, NumMinors, grad,))
    db.commit()
    return

def updateAssignment():
    id = int(input("What is the ID of the assignment you would like to update?"))
    column = input("Which attribute would you like to update? (Name, DueDate, All) ")
    if column.toLowerCase() == "name":
        name = input("What would you like to change the name of the assignment to?")
        mycursor.execute('Update Assignment set AssignmentName = ? where AssignmentID = ?', (name, id))
        db.commit()

    elif column.toLowerCase() == "duedate":
        dd = input("What would you like to change the due date of the assignment to?")
        mycursor.execute('Update Assignment set AssignmentDueDate = ? where AssignmentID = ?', (dd, id))
        db.commit()

    elif column.toLowerCase() == "all":
        name = input("What would you like to change the name of the assignment to?")
        mycursor.execute('Update Assignment set AssignmentName = ? where AssignmentID = ?', (name, id))
        db.commit()

        dd = input("What would you like to change the due date of the assignment to?")
        mycursor.execute('Update Assignment set AssignmentDueDate = ? where AssignmentID = ?', (dd, id))
        db.commit()
    else:
        print("Invalid input.")

    return


def updateCourse():
    id = int(input("What is the ID of the course you would like to update?"))
    column = input("Which attribute would you like to update? (Name, Code, All) ")
    if column.toLowerCase() == "name":
        name = input("What would you like to change the name of the course to?")
        mycursor.execute('Update Courses set CourseName = ? where CourseID = ?', (name, id))
        db.commit()

    elif column.toLowerCase() == "code":
        code = input("What would you like to change the code of the course to?")
        mycursor.execute('Update Courses set CourseCode = ? where CourseID = ?', (code, id))
        db.commit()

    elif column.toLowerCase() == "all":
        name = input("What would you like to change the name of the course to?")
        mycursor.execute('Update Courses set CourseName = ? where CourseID = ?', (name, id))
        db.commit()

        code = input("What would you like to change the code of the course to?")
        mycursor.execute('Update Courses set CourseCode = ? where CourseID = ?', (code, id))
        db.commit()
    else:
        print("Invalid input.")

    return

def updateDepartment():
    id = int(input("What is the ID of the department you would like to update?"))
    name = input("What would you like to updates the department's name to?")

    mycursor.execute('Update Department set DepartmentName = ? where DepartmentID = ?', (name, id))
    db.commit()

    return

def updateFaculty():
    id = int(input("What is the ID of the Faculty you would like to update?"))
    column = input("Which attribute would you like to update? (Name, Rank, Tenure, Education Level, all) ")
    if column.toLowerCase() == "name":
        name = input("What would you like to change the name of the faculty to?")
        mycursor.execute('Update Faculty set FacultyName = ? where FacultyID = ?', (name, id))
        db.commit()

    elif column.toLowerCase() == "rank":
        rank = input("What would you like to change the rank of the faculty to?")
        mycursor.execute('Update Faculty set FacultyRank = ? where FacultyID = ?', (rank, id))
        db.commit()

    elif column.toLowerCase() == "education level":
        level = input("What would you like to change the education level of the faculty to?")
        mycursor.execute('Update Faculty set educationLevel = ? where FacultyID = ?', (level, id))
        db.commit()

    elif column.toLowerCase() == "tenure":
        status = input("What would you like to change the tenure status of the faculty to?")
        mycursor.execute('Update Faculty set isTenured = ? where FacultyID = ?', (status, id))
        db.commit()

    elif column.toLowerCase() == "all":
        name = input("What would you like to change the name of the faculty to?")
        mycursor.execute('Update Faculty set FacultyName = ? where FacultyID = ?', (name, id))
        db.commit()

        rank = input("What would you like to change the rank of the faculty to?")
        mycursor.execute('Update Faculty set FacultyRank = ? where FacultyID = ?', (rank, id))
        db.commit()

        level = input("What would you like to change the education level of the faculty to?")
        mycursor.execute('Update Faculty set educationLevel = ? where FacultyID = ?', (level, id))
        db.commit()

        status = input("What would you like to change the tenure status of the faculty to?")
        mycursor.execute('Update Faculty set isTenured = ? where FacultyID = ?', (status, id))
        db.commit()
    else:
        print("Invalid input.")
    return

def updateCollege():
    id = int(input("What is the ID of the college you would like to update?"))
    column = input("Which attribute would you like to update? (Name, Number of majors, Number of minors, graduate degree, all")
    if column.toLowerCase() == "name":
        name = input("What would you like to change the name of the college to?")
        mycursor.execute('Update universitySchools set CollegeName = ? where CollegeID = ?', (name, id))
        db.commit()

    elif column.toLowerCase() == "number of majors":
        majors = int(input("What would you like to change the number of majors offered by the college to?"))
        mycursor.execute('Update universitySchools set NumOfMajors = ? where CollegeID = ?', (majors, id))
        db.commit()

    elif column.toLowerCase() == "number of minors":
        minors = int(input("What would you like to change the number of minors offered by the college to?"))
        mycursor.execute('Update universitySchools set NumOfMinors = ? where CollegeID = ?', (minors, id))
        db.commit()

    elif column.toLowerCase() == "graduate degree":
        grad = input("What would you like to change the graduate degree offered by the college to?")
        mycursor.execute('Update universitySchools set gradDegreeOffered = ? where CollegeID = ?', (grad, id))
        db.commit()

    elif column.toLowerCase() == "all":
        name = input("What would you like to change the name of the college to?")
        mycursor.execute('Update universitySchools set CollegeName = ? where CollegeID = ?', (name, id))
        db.commit()

        majors = int(input("What would you like to change the number of majors offered by the college to?"))
        mycursor.execute('Update universitySchools set NumOfMajors = ? where CollegeID = ?', (majors, id))
        db.commit()

        minors = int(input("What would you like to change the number of minors offered by the college to?"))
        mycursor.execute('Update universitySchools set NumOfMinors = ? where CollegeID = ?', (minors, id))
        db.commit()

        grad = input("What would you like to change the graduate degree offered by the college to?")
        mycursor.execute('Update universitySchools set gradDegreeOffered = ? where CollegeID = ?', (grad, id))
        db.commit()
    else:
        print("Invalid input.")
    return
# printAllRecords()




#for i in foundCourseIDs:
    #print(i)
