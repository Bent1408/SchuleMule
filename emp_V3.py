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
    print("Please provide the following information to add the employee. ")
    firstname = str(input("First name of the employee: "))
    lastname = str(input("Last name of the employee: "))
    date_entry = input("Birthday in YYYY-MM-DD format: ")
    year, month, day = map(int, date_entry.split("-"))
    date1 = datetime.date(year, month, day)
    x = datetime.datetime.now()
    age = x.year - date1.year

    address = str(input("Address: "))
    department = str(input("Department: "))
    phone = int(input("Phone number: "))
    gender = str(input("Gender: "))
    drivers_license = str(input("Driver's Licence Category: "))
    religion = str(input("Religion: "))
    health = str(input("Health Insurance: "))
    marital_status = str(input("Marital status: "))
    email_address = str(input("Email address: "))
    superior = str(input("Superior: "))
    date_entry_2 = input("Entry date in YYYY-MM-DD format: ")
    i_d = int(input("ID number: "))
    print("The employee", firstname, lastname, "was added successfully.")
    employee = [{'ID': i_d, 'First name': firstname, 'Last name': lastname, 'Department': department, 'Age': age,
                 'Address': address, 'Gender': gender, 'Phone#': phone, 'Religion': religion, 'Health Ins.': health,
                 'Marital St.': marital_status, 'DL': drivers_license, 'Email': email_address, 'Superior': superior,
                 'Entry Date': date_entry_2}]

    # writes the created employee into a text file
    file = open("employee_file.txt", "a")
    file.write(str(employee) + "\n")
    file.close()

    input("Press ENTER to exit back to the menu.")


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
