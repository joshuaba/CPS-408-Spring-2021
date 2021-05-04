import mysql.connector
from faker import Faker
import csv
import EstablishConnection

mycursor = EstablishConnection.db.cursor()

def theAssignmentDetails():
    print("Please enter the following properties of the assignment you wish to enter into the Assignments database: ")
    print() # formatting

    assignmentName = input("Assignment name: ")
    assignmentDueDate = input("Assignment due date (enter in the following format: MM-DD-YYYY): ")
    correspondingCourse = input("For what course is this assignment? Reference the course by its code as in \"CPSC 231\": ")

    correspondingCourseID = findIDOfCorrespondingCourse(correspondingCourse)

    print(correspondingCourseID)

    mycursor.execute("INSERT INTO Assignments VALUES (?, ?, ?);", (correspondingCourseID, assignmentName, assignmentDueDate,))
    EstablishConnection.db.commit()

    print("Student successfully added")

def findIDOfCorrespondingCourse(courseCode):
    mycursor = EstablishConnection.db.cursor()

    mycursor.execute('SELECT CourseID FROM Courses WHERE CourseCode = ?;', (courseCode,))
    courseID = mycursor.fetchall()


    if(courseID == "None"):
        print("Error. There is no course with that course code in the Courses database. Please enter another course code")

    return courseID

findIDOfCorrespondingCourse("CPSC 231")








