from validations import validate_identification,new_studient,validate_age,validate_course,validate_status

def show_options_status ():
    status_list = {
        "Active":"opcion1",
        "Inactive":"opcion2"}
    count=0
    for i in status_list:
        print(f"{count+1}. {i}")
        count+=1
def enter_new_studient(studients):
    identification = validate_identification()
    studient_name = new_studient()
    age = validate_age()
    course = validate_course()
    show_options_status()
    status =validate_status()
    studients.append({
        "identification":identification,
        "name":studient_name,
        "age":age,
        "course":course,
        "status":status})
def show_list_of_the_studients(studients):
    amount_of_studients = len(studients)
    if amount_of_studients > 0:
        numer_studient = 0
        print("\nSTUDIENTS\n")
        for i in studients:
            print(f"{numer_studient+1}. {i["identification"]} - {i["name"]} - {i["age"]} - {i["course"]} - {i["status"]}")
            numer_studient+=1
    else: print("\n""The list of the studients is empty""\n")