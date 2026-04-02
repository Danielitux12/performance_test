# This validation is because I want the user to enter only 5 numbers for the "identification".
def validate_identification():
    # I use a while loop because I want the user to enter 5 valid numbers.
    while True:
        # I used try for except to prevent errors or failures.
        try:
            # I ask the user to enter a number.
            identification = int(input("\nPlease type five student IDs: "))
            # Therefore, if this number is within the range, it is accepted.
            if identification in range (10000,100000):
                # Show the user that the registered number is correct or saved :)
                print("ID saved :)")
                #Return the valid identification.
                return identification
            # If this number does not meet my range, please enter a new number.
            else:
                # Please try again because the number entered is not valid.
                print("Invalid ID, please enter five correct numbers.")
        # I used the "except" for errors, for example, the user wants to enter some word or words in alphabetical order.
        except ValueError: print("Error, please only enter a caracters numbers")

# This validation is because I want the user to only enter alphabetic characters for the "name"
def validate_name ():
    # I use a while loop because I want the user to enter only caracters alphabeticals.
    while True:
        # I ask the user to enter a name.
        student_name = str (input("\nEnter name of the studient: "))
        # I used the ".strip", ".replace" and ".isalpha" because I only want alphabetic characters.
        if student_name.strip().replace(" ","").isalpha():
            # Show the user that the registered is saved :)
            print("Name saved :)")
            # Return the valid name.
            return student_name
        # If this name does not meet my conditions, please enter a new name.
        else: print("Please enter only caracters alphabetical")

# This validation is because I want the user to enter only ages between 1 and 80 years for the "age" field.
def validate_age():
    # I use a while loop because I want the user to enter only ages between 1 and 80 years old.
    while True:
        # I used try for except to prevent errors or failures.
        try:
            # I ask the user to enter a age
            age = int(input("\nEnter age of the studient: "))
            # Therefore, if this age is within the range, it is accepted.
            if age > 0 and age <= 80:
                # Show the user the registered the "age" is correct or saved :)
                print("Age saved :)")
                # Return the valid age
                return age
            # If this age does not meet my range, please enter a new age.
            else:
                # Please try again because the age entered is not valid. 
                print("Only students under 80 are allow to register")
        # I used the "except" for errors, for example, the user wants to enter some word or words in alphabetical order.
        except ValueError: print("Error, please only enter a caracters numbers")
        
# This validations is because I want the user to enter only the default course setting when the default course settings are displayed.
def validate_course():
    # I use a while loop because I want the user to enter only default course setting
    while True:
        # I ask the user to enter a course from those they see on the list.
        course = str(input("\nEnter course of the studient: "))
        # Therefore, if this course is not on the list, it is not accepted.
        if course not in ["technology", "marketing", "desing", "finance", "crafts"]:
            # Please try again because the course entered is not valid
            print("Invalid course, please try again and enter a valid course")
        # If the above condition is not met, show the user the saved course :)
        else:
            # Show the user registered the "Course" is correct or saved.
            print("Course saved :)")
            # Return the valid course.
            return course
        
# This validations is because I want the user to enter only the default status setting when the default status settings are displayed.
def validate_status():
    # I use a while loop because I want the user to enter only default status setting.
    while True:
            # I ask the user to enter a status from those they see on the list.
            status = str(input("\n""Enter status of the studient: "))
            # Therefore, if this status is not on the list, it is not accepted.
            if status not in ["active", "inactive"]:
                # Please try again because the status entered is not valid
                print("Invalid status, please try again and select a valid status")
            # If the above condition is not met, show the user the saved status :)
            else:
                # Show the user registered the "Status" is correct or saved.
                print("Status saved :)")
                # Return the valid course.
                return status
def validate_option():
    while True:
        try:
            option = int(input("\nSelect an option: "))
            if option >= 1 and option <= 6:
                return option
            else:
                print("Invalid option in the range of the options, please try again")
        except ValueError: print("Error, invalid option in the range of the options, please try again")
def validate_studient_edit(students):
    amount_of_studients = len(students)
    while True:
        studient_for_edit = int(input("Number of the studient  you want edit"))
        if studient_for_edit in range (1,amount_of_studients):
            break
        else:
            print("Enter a valid number of the studient what you want edit")