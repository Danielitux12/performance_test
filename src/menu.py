from  services import enter_new_studient,show_list_of_the_studients,shearch_studient,edit_information_of_the_studient
from validations import validate_option

# Create this list for in future i want expand this list and don't need use 1000 elifts :)
def show_options():
    list_options = {
        "Enter new studient":"option1",
        "Show list of the studients":"option2",
        "Shearch studient":"option3",
        "Edit information of the studient":"option4",
        "Delete studient":"option5",
        "Exit the program":"option6"}
    count=0
    print("\n")
    for i in list_options:
        print(f"{count+1}. {i}")
        count+=1
# Create this funtion for show the all options for the user use in this program                    
def menu (studients):
    while True:
        show_options()
        option = validate_option()
        if option == 1:
            enter_new_studient(studients)
        elif option == 2:
            show_list_of_the_studients(studients)
        elif option == 3:
            shearch_studient()
        elif option == 4:
            edit_information_of_the_studient(studients)