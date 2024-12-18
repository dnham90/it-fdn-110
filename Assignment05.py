# ------------------------------------------------------------------------------------------ #
# Title: Assignment05
# Desc: This assignment demonstrates using dictionaries, files, and exception handling
# Change Log: (Who, When, What)
#   DNham,11/13/2024,Created Script
# ------------------------------------------------------------------------------------------ #
from csv import excel

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
# Define the Data Constants
FILE_NAME: str = "Enrollments.csv"

# Define the Data Variables and constants
student_first_name: str = ''  # Holds the first name of a student entered by the user.
student_last_name: str = ''  # Holds the last name of a student entered by the user.
course_name: str = ''  # Holds the name of a course entered by the user.
student_data: dict[str,str] = {}  # one row of student data
students: list = []  # a table of student data
csv_data: str = ''  # Holds combined CSV data. Note: Remove later since it is NOT needed with the JSON File

menu_choice: str  # Hold the choice made by the user.
parts:list[str]

# When the program starts, read the file data into a list of lists (table)
# Extract the data from the file
try:
    file = open(FILE_NAME, "r")
    for row in file.readlines():
        # Transform the data from the file
        student_data = row.split(',')
        student_data = [student_data[0], student_data[1], student_data[2].strip()]
        # Load it into our collection (list of lists)
        students.append(student_data)
    file.close()
except FileNotFoundError:
    print('File not found. Creating...')
    open(FILE_NAME, 'w')
except Exception as e:
    print('Unknown exception. Resetting roster...')
    students = []
    print(type(e), e, sep='\n')
finally:
    if file and not file.closed:
        file.close()

# Present and Process the data
while (True):

    # Present the menu of choices
    print(MENU)
    menu_choice = input("What would you like to do: ")

    # Input user data
    if menu_choice == "1":  # This will not work if it is an integer!
        try:
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name.isalpha():
                raise ValueError('First_name must be alphabetic')
            student_last_name = input("Enter the student's last name: ")
            if not student_last_name.isalpha():
                raise ValueError('Last_name must be alphabetic')
            course_name = input("Please enter the name of the course: ")
            student_data = [student_first_name,student_last_name,course_name]
            students.append(student_data)
            print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
        except ValueError as e:
            print(e)

    # Present the current data
    elif menu_choice == "2":

        # Process the data to create and display a custom message
        print("-"*50)
        for student in students:
            print(f"Student {student['first_name']} {student['last_name']} is enrolled in {student['course_name']}")
        print("-"*50)
        continue

    # Save the data to a file
    elif menu_choice == "3":
        try:
            file = open(FILE_NAME, "w")
            for student in students:
                csv_data = f"{student['first_name']},{student['last_name']},{student['course_name']}\n"
                file.write(csv_data)

            print("The following data was saved to file!")
            for student in students:
                print(f"Student {student['first_name']} {student['last_name']} is enrolled in {student['course_name']}")
        except Exception as e:
            print('Error saving data to file')
    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop
    else:
        print("Please only choose option 1, 2, or 3")

print("Program Ended")
