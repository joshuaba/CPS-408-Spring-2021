import mysql.connector
from faker import Faker
import pandas as pd
import csv
import datetime
import EstablishConnection
import InsertDeleteValues

mycursor = InsertDeleteValues.mycursor

def CreateViewAssignmentsCourses():
    mycursor.execute('CREATE VIEW AssignmentsCourses AS SELECT AssignmentName, AssignmentDueDate, Assignments.isDeleted, '
                     'Courses.CourseID, CourseInstructorID, DepartmentOfCourse, CourseName, CourseCode, Courses.isDeleted AS IsCourseDeleted FROM Assignments, Courses')
    EstablishConnection.db.commit()

def CreateViewAssignmentsFaculty():
    mycursor.execute(
        'CREATE VIEW AssignmentsCourses AS SELECT AssignmentName, AssignmentDueDate, Assignments.isDeleted, '
        'Courses.CourseID, CourseInstructorID, DepartmentOfCourse, CourseName, CourseCode, Courses.isDeleted AS IsCourseDeleted FROM Assignments, Courses')
    EstablishConnection.db.commit()

# to complete later 

