import sqlite3
import re # for regular expression checking (mobile phone number and gpa)
import pandas as pd


conn = sqlite3.connect('./student.db')
mycursor = conn.cursor()

#helper functions are below

def userExists(idNum):
    result = conn.execute("SELECT COUNT(*) FROM Student S WHERE S.StudentID = ?", idNum)
    conn.commit()

    # making sure the requested student ID# is in the database
    for i in result:
        for j in i:
            if j == 0:  # if found == 0
                print("Error! No student with requested ID # found in the Database. Please try again")
                return 0
    else:
        return 1

def studentAlreadyExists(idNum):
    idNumList = [idNum]
    result = conn.execute("SELECT COUNT(*) FROM Student S WHERE S.StudentID = ?", idNumList)
    conn.commit()


    # making sure the requested student ID# is not already in the database
    for i in result:
        for j in i:
            if j == 1:  # if found == 0
                print("Error! A student with that ID number already exists. Please select a different ID number and try again.")
                return 1
    else:
        return 0

def stringNotEmpty(value):
    if value == "":
        print("Value cannot be empty. All input fields are required")
        exit(1)

#the function below is used primarily with the numerical data to ensure the user does not type in invalid data (ex. user types in "hello" for student GPA)
def validateInput(num):
    if num.isnumeric():
        return True
    else:
        print("Error on one of the numeric inputs. Please check the inputs")
        exit(1)

#used to validate the GPA data that the user passes in when requested
def validateGPA(num):
    pattern = "^\d{1}.\d{1}"
    isValid = re.match(pattern, num)

    if isValid:
        return True
    else:
        print("Error in GPA. Please check the input")
        exit(1)

def validatePhoneNum(num):
    pattern = "\((\d{3})\) (\d{3})-(\d{4})" # for mobile phone number
    isValid = re.match(pattern, num)

    if isValid:
        return True
    else:
        print("Error in phone number. Please check the input")
        exit(1)

# begin application functions to be used in main method
def searchDB():
    mycursor = conn.execute("SELECT * FROM Student")
    conn.commit()

    for i in mycursor:
        print(i)

def createNewStudent():
    stuValues = [] # an empty list which will contain the numeric properties/values of the new student being added to the student DB. This will be used in the below function to validate the numeric parameters/values
    print("Please input the following parameters for the new student: StudentID Number, FirstName, LastName, GPA, Major, FacultyAdvisor, Address (only street address), City, State, ZIP Code, MobilePhoneNumber")

    stuID = input("Please enter the student ID Number, then press \'Enter\'")
    validateInput(stuID)
    #below we check to make sure that the student ID # does not already exist in the DB. Since student ID# is the primary key, it cannot be duplicated. The db will already do this, but here we make it pretty for the user
    if(studentAlreadyExists(stuID)):
        return 1
    stuValues.append(stuID)

    fName = input("Please enter the firstname of the student, then press \'Enter\'")
    stuValues.append(fName)

    lName = input("Please enter the lastname of the student, then press \'Enter\'")
    stuValues.append(lName)

    gpa = input("Please enter the GPA of the student, rounded to the nearest tenth")
    validateGPA(gpa)
    stuValues.append(gpa)

    major = input("Please enter the student's major")
    stuValues.append(major)

    facultyAdvisor = input("Please enter the first and last name of the student's faculty advisor. If the student has no faculty advisor, enter \'None\'")
    stuValues.append(facultyAdvisor)

    address = input("Please enter the street address (ONLY) of the student")
    stuValues.append(address)

    city = input("Please enter the student's city that pertains to his/her street address")
    stuValues.append(city)

    state = input("Please enter the student's state that pertains to his/her street address")
    stuValues.append(state)

    zip = input("Please enter the student's ZIP code that pertains to his/her street address")
    #the below conditional checks to make sure that the zip code is five digits in length
    if len(zip) != 5:
        print("Zip code must be 5 digits")
        return 1
    validateInput(zip)
    stuValues.append(zip)

    phonenum = input("Please enter the student's mobile phone number, in the following format: (xxx) xxx-xxxx. You MUST input the phone number in this format or the program will throw an error")
    validatePhoneNum(phonenum)
    stuValues.append(phonenum)

    #below we are checking to make sure the user did not leave any fields blank
    for i in stuValues:
        stringNotEmpty(i)

    #if the user is being added, he is obviously not deleted, so set isDeleted to False (or 0)
    stuValues.append(False)

    conn.execute("INSERT INTO Student VALUES(?,?,?,?,?,?,?,?,?,?,?,?)", stuValues)
    conn.commit()

    print("Student with id {} added".format(stuID))


def updateStudent():
    IDNumList = [] # list to be used in conjunction with the SQL statement below
    IDNum= input("Please input the ID# of the student you would like to update: ")
    validateInput(IDNum) # validate the ID #
    int(IDNum) # type casting
    IDNumList.append(IDNum)
    # if the user does not exist, return a 1, indicating an error
    if (not userExists(IDNumList)):
        return 1

    majorUpdate = input("Would you like to update student's major? (Y/N)")
    advisorUpdate = input("Would you like to update student's faculty advisor? (Y/N)")
    mobilephoneUpdate = input("Would you like to update student's mobile phone number? (Y/N)")

    if majorUpdate == "Y" or majorUpdate == "y":
        queryParams = [] # list to be used in conjunction with the SQL statement below
        newMajor = input("What is the student's new major?")
        queryParams.append(newMajor)
        queryParams.append(IDNum)
        conn.execute("UPDATE Student SET Major = ? WHERE Student.StudentID = ?", queryParams)
        conn.commit()  # commit
        print("Major field has been updated")

    if advisorUpdate == "Y" or advisorUpdate == "y":
        queryParams = []  # list to be used in conjunction with the SQL statement below
        newFacultyAdvisor = input("Who is the student's new faculty advisor? Enter the first and last name of the faculty member")
        queryParams.append(newFacultyAdvisor)
        queryParams.append(IDNum)
        conn.execute("UPDATE Student SET FacultyAdvisor = ? WHERE Student.StudentID = ?", queryParams)
        conn.commit()  # commit
        print("Faculty advisor field has been updated")


    if mobilephoneUpdate == "Y" or mobilephoneUpdate == "y":
        queryParams = []  # list to be used in conjunction with the SQL statement below
        newMobilePhone = input("What is the student's new mobile phone number? You must enter the phone number in the following format: (xxx) xxx-xxxx or the program will reject the update")
        validatePhoneNum(newMobilePhone) #validate the new mobile phone number
        queryParams.append(newMobilePhone)
        queryParams.append(IDNum)
        conn.execute("UPDATE Student SET MobilePhoneNumber = ? WHERE Student.StudentID = ?", queryParams)
        conn.commit()  # commit
        print("Mobile Phone Number field has been updated")

def deleteStudentByID():
    IDNumList = []  # list to be used in conjunction with the SQL statement below
    IDNum = input("Please input the ID# of the student you would like to delete: ")
    validateInput(IDNum)  # validate the ID #
    int(IDNum)  # type casting
    IDNumList.append(IDNum)
    if (not userExists(IDNumList)):
        return 1
    # result = conn.execute("SELECT COUNT(*) FROM Student S WHERE S.StudentID = ?", IDNumList)
    # conn.commit()
    #
    # # making sure the requested student ID# is in the database
    # for i in result:
    #     for j in i:
    #         if j == 0:  # if found == 0
    #             print("Error! No student with requested ID # found in the Database. Please try again")
    #             return 0

    # if the student with the requested ID # is in the database
    queryParams = [1, IDNum] # set isDeleted to True (or 1)
    conn.execute("UPDATE Student SET isDeleted =  ? WHERE Student.StudentID = ?", queryParams) # delete the student with the requested student id # from the list of students in the database
    conn.commit()
    print("Student with ID number: {} has been deleted".format(queryParams[1]))

def searchStudentsByAttribute():
    searchParam = input("How would you like to search students? Type Major, GPA, City, State or Advisor. NOTE: Nothing returned indicates that there are no students matching the requested criteria/attributes")

    if searchParam == "Major":
        majorToSearch = input("What is the major by which you would like to search the student DB?")
        major = [majorToSearch]
        cursor = conn.execute("SELECT * FROM Student S WHERE S.Major = ?", major)

        for i in cursor:
            print(i)

    elif searchParam == "GPA":
        GPAToSearch = input("What is the GPA by which you would like to search the student DB?")
        validateGPA(GPAToSearch)
        theGPA = [GPAToSearch]
        cursor = conn.execute("SELECT * FROM Student S WHERE S.GPA = ?", theGPA)

        for i in cursor:
            print(i)

    elif searchParam == "City":
        cityToSearch = input("What is the city by which you would like to search the student DB?")
        city = [cityToSearch]
        cursor = conn.execute("SELECT * FROM Student S WHERE S.City = ?", city)

        for i in cursor:
            print(i)

    elif searchParam == "State":
        stateToSearch = input("What is the state by which you would like to search the student DB?")
        state = [stateToSearch]
        cursor = conn.execute("SELECT * FROM Student S WHERE S.State = ?", state)

        for i in cursor:
            print(i)

    elif searchParam == "Advisor":
        advisorToSearch = input("What is the name of the faculty advisor (first and last name) by which you would like to search the student DB?")
        advisor = [advisorToSearch]
        cursor = conn.execute("SELECT * FROM Student S WHERE S.Major = ?", advisor)

        for i in cursor:
            print(i)



if __name__ == "__main__":
    userOption = int(input("Welcome to the student database program. From here, you will be able to insert, update, delete, or search your students that are currently in the student database. \n "
                           "Type \'0\' to quit or please indicate the option you would like to perform by typing the number associated with that option: \n 1: Display all students currently in the database as well as their attributes \n 2: Add in a new student into the database"
          "\n 3: Update a current student (requires the student ID number) \n 4: Delete student by student ID number \n 5: Search/Display students by either Major, GPA, City, State, or Advisor."))

    while userOption != 0:

        if userOption == 1:
            searchDB()
            print() # formatting
            print("Please note that a 0 in the last attribute field of the student indicates that the student is not deleted in the database, while a value of 1 indicates the student is deleted from the database")
            # user clarification in above print statement
            print() # formatting
            userOption = int(input("Please type another option, or \'0\' to quit.\n 1: Display all students currently in the database as well as their attributes \n 2: Add in a new student into the database"
            "\n 3: Update a current student (requires the student ID number) \n 4: Delete student by student ID number \n 5: Search/Display students by either Major, GPA, City, State, or Advisor."))


        elif userOption == 2:
            createNewStudent()
            print() # formatting
            userOption = int(input("Please type another option, or \'0\' to quit.\n 1: Display all students currently in the database as well as their attributes \n 2: Add in a new student into the database"
            "\n 3: Update a current student (requires the student ID number) \n 4: Delete student by student ID number \n 5: Search/Display students by either Major, GPA, City, State, or Advisor."))

        elif userOption == 3:
            updateStudent()
            print() # formatting
            userOption = int(input("Please type another option, or \'0\' to quit.\n 1: Display all students currently in the database as well as their attributes \n 2: Add in a new student into the database"
            "\n 3: Update a current student (requires the student ID number) \n 4: Delete student by student ID number \n 5: Search/Display students by either Major, GPA, City, State, or Advisor."))

        elif userOption == 4:
            deleteStudentByID()
            print() # formatting
            userOption = int(input("Please type another option, or \'0\' to quit.\n 1: Display all students currently in the database as well as their attributes \n 2: Add in a new student into the database"
            "\n 3: Update a current student (requires the student ID number) \n 4: Delete student by student ID number \n 5: Search/Display students by either Major, GPA, City, State, or Advisor."))

        elif userOption == 5:
            searchStudentsByAttribute()
            print() # formatting
            userOption = int(input("Please type another option, or \'0\' to quit.\n 1: Display all students currently in the database as well as their attributes \n 2: Add in a new student into the database"
            "\n 3: Update a current student (requires the student ID number) \n 4: Delete student by student ID number \n 5: Search/Display students by either Major, GPA, City, State, or Advisor."))

        elif userOption == 0:
            print("Exitting program. Good-bye!")
            exit(0)

        else:
            print("Input not recognized. Please type a value between 1 and 5 (inclusive)")
            print() # formatting
            userOption = int(input(
                "Please type another option, or \'0\' to quit.\n 1: Display all students currently in the database as well as their attributes \n 2: Add in a new student into the database"
                "\n 3: Update a current student (requires the student ID number) \n 4: Delete student by student ID number \n 5: Search/Display students by either Major, GPA, City, State, or Advisor."))
            continue # go back to the top of the while loop

