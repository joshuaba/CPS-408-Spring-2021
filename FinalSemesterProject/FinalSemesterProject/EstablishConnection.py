import mysql.connector
from faker import Faker
import csv

db = mysql.connector.connect(
    host="34.94.39.105",
    user="mydbappuser",
    password="4IserveHim!!",
    database="Assignments"
)

def findIDOfCorrespondingCourse(courseName):
    mycursor = db.cursor(buffered=True)

    # courseCode = []
    # courseCode.append("CPSC 231")
    # courseID = mycursor.execute("SELECT * FROM Courses C WHERE C.CourseCode = ?;", courseCode)
    # db.commit()
    # return courseID

    results = mycursor.execute("SELECT * FROM Assignments")
    db.commit()

    print(results)

    return results

foundCourseIDs = findIDOfCorrespondingCourse("CPSC 231")

for i in foundCourseIDs:
    print(i)
