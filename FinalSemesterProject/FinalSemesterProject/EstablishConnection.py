import mysql.connector
from faker import Faker
import csv
import datetime

db = mysql.connector.connect(
    host="34.94.39.105",
    user="mydbappuser",
    password="4IserveHim!!",
    database="Assignments"
)

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

def printAllRecords():
    mycursor.execute("SELECT * FROM Assignments")
    results = mycursor.fetchall()

    # in the below for loops we modify the due date so that it display in the following format: MM/DD/YY instead of showing up as a datetime object
    for i in results:
        iasList = list(i) # convert the tuple i into a list
        for j in iasList: # for each element in the list iasList (j are essentially the fields in the tuple)
            if isinstance(j, datetime.date): # if j is a datetime.date object --> this should only apply to the last field, DueDate
                iasList.remove(j)
                j = j.strftime('%m/%d/%y') # convert j from displaying as a datetime object into a string
                iasList.append(j) # append the new value of j to the list
        iasTuple = tuple(iasList) # convert iasList back into a tuple, the original type of i
        print(iasTuple)

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

# printAllRecords()




#for i in foundCourseIDs:
    #print(i)
