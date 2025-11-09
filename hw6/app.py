import tkinter as tk
from tkinter import ttk, messagebox
from database import *

root = tk.Tk()
root.title("Student Record Manager")

root.geometry("800x600+100+100")

# name label and input 
name_label = ttk.Label(root, text="Name: ")
name_label.pack(padx=5, pady=10)

name_entry = tk.StringVar()
name = ttk.Entry(root, textvariable=name_entry, width=30)
name.pack(padx=10, pady=10)

# major label and input
major_label = ttk.Label(root, text="Major: ")
major_label.pack(padx=10, pady=10)

major_entry = tk.StringVar()
major = ttk.Entry(root, textvariable=major_entry, width=30)
major.pack(padx=10, pady=10)

# add student button
def add_student():
    name = name_entry.get()
    major = major_entry.get()

    if name and major:
        session = Session()
        new_student = Student(name=name, major=major)
        session.add(new_student)

        session.commit()
        session.close()

        messagebox.showinfo("Success", f"Success! Added student: {name} and major: {major}")
        name_entry.set("")
        major_entry.set("")

    else:
        messagebox.showerror("Error", "Please enter in name and major")

add_button = ttk.Button(root, text="Add Student", command=add_student)
add_button.pack(padx=10, pady=10)

# view students button
def view_students():
    session = Session()

    all_students = session.query(Student).all()

    for row in table.get_children():
        table.delete(row)

    for student in all_students:
        table.insert("", tk.END, text="", values=(student.id,student.name, student.major))
    

view_button = ttk.Button(root, text="View Students", command=view_students)
view_button.pack(padx=10, pady=10)

table = ttk.Treeview(columns=("ID","Name", "Major"))
table.heading("ID", text="ID")
table.heading("Name", text="Name")
table.heading("Major", text="Major")
table.pack(padx=10, pady=10)

table.bind('Button1')

# delete students button
def delete_student():
    session = Session()

    row = table.focus()
    selection = table.item(row, 'values')

    student = session.query(Student).filter(Student.id == selection[0]).one()

    session.delete(student)
    table.delete(row)

    session.commit()
    session.close()

    messagebox.showinfo("Success", "Removed student successfully!")

delete_button = ttk.Button(root, text="Delete Selected", command=delete_student)
delete_button.pack(padx=10, pady=10)

root.mainloop()