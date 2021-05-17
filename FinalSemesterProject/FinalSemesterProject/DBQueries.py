import mysql.connector
from faker import Faker
import pandas as pd
import csv
import datetime
import EstablishConnection
import InsertDeleteValues

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
mycursor = InsertDeleteValues.mycursor

def printAssignmentsCoursesDepartmentInfo(departmentName):
    mycursor.execute('SELECT AssignmentID, AssignmentName, AssignmentDueDate, Assignments.isDeleted, Courses.CourseID, Courses.CourseInstructorID, '
                     'Courses.CourseName, Courses.CourseCode, Courses.isDeleted, Department.DepartmentID, Department.DepartmentName, Department.isDeleted FROM Assignments INNER JOIN Courses ON Assignments.CourseID = Courses.CourseID INNER JOIN Department ON Courses.DepartmentOfCourse = Department.DepartmentID '
                     'WHERE DepartmentName = %s;', (departmentName,))
    results = mycursor.fetchall()

    # for i in results:
    #     resultsAsList.extend(list(i))
    #
    # for i in range(len(resultsAsList)):
    #     for j in range(i + 1, len(resultsAsList)):
    #         if(compare(resultsAsList[i], resultsAsList[j])):
    #             resultsAsList.remove(j)

    # for i in results:
    #     resultsAsList.append(i)
    #
    # for i in resultsAsList:
    #     for j in range(len(resultsAsList)):
    #         for k in range(j + 1, len(resultsAsList)):
    #             if(compare(resultsAsList[i], resultsAsList[j])):
    #                 print("Found!")
    #                 resultsAsList.remove(j)

    df = pd.DataFrame(results, columns = ['AssignmentID',' AssignmentName', 'AssignmentDueDate', 'AssignmentDeleted?', 'CourseID', 'CourseInstructorID',
                     'CourseName', 'CourseCode', 'CourseDeleted?', 'DepartmentID', 'DepartmentName', 'DepartmentisDeleted?'])

    print(df)

    # for i in results:
    #     print(results)

def printAssignmentsCoursesFacultyInfo(facultyName):
    mycursor.execute('SELECT AssignmentID, AssignmentName, AssignmentDueDate, Assignments.isDeleted, Courses.CourseID, Courses.CourseInstructorID, '
                     'Courses.CourseName, Courses.CourseCode, Courses.isDeleted, Faculty.FacultyName, Faculty.isDeleted '
                     'FROM Assignments INNER JOIN Courses on Assignments.CourseID = Courses.CourseID INNER JOIN Faculty ON Courses.CourseInstructorID = Faculty.FacultyID '
                     'WHERE FacultyName = %s;', (facultyName,))
    results = mycursor.fetchall()


    df = pd.DataFrame(results, columns=['AssignmentID', ' AssignmentName', 'AssignmentDueDate', 'AssignmentDeleted?', 'CourseID',
                               'CourseInstructorID', 'CourseName', 'CourseCode', 'CourseDeleted?', 'FacultyName', 'FacultyisDeleted?'])

    print(df)

def printAssignmentsCoursesDepartmentCollegeInfo(schoolName):
    mycursor.execute('SELECT AssignmentID, AssignmentName, AssignmentDueDate, Assignments.isDeleted, Courses.CourseID, Courses.CourseInstructorID, '
                     'Courses.CourseName, Courses.CourseCode, Courses.isDeleted, Department.DepartmentID, Department.DepartmentName, Department.isDeleted, CollegeID, CollegeName, universitySchools.isDeleted '
                     'FROM Assignments INNER JOIN Courses ON Assignments.CourseID = Courses.CourseID INNER JOIN Department ON Courses.DepartmentOfCourse = Department.DepartmentID INNER JOIN '
                     'universitySchools ON Department.collegeID = universitySchools.collegeID WHERE CollegeName = %s;', (schoolName,))
    results = mycursor.fetchall()

    df = pd.DataFrame(results, columns=['AssignmentID',' AssignmentName', 'AssignmentDueDate', 'AssignmentDeleted?', 'CourseID', 'CourseInstructorID',
                     'CourseName', 'CourseCode', 'CourseDeleted?', 'DepartmentID', 'DepartmentName', 'DepartmentisDeleted?', 'CollegeID', 'CollegeName', 'CollegeIsDeleted'])

    print(df)

def printAssignmentsCoursesInfo(courseName):
    mycursor.execute('SELECT AssignmentID, AssignmentName, AssignmentDueDate, Assignments.isDeleted, Courses.CourseID, Courses.CourseInstructorID, '
                     'Courses.CourseName, Courses.CourseCode, Courses.isDeleted FROM Assignments INNER JOIN Courses ON Assignments.CourseID = Courses.CourseID WHERE CourseName = %s;', (courseName,))
    results = mycursor.fetchall()

    df = pd.DataFrame(results, columns=['AssignmentID', ' AssignmentName', 'AssignmentDueDate', 'AssignmentDeleted?', 'CourseID',
                               'CourseInstructorID', 'CourseName', 'CourseCode', 'CourseDeleted?'])

    print(df)

def filterOutstandingAssignmentsByDepartment(theDepartment):
    mycursor.execute('SELECT * FROM Assignments WHERE CourseID IN (SELECT CourseID FROM Courses INNER JOIN Department ON Courses.DepartmentOfCourse = Department.DepartmentID WHERE Department.DepartmentName = %s);', (theDepartment, ))
    results = mycursor.fetchall()

    for i in results:
        for j in i:
            print(j, end = ' ')
        print()

def filterOutstandingAssignmentsByFaculty(theFaculty):
    mycursor.execute('SELECT * FROM Assignments WHERE CourseID IN (SELECT CourseInstructorID FROM Courses INNER JOIN Faculty ON Courses.CourseInstructorID = Faculty.CourseInstructorID WHERE Faculty.FacultyName = %s);',
        (theFaculty,))
    results = mycursor.fetchall()

    for i in results:
        for j in i:
            print(j, end=' ')
        print()

def filterOutstandingAssignmentsByCourse(theCourse):
    mycursor.execute('SELECT * FROM Assignments WHERE CourseID IN (SELECT CourseID FROM Courses WHERE Courses.CourseName = %s);', (theCourse,))
    results = mycursor.fetchall()

    for i in results:
        for j in i:
            print(j, end=' ')
        print()

#we may not need the below function
def filterOutstandingAssignmentsBySchool(theCollege):
    mycursor.execute('SELECT * FROM Assignments WHERE CourseID IN (SELECT CourseID FROM Courses INNER JOIN Department ON Courses.DepartmentOfCourse = Department.Department ID '
                     'INNER JOIN universitySchools ON Department.CollegeID = universitySchools.CollegeID WHERE universitySchools.CollegeName = %s);', (theCollege,))
    results = mycursor.fetchall()

    for i in results:
        for j in i:
            print(j, end=' ')
        print()

printAssignmentsCoursesDepartmentInfo("Anthropology")

