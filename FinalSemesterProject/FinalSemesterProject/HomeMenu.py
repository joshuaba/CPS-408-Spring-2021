import InsertDeleteValues
import EstablishConnection
import DBQueries
import mysql.connector
from faker import Faker
import csv
import datetime


def mainMenu():
    print("Welcome to the assignment database")

    while(True):

        print() # formatting

        print("You have the following options:\n\
                  1: Display all assignments currently in the database\n\
                  2: Display records from the other tables\n\
                  3: Filter assignments by certain parameters (date due, instructor, class, department, etc.)\n\
                  4: Add in a new record\n\
                  5: Delete a record\n\
                  6: Create a separate table with specified information\n\
                  7: Generate table to CSV file\n\
                  8: Undo all previous changes\n\
                  9: Commit all current changes (NOTE: ONCE YOU SELECT THIS OPTION ALL CURRENT CHANGES WILL BE WRITTEN TO THE DB AND THE ACTION CANNOT BE UNDONE")

        print() # formatting

        userOption = input("Please input the number associated with the option you would like to perform (type \"Q\" or \"q\" to exit the program: ")

        if((userOption) == 'Q' or userOption == 'q'):
            print() #formatting
            print("Exiting")
            break

        userOption = int(userOption)

        if(userOption == 1):
            EstablishConnection.printAllAssignments() # print out all of the assignments currently in the database
        elif(userOption == 2):
            repeat = True
            while(repeat):
                tableOutput = int(input("From which table would you like to print the records: \n\
                                      1: Faculty\n\
                                      2: Courses\n\
                                      3: Department\n\
                                      4: Schools\n\
                                      Option: "))
                if(tableOutput == 1):
                    EstablishConnection.displayFacultyData()
                    repeat = False
                elif(tableOutput == 2):
                    EstablishConnection.displayCourseData()
                    repeat = False
                elif(tableOutput == 3):
                    EstablishConnection.displayDepartmentData()
                    repeat = False
                elif(tableOutput == 4):
                    EstablishConnection.displaySchoolData()
                    repeat = False
                else:
                    print("Unrecognized input. Please type a value from 1 - 4, depending on the table from which you would like to print the records")

        elif(userOption == 3):
            detailedView = input("Would you like to see a detailed view of the assignments (as in instructor of the course, course name, etc.? \n\
            Typing \'N\' will only print out the Assignment and its related details rather than a detailed list including instructor details, course details, etc: ")

            if(detailedView == 'Y' or detailedView == 'y'):
                repeat = True
                while (repeat):
                    parameterChosen = int(input("Which details would you like to print/output: \n\
                                             1: Assignments, Courses, and Department\n\
                                             2: Assignments, Courses, Faculty\n\
                                             3: Assignments, Courses, Department, and Specific College\n\
                                             4: Assignments and Courses Only \n\
                                             Option: "))
                    if (parameterChosen == 1):
                        departmentName = input("Name of Department (case sensitive): ")
                        DBQueries.printAssignmentsCoursesDepartmentInfo(departmentName)
                        repeat = False
                    elif (parameterChosen == 2):
                        facultyName = input("Name of faculty member (FirstName LastName with a space): ")
                        DBQueries.printAssignmentsCoursesFacultyInfo(facultyName)
                        repeat = False
                    elif (parameterChosen == 3):
                        collegeName = input("Name of college from which you would like to filter the assignments outstanding: ")
                        # InsertValues.filterAssignmentsOutstandingByDepartment(departmentName)
                        DBQueries.printAssignmentsCoursesDepartmentCollegeInfo(collegeName)
                        repeat = False
                    elif (parameterChosen == 4):
                        courseName = input("Name of course from which you would like to filter the assignments outstanding: ")
                        DBQueries.printAssignmentsCoursesInfo(courseName)
                        repeat = False
                    else:
                        print(
                            "Unrecognized input. Please type a value from 1 - 4, depending on the table from which you would like to print the records")
            else:
                repeat = True
                while(repeat):
                    parameterChosen = int(input("By which parameter would you like to filter the assignments outstanding: \n\
                                     1: Faculty\n\
                                     2: Courses\n\
                                     3: Department\n\
                                     4: Schools \n\
                                     Option: "))

                    if (parameterChosen == 1):
                        facultyName = input("Name of faculty member: MUST BE in FirstName LastName format (with a space) ")
                        DBQueries.filterOutstandingAssignmentsByFaculty(facultyName)
                        repeat = False
                    elif (parameterChosen == 2):
                        courseName = input("Name of course: ")
                        DBQueries.filterOutstandingAssignmentsByCourse(courseName)
                        repeat = False
                    elif (parameterChosen == 3):
                        departmentName = input("Name of department: ")
                        # InsertValues.filterAssignmentsOutstandingByDepartment(departmentName)
                        DBQueries.filterOutstandingAssignmentsByDepartment(departmentName)
                        repeat = False
                    elif (parameterChosen == 4):
                        schoolName = input("School/College Name: ")
                        DBQueries.filterOutstandingAssignmentsBySchool(schoolName)
                        repeat = False
                    else:
                        print(
                            "Unrecognized input. Please type a value from 1 - 4, depending on the table from which you would like to print the records")

        elif(userOption == 4):
            repeat = True
            while (repeat):
                tableToAdd = int(input("Please input the option of the table to which you wish to add: \n\
                                             1: Assignments\n\
                                             2: Faculty\n\
                                             3: Courses\n\
                                             4: Department\n\
                                             5: Schools\n\
                                             Option: "))

                if (tableToAdd == 1):
                    InsertDeleteValues.theAssignmentDetails()
                    repeat = False
                elif (tableToAdd == 2):
                    InsertDeleteValues.theFacultyDetails()
                    repeat = False
                elif (tableToAdd == 3):
                    InsertDeleteValues.theCourseDetails()
                    repeat = False
                elif (tableToAdd == 4):
                    InsertDeleteValues.theDepartmentDetails()
                    repeat = False
                elif (tableToAdd == 5):
                    InsertDeleteValues.universitySchoolsDetails()
                else:
                    print(
                        "Unrecognized input. Please type a value from 1 - 4, depending on the table from which you would like to print the records")

        elif(userOption == 5):
            repeat = True
            while (repeat):
                tableToAdd = int(input("Please input the option of the table to which you wish to delete a record: \n\
                                        1: Assignment\n\
                                        2: Faculty\n\
                                        3: Courses\n\
                                        4: Department\n\
                                        5: Schools\n\
                                        Option: "))

                if (tableToAdd == 1):
                    InsertDeleteValues.deleteFromAssignments()
                    repeat = False
                elif (tableToAdd == 2):
                    InsertDeleteValues.deleteFromFaculty()
                    repeat = False
                elif (tableToAdd == 3):
                    InsertDeleteValues.deleteFromCourses()
                    repeat = False
                elif (tableToAdd == 4):
                    InsertDeleteValues.deleteFromDepartment()
                    repeat = False
                elif (tableToAdd == 5):
                    InsertDeleteValues.deleteFromUniversitySchools()
                else:
                    print(
                        "Unrecognized input. Please type a value from 1 - 4, depending on the table from which you would like to print the records")

        elif(userOption == 6):
            specifics = input("From which tables would you like to pull information: \n\
                             1: Assignments and Courses\n\
                             2: Assignments and Faculty\n\
                             3: Assignments and Department\n\
                             4: Assignments and College")

        elif(userOption == 7):
            repeat = True
            while (repeat):
                selection = input("Which table would you like to have a report of? (Assignments, Courses, Departments, Faculty, Schools)")
                if selection.lower() == "assignments":
                    EstablishConnection.returnAssignments()
                elif selection.lower() == "courses":
                    EstablishConnection.returnCourses()
                elif selection.lower() == "departments":
                    EstablishConnection.returnDepartment()
                elif selection.lower() == "faculty":
                    EstablishConnection.returnFaculty()
                elif selection.lower() == "schools":
                    EstablishConnection.returnSchool()
                elif selection.lower() == "exit":
                    repeat = False
                else:
                    print("Invalid input. Type \'exit\' to quit.")


        elif(userOption == 8):
            InsertDeleteValues.CommitAction() # Commit all of the actions the user has taken

        elif(userOption == 9):
            InsertDeleteValues.RollbackAction() # Rollback all of the actions the user has taken

if __name__ == "__main__":
    mainMenu()


