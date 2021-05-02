import mysql.connector
from faker import Faker
import csv

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

foundCourseIDs = findIDOfCorrespondingCourse("CPSC 231")

def printAllRecords():
    mycursor.execute("SELECT * FROM Assignments")
    results = mycursor.fetchall()
    print(results)
    return

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

def addCourse(departmentID, name, rank, tenure):
    mycursor.execute(
        'Insert into Assignments(DepartmentID, FacultyName, FacultyRank, isTenured) VALUES (?,?,?,?)',
        (departmentID, name, rank, tenure,))
    db.commit()
    return

def addCollege(name, NumMajors, NumMinors, grad):
    mycursor.execute(
        'Insert into Assignments(CollegeName, NumOfMajors, NumOfMinors, gradDegreeOffered) VALUES (?,?,?,?)',
        (name, NumMajors, NumMinors, grad,))
    db.commit()
    return






#for i in foundCourseIDs:
    #print(i)
