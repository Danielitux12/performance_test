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
                #Return the valid identification.
                return identification
            # If this number does not meet my range, please enter a new number.
            else:
                # Please try again because the number entered is not valid.
                print("Invalid ID, please enter five correct numbers.")
        # I used the "except" for errors, for example, the user wants to enter some word or words in alphabetical order.
        except ValueError: print("Error, please only enter a caracters numbers")

# This validation is because I want the user to only enter alphabetic characters for the "name"
def validate_name():
    # I use a while loop because I want the user to enter only caracters alphabeticals.
    while True:
        # I ask the user to enter a name.
        student_name = str (input("\nEnter name of the studient: "))
        # I used the ".strip", ".replace" and ".isalpha" because I only want alphabetic characters.
        if student_name.strip().replace(" ","").isalpha():
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
            age = int(input("\nEnter age of the student: "))
            # Therefore, if this age is within the range, it is accepted.
            if age > 0 and age <= 80:
                # Return the valid age
                return age
            # If this age does not meet my range, please enter a new age.
            else:
                # Please try again because the age entered is not valid. 
                print("Only students under 80 are allow to register")
        # I used the "except" for errors, for example, the user wants to enter some word or words in alphabetical order.
        except ValueError: print("Error, please only enter a caracters numbers")
        
# This validation is because I want the user to enter only the default course setting when the default course settings are displayed.
def validate_course():
    # I use a while loop because I want the user to enter only default course setting
    while True:
        # I ask the user to enter a course from those they see on the list.
        course = str(input("\nEnter course of the student: "))
        # Therefore, if this course is not on the list, it is not accepted.
        if course not in ["technology", "marketing", "desing", "finance", "crafts"]:
            # Please try again because the course entered is not valid
            print("Invalid course, please try again and enter a valid course")
        # If the above condition is not met, show the user the saved course :)
        else:
            # Return the valid course.
            return course
        
# This validation is because I want the user to enter only the default status setting when the default status settings are displayed.
def validate_status():
    # I use a while loop because I want the user to enter only default status setting.
    while True:
            # I ask the user to enter a status from those they see on the list.
            status = str(input("\n""Enter status of the student: "))
            # Therefore, if this status is not on the list, it is not accepted.
            if status not in ["active", "inactive"]:
                # Please try again because the status entered is not valid
                print("Invalid status, please try again and select a valid status")
            # If the above condition is not met, show the user the saved status :)
            else:
                # Return the valid course.
                return status

# This validation is because I want the user enter only numbers from 1 to 6.
def validate_option():
    # I use a while loop because I want the user to enter only options between 1 and 6.
    while True:
        # I used try for except to prevent errors or failures.
        try:
            # I ask the user to enter an option.
            option = int(input("\nSelect an option: "))
            # Therefore, if this option is within the range, it is accepted.
            if option >= 1 and option <= 6:
                # Return the valid option
                return option
            # If this option does not meet my range, please enter a new option.
            else:
                # Please try again because the option entered is not valid.
                print("Invalid option in the range of the options, please try again")
        # I used the "except" for errors, for example, the user wants to enter some word or words in alphabetical order.        
        except ValueError: print("Error, invalid option in the range of the options, please try again")