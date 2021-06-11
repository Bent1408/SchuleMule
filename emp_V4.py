import tkinter as tk
from tkinter import ttk, BOTH, RIDGE, HORIZONTAL, Scrollbar, messagebox
from tkinter.constants import E, EW, RIGHT, W
import urllib.request

global firstname, lastname, birthday, address, department, phone, gender, dl, religion, hi, marital, email
global superior, entry, identification


def error():
    messagebox.showerror("Error", "This function is not developed yet.")


def not_developed():
    popup = tk.Toplevel()
    popup.geometry("200x80")
    # popup.eval("tk::PlaceWindow . center")
    popup.wm_title("Error")

    # Icon
    urllib.request.urlopen("https://findicons.com/files/icons/998/airicons/256/error.png").read()
    tk.PhotoImage(data=icon)
    popup.iconphoto(False, icon_data)

    tk.Label(popup, text="This function is not developed yet.").pack(side="top", fill="x", pady=15)
    popup_button = tk.Button(popup, text="Okay", command=popup.destroy)
    popup_button.pack()


def clear_frame2():
    for widgets in frame_2.winfo_children():
        widgets.destroy()


def create_menu():
    clear_frame2()

    tk.Button(frame_2, text="Add dataset from file", command=error).pack(side="top", fill="x", padx="5")
    tk.Button(frame_2, text="Add new single dataset", command=add_employee).pack(side="top", fill="x", padx="5")
    tk.Button(frame_2, text="Add new column", command=error).pack(side="top", fill="x", padx="5")


def add_employee():
    global firstname, lastname, birthday, address, department, phone, gender, dl, religion, hi, marital, email
    global superior, identification

    employee_window = tk.Toplevel()
    employee_window.geometry("250x330")
    employee_window.title("Add Employee")

    # Icon
    urllib.request.urlopen("https://image.flaticon.com/icons/png/512/49/49709.png").read()
    tk.PhotoImage(data=icon)
    employee_window.iconphoto(False, icon_data)

    tk.Label(employee_window, text="First name: ").grid(row=0, column=0, sticky=E)
    firstname = tk.StringVar(employee_window)
    tk.Entry(employee_window, textvariable=firstname).grid(row=0, column=1)

    tk.Label(employee_window, text="Last name: ").grid(row=1, column=0, sticky=E)
    lastname = tk.StringVar(employee_window)
    tk.Entry(employee_window, textvariable=lastname).grid(row=1, column=1)

    tk.Label(employee_window, text="Birthday: ").grid(row=2, column=0, sticky=E)
    birthday = tk.StringVar(employee_window)
    tk.Entry(employee_window, textvariable=birthday).grid(row=2, column=1)

    tk.Label(employee_window, text="Address: ").grid(row=3, column=0, sticky=E)
    address = tk.StringVar(employee_window)
    tk.Entry(employee_window, textvariable=address).grid(row=3, column=1)

    tk.Label(employee_window, text="Department: ").grid(row=4, column=0, sticky=E)
    department = tk.StringVar(employee_window)
    tk.Entry(employee_window, textvariable=department).grid(row=4, column=1)

    tk.Label(employee_window, text="Phone number: ").grid(row=5, column=0, sticky=E)
    phone = tk.StringVar(employee_window)
    tk.Entry(employee_window, textvariable=phone).grid(row=5, column=1)

    tk.Label(employee_window, text="Gender: ").grid(row=6, column=0, sticky=E)
    gender = tk.StringVar(employee_window)
    tk.Entry(employee_window, textvariable=gender).grid(row=6, column=1)

    tk.Label(employee_window, text="Drivers license: ").grid(row=7, column=0, sticky=E)
    dl = tk.StringVar(employee_window)
    tk.Entry(employee_window, textvariable=dl).grid(row=7, column=1)

    tk.Label(employee_window, text="Religion: ").grid(row=8, column=0, sticky=E)
    religion = tk.StringVar(employee_window)
    tk.Entry(employee_window, textvariable=religion).grid(row=8, column=1)

    tk.Label(employee_window, text="Health Insurance: ").grid(row=9, column=0, sticky=E)
    hi = tk.StringVar(employee_window)
    tk.Entry(employee_window, textvariable=hi).grid(row=9, column=1)

    tk.Label(employee_window, text="Marital status: ").grid(row=10, column=0, sticky=E)
    marital = tk.StringVar(employee_window)
    tk.Entry(employee_window, textvariable=marital).grid(row=10, column=1)

    tk.Label(employee_window, text="Email address: ").grid(row=11, column=0, sticky=E)
    email = tk.StringVar(employee_window)
    tk.Entry(employee_window, textvariable=email).grid(row=11, column=1)

    tk.Label(employee_window, text="Superior: ").grid(row=12, column=0, sticky=E)
    superior = tk.StringVar(employee_window)
    tk.Entry(employee_window, textvariable=superior).grid(row=12, column=1)

    tk.Label(employee_window, text="ID: ").grid(row=13, column=0, sticky=E)
    identification = tk.StringVar(employee_window)
    tk.Entry(employee_window, textvariable=identification).grid(row=13, column=1)

    tk.Button(employee_window, text="Confirm", bg="green3",
              command=lambda: [import_information(), employee_window.destroy()]).grid(row=14, column=1)


def import_information():
    global firstname, lastname, birthday, address, department, phone, gender, dl, religion, hi, marital, email
    global superior, identification

    firstname = firstname.get()
    lastname = lastname.get()
    birthday = birthday.get()
    address = address.get()
    department = department.get()
    phone = phone.get()
    gender = gender.get()
    dl = dl.get()
    religion = religion.get()
    hi = hi.get()
    marital = marital.get()
    email = email.get()
    superior = superior.get()
    identification = identification.get()

    employee = [{'ID': identification, 'First name': firstname, 'Last name': lastname, 'Department': department,
                 'Birthday': birthday, 'Address': address, 'Gender': gender, 'Phone#': phone, 'Religion': religion,
                 'Health Ins.': hi, 'Marital St.': marital, 'DL': dl, 'Email': email, 'Superior': superior}]

    file = open("employee_file.txt", "a")
    file.write(str(employee) + "\n")
    file.close()


def open_file():
    file = tk.Toplevel()

    with open("employee_file.txt", "r") as f:
        tk.Label(file, text=f.read()).pack()


def open_employee_file():
    employee_file = tk.Toplevel()
    employee_file.geometry("2000x500")
    employee_file.title("Employees")

    # Icon
    urllib.request.urlopen("https://image.flaticon.com/icons/png/512/49/49709.png").read()
    tk.PhotoImage(data=icon)
    employee_file.iconphoto(False, icon_data)

    f = open("employee_file.txt", "r")
    r = f.readlines()

    row = 0

    for i in r:
        row += 1
        tk.Label(employee_file, text=f"{i}").grid(row=row, column=0)
    f.close()


def read_menu():
    clear_frame2()

    tk.Button(frame_2, text="Show all datasets", command=open_file).pack(side="top", fill="x", padx="5")
    tk.Button(frame_2, text="Show single dataset", command=error).pack(side="top", fill="x", padx="5")
    tk.Button(frame_2, text="Show empty fields", command=error).pack(side="top", fill="x", padx="5")
    tk.Button(frame_2, text="filter...", command=error).pack(side="top", fill="x", padx="5")


def update_menu():
    clear_frame2()

    tk.Button(frame_2, text="Update all", command=error).pack(side="top", fill="x", padx="5")
    tk.Button(frame_2, text="Update single dataset", command=error).pack(side="top", fill="x", padx="5")


def delete_menu():
    clear_frame2()

    tk.Button(frame_2, text="Delete all", command=error).pack(side="top", fill="x", padx="5")
    tk.Button(frame_2, text="Delete single row", command=error).pack(side="top", fill="x", padx="5")
    tk.Button(frame_2, text="Delete single column", command=error).pack(side="top", fill="x", padx="5")


# Main window configuration
gui = tk.Tk()
gui.geometry("500x300")
gui.title("Employee Management Tool")

# Icon
icon = urllib.request.urlopen("https://image.flaticon.com/icons/png/512/49/49709.png").read()
icon_data = tk.PhotoImage(data=icon)
gui.iconphoto(False, icon_data)

gui = ttk.PanedWindow(gui, orient=HORIZONTAL)
gui.pack(fill=BOTH, expand=True)

# Frame color
s = ttk.Style()
s.configure("TFrame", background="gray99")

# Defining frames
frame_1 = ttk.Frame(gui, width=200, height=100, relief=RIDGE)
gui.add(frame_1, weight=2)
frame_2 = ttk.Frame(gui, width=200, height=100, relief=RIDGE)
gui.add(frame_2, weight=2)

# Main menu Button configuration
tk.Button(frame_1, text="create", command=create_menu, bg="gray80").pack(side="top", fill="x", padx="5")
tk.Button(frame_1, text="read", command=read_menu, bg="gray80").pack(side="top", fill="x", padx="5")
tk.Button(frame_1, text="update", command=update_menu, bg="gray80").pack(side="top", fill="x", padx="5")
tk.Button(frame_1, text="delete", command=delete_menu, bg="gray80").pack(side="top", fill="x", padx="5")
tk.Button(frame_1, text="save and export", command=error, bg="gray80").pack(side="top", fill="x", padx="5")
tk.Button(frame_1, text="close program", command=exit, bg="tomato").pack(side="top", fill="x", padx="5")

gui.mainloop()
