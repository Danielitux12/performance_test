def validate_identification():
    while True:
        try:
            identification = int(input("\nEnter identification of the studient: "))
            if identification in range (10000,100000):
                print("Identification saved :)")
                return identification
            else:
                print("Invalid identification, please enter a five numbers corrects")
        except ValueError: print("Error, invalid identification, please try again")
def new_studient ():
    while True:
        studient_name = str (input("\nEnter name of the studient: "))
        if studient_name.isalpha():
            print("Name saved :)")
            return studient_name
        else: print("Please enter only caracters alphabetical")
def validate_age():
    while True:
        try:
            age = int(input("\nEnter age of the studient: "))
            if age > 0:
                print("Age saved :)")
                return age
            else:
                print("Invalid age, please enter a numbers positives")
        except ValueError: print("Error, invalid age, please try again")
def validate_course ():
    while True:
        try:
            course = int(input("\nEnter course of the studient: "))
            if course in range (1,13):
                print("Course saved :)")
                return course
            else:
                print("Invalid course, please enter a valid course")
        except ValueError: print("Error, invalid course, please try again")
def validate_status():
    while True:
        try:
            status = int(input("\n""Select status of the studient: "))
            if status in range (1,3):
                print("Status saved :)")
                return status
            else:
                print("Invalid status, please select a valid status")
        except ValueError: print("Error, invalid status, please try again")
def validate_option():
    while True:
        try:
            option = int(input("\nSelect an option: "))
            if option >= 1 and option <= 5:
                return option
            else:
                print("Invalid option in the range of the options, please try again")
        except ValueError: print("Error, invalid option in the range of the options, please try again")
            
    