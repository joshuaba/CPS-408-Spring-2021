import mysql.connector
from faker import Faker
import csv
import datetime
import re # for regular expressions
import EstablishConnection

mycursor = EstablishConnection.db.cursor()

def theAssignmentDetails():
    print("Please enter the following properties of the assignment you wish to enter into the Assignments database: ")
    print() # formatting

    assignmentName = input("Assignment name: ")
    assignmentDueDate = input("Assignment due date (enter in the following format: MM-DD-YYYY): ")

    while(validateAssignmentDueDate(assignmentDueDate) == False): # prompt the user repeatedly if they do not enter a date in the format MM-DD-YYYY
        print("You have an error in your due date entry. Please enter it in the specified format. ", end = "")
        assignmentDueDate = input("Assignment due date (enter in the following format: MM-DD-YYYY): ")

    correspondingCourse = input("For what course is this assignment? Reference the course by its code as in \"CPSC 231\": ")

    correspondingCourseID = findIDOfCorrespondingCourse(correspondingCourse)

    while(correspondingCourseID == 0): # prompt the user for a valid course that is in the Courses database
        print("That course is either not in the database or you have an invalid entry. Please try again ", end="")
        correspondingCourse = input("For what course is this assignment? Reference the course by its code as in \"CPSC 231\": ")
        correspondingCourseID = findIDOfCorrespondingCourse(correspondingCourse)

    EstablishConnection.addAssignment(correspondingCourseID, assignmentName, assignmentDueDate) # call the addAssignment method defined in EstablishConnection

    # mycursor.execute("INSERT INTO Assignments(CourseID, AssignmentName, AssignmentDueDate) VALUES (%s, %s, %s);", (correspondingCourseID, assignmentName, assignmentDueDate,))
    # EstablishConnection.db.commit()

    print("Assignment successfully added. NOTE: The assignment will not be added into the database, however, until you choose to commit this change (option 9)")

def theCourseDetails():
    print("Please enter the following properties of the course you wish to enter into the Courses database: ")
    print()  # formatting

    courseName = input("Course name: ")
    courseCode = input("Please input the course's code, as in \"CPSC 231\": ")

    # while(not validateCourseCoude(courseCode)): #make sure the user inputted a valid course code
    #     print() #formatting
    #     print("Course code is invalid. ", end="")
    #     courseCode = input("Please input the course's code, as in \"CPSC 231\": ")

    instructorName = input("Please input the name of the instructor of this course (the instructor/faculty member must be in the faculty table): ")
    departmentOfCourse = input("Please enter the academic department under which this course will fall (i.e. \"Computer Science\"). Note that the course must already be in the Courses table: ")

    correspondingFacultyID = findIDOfCorrespondingFaculty(instructorName)
    correspondingDepartmentID = findIDOfCorrespondingDepartment(departmentOfCourse)

    while(correspondingFacultyID == 0):
        print("That faculty member is either not in the database or you have an invalid entry. Please try again ", end="")
        instructorName = input("Please input the name of the instructor of this course (the instructor/faculty member must be in the faculty table): ")
        correspondingFacultyID = findIDOfCorrespondingFaculty(instructorName)

    while(correspondingDepartmentID == 0):
        print("That department is either not in the database or you have an invalid entry. Please try again ", end="")
        departmentOfCourse = input("Please enter the academic department under which this course will fall (i.e. \"Computer Science\"). Note that the course must already be in the Courses table: ")
        correspondingDepartmentID = findIDOfCorrespondingDepartment(departmentOfCourse)

    EstablishConnection.addCourse(correspondingFacultyID, correspondingDepartmentID, courseName, courseCode)

    # mycursor.execute("INSERT INTO Assignments(CourseID, AssignmentName, AssignmentDueDate) VALUES (%s, %s, %s);", (correspondingCourseID, assignmentName, assignmentDueDate,))
    # EstablishConnection.db.commit()

    print("Course successfully added. NOTE: The course will not be added into the database, however, until you choose to commit this change (option 9)")

def theDepartmentDetails():
    print("Please enter the following properties of the department you wish to enter into the Department database: ")
    print()  # formatting

    departmentName = input("Department name: ")
    correspondingCollegeName = input("Please enter the name of the school or college under which this department will fall (i.e. \"Keck School of Medicine\"). Note that the school/college must already be in the universitySchools table: ")
    correspondingCollegeID = findIDOfCorrespondingSchool(correspondingCollegeName)

    while(correspondingCollegeID == 0):
        print("That college is either not in the database or you have an invalid entry. Please try again ", end="")
        correspondingCollegeName = input("Please enter the name of the school or college under which this department will fall (i.e. \"Keck School of Medicine\"). Note that the school/college must already be in the universitySchools table: ")
        correspondingCollegeID = findIDOfCorrespondingSchool(correspondingCollegeName)

    EstablishConnection.addDepartment(departmentName, correspondingCollegeID)

    # mycursor.execute("INSERT INTO Assignments(CourseID, AssignmentName, AssignmentDueDate) VALUES (%s, %s, %s);", (correspondingCourseID, assignmentName, assignmentDueDate,))
    # EstablishConnection.db.commit()

    print("Department successfully added. NOTE: The department will not be added into the database, however, until you choose to commit this change (option 9)")

def theFacultyDetails():
    print("Please enter the following properties of the faculty member you wish to enter into the Faculty table: ")
    print()  # formatting

    facultyName = input("Faculty name: ")
    facultyRank = input("Rank of faculty (i.e. \"Assistant/Associate/Full Professor, Lecturer, Instructor, etc.: ")
    isTenured = input("Is this faculty member tenured? (Y/N): ")
    isTenuredBool = 0

    while(isTenured != "Y" and isTenured != "N"): # validate input
        print("Invalid input. Please type /Y/' or /'N/'")
        isTenured = input("Is this faculty member tenured? (Y/N): ")

    if(isTenured == "Y"):
        isTenuredBool = 1

    educationLevel = input("What is the education level of this faculty member? (B.S./B.A, M.S./M.A., Ph.D. etc.")
    correspondingDepartmentName = input("Please enter the name of the department under which this faculty member will fall (i.e. \"Computer Science\"). Note that the department must already be in the Department table: ")

    correspondingDepartmentID = findIDOfCorrespondingDepartment(correspondingDepartmentName)

    while(correspondingDepartmentID == 0):
        print("That department is either not in the database or you have an invalid entry. Please try again ", end="")
        correspondingDepartmentName = input("Please enter the name of the department under which this faculty member will fall (i.e. \"Computer Science\"). Note that the department must already be in the Department table: ")
        correspondingDepartmentID = findIDOfCorrespondingDepartment(correspondingDepartmentName)

    EstablishConnection.addFaculty(correspondingDepartmentID, facultyName, facultyRank, educationLevel, isTenuredBool)

    # if(doubleCheck):
    #     CommitAction()
    # else:
    #     RollbackAction()

    # mycursor.execute("INSERT INTO Assignments(CourseID, AssignmentName, AssignmentDueDate) VALUES (%s, %s, %s);", (correspondingCourseID, assignmentName, assignmentDueDate,))
    # EstablishConnection.db.commit()

    print("Faculty member successfully added. NOTE: The faculty member will not be added into the database, however, until you choose to commit this change (option 9)")

def universitySchoolsDetails():
    print("Please enter the following properties of the school/college you wish to enter into the universitySchools table: ")
    print()  # formatting

    collegeName = input("Name of the school or college (i.e. \"Keck School of Medicine\"): ")
    numMajors = int(input("Number of majors in this school/college: "))
    numMinors = int(input("Number of minors in this school/college: "))
    gradDegreeOffered = input("Are graduate degrees offered through this school/college? (Y/N): ")
    gradDegreeOfferedBool = 0

    while(gradDegreeOffered != "Y" and gradDegreeOffered != "N"):  # validate input
        print("Invalid input. Please type /Y/' or /'N/'")
        gradDegreeOffered = bool(input("Is this faculty member tenured? (Y/N): "))

    if (gradDegreeOffered == "Y"):
        gradDegreeOfferedBool = 1

    EstablishConnection.addCollege(collegeName, numMajors, numMinors, gradDegreeOfferedBool)
    #
    # if (doubleCheck):
    #     CommitAction()
    # else:
    #     RollbackAction()

    # mycursor.execute("INSERT INTO Assignments(CourseID, AssignmentName, AssignmentDueDate) VALUES (%s, %s, %s);", (correspondingCourseID, assignmentName, assignmentDueDate,))
    # EstablishConnection.db.commit()

    print("School/college successfully added. NOTE: The school/college will not be added into the database, however, until you choose to commit this change (option 9)")


def findIDOfCorrespondingCourse(courseCode):
    mycursor.execute('SELECT CourseID FROM Courses WHERE CourseCode = %s AND Courses.isDeleted = 0;', (courseCode,))
    courseID = mycursor.fetchall()
    courseIDValue = 0

    #extract out the courseID, since the value returned from the DB query is a tuple

    for i in courseID:
        for j in i:
            courseIDValue = j

    # if (courseIDValue == 0):
    #     # print("Error. There is no course with that course code in the Courses database. Please enter another course code")

    return courseIDValue

def findIDOfCorrespondingFaculty(theFacultyName):
    mycursor.execute('SELECT FacultyID FROM Faculty WHERE FacultyName = %s AND Faculty.isDeleted = 0;', (theFacultyName,))
    facultyID = mycursor.fetchall()
    facultyIDValue = 0

    # extract out the courseID, since the value returned from the DB query is a tuple

    for i in facultyID:
        for j in i:
            facultyIDValue = j

    # if (facultyIDValue == 0):
        # print(
        #     "Error. There is no course with that course code in the Courses database. Please enter another course code")

    return facultyIDValue

def findIDOfCorrespondingDepartment(departmentOfCourse):
    mycursor.execute('SELECT DepartmentID FROM Department WHERE DepartmentName = %s AND Department.isDeleted = 0;', (departmentOfCourse,))
    departmentID = mycursor.fetchall()
    departmentIDValue = 0

    # extract out the courseID, since the value returned from the DB query is a tuple

    for i in departmentID:
        for j in i:
            departmentIDValue = j

    # if (departmentIDValue == 0):
    #     # print("Error. There is no course with that course code in the Courses database. Please enter another course code")

    return departmentIDValue

def findIDOfCorrespondingSchool(correspondingCollegeName):
    mycursor.execute('SELECT CollegeID FROM universitySchools WHERE CollegeName = %s AND universitySchools.isDeleted = 0;', (correspondingCollegeName,))
    collegeID = mycursor.fetchall()
    collegeIDValue = 0

    # extract out the courseID, since the value returned from the DB query is a tuple

    for i in collegeID:
        for j in i:
            collegeIDValue = j

    # if (collegeIDValue == 0):
    #     # print("Error. There is no course with that course code in the Courses database. Please enter another course code")

    return collegeIDValue


# mycursor.execute('SELECT Faculty.educationLevel, COUNT(*) as \'Count of Courses\' FROM Courses, Faculty WHERE Courses.CourseInstructorID = Faculty.FacultyID GROUP BY Faculty.educationLevel '
#                  'HAVING Faculty.educationLevel = \'Ph.D.\'')

#findNumOfAssignmentsOutStandingByCourse("United States History: 1918-present")

def deleteFromAssignments():
    idOfAssignment = int(input("What is the id of the assignment you wish to delete? "))

    mycursor.execute('UPDATE Assignments SET Assignments.isDeleted = 1 WHERE Assignments.AssignmentID = %s;', (idOfAssignment,))

def deleteFromCourses():
    idOfCourse = int(input("What is the id of the course you wish to delete? "))

    mycursor.execute('UPDATE Courses SET Courses.isDeleted = 1 WHERE Courses.CourseID = %s;', (idOfCourse,))

def deleteFromFaculty():
    idOfFaculty = int(input("What is the id of the faculty member you wish to delete? "))

    mycursor.execute('UPDATE Faculty SET Faculty.isDeleted = 1 WHERE Faculty.FacultyID = %s;', (idOfFaculty,))
    userSure = doubleCheck()
    if(userSure):
        EstablishConnection.db.commit() # commit transaction

def deleteFromDepartment():
    idOfDepartment = int(input("What is the id of the assignment you wish to delete? "))

    mycursor.execute('UPDATE Department SET Department.isDeleted = 1 WHERE Department.DepartmentID = %s;', (idOfDepartment,))

def deleteFromUniversitySchools():
    idOfCollege = int(input("What is the id of the assignment you wish to delete? "))

    mycursor.execute('UPDATE universitySchools SET universitySchools.isDeleted = 1 WHERE universitySchools.CollegeID = %s;', (idOfCollege,))


def RollbackAction():
    EstablishConnection.db.rollback()

def CommitAction():
    EstablishConnection.db.commit()

def generateReport(tuple):
    #SELECT
    #address,
    #address2,
    #address_id
    #FROM location INTO OUTFILE 'C:\ProgramData\MySQL\location.csv';
    return

# def departmentSubQuery(theDepartment):
#     # To complete down below; getting some syntax errors for the sub-query
#     mycursor.execute('SELECT COUNT(*) FROM Department WHERE DepartmentID = (SELECT DepartmentOfCourse FROM Courses INNER JOIN Assignments ON Courses.CourseID = Assignments.CourseID WHERE Assignments.AssignmentDueDate = \'2021-01-11\')')
#     results = mycursor.fetchall()

def doubleCheck():
    doubleCheck = input("Are you sure you wish to complete this update? This cannot be undone. You'll have to perform another update later on: ")

    if(doubleCheck == 'Y' or doubleCheck == 'y'):
        return 1
    else:
        return 0

def validateCourseCoude(theCourseCode):
    thePattern = "({4}) (\d{3})"
    isValid = re.match(thePattern, theCourseCode)

    if(isValid):
        return True
    else:
        return False

def validateAssignmentDueDate(theDueDate):
    thePattern = "(\d{2})-(\d{2})-(\d{4})"
    isValid = re.match(thePattern, theDueDate)

    if(isValid):
        return True
    else:
        return False

def validateNumericInput(num): # used to validate numeric inputs
    if num.isnumeric():
        return True
    else:
        return False

