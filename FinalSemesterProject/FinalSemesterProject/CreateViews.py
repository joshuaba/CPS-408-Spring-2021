import mysql.connector
from faker import Faker
import pandas as pd
import csv
import datetime
import EstablishConnection
import InsertDeleteValues

mycursor = InsertDeleteValues.mycursor

def CreateViewAssignmentsCourses():
    # mycursor.execute('CREATE VIEW AssignmentsCourses AS SELECT AssignmentName, AssignmentDueDate, '
    #                  'Courses.CourseID, CourseInstructorID, DepartmentOfCourse, CourseName, CourseCode FROM Assignments, Courses WHERE Assignments.isDeleted = 0 '
    #                  'AND Courses.isDeleted = 0')
    # EstablishConnection.db.commit()

    mycursor.execute('SELECT * FROM AssignmentsCourses')
    results = mycursor.fetchall()

    df = pd.DataFrame(results, columns=['AssignmentName', 'AssignmentDueDate', 'AssignmentDeleted?', 'CourseID', 'CourseInstructor', 'Course Department', 'CourseName', 'CourseCode', 'Course Deleted?'])

    print(df)


def CreateViewAssignmentsFaculty():
    # mycursor.execute('CREATE VIEW AssignmentsFaculty AS SELECT AssignmentName, AssignmentDueDate, '
    #     'Faculty.FacultyID, Faculty.DepartmentID, FacultyName, FacultyRank, isTenured, educationLevel FROM Assignments, Faculty WHERE Assignments.isDeleted = 0 AND Faculty.isDeleted = 0')
    # EstablishConnection.db.commit()

    # print out the entries in this table view
    mycursor.execute('SELECT * FROM AssignmentsFaculty')
    results = mycursor.fetchall()

    df = pd.DataFrame(results,columns=['AssignmentID', 'AssignmentName', 'AssignmentDueDate', 'AssignmentDeleted?', 'FacultyID', 'FacultyDepartment', 'FacultyName', 'FacultyRank', 'facultyDeleted?'])

    print(df)


def CreateViewAssignmentsDepartment():
    # mycursor.execute('CREATE VIEW AssignmentsDepartment AS SELECT AssignmentName, AssignmentDueDate, '
    #     'Department.DepartmentID, Department.DepartmentName, Department.CollegeID FROM Assignments, Department WHERE Assignments.isDeleted = 0 '
    #                  'AND Department.isDeleted = 0')
    # EstablishConnection.db.commit()

    mycursor.execute('SELECT * FROM AssignmentsDepartment')
    results = mycursor.fetchall()

    df = pd.DataFrame(results, columns=['AssignmentName', 'AssignmentDueDate', 'AssignmentDeleted', 'DepartmentID', 'DepartmentName', 'Corresponding College/School', 'School/College Deleted'])

    print(df)

def CreateViewAssignmentsCollege():
    # mycursor.execute('CREATE VIEW AssignmentsCollege AS SELECT AssignmentName, AssignmentDueDate, '
    #     'universitySchools.CollegeID, universitySchools.CollegeName, universitySchools.NumOfMajors, universitySchools.NumOfMinors, universitySchools.gradDegreeOffered'
    #     'FROM Assignments, universitySchools WHERE Assignments.isDeleted = 0 AND universitySchools.isDeleted = 0')
    # EstablishConnection.db.commit()

    mycursor.execute('SELECT * FROM AssignmentsCollege')
    results = mycursor.fetchall()

    df = pd.DataFrame(results, columns=['AssignmentName', 'AssignmentDueDate', 'AssignmentDeleted?', 'CollegeID', 'School/College Name',
                                        'Number of Majors', 'Number of minors', 'Graduate Degree Offered?', 'School/College Deleted'])

    print(df)

# to complete later 

