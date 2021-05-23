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

mycursor = db.cursor(buffered=True)

dbcon = pymysql.connect(host='34.94.39.105',user='mydbappuser',password='4IserveHim!!',db='Assignments',)

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

    df = pd.DataFrame(results, columns=['AssignmentID', 'ID of Corresponding Course', ' AssignmentName', 'AssignmentDueDate', 'AssignmentDeleted?'])

    print(df)

    # print("Assignment ID     Assignment Name/Title     ID of Corresponding Course      Assignment Due Date")
    # for i in results:
    #     for j in i:
    #         print(j, end = ' ')
    #         print("     ", end = ' ')
    #     print() # formatting


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
    try:
        SQL_Query = pd.read_sql_query(
            '''select
              *
              from Courses''', dbcon)

        df = pd.DataFrame(SQL_Query,
                          columns=['CourseID', 'CourseInstructorID', 'DepartmentOfCourse', 'CourseName', 'CourseCode', 'isDeleted'])
        results = df.to_csv('courses.csv')
    except:
        print("Error: unable to convert the data")

    return


def returnFaculty():
    try:
        SQL_Query = pd.read_sql_query(
            '''select
              *
              from Faculty''', dbcon)

        df = pd.DataFrame(SQL_Query,
                          columns=['FacultyID', 'DepartmentID', 'FacultyName', 'FacultyRank', 'isTenured',
                                   'educationLevel', 'isDeleted'])
        results = df.to_csv('faculty.csv')
    except:
        print("Error: unable to convert the data")

    return


def returnDepartment():
    try:
        SQL_Query = pd.read_sql_query(
            '''select
              *
              from Department''', dbcon)

        df = pd.DataFrame(SQL_Query,
                          columns=['DepartmentID', 'DepartmentName', 'CollegeID',
                                   'isDeleted'])
        results = df.to_csv('departments.csv')
    except:
        print("Error: unable to convert the data")

    return


def returnSchool():
    try:
        SQL_Query = pd.read_sql_query(
            '''select
              *
              from universitySchools''', dbcon)

        df = pd.DataFrame(SQL_Query,
                          columns=['CollegeID', 'CollegeName', 'NumOfMajors', 'NumOfMinors', 'gradDegreeOffered',
                                   'isDeleted'])
        results = df.to_csv('colleges.csv')
    except:
        print("Error: unable to convert the data")

    return

def displayCourseData():
    mycursor.execute('SELECT CourseID, CourseInstructorID, DepartmentOfCourse, CourseName, CourseCode FROM Courses WHERE Courses.isDeleted = 0')
    results = mycursor.fetchall()

    df = pd.DataFrame(results, columns=['CourseID', 'CourseInstructorID', 'DepartmentID', 'CourseName', 'CourseCode'])

    print(df)

def displaySchoolData():
    mycursor.execute('SELECT CollegeID, CollegeName, NumOfMajors, NumOfMinors, gradDegreeOffered FROM universitySchools WHERE universitySchools.isDeleted = 0')
    results = mycursor.fetchall()

    df = pd.DataFrame(results, columns=['CollegeID', 'CollegeName', 'Number of Majors', 'Number of Minors', 'Graduate Degree Offered'])

    print(df)

def displayFacultyData():
    mycursor.execute('SELECT FacultyID, DepartmentID, FacultyName, FacultyRank, isTenured, educationLevel FROM Faculty WHERE Faculty.isDeleted = 0')
    results = mycursor.fetchall()

    df = pd.DataFrame(results, columns=['FacultyID', 'Department to Which Faculty is Assigned', 'Name of Faculty Member', 'Rank of Faculty Member', 'Tenured?', 'Education Level'])

    print(df)

def displayDepartmentData():
    mycursor.execute('SELECT DepartmentID, DepartmentName, CollegeID FROM Department WHERE Department.isDeleted = 0')
    results = mycursor.fetchall()

    df = pd.DataFrame(results, columns = ['DepartmentID', 'DepartmentName', 'Corresponding College ID',])
    print(df)

def addAssignment(courseid, name, dueDate):
    mycursor.execute('Insert into Assignments(CourseID, AssignmentName, AssignmentDueDate, isDeleted) VALUES (%s,%s,%s,0)',(courseid, name, dueDate,))
    # db.commit()
    return

def addCourse(instructorID, dept, courseName, courseCode):
    mycursor.execute('Insert into Courses(CourseInstructorID, DepartmentOfCourse, CourseName, CourseCode, isDeleted) VALUES (%s, %s, %s, %s,0)',
        (instructorID, dept, courseName, courseCode,))
    # db.commit()
    return

def addDepartment(name, collegeid):
    mycursor.execute('INSERT INTO Department(DepartmentName, CollegeID, isDeleted) VALUES (%s, %s,0)',
        (name, collegeid,))
    # db.commit()
    return

def addFaculty(departmentID, name, rank, educationLevel, tenure):
    mycursor.execute('Insert into Faculty(DepartmentID, FacultyName, FacultyRank, educationLevel, isTenured, isDeleted) VALUES (%s, %s, %s, %s, %s,0)', (departmentID, name, rank, educationLevel, tenure,))
    # db.commit()
    return

def addCollege(name, NumMajors, NumMinors, grad):
    mycursor.execute(
        'Insert into universitySchools(CollegeName, NumOfMajors, NumOfMinors, gradDegreeOffered, isDeleted) VALUES (%s, %s, %s, %s,0)',
        (name, NumMajors, NumMinors, grad,))
    # db.commit()
    return

def updateAssignment():
    id = int(input("What is the ID of the assignment you would like to update?"))
    column = input("Which attribute would you like to update? (Name, DueDate, All) ")
    if column.lower() == "name":
        name = input("What would you like to change the name of the assignment to?")
        mycursor.execute('Update Assignment set AssignmentName = %s where AssignmentID = %s', (name, id))
        # db.commit()

    elif column.lower() == "duedate":
        dd = input("What would you like to change the due date of the assignment to?")
        mycursor.execute('Update Assignment set AssignmentDueDate = %s where AssignmentID = %s', (dd, id))
        # db.commit()

    elif column.lower() == "all":
        name = input("What would you like to change the name of the assignment to?")
        mycursor.execute('Update Assignment set AssignmentName = %s where AssignmentID = %s', (name, id))
        # db.commit()

        dd = input("What would you like to change the due date of the assignment to?")
        mycursor.execute('Update Assignment set AssignmentDueDate = %s where AssignmentID = %s', (dd, id))
        # db.commit()
    else:
        print("Invalid input.")

    return


def updateCourse():
    id = int(input("What is the ID of the course you would like to update?"))
    column = input("Which attribute would you like to update? (Name, Code, All) ")
    if column.lower() == "name":
        name = input("What would you like to change the name of the course to?")
        mycursor.execute('Update Courses set CourseName = %s where CourseID = %s', (name, id))
        # db.commit()

    elif column.lower() == "code":
        code = input("What would you like to change the code of the course to?")
        mycursor.execute('Update Courses set CourseCode = %s where CourseID = %s', (code, id))
        # db.commit()

    elif column.lower() == "all":
        name = input("What would you like to change the name of the course to?")
        mycursor.execute('Update Courses set CourseName = %s where CourseID = %s', (name, id))
        # db.commit()

        code = input("What would you like to change the code of the course to?")
        mycursor.execute('Update Courses set CourseCode = %s where CourseID = %s', (code, id))
        # db.commit()
    else:
        print("Invalid input.")

    return

def updateDepartment():
    id = int(input("What is the ID of the department you would like to update?"))
    name = input("What would you like to updates the department's name to?")

    mycursor.execute('Update Department set DepartmentName = %s where DepartmentID = %s', (name, id))
    # db.commit()

    return

def updateFaculty():
    id = int(input("What is the ID of the Faculty you would like to update?"))
    column = input("Which attribute would you like to update? (Name, Rank, Tenure, Education Level, all) ")
    if column.lower() == "name":
        name = input("What would you like to change the name of the faculty to?")
        mycursor.execute('Update Faculty set FacultyName = %s where FacultyID = %s', (name, id))
        # db.commit()

    elif column.lower() == "rank":
        rank = input("What would you like to change the rank of the faculty to?")
        mycursor.execute('Update Faculty set FacultyRank = %s where FacultyID = %s', (rank, id))
        # db.commit()

    elif column.lower() == "education level":
        level = input("What would you like to change the education level of the faculty to?")
        mycursor.execute('Update Faculty set educationLevel = %s where FacultyID = %s', (level, id))
        # db.commit()

    elif column.lower() == "tenure":
        status = input("What would you like to change the tenure status of the faculty to?")
        mycursor.execute('Update Faculty set isTenured = %s where FacultyID = %s', (status, id))
        # db.commit()

    elif column.lower() == "all":
        name = input("What would you like to change the name of the faculty to?")
        mycursor.execute('Update Faculty set FacultyName = %s where FacultyID = %s', (name, id))
        # db.commit()

        rank = input("What would you like to change the rank of the faculty to?")
        mycursor.execute('Update Faculty set FacultyRank = %s where FacultyID = %s', (rank, id))
        # db.commit()

        level = input("What would you like to change the education level of the faculty to?")
        mycursor.execute('Update Faculty set educationLevel = %s where FacultyID = %s', (level, id))
        # db.commit()

        status = input("What would you like to change the tenure status of the faculty to?")
        mycursor.execute('Update Faculty set isTenured = %s where FacultyID = %s', (status, id))
        # db.commit()
    else:
        print("Invalid input.")
    return

def updateCollege():
    id = int(input("What is the ID of the college you would like to update?"))
    column = input("Which attribute would you like to update? (Name, Number of majors, Number of minors, graduate degree, all")
    if column.lower() == "name":
        name = input("What would you like to change the name of the college to?")
        mycursor.execute('Update universitySchools set CollegeName = %s where CollegeID = %s', (name, id))
        # db.commit()

    elif column.lower() == "number of majors":
        majors = int(input("What would you like to change the number of majors offered by the college to?"))
        mycursor.execute('Update universitySchools set NumOfMajors = %s where CollegeID = %s', (majors, id))
        # db.commit()

    elif column.lower() == "number of minors":
        minors = int(input("What would you like to change the number of minors offered by the college to?"))
        mycursor.execute('Update universitySchools set NumOfMinors = %s where CollegeID = %s', (minors, id))
        # db.commit()

    elif column.lower() == "graduate degree":
        grad = input("What would you like to change the graduate degree offered by the college to?")
        mycursor.execute('Update universitySchools set gradDegreeOffered = %s where CollegeID = %s', (grad, id))
        # db.commit()

    elif column.lower() == "all":
        name = input("What would you like to change the name of the college to?")
        mycursor.execute('Update universitySchools set CollegeName = %s where CollegeID = %s', (name, id))
        # db.commit()

        majors = int(input("What would you like to change the number of majors offered by the college to?"))
        mycursor.execute('Update universitySchools set NumOfMajors = %s where CollegeID = %s', (majors, id))
        # db.commit()

        minors = int(input("What would you like to change the number of minors offered by the college to?"))
        mycursor.execute('Update universitySchools set NumOfMinors = %s where CollegeID = %s', (minors, id))
        # db.commit()

        grad = input("What would you like to change the graduate degree offered by the college to?")
        mycursor.execute('Update universitySchools set gradDegreeOffered = %s where CollegeID = %s', (grad, id))
        # db.commit()
    else:
        print("Invalid input.")
    return
# printAllRecords()




#for i in foundCourseIDs:
    #print(i)
