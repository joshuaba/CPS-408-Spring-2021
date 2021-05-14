import mysql.connector
from faker import Faker
import csv

db = mysql.connector.connect(
    host="34.94.39.105",
    user="mydbappuser",
    password="4IserveHim!!",
    database="Assignments"
)

fake = Faker()

#faker material to generate fake components of the various attributes of the database (i.e. assignments, courses, faculty names/ids, etc.)
majorList = ['Computer Science', 'Software Engineering', 'Biological Sciences', 'Zoology', 'History', 'Creative Writing', 'English', 'Accounting', 'Finance', 'Business Administration', 'Literary Studies',
                  'Chemistry', 'Physics', 'Automotive Design', 'Optics', 'Electrical Engineering', 'Broadcast Journalism', 'Biomedical Sciences', 'Biomedical Engineering', 'Chemical Engineering', 'Computational Biology',
             'Applied Mathematics', 'Oceanography', 'Marine Biology', 'Earth Science']

departmentList = ['Social Sciences', 'English', 'Creative Writing', 'Chemistry', 'Biological Sciences', 'Computer Science', 'Mathematics', 'Film and Production', 'Engineering', 'Computations', 'Library Studies',
                  'Archaelogy', 'Anthropology', 'Accounting', 'Finance', 'Business Administration']

schoolList = ['School of Engineering', 'School of Sciences', 'School of Arts and Humanities', 'School of Social Sciences', 'Durk School of Communication', 'Johnson School of Oceanography', 'Gould School of Law',
              'Keck School of Medicine', 'Leonard Davis School of Gerontology', 'Dornsife College of Letters, Arts, and Sciences', 'School of Architecture', 'Merage School of Business', 'Argyros School of Economics',
              'Schmid College of Science and Technology', 'Fowler School of Engineering', 'Fowler School of Law']

courseNameList = ['Computer Science I', 'Computer Science II', 'Visual Programming', 'Electrical Engineering Fundamentals', 'Hardware Design', 'Circuitry', 'Embedded Engineering', 'Embedded Systems',
                  'Creative Writing I', 'Creative Writing II', 'Creative Writing Seminar: Telling Stories', 'Advanced Creative Writing in Non-Fiction', 'United States History: 1492-1918',
                  'United States History: 1918-present', 'World History I', 'World History II', 'History of Vietnam', 'History of Korea', 'Literary Techniques', 'English Vocabulary',
                  'Counseling Fundamentals', 'Advanced Linear Algebra', 'Topography', 'Advanced Numerical Methods', 'Advanced Linear Algebraic Systems', 'Hardware Design', 'Computer Information Systems']

courseCodeList = ['CPSC 230', 'CPSC 231', 'CPSC 357', 'CPSC 392', 'CPSC 402', 'CPSC 380', 'CPSC 400', 'HIST 209', 'HIST 201', 'HIST 202', 'ENG 101', 'ENG 102', 'ENG 107', 'ENG 109', 'ART 170', 'ART 190', 'ARCHIT 208',
                  'ARCHIT 290', 'ARCHIT 101', 'ARCHIT 102', 'CRIM 107', 'CRIM 180', 'LITSTU 190', 'LITSTU 217']

assignmentName = ['Semester Project', 'Homework Assignment', 'Quarter Project', 'Section Quiz', 'Chapter Review Assignment', 'Writing Assignment', 'Literary Analysis Assignment', 'I-Search Essay', 'Programming Assignment',
                  'Database Assignment', 'Engineering Assignment', 'Research Essay', 'Historical Analysis Essay', 'Journal report', 'Clinical Lab']

facultyRank = ['Assistant Professor', 'Associate Professor', 'Professor', 'Instructor', 'Lecturer', 'Adjunct Faculty']

def generateData(): # we will call this function to generate random data that we will then assign to the normalized tables (5) that we have created

    #user input is below
    csvFileName = input("Please enter the name of the file to which you would like to export the csv data")
    numOfValuesToGenerate = int(input("Please enter the number of records you wish to be created"))

    csv_file = open(csvFileName, 'w') # open the csv file csvFileName in write 'w' mode
    writer = csv.writer(csv_file) # create the writer object with which we will write the fake data to the csv_file
    writer.writerow(["Assignment Name", "Assignment Due Date", "Course Name", "Course Code", "Faculty Name", "Faculty Rank", "Tenured/Tenure Track?", "Department Name", "School/College Name", "NumOfMajors", "NumOfMinors", "GradDegreeOffered?"])

    for x in range(0, numOfValuesToGenerate): # generate fake data. We will generate as many rows as the user specified in numOfValuesToGenerate
        writer.writerow([fake.word(ext_word_list=assignmentName), fake.date_this_year(), fake.word(ext_word_list=courseNameList), fake.word(ext_word_list=courseCodeList), fake.name(), fake.word(ext_word_list=facultyRank), fake.boolean(),
                         fake.word(ext_word_list=departmentList), fake.word(ext_word_list=schoolList), fake.pyint(0, 250, 1), fake.pyint(0, 250, 1), fake.boolean()])

    return csvFileName

def importData(csvFileToParse):
    mycursor = db.cursor()

    with open(csvFileToParse) as csvfile:
        reader = csv.DictReader(csvfile) # create the reader object with which we will read in the contents of the csv_file

        for row in reader:

            #insert content into the universitySchools table
            print("Importing school/college data and information")

            mycursor.execute("INSERT INTO universitySchools(CollegeName, NumOfMajors, NumOfMinors, gradDegreeOffered) VALUES(%s,%s,%s,%s);", (row['School/College Name'], row['NumOfMajors'], row['NumOfMinors'], row['GradDegreeOffered?']))
            db.commit() # commit the previous command

            collegeID = mycursor.lastrowid # this will be used to maintain referential integrity and as the foreign key for the entry in the Department table

            #insert content into the Department table
            print("Importing Department data and information")
            mycursor.execute("INSERT INTO Department(DepartmentName, CollegeID) VALUES(%s, %s);", (row['Department Name'], collegeID))
            db.commit()

            departmentID = mycursor.lastrowid # this will be used to maintain referential integrity and as the foreign key for the entry in the Faculty table

            #insert content into the Faculty table
            print("Importing Faculty data and information")
            mycursor.execute("INSERT INTO Faculty(DepartmentID, FacultyName, FacultyRank, isTenured) VALUES(%s, %s, %s, %s);", (departmentID, row['Faculty Name'], row['Faculty Rank'], row['Tenured/Tenure Track?']))
            db.commit()

            facultyID = mycursor.lastrowid # this will be used to maintain referential integrity and as the foreign key for the entry in the Courses table

            #insert content into the Courses table
            print("Importing Course data and information")
            mycursor.execute("INSERT INTO Courses(CourseInstructorID, DepartmentOfCourse, CourseName, CourseCode) VALUES(%s, %s, %s, %s);", (facultyID, departmentID, row['Course Name'], row['Course Code']))
            db.commit()

            courseID = mycursor.lastrowid # this will be used to maintain referential integrity and as the foreign key for the entry in the Assignments table

            mycursor.execute("ALTER TABLE Assignments AUTO_INCREMENT = 1;")
            db.commit()

            #insert content into the Assignments table
            print("Importing Assignment data and information")
            mycursor.execute("INSERT INTO Assignments(CourseID, AssignmentName, AssignmentDueDate) VALUES(%s, %s, %s);",(courseID, row['Assignment Name'], row['Assignment Due Date']))
            db.commit()

            print() # formatting

if __name__ == "__main__":
    print("The goal of this program is to auto-generate data that would be found in an assignment database for a school/university and import the auto-generated data into a normalized, 3NF database")
    print() # formatting
    fileToProcess = generateData()
    importData(fileToProcess)
