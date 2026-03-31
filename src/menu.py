from  services import enter_new_studient,show_list_of_the_studients
from validations import validate_option

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
                        
def menu (studients):
    while True:
        show_options()
        option = validate_option()
        if option == 1:
            enter_new_studient(studients)
        elif option == 2:
            show_list_of_the_studients(studients)