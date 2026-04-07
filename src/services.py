from validations import validate_identification,validate_name,validate_age,validate_course,validate_status

def show_options_status ():
    status_list = {
        "Active":"option1",
        "Inactive":"option2"}
    count=0
    for i in status_list:
        print(f"{count+1}. {i}")
        count+=1
        
def show_options_course ():
    course_list = {
        "technology":"option1",
        "marketing":"option2",
        "desing":"option3",
        "finance":"option4",
        "crafts":"option5"}
    count=0
    for i in course_list:
        print(f"{count+1}. {i}")
        count+=1

def enter_new_student(students):
    identification = validate_identification()
    student_name = validate_name()
    age = validate_age()
    show_options_course()
    course = validate_course()
    show_options_status()
    status =validate_status()
    students.append({
        "identification":identification,
        "name":student_name,
        "age":age,
        "course":course,
        "status":status})

def show_list_of_the_students(students):
    amount_of_students = len(students)
    if amount_of_students > 0:
        numer_student = 0
        print("\nSTUDIENTS")
        for i in students:
            print(f"{numer_student+1}. {i["identification"]} - {i["name"]} - {i["age"]} - {i["course"]} - {i["status"]}")
            numer_student+=1
    else: print("\n""The list of the studients is empty")

def shearch_student(students):
    amount_students = len(students)
    if amount_students > 0:
        identification = validate_identification()
        bandera = False
        for i,s in enumerate(students):
            if s['identification'] == identification:
                print(f"{i+1} - {s["identification"]} - {s["name"]} - {s["age"]} - {s["course"]} - {s["status"]}")
                bandera = True
                break
        if bandera == False:
            print("\n""Don't found it")
    else: print("\n""The list of the studients is empty")
    
def edit_information_of_the_student(students):
    amount_students = len(students)
    if amount_students > 0:
        identification = validate_identification()
        found = False
        for i in students:
            if int (i["identification"]) == identification:
                i["name"] = validate_name()
                i["age"] = validate_age()
                i["course"] = validate_course()
                i["status"] = validate_status()
                print("\nStudent update successfully")
                found = True
                break
        if not found: print("Not found")
    else: print("\n""The list of the studients is empty")

def delete_student(students):
    amount_students = len(students)
    found = False
    if amount_students > 0:
        identification = validate_identification()
        for i in students:
            if i["identification"] == identification:
                students.remove(i)
                print("\nStudent deleted successfully")
                found = True
                break
        if not found: print("Not found")
    else: print("\nThe list of the studients is empty")