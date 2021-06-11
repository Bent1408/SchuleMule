# My EMP will be saved as a simple text file. This makes it easy for everyone to open, read and edit it.
import datetime


def print_choose():
    print("Please choose one of the following options:")


def print_not_developed():
    print("This function is not developed yet.")


def print_not_valid():
    print("This is not a valid option!")


def choose_between(start, end):
    print("Please enter a number between", start, "and", str(end) + "!")
    return input("Input: ")


def create_menu():
    while True:

        print_choose()
        print("1. add datasets from file (merge)\n2. add new single dataset (via console)\n"
              "3. add new column (for all datasets)\n4. back")
        selection = choose_between(1, 4)
        if selection == "1":
            print_not_developed()
        elif selection == "2":
            add_employee()
        elif selection == "3":
            print_not_developed()
        elif selection == "4":
            break
        else:
            print_not_valid()


def add_employee():
    global employees
    # Instructions output
    f = open("all_employees.txt", "a")
    print("Please add the employee data!")
    import datetime
    firstname = str(input("please enter the firstname of the employee:"))
    lastname = str(input("please enter the lastname of the employee:"))
    date_entry = input('Enter the birthday of the employee in YYYY-MM-DD format:')
    year, month, day = map(int, date_entry.split('-'))
    date1 = datetime.date(year, month, day)
    x = datetime.datetime.now()
    age = x.year - date1.year
    # print (date1)
    # print(x.year)
    # print(age)

    address = str(input("please enter the address of the employee:"))
    department = str(input("please enter the department of the employee:"))
    phone = int(input("please enter the phone number of the employee:"))
    relation = str(input("please enter the relationship of the employee:"))
    gender = str(input("please enter the gender of the employee:"))
    drivers_license = str(input("please enter the driving license class of the employee:"))
    religion = str(input("please enter the religion of the employee:"))
    health = str(input("please enter the health insurance of the employee:"))
    marital = str(input("please enter the marital status of the employee:"))
    email = str(input("please enter the email address of the employee:"))
    superior = str(input("please enter the superior of the employee:"))
    date_entry_2 = input('Enter the entry date of the employee in YYYY-MM-DD format:')
    year, month, day = map(int, date_entry.split('-'))
    date2 = datetime.date(year, month, day)
    identification = int(input("please enter the ID number of the employee:"))
    print("The employee", lastname, firstname, "was added")
    employee = [{'first_name': firstname, 'last_name': lastname, 'birthday': date_entry, 'address': address,
                 'department': department, 'phone_number': phone, 'employment': relation, 'gender': gender,
                 'drivers_license': drivers_license, 'religion': religion, 'health_insurance': health,
                 'martial_status': marital, 'Email': email, 'superior': superior, 'date_entry': date_entry_2, 'date2':
                     date2, 'identification': identification, age: "age"}]

    # writes the created employee into a text file
    file = open("employee_file.txt", "a")
    file.write(str(employee) + "\n")
    file.close()

   
def open_employee_file():
    # opens the text file where the employees are saved and prints each line
    f = open("employee_file.txt", "r")
    r = f.readlines()
    for element in r:
        print(element)
    f.close()
    

def read_menu():
    while True:
        print_choose()
        print("1. show all datasets\n2. show single dataset\n3. filter ...\n"
              "4. show empty fields\n5. back")
        selection = choose_between(1, 5)
        if selection == "1":
            open_employee_file()
        elif selection == "2":
            print_not_developed()
        elif selection == "3":
            print_not_developed()
        elif selection == "4":
            print_not_developed()
        elif selection == "5":
            break
        else:
            print_not_valid()


def update_menu():
    while True:
        print_choose()
        print("1. update all\n2. update single dataset\n3. back")
        selection = choose_between(1, 3)
        if selection == "1":
            print_not_developed()
        elif selection == "2":
            print_not_developed()
        elif selection == "3":
            break
        else:
            print_not_valid()


def delete_menu():
    while True:
        print_choose()
        print("1. delete all\n2. delete single row\n3. delete single column\n4. back")
        selection = choose_between(1, 4)
        if selection == "1":
            print_not_developed()
        elif selection == "2":
            print_not_developed()
        elif selection == "3":
            print_not_developed()
        elif selection == "4":
            break
        else:
            print_not_valid()


def main_menu():
    print("Welcome to the Employee Management Program (EMP)\n==================================================")
    while True:
        print_choose()
        print("1. create\n2. read\n3. update\n4. delete\n5. save/export\n6. end program")
        selection = choose_between(1, 6)
        if selection == "1":
            create_menu()
        elif selection == "2":
            read_menu()
        elif selection == "3":
            update_menu()
        elif selection == "4":
            delete_menu()
        elif selection == "5":
            print_not_developed()
        elif selection == "6":
            print("Good Bye!\n====================== END =======================")
            break
        else:
            print_not_valid()


if __name__ == '__main__':
    main_menu()
