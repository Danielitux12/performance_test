from validations import validate_identification,validate_name,validate_age,validate_course,validate_status,validate_studient_edit

# Whit this funtion i show the user 2 options for the enter tipe of the status studient
def show_options_status ():
    # Create this list for in future i want expand this list and use 1000 ilefts :)
    status_list = {
        "Active":"option1",
        "Inactive":"option2"}
    count=0
    # I walk this list and show the options for the user and her select correct
    for i in status_list:
        print(f"{count+1}. {i}")
        count+=1
        
def show_options_course ():
    # Create this list for in future i want expand this list and use 1000 ilefts :)
    course_list = {
        "technology":"option1",
        "marketing" :"option2",
        "desing"    :"option3",
        "finance"   :"option4",
        "crafts"    :"option5"}
    count=0
    # I walk this list and show the options for the user and her select correct
    for i in course_list:
        print(f"{count+1}. {i}")
        count+=1
        
# Whit this function added the all dates for the new studient in the list studients, and use parameter "studients" because this list is ubicate in "main"
def enter_new_studient(students):
    identification = validate_identification()
    studient_name = validate_name()
    age = validate_age()
    show_options_course()
    course = validate_course()
    show_options_status()
    status =validate_status()
    students.append({
        "identification":identification,
        "name":studient_name,
        "age":age,
        "course":course,
        "status":status})
# Whit this funtion i show the user all studients in list whit "identification, name, age, course and status"
def show_list_of_the_studients(students):
    amount_of_studients = len(students)
    if amount_of_studients > 0:
        numer_studient = 0
        print("\nSTUDIENTS\n")
        for i in students:
            print(f"{numer_studient+1}. {i["identification"]} - {i["name"]} - {i["age"]} - {i["course"]} - {i["status"]}")
            numer_studient+=1
    else: print("\n""The list of the studients is empty""\n")
def shearch_studient(studients):
    identification = validate_identification()
    if len(studients) == 0:
        print("\n""The list of the studients is empty""\n")
        return
    bandera = False
    for i,s in enumerate(studients):
        if s['identification'] == identification:
            print(f"{i+1} - {s["identification"]} - {s["name"]} - {s["age"]} - {s["course"]} - {s["status"]}")
            bandera = True
            break
    if bandera == False:
        print("\n""Don't found it""\n")
    
def edit_information_of_the_studient(studients):
    amount_studients = len(studients)
    if amount_studients > 0:
        numer_studient = 0
        print("\nSTUDIENTS\n")
        for i in studients:
            print(f"{numer_studient+1}. {i["identification"]} - {i["name"]} - {i["age"]} - {i["course"]} - {i["status"]}")
            numer_studient+=1
        studient_for_edit = validate_studient_edit()-1