from  services import enter_new_student,show_list_of_the_students,shearch_student,edit_information_of_the_student,edit_information_of_the_student
from validations import validate_option
# Create this list for in future i want expand this list and don't need use 1000 elifts :)
def show_options():
    list_options = ({
        "Enter new student":"option1",
        "Show list of the students":"option2",
        "Shearch student":"option3",
        "Edit information of the student":"option4",
        "Delete student":"option5",
        "Exit the program":"option6"})
    count=0
    print("\n")
    for i in list_options:
        print(f"{count+1}. {i}")
        count+=1
# Create this funtion for show the all options for the user use in this program                    
def menu (students):
    while True:
        show_options()
        option = validate_option()
        if option == 1:
            enter_new_student(students)
        elif option == 2:
            show_list_of_the_students(students)
        elif option == 3:
            shearch_student(students)
        elif option == 4:
            edit_information_of_the_student(students)
        elif option == 5:
            print()
        elif option == 6:
            print("Thanks for using the program :)")